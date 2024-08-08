# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.primera_pool_details import PrimeraPoolDetails

class TestPrimeraPoolDetails(unittest.TestCase):
    """PrimeraPoolDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrimeraPoolDetails:
        """Test PrimeraPoolDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrimeraPoolDetails`
        """
        model = PrimeraPoolDetails()
        if include_optional:
            return PrimeraPoolDetails(
                alert = dscc.models.cpg_alert.cpgAlert(
                    fail = '--', 
                    limit = '--', 
                    warn = '--', 
                    warn_percent = 2, ),
                allocation_settings = dscc.models.allocation.allocation(
                    ha = dscc.models.device_type4allocation_ha.DeviceType4allocation_HA(
                        default = '', 
                        key = '', ), 
                    raid_type = 'RAID_SIX', 
                    chunklet_pos_pref = 'Position1', 
                    device_speed = dscc.models.device_type4allocation_device_speed.DeviceType4allocation_deviceSpeed(
                        default = '', 
                        key = '', 
                        text = '', 
                        value = 56, ), 
                    device_type = 'DEVICE_TYPE_SSD', 
                    disk_filter = 'test', 
                    requested_ha = dscc.models.device_type4allocation_ha.DeviceType4allocation_HA(
                        default = '', 
                        key = '', ), 
                    set_size = '6 data, 2 parity', 
                    step_size = -1, ),
                ao_config_id = 1,
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type1/7CE809P009","type":"storage-systems"},{"resourceUri":"/api/v1/storage-systems/device-type1/7CE809P009/storage-pools/8fdba044f8d90c7922c17b9340b65178/volumes","type":"volumes"}],
                base_size_mi_b = 67584,
                base_size_private_mi_b = 1215872,
                base_size_raw_mi_b = 90111,
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                compact_ratio = 5.722643930878938,
                compress_ratio = 4.233684210526316,
                customer_id = 'string',
                data_reduce_ratio = 2.25,
                dedup_capable = True,
                dedup_ratio = 2.2464644143676713,
                dedup_version = dscc.models.device_type4_pool_details_dedup_version.DeviceType4PoolDetails_dedupVersion(
                    default = '', 
                    key = '', ),
                displayname = 'CPG Vega_7_test',
                domain = 'testdomain',
                free_for_allocation_mi_b = 4141056,
                free_size_mi_b = 44672,
                free_size_raw_mi_b = 16896,
                generation = 0,
                id = 'e9d353bf98fc1a6bdb90b824e3ca14b5',
                name = 'Vega_7_test',
                number_of_snap_rc = 5,
                number_of_tdvv = 14,
                number_of_tpvv = 1062,
                number_of_user_rc = 5,
                over_prov_ratio = 0.58,
                request_uri = '/api/v1/storage-systems/device-type1/7CE809P009/storage-pools/8fdba044f8d90c7922c17b9340b65178',
                resource_uri = '/api/v1/storage-systems/device-type1/7CE809P009/storage-pools/8fdba044f8d90c7922c17b9340b65178',
                sa_grow = dscc.models.cpg_grow.cpgGrow(
                    args = '-p -devtype SSD', 
                    limit_mi_b = 10, 
                    size_mi_b = 12, 
                    warn_mi_b = 10, ),
                sd_grow = dscc.models.cpg_grow.cpgGrow(
                    args = '-p -devtype SSD', 
                    limit_mi_b = 10, 
                    size_mi_b = 12, 
                    warn_mi_b = 10, ),
                shared_size_mi_b = 512,
                snap_size_private_mi_b = 526848,
                snap_size_raw_mi_b = 56831,
                snap_space_admin = dscc.models.snap_space.snapSpace(
                    ld_count = 4, 
                    total_mi_b = 83968, 
                    total_raw_mi_b = 251904, 
                    used_mi_b = 75008, 
                    used_raw_mi_b = 225024, ),
                snap_space_data = dscc.models.snap_space.snapSpace(
                    ld_count = 4, 
                    total_mi_b = 83968, 
                    total_raw_mi_b = 251904, 
                    used_mi_b = 75008, 
                    used_raw_mi_b = 225024, ),
                state = dscc.models.state.state(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                storage_pool_id = 4,
                system_id = '7CE809P009',
                total_reserved_mi_b = 1806336,
                total_size_mi_b = 122880,
                total_size_raw_mi_b = 163839,
                type = 'string',
                user_space = dscc.models.snap_space.snapSpace(
                    ld_count = 4, 
                    total_mi_b = 83968, 
                    total_raw_mi_b = 251904, 
                    used_mi_b = 75008, 
                    used_raw_mi_b = 225024, ),
                warn_percent = 5
            )
        else:
            return PrimeraPoolDetails(
        )
        """

    def testPrimeraPoolDetails(self):
        """Test PrimeraPoolDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
