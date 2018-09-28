# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
import os
import sys
import urllib
import requests
from django.utils.functional import SimpleLazyObject, cached_property

from bkapi.base import RestAPI
from bkapi import create_instance_with_config
from bkapi.log import root_logger as logger


class BluekingAuth(RestAPI):
    """ bk_token && user_info
    """

    @cached_property
    def login_verify_url(self):
        """ 平台验证用户登录态接口"""
        return urllib.parse.urljoin(self.paas_host, "/login/accounts/is_login/")

    @cached_property
    def login_get_user_url(self):
        """ 平台获取用户信息接口"""
        return urllib.parse.urljoin(self.paas_host, "/login/accounts/get_user/")

    @cached_property
    def _default_headers(self):
        return {
            "Content-Type": "application/json",
            "X-APP-CODE": self.app_id,
            "X-APP-TOKEN": self.app_token,
        }

    def _request(self, method, url, data=None, headers=None):
        if headers is None:
            headers = self._default_headers
        try:
            if method == "GET":
                resp = requests.get(url=url, headers=headers, params=data)
            elif method == "HEAD":
                resp = requests.head(url=url, headers=headers)
            elif method == "POST":
                resp = requests.post(url=url, headers=headers, json=data)
            elif method == "DELETE":
                resp = requests.delete(url=url, headers=headers, json=data)
            elif method == "PUT":
                resp = requests.put(url=url, headers=headers, json=data)
            else:
                return False, None
        except requests.exceptions.RequestException:
            logger.exception(
                "login http request error! type: %s, "\
                "url: %s, data: %s",
                method, url, str(data))
            return False, None
        else:
            if resp.status_code != 200:
                content = resp.content[:100] if resp.content else ''
                logger.error(
                    "login http request error! type: %s, url: %s, "\
                    "data: %s, response_status_code: %s, "\
                    "response_content: %s",
                    method, url, str(data), resp.status_code, content)
                return False, None

            return True, resp.json()

    def verify_bk_login(self, bk_token):
        """请求平台接口验证登录是否失效"""
        param = {'bk_token': bk_token}
        result, resp = self._request("GET", self.login_verify_url, param)
        resp = resp if result and resp else {}
        ret = resp.get('result', False)
        # 验证失败
        if not ret:
            logger.info("验证用户登录token无效：%s", resp.get('message', ''))
            return False, {}
        return True, resp.get('data', {})

    def get_bk_user_info(self, bk_token):
        """请求平台接口获取用户信息"""
        param = {'bk_token': bk_token}
        result, resp = self._request("GET", self.login_get_user_url, param)
        resp = resp if result and resp else {}
        ret = resp.get('result', False) if result and resp else False
        # 获取用户信息失败
        if not ret:
            logger.error("请求平台接口获取用户信息失败：%s", resp.get('message', ''))
            return False, {}
        return True, resp.get('data', {})


@SimpleLazyObject
def bkauth():
    """ Default Blueking instance with settings.APP_ID and settings.APP_TOKEN
    """
    return create_instance_with_config(BluekingAuth)


def _main():
    """
    Usage:
    # with options
    python libs/bkapi/bkapi/auth.py APP_ID APP_TOKEN BK_PAAS_HOST BK_TOKEN

    # OR with environ
    APP_ID=? APP_TOKEN=? BK_PAAS_HOST=? python libs/bkapi/bkapi/client.py BK_TOKEN

    # OR django project, change pwd to directory who contains manage.py and settings.py files
    python libs/bkapi/bkapi/auth.py BK_TOKEN
    """
    from bkapi import _options_or_environ_or_default
    instance = _options_or_environ_or_default(
        BluekingAuth, sys.argv, os.environ, bkauth)
    print(instance.verify_bk_login(sys.argv[-1]))


if __name__ == "__main__":
    _main()
