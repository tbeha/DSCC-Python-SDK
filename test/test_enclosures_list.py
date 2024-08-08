# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.enclosures_list import EnclosuresList

class TestEnclosuresList(unittest.TestCase):
    """EnclosuresList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnclosuresList:
        """Test EnclosuresList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnclosuresList`
        """
        model = EnclosuresList()
        if include_optional:
            return EnclosuresList(
                associated_links = [{"resourceUri":"/v1/storage-systems/device-type1/7CE751P312","type":"systems"},{"resourceUri":"/v1/storage-systems/device-type1/7CE751P312/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-card-ports","type":"enclosure-card-ports"},{"resourceUri":"/v1/storage-systems/device-type1/7CE751P312/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-cards","type":"enclosure-cards"},{"resourceUri":"/v1/storage-systems/device-type1/7CE751P312/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-disks","type":"enclosure-disks"},{"resourceUri":"/v1/storage-systems/device-type1/7CE751P312/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-sleds","type":"enclosure-sleds"},{"resourceUri":"/v1/storage-systems/device-type1/7CE751P312/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-fans","type":"enclosure-fans"},{"resourceUri":"/v1/storage-systems/device-type1/7CE751P312/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-expanders","type":"enclosure-expanders"}],
                chain_pos_loop_a = 0,
                chain_pos_loop_b = 0,
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                customer_id = 'string',
                dc4data = dscc.models.dc4data.dc4data(
                    cpu_status = '', 
                    fw_status = '', 
                    fw_version = True, ),
                dcsdata = dscc.models.enc_dcsdata.encDcsdata(
                    fw_status = '', 
                    fw_version = '', ),
                detailed_state = '',
                displayname = '',
                domain = '',
                enclosure_id = 0,
                enclosure_type = 'ENCLOSURE_DCS8',
                errors = [
                    dscc.models.device_type4errors_inner.DeviceType4errors_inner(
                        alarm_code = '', 
                        alarm_text = '', 
                        iom = '', )
                    ],
                fail_indicator = False,
                fail_requested = False,
                form_factor = 'SFF',
                generation = 0,
                id = '9c3c4f29a82fd8d632ff379116fa0b8f',
                locate_enabled = False,
                location = '',
                loop_split = True,
                manufacturing = dscc.models.manufacturing_single.manufacturingSingle(
                    assembly_rev = '002*', 
                    check_sum = '--', 
                    hpe_model_name = 'HPE 3PAR 600 2S Node', 
                    manufacturer = 'XYRATEX', 
                    model = '0974244-06', 
                    saleable_part_number = '0974244-06', 
                    saleable_serial_number = '4UW0002941', 
                    serial_number = 'PMW0974244G4T88', 
                    spare_part_number = 'P04031-001', ),
                name = 'cage1',
                node_wwn = '50050CC106233428',
                resource_uri = '/v1/storage-systems/device-type1/7CE751P312/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f',
                state = dscc.models.enc_state.ENC_STATE(
                    detailed = '', 
                    overall = 'STATE_UNKNOWN', ),
                sub_type = '',
                system_id = '7CE751P312',
                type = 'string',
                warn_indicator = False,
                warn_requested = False
            )
        else:
            return EnclosuresList(
        )
        """

    def testEnclosuresList(self):
        """Test EnclosuresList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
