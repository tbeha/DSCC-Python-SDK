# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.primera_application_set_details import PrimeraApplicationSetDetails

class TestPrimeraApplicationSetDetails(unittest.TestCase):
    """PrimeraApplicationSetDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrimeraApplicationSetDetails:
        """Test PrimeraApplicationSetDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrimeraApplicationSetDetails`
        """
        model = PrimeraApplicationSetDetails()
        if include_optional:
            return PrimeraApplicationSetDetails(
                app_set_business_unit = 'cssl',
                app_set_comments = 'app set comments',
                app_set_exclude_aiqo_s = 'no',
                app_set_id = 5,
                app_set_importance = 'NORMAL',
                app_set_name = 'KA_VEGA_APPSET1_186',
                app_set_qo_s_config = dscc.models.app_set_qo_s_config.AppSetQoSConfig(
                    bandwidth_max_limit_ki_b = 500, 
                    displayname = '', 
                    domain = '', 
                    enable = True, 
                    generation = 1666788678, 
                    id = 59978, 
                    iops_max_limit = 500, 
                    last_modified_epoch = 1666788678, 
                    system_uid = '756XNSKA', 
                    system_wwn = '2FWWN2004134', 
                    target_name = 'volumeset', 
                    target_type = 'QOS_TGT_APPSET', 
                    uid = '12335546bgbgnbgnaq12', 
                    volumes = ["vol1","vol2"], ),
                app_set_type = 'Oracle Database',
                app_set_type_enum = 'ORACLE_DATA',
                associated_links = [{"resourceUri":"/v1/storage-systems/device-type1/2FF70002AC01F0FF","type":"systems"},{"resourceUri":"/v1/storage-systems/device-type1/2FF70002AC01F0FF/volumes","type":"volumes"}],
                comment = 'Comments',
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'data-ops-manager/storage-systems/device-type1/SGH014XGSP/applicationsets/fd3244ef7f1ab8bd16500c7a41bdf8f8',
                customer_id = 'string',
                display_name = 'Application Set KA_VEGA_APPSET1_186 ',
                domain = 'Domain',
                dr_state = 'Normal',
                export_status = 'PARTIALLY_EXPORTED',
                generation = 0,
                id = '4c74ec5c-ecec-4483-9506-3fb5dc45b5d0',
                initiators = [
                    dscc.models.device_type4_application_set_details_initiators_inner.DeviceType4ApplicationSetDetails_initiators_inner(
                        device_discovered_name = 'TEST11', 
                        id = '6848ef683c27403e96caa51816ddc72c', 
                        resource_uri = '/v1/host-initiators/6848ef683c27403e96caa51816ddc72c', 
                        type = 'host-initiators', )
                    ],
                is_failover_allowed = True,
                is_override_allowed = False,
                is_primary = True,
                is_sync_allowed = True,
                kv_pairs_present = True,
                members = ["vol1","vol2"],
                name = 'KA_VEGA_APPSET2_186',
                non_zero_rto_config = 'ActiveSync',
                remote_recovery_point = dscc.models.recovery_point.recoveryPoint(
                    ms = 1591601529000, 
                    tz = 'Local', ),
                replication_partner = [{"partnerSystem":"cs2-C630-2939-141","replicationPartner":"cs2-C630-2939_s1511"},{"partnerSystem":"s2940_208","replicationPartner":"s2940_1"}],
                replication_state = 'Started',
                replication_traffic = 'Sending',
                replication_type = 'periodic',
                request_uri = '/v1/storage-systems/device-type1/2FF70002AC01F0FF/applicationsets/fd3244ef7f1ab8bd16500c7a41bdf8f8',
                role = 'Primary',
                serial_number = '7CE738P06J',
                size_mi_b = 153600,
                snap_set_parent_id = 5,
                snap_set_parent_name = 'HPE',
                system_id = '7CE751P312',
                type = 'string',
                vv_set_type = 'VVSET',
                zero_rto_config = 'PP'
            )
        else:
            return PrimeraApplicationSetDetails(
        )
        """

    def testPrimeraApplicationSetDetails(self):
        """Test PrimeraApplicationSetDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
