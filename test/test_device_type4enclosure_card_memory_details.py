# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4enclosure_card_memory_details import DeviceType4enclosureCardMemoryDetails

class TestDeviceType4enclosureCardMemoryDetails(unittest.TestCase):
    """DeviceType4enclosureCardMemoryDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4enclosureCardMemoryDetails:
        """Test DeviceType4enclosureCardMemoryDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4enclosureCardMemoryDetails`
        """
        model = DeviceType4enclosureCardMemoryDetails()
        if include_optional:
            return DeviceType4enclosureCardMemoryDetails(
                common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                customer_id = 'string',
                displayname = '',
                domain = '',
                enclosure_card_id = 56,
                enclosure_card_mem_type = '',
                enclosure_card_uid = '',
                enclosure_id = 56,
                enclosure_uid = '',
                generation = 0,
                id = '',
                index = 56,
                manufacturing = dscc.models.device_type4_manufacturing_single.DeviceType4ManufacturingSingle(
                    assembly_rev = '002*', 
                    check_sum = '--', 
                    hpe_model_name = 'HPE 3PAR 600 2S Node', 
                    manufacturer = 'XYRATEX', 
                    model = '0974244-06', 
                    saleable_part_number = '0974244-06', 
                    saleable_serial_number = '4UW0002941', 
                    serial_number = 'PMW0974244G4T88', 
                    spare_part_number = 'P04031-001', ),
                name = '',
                rcd = '',
                size = 56,
                speed = 56,
                system_id = '',
                type = 'string'
            )
        else:
            return DeviceType4enclosureCardMemoryDetails(
        )
        """

    def testDeviceType4enclosureCardMemoryDetails(self):
        """Test DeviceType4enclosureCardMemoryDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
