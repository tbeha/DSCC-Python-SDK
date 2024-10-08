# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_enclosures_detailed_fields_enclosure_cdms import DeviceType4EnclosuresDetailedFieldsEnclosureCdms

class TestDeviceType4EnclosuresDetailedFieldsEnclosureCdms(unittest.TestCase):
    """DeviceType4EnclosuresDetailedFieldsEnclosureCdms unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4EnclosuresDetailedFieldsEnclosureCdms:
        """Test DeviceType4EnclosuresDetailedFieldsEnclosureCdms
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4EnclosuresDetailedFieldsEnclosureCdms`
        """
        model = DeviceType4EnclosuresDetailedFieldsEnclosureCdms()
        if include_optional:
            return DeviceType4EnclosuresDetailedFieldsEnclosureCdms(
                items = [
                    dscc.models.device_type4enclosure_cdm_details.DeviceType4enclosureCdmDetails(
                        common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                            cloud_state = 'CONNECTED', ), 
                        customer_id = 'string', 
                        displayname = 'Enclosure 1 CDM', 
                        domain = 'string', 
                        element_status_code = 'ok', 
                        enclosure_id = 1, 
                        enclosure_uid = '9c3c4f29a82fd8d632ff379116fa0b8f', 
                        fail_ind = 'false', 
                        fw_version = 'string', 
                        generation = 0, 
                        id = '9c3c4f29a82fd8d632ff379116fa0b80', 
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
                        ok_int = 'false', 
                        os_version = 'string', 
                        p_uid = '51402EC0011762B0', 
                        safe_to_remove = 'true', 
                        system_id = '9c3c4f29a82fd8d632ff379116fa0b88', 
                        type = 'string', 
                        updating = 'false', )
                    ],
                page_limit = 1,
                page_offset = 1,
                total = 1
            )
        else:
            return DeviceType4EnclosuresDetailedFieldsEnclosureCdms(
        )
        """

    def testDeviceType4EnclosuresDetailedFieldsEnclosureCdms(self):
        """Test DeviceType4EnclosuresDetailedFieldsEnclosureCdms"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
