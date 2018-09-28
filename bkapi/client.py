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

Component API Client
"""
import os
import sys
import json
import requests
from django.utils.functional import SimpleLazyObject

from bkapi import create_instance_with_config
from bkapi import collections
from bkapi.log import component_logger as logger


class BaseComponentClient():
    """Base client class for component"""

    available_collections = collections.AVAILABLE_COLLECTIONS.copy()

    def __init__(self, app_code, app_secret, paas_host, **kwargs):
        """
        :param str app_code: App code to use
        :param str app_secret: App secret to use
        :param dict common_args: Args that will apply to every request
        :param bool use_test_env: whether use test version of components
        """
        self.app_code = app_code
        self.app_secret = app_secret
        self.paas_host = paas_host
        self.common_args = kwargs.get('common_args') or {}
        self.use_test_env = kwargs.get('use_test_env')
        self._cached_collections = {}

    def set_use_test_env(self, use_test_env):
        """Change the value of use_test_env

        :param bool use_test_env: whether use test version of components
        """
        self.use_test_env = use_test_env

    def merge_params_data_with_common_args(self, method, params, data, enable_app_secret=False):
        """get common args when request
        """
        common_args = dict(app_code=self.app_code, **self.common_args)
        if enable_app_secret:
            common_args['app_secret'] = self.app_secret
        if method == 'GET':
            _params = common_args.copy()
            _params.update(params or {})
            params = _params
        elif method == 'POST':
            _data = common_args.copy()
            _data.update(data or {})
            data = json.dumps(_data)
        return params, data

    def request(self, method, url, params=None, data=None, **kwargs):
        """Send request
        """
        # determine whether access test environment of third-party system
        headers = kwargs.pop('headers', {})
        if self.use_test_env:
            headers['x-use-test-env'] = '1'
        params, data = self.merge_params_data_with_common_args(
            method, params, data, enable_app_secret=True)
        logger.debug('Calling %s %s with params=%s, data=%s, headers=%s',
                     method, url, params, data, headers)
        return requests.request(method, url,
                                params=params, data=data,
                                headers=headers, verify=False, **kwargs)

    def __getattr__(self, key):
        if key not in self.available_collections:
            return getattr(super(BaseComponentClient, self), key)

        if key not in self._cached_collections:
            collection = self.available_collections[key]
            self._cached_collections[key] = collection(self)
        return self._cached_collections[key]


ComponentClient = BaseComponentClient


@SimpleLazyObject
def client():
    """ 默认 ComponentClient 实例
    """
    return create_instance_with_config(ComponentClient)


def _main():
    """
    Usage:
    # with options
    python libs/bkapi/bkapi/client.py APP_ID APP_TOKEN BK_PAAS_HOST BK_TOKEN

    # OR with environ
    APP_ID=? APP_TOKEN=? BK_PAAS_HOST=? python libs/bkapi/bkapi/client.py BK_TOKEN

    # OR django project, change pwd to directory who contains manage.py and settings.py files
    python libs/bkapi/bkapi/client.py BK_TOKEN
    """
    from bkapi import _options_or_environ_or_default
    instance = _options_or_environ_or_default(
        ComponentClient, sys.argv, os.environ, client)
    print(instance.bk_login.get_user(bk_token=sys.argv[-1]))


if __name__ == "__main__":
    _main()
