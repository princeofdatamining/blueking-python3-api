# -*- coding: utf-8 -*-
# pylint: disable=too-many-instance-attributes,too-few-public-methods
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
from ..base import ComponentAPI


class CollectionsJOB():
    """Collections of JOB APIS"""

    def __init__(self, client):
        self.client = client

        self.change_cron_status = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/job/change_cron_status/',
            description='更新定时作业状态',
        )
        self.execute_task = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/job/execute_task/',
            description='根据作业模板ID启动作业',
        )
        self.execute_task_ext = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/job/execute_task_ext/',
            description='启动作业Ext(带全局变量启动)',
        )
        self.fast_execute_script = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/job/fast_execute_script/',
            description='快速执行脚本',
        )
        self.fast_push_file = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/job/fast_push_file/',
            description='快速分发文件',
        )
        self.get_agent_status = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/job/get_agent_status/',
            description='查询Agent状态',
        )
        self.get_cron = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/job/get_cron/',
            description='查询业务下定时作业信息',
        )
        self.get_task = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/job/get_task/',
            description='查询作业模板',
        )
        self.get_task_detail = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/job/get_task_detail/',
            description='查询作业模板详情',
        )
        self.get_task_ip_log = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/job/get_task_ip_log/',
            description='根据作业实例ID查询作业执行日志',
        )
        self.get_task_result = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/job/get_task_result/',
            description='根据作业实例 ID 查询作业执行状态',
        )
        self.save_cron = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/job/save_cron/',
            description='新建或保存定时作业',
        )
