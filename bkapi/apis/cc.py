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


class CollectionsCC():
    """Collections of CC APIS"""

    def __init__(self, client):
        self.client = client

        self.add_plat_id = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/add_plat_id/',
            description='新增子网ID',
        )
        self.add_set = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/add_set/',
            description='新建集群',
        )
        self.clone_host_property = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/clone_host_property/',
            description='克隆主机属性',
        )
        self.del_plat = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/del_plat/',
            description='删除子网',
        )
        self.del_set = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/del_set/',
            description='删除集群',
        )
        self.del_set_host = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/del_set_host/',
            description='清空集群主机',
        )
        self.get_app_agent_status = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_app_agent_status/',
            description='查询业务下Agent状态',
        )
        self.get_app_by_id = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_app_by_id/',
            description='查询业务信息',
        )
        self.get_app_by_user = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_app_by_user/',
            description='查询用户有权限的业务',
        )
        self.get_app_by_user_role = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_app_by_user_role/',
            description='根据用户角色查询用户业务',
        )
        self.get_app_host_list = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_app_host_list/',
            description='查询业务主机列表',
        )
        self.get_app_list = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_app_list/',
            description='查询业务列表',
        )
        self.get_host_by_company_id = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_host_by_company_id/',
            description='根据开发商ID、子网ID、主机IP获取主机信息',
        )
        self.get_host_company_id = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_host_company_id/',
            description='获取主机开发商',
        )
        self.get_host_list_by_field = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_host_list_by_field/',
            description='根据主机属性的值group主机列表',
        )
        self.get_host_list_by_ip = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_host_list_by_ip/',
            description='根据IP查询主机信息',
        )
        self.get_hosts_by_property = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_hosts_by_property/',
            description='根据 set 属性查询主机',
        )
        self.get_ip_and_proxy_by_company = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_ip_and_proxy_by_company/',
            description='查询业务下IP及ProxyIP',
        )
        self.get_module_host_list = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_module_host_list/',
            description='查询模块主机列表',
        )
        self.get_modules = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_modules/',
            description='查询业务下的所有模块',
        )
        self.get_modules_by_property = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_modules_by_property/',
            description='根据 set 属性查询模块',
        )
        self.get_plat_id = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_plat_id/',
            description='查询子网列表',
        )
        self.get_process_port_by_app_id = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_process_port_by_app_id/',
            description='查询进程端口',
        )
        self.get_property_list = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_property_list/',
            description='查询属性列表',
        )
        self.get_set_host_list = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_set_host_list/',
            description='查询Set主机列表',
        )
        self.get_set_property = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_set_property/',
            description='获取所有 set 属性',
        )
        self.get_sets_by_property = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_sets_by_property/',
            description='根据 set 属性获取 set',
        )
        self.get_topo_tree_by_app_id = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/cc/get_topo_tree_by_app_id/',
            description='查询业务拓扑树',
        )
        self.update_custom_property = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/update_custom_property/',
            description='更新集群属性',
        )
        self.update_gse_proxy_status = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/update_gse_proxy_status/',
            description='更新主机gse agent proxy 状态',
        )
        self.update_host_by_app_id = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/update_host_by_app_id/',
            description='更新主机的gse agent状态',
        )
        self.update_host_module = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/update_host_module/',
            description='修改主机模块',
        )
        self.update_host_plat = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/update_host_plat/',
            description='更新主机云子网',
        )
        self.update_module_property = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/update_module_property/',
            description='更新模块属性',
        )
        self.update_set_property = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/update_set_property/',
            description='更新集群属性',
        )
        self.update_set_service_status = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/cc/update_set_service_status/',
            description='更新集群状态',
        )
