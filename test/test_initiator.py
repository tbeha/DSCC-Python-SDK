# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.initiator import Initiator

class TestInitiator(unittest.TestCase):
    """Initiator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Initiator:
        """Test Initiator
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Initiator`
        """
        model = Initiator()
        if include_optional:
            return Initiator(
                address = '100008F1EABFE61C',
                associated_links = [
                    dscc.models.sc_associated_links_inner.scAssociatedLinks_inner(
                        resource_uri = '', 
                        type = '', )
                    ],
                customer_id = 'fc5f41652a53497e88cdcebc715cc1cf',
                driver_version = '4.1',
                firmware_version = '10.0',
                generation = 1627534116,
                hba_model = 'myobject-5',
                host_speed = 1000,
                hosts = [
                    dscc.models.host_summary_for_initiator_object.HostSummaryForInitiatorObject(
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
                        ip_address = '15.212.100.100', 
                        is_mergable = True, 
                        is_vvol_host = True, 
                        marked_for_delete = True, 
                        name = 'host1', 
                        systems = [
                            ''
                            ], 
                        user_created = True, )
                    ],
                id = 'd548ef683c27403e96caa51816ddc72c',
                ip_address = '15.212.100.100',
                name = 'init1',
                protocol = 'FC',
                systems = [
                    ''
                    ],
                type = 'initiator',
                vendor = 'hpe'
            )
        else:
            return Initiator(
        )
        """

    def testInitiator(self):
        """Test Initiator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
