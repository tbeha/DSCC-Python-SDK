# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.hosts_list import HostsList

class TestHostsList(unittest.TestCase):
    """HostsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HostsList:
        """Test HostsList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HostsList`
        """
        model = HostsList()
        if include_optional:
            return HostsList(
                items = [
                    dscc.models.host_object.HostObject(
                        associated_links = [
                            dscc.models.sc_associated_links_inner.scAssociatedLinks_inner(
                                resource_uri = '', 
                                type = '', )
                            ], 
                        associated_systems = [
                            ''
                            ], 
                        comment = 'a sample host comment', 
                        console_uri = '/data-ops-manager/host-initiators/0951b6508ec9f8747f08daf68925d81d', 
                        contact = 'sanjay@hpe.com', 
                        customer_id = 'fc5f41652a53497e88cdcebc715cc1cf', 
                        edit_status = 'Delete_Failed', 
                        fqdn = 'host1.hpe.com', 
                        generation = 1627534116, 
                        host_groups = [
                            dscc.models.host_group_summary_object.HostGroupSummaryObject(
                                id = 'd548ef683c27403e96caa51816ddc72c', 
                                is_mergable = True, 
                                marked_for_delete = True, 
                                name = 'host-group1', 
                                systems = [
                                    ''
                                    ], 
                                user_created = True, )
                            ], 
                        id = '6848ef683c27403e96caa51816ddc72c', 
                        initiators = [
                            dscc.models.initiator_summary.InitiatorSummary(
                                address = '100008F1EABFE61C', 
                                id = 'd548ef683c27403e96caa51816ddc72c', 
                                ip_address = '15.212.100.100', 
                                name = 'init1', 
                                protocol = 'FC', )
                            ], 
                        ip_address = '15.212.100.100', 
                        is_mergable = True, 
                        is_vvol_host = True, 
                        location = 'India', 
                        marked_for_delete = True, 
                        model = 'model1', 
                        name = 'host1', 
                        operating_system = 'Windows', 
                        persona = 'AIX-Legacy', 
                        protocol = 'FC', 
                        subnet = '255.255.255.0', 
                        systems = [
                            ''
                            ], 
                        type = 'host-initiator', 
                        user_created = True, )
                    ],
                page_limit = 1,
                page_offset = 0,
                request_uri = '/api/v1/host-initiators',
                total = 1
            )
        else:
            return HostsList(
        )
        """

    def testHostsList(self):
        """Test HostsList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
