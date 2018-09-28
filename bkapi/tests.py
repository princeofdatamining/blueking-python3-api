# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,no-self-use
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

Usage:

"""
import unittest
from django.core.exceptions import ImproperlyConfigured
from bkapi.auth import bkauth
from bkapi.client import client as bkclient


class TestBluekingAPI(unittest.TestCase):

    def _test_auth(self, auth):
        result, data = auth.verify_bk_login('token')
        self.assertEqual(False, result)
        self.assertEqual({}, data)

    def test_auth_as_django_project(self):
        try:
            self._test_auth(bkauth)
        except ImproperlyConfigured:
            return

    def _test_component(self, client, collection, component, *args, **kwargs):
        collection = getattr(client, collection)
        component = getattr(collection, component)
        data = component(*args, **kwargs)
        message = data['message']
        self.assertEqual('用户认证失败，请检查bk_token是否有效', message)

    def test_component_as_django_project(self):
        try:
            self._test_component(bkclient, 'bk_login', 'get_user',
                                 bk_token='token')
        except ImproperlyConfigured:
            return
