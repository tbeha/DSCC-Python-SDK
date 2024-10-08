# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.node_mcus_summary_list import NodeMcusSummaryList

class TestNodeMcusSummaryList(unittest.TestCase):
    """NodeMcusSummaryList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeMcusSummaryList:
        """Test NodeMcusSummaryList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeMcusSummaryList`
        """
        model = NodeMcusSummaryList()
        if include_optional:
            return NodeMcusSummaryList(
                items = [
                    dscc.models.node_mcu_list.nodeMcuList(
                        associated_links = [{"resourceUri":"/v1/storage-systems/device-type1/2FF70002AC01F0FF","type":"systems"},{"resourceUri":"/v1/storage-systems/device-type1/2FF70002AC01F0FF/nodes/e9d353bf98fc1a6bdb90b824e3ca14b5","type":"nodes"}], 
                        common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                            cloud_state = 'CONNECTED', ), 
                        customer_id = 'string', 
                        domain = '', 
                        fw_version = '4.9.20', 
                        generation = 0, 
                        id = 'be97ad7351f8562440c909460061d0cb', 
                        model = 'NEMOE', 
                        name = 'Controller Node 1 MCU', 
                        node_device_id = 1, 
                        node_id = '624fc670a5bc9a6e6e5c7833da4bab13', 
                        reset_reason = 'Cold Power-on', 
                        resource_uri = '/v1/storage-systems/device-type1/2FF70002AC018D94/nodes/e9d353bf98fc1a6bdb90b824e3ca14b5/node-mcus/be97ad7351f8562440c909460061d0cb', 
                        state = dscc.models.state.State(
                            detailed = [
                                ''
                                ], 
                            overall = 'STATE_NORMAL', ), 
                        system_id = '7CE751P312', 
                        type = 'string', 
                        up_since = dscc.models.uptime.uptime(
                            ms = 123423423, 
                            tz = 'IST', ), )
                    ],
                page_limit = 1,
                page_offset = 1,
                request_uri = '/v1/storage-systems/device-type1/2FF70002AC01F0FF/nodes/e9d353bf98fc1a6bdb90b824e3ca14b5/node-mcus',
                total = 2
            )
        else:
            return NodeMcusSummaryList(
        )
        """

    def testNodeMcusSummaryList(self):
        """Test NodeMcusSummaryList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
