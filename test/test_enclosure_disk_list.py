# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.enclosure_disk_list import EnclosureDiskList

class TestEnclosureDiskList(unittest.TestCase):
    """EnclosureDiskList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnclosureDiskList:
        """Test EnclosureDiskList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnclosureDiskList`
        """
        model = EnclosureDiskList()
        if include_optional:
            return EnclosureDiskList(
                associated_links = [{"resourceUri":"/v1/storage-systems/device-type1/2FF70002AC01F0FF","type":"systems"},{"resourceUri":"/v1/storage-systems/device-type1/2FF70002AC01F0FF/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f","type":"enclosures"}],
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                customer_id = 'string',
                dc4data = dscc.models.ed_dc4data.edDc4data(
                    esi = True, 
                    esi_status = '', 
                    system_led = 'LED_UNKNOWN', ),
                dcsdata = dscc.models.ed_dcsdata.edDcsdata(
                    esi = True, 
                    esi_status = '', ),
                displayname = '',
                domain = '',
                enclosure_device_id = 1,
                enclosure_id = '9c3c4f29a82fd8d632ff379116fa0b8f',
                enclosure_name = '',
                enclosure_type = 'ENCLOSURE_DCS8',
                generation = 0,
                id = '9c3c4f29a82fd8d632ff379116fa0b8f',
                loop_a = dscc.models.enclosure_disk_loop.enclosureDiskLoop(
                    alpa = 56, 
                    state = dscc.models.state.State(
                        detailed = [
                            ''
                            ], 
                        overall = 'STATE_NORMAL', ), ),
                loop_b = dscc.models.enclosure_disk_loop.enclosureDiskLoop(
                    alpa = 56, 
                    state = dscc.models.state.State(
                        detailed = [
                            ''
                            ], 
                        overall = 'STATE_NORMAL', ), ),
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
                name = 'SASB',
                position = dscc.models.disk_position.diskPosition(
                    cage = 56, 
                    disk = 56, 
                    side = 'SIDE_NONE', 
                    sled = 56, ),
                resource_uri = '/v1/storage-systems/device-type1/2FF70002AC018D94/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-disks/8621946048c1cb24bdfc57e9b3b460ac',
                system_id = '7CE751P312',
                temperature = 56,
                type = 'string',
                wwn = '5000C500997AB7B0'
            )
        else:
            return EnclosureDiskList(
        )
        """

    def testEnclosureDiskList(self):
        """Test EnclosureDiskList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
