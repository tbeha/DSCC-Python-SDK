# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.primera_host_path_list import PrimeraHostPathList

class TestPrimeraHostPathList(unittest.TestCase):
    """PrimeraHostPathList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrimeraHostPathList:
        """Test PrimeraHostPathList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrimeraHostPathList`
        """
        model = PrimeraHostPathList()
        if include_optional:
            return PrimeraHostPathList(
                items = [
                    dscc.models.primera_host_path_list_obj.PrimeraHostPathListObj(
                        ip_addr = '1.1.1.1', 
                        address = '810009440c9ce5824', 
                        associated_links = [
                            dscc.models.associated_links_inner.AssociatedLinks_inner(
                                resource_uri = '', 
                                type = '', )
                            ], 
                        common_resource_attributes = dscc.models.common_resource_attributes_primera_host.commonResourceAttributesPrimeraHost(
                            cloud_state = 'CONNECTED', ), 
                        displayname = 'Drive 0.SIDE_NONE.2.0', 
                        domain = '-', 
                        driver_version = 'v1.0.0', 
                        firmware_version = 'v1.0.0', 
                        generation = 1652172206, 
                        host_id = 101780, 
                        host_name = 'test-host', 
                        host_speed = 100, 
                        id = '1223f5s', 
                        model = 'model_1', 
                        path_type = 'FC', 
                        port_pos = dscc.models.device_type4_host_path_list_obj_port_pos.DeviceType4HostPathListObj_portPos(
                            node = 1, 
                            port = 1, 
                            slot = 1, ), 
                        resource_uri = '/v1/storage-systems/host-paths/dbce79b2612cde02a6e0be8934c330ec', 
                        sc_host_initiator_id = '1223f5s', 
                        switch_port_wwn = '5001438026e98a60', 
                        system_uid = '7CE727P35M', 
                        system_wwn = 'swK21', 
                        uri = '/api/v3/hostpaths/dbce79b2612cde02a6e0be8934c330ec', 
                        vendor = '-', )
                    ],
                page_limit = 1,
                page_offset = 1,
                request_uri = 'api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817/host-paths',
                total = 1
            )
        else:
            return PrimeraHostPathList(
        )
        """

    def testPrimeraHostPathList(self):
        """Test PrimeraHostPathList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
