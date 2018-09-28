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


__author__ = u"蓝鲸智云"
__copyright__ = "Copyright © 2012-2017 Tencent BlueKing. All Rights Reserved."
__version__ = "4.0.1.1"


def get_config_from_django():
    """ 从 Django 项目中获取关键配置
    """
    from django.conf import settings
    return settings.APP_ID, settings.APP_TOKEN, settings.BK_PAAS_HOST


def create_instance_with_config(klass, *args, config=None, **kwargs):
    """ 使用 Django 配置生成实例
    """
    if not config:
        conf = get_config_from_django()
    elif callable(config):
        conf = config()
    else:
        conf = config
    #
    if isinstance(conf, dict):
        return klass(*args, **conf, **kwargs)
    if args:
        return klass(*args, **kwargs)
    return klass(*conf, **kwargs)


def _options_or_environ_or_default(klass, argv, environ, default):
    if len(argv) > 4:
        return klass(argv[1], argv[2], argv[3])
    try:
        return klass(
            environ['APP_ID'],
            environ['APP_TOKEN'],
            environ['BK_PAAS_HOST'])
    except KeyError:
        sys.path.append(os.getcwd())
        environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
        import django
        django.setup()
        return default
