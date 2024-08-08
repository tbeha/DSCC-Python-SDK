# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_volume_common_export_details import NimbleVolumeCommonExportDetails

class TestNimbleVolumeCommonExportDetails(unittest.TestCase):
    """NimbleVolumeCommonExportDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleVolumeCommonExportDetails:
        """Test NimbleVolumeCommonExportDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleVolumeCommonExportDetails`
        """
        model = NimbleVolumeCommonExportDetails()
        if include_optional:
            return NimbleVolumeCommonExportDetails(
                volume_export_details = dscc.models.nimble_volume_export_details.NimbleVolumeExportDetails(
                    host_groups = [
                        dscc.models.nimble_host_group_detail.NimbleHostGroupDetail(
                            hosts = [
                                dscc.models.nimble_host_summary_details.NimbleHostSummaryDetails(
                                    access_protocol = 'fc', 
                                    acr_id = '2a0df0fe6f7dc7bb16000000000000000000004009', 
                                    apply_to = 'volume', 
                                    chap_user_id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                                    chap_user_name = 'myobject-5', 
                                    fc_initiators = [
                                        dscc.models.fc_initiator_list.FCInitiatorList(
                                            alias = 'my_initiator-4', 
                                            id = '0d4323bdd90b39c3a7000000000000000000000012', 
                                            wwpn = 'af:32:f1:20:bc:ba:43:1a', )
                                        ], 
                                    fc_target_ports = [
                                        dscc.models.fc_port_list.FCPortList(
                                            name = 'fc3b.1', )
                                        ], 
                                    host_type = '', 
                                    id = '0d4323bdd90b39c3a7000000000000000000000012', 
                                    initiator_group_id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                                    initiator_group_name = 'host1', 
                                    iscsi_initiators = [
                                        dscc.models.iscsi_initiator_list.IscsiInitiatorList(
                                            id = '0d4323bdd90b39c3a7000000000000000000000012', 
                                            ip_address = 'iqn.2007-11.com.storage:zmytestvol1-v0df0fe6f7dc7bb16.0000016b.70374579', 
                                            iqn = 'iqn.2007-11.com.storage:zmytestvol1-v0df0fe6f7dc7bb16.0000016b.70374579', 
                                            label = 'myobject-5', )
                                        ], 
                                    lun = 8, 
                                    name = 'hostgrp1', 
                                    num_connections = 8, 
                                    sc_host_id = '60f1a749a5bd4f0bb0644c9220eef7ce', 
                                    snap_id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                                    user_created = False, )
                                ], 
                            sc_host_group_id = '60f1a749a5bd4f0bb0644c9220eef7ce', 
                            sc_host_group_name = 'hostgrp1', 
                            user_created = False, )
                        ], )
            )
        else:
            return NimbleVolumeCommonExportDetails(
        )
        """

    def testNimbleVolumeCommonExportDetails(self):
        """Test NimbleVolumeCommonExportDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
