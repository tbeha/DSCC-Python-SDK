# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.syscapacity import Syscapacity

class TestSyscapacity(unittest.TestCase):
    """Syscapacity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Syscapacity:
        """Test Syscapacity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Syscapacity`
        """
        model = Syscapacity()
        if include_optional:
            return Syscapacity(
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type1/{uid}","type":"systems"}],
                capacity_by_tier = dscc.models.capacity_by_tier.capacityByTier(
                    fc_free = 0, 
                    fc_used = 0, 
                    nl_free = 58368, 
                    nl_used = 17408, 
                    ssd_free = 0, 
                    ssd_used = 0, 
                    total_used = 17408, 
                    usable_capacity = 58368, ),
                capacity_detail = dscc.models.system_detailed_capacity.SystemDetailedCapacity(
                    snap_space = 228565.15, 
                    volume_space = 233359.43, ),
                capacity_summary = dscc.models.system_capacity_summary.systemCapacitySummary(
                    allocated = dscc.models.allocated.allocated(
                        cpgs = 0, 
                        cpgs_free = 0, 
                        cpgs_private = 0, 
                        cpgs_private_base = dscc.models.private.private(
                            reserved = 1.337, 
                            reserved_v_vols = 1.337, 
                            total = 1.337, ), 
                        cpgs_private_snap = dscc.models.private.private(
                            reserved = 1.337, 
                            reserved_v_vols = 1.337, 
                            total = 1.337, ), 
                        cpgs_shared = 0, 
                        legacy_volumes = 0, 
                        legacy_volumes_snap = 0, 
                        legacy_volumes_user = 0, 
                        system = 3782656, 
                        system_admin = 0, 
                        system_internal = 122880, 
                        system_spare = 3659776, 
                        system_spare_unused = 3659776, 
                        system_spare_used = 0, 
                        total = 7152640, 
                        unmapped = 0, ), 
                    allocated_percentage = 0.23703678566580696, 
                    compaction = 8384.594860579551, 
                    compression = 1.337, 
                    data_reduction = 1.337, 
                    dedup = 1.337, 
                    failed = 2048, 
                    failed_percentage = 0.00006787023211619383, 
                    free = 23020544, 
                    free_initialized = 23020544, 
                    free_percentage = 0.7628953441020768, 
                    free_uninitialized = 1.337, 
                    over_provisioning = 0.08, 
                    total = 30175232, 
                    unavailable = 0, 
                    unavailable_percentage = 0, ),
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                customer_id = 'string',
                fc_capacity_summary = dscc.models.system_capacity_summary.systemCapacitySummary(
                    allocated = dscc.models.allocated.allocated(
                        cpgs = 0, 
                        cpgs_free = 0, 
                        cpgs_private = 0, 
                        cpgs_private_base = dscc.models.private.private(
                            reserved = 1.337, 
                            reserved_v_vols = 1.337, 
                            total = 1.337, ), 
                        cpgs_private_snap = dscc.models.private.private(
                            reserved = 1.337, 
                            reserved_v_vols = 1.337, 
                            total = 1.337, ), 
                        cpgs_shared = 0, 
                        legacy_volumes = 0, 
                        legacy_volumes_snap = 0, 
                        legacy_volumes_user = 0, 
                        system = 3782656, 
                        system_admin = 0, 
                        system_internal = 122880, 
                        system_spare = 3659776, 
                        system_spare_unused = 3659776, 
                        system_spare_used = 0, 
                        total = 7152640, 
                        unmapped = 0, ), 
                    allocated_percentage = 0.23703678566580696, 
                    compaction = 8384.594860579551, 
                    compression = 1.337, 
                    data_reduction = 1.337, 
                    dedup = 1.337, 
                    failed = 2048, 
                    failed_percentage = 0.00006787023211619383, 
                    free = 23020544, 
                    free_initialized = 23020544, 
                    free_percentage = 0.7628953441020768, 
                    free_uninitialized = 1.337, 
                    over_provisioning = 0.08, 
                    total = 30175232, 
                    unavailable = 0, 
                    unavailable_percentage = 0, ),
                id = '',
                nl_capacity_summary = dscc.models.system_capacity_summary.systemCapacitySummary(
                    allocated = dscc.models.allocated.allocated(
                        cpgs = 0, 
                        cpgs_free = 0, 
                        cpgs_private = 0, 
                        cpgs_private_base = dscc.models.private.private(
                            reserved = 1.337, 
                            reserved_v_vols = 1.337, 
                            total = 1.337, ), 
                        cpgs_private_snap = dscc.models.private.private(
                            reserved = 1.337, 
                            reserved_v_vols = 1.337, 
                            total = 1.337, ), 
                        cpgs_shared = 0, 
                        legacy_volumes = 0, 
                        legacy_volumes_snap = 0, 
                        legacy_volumes_user = 0, 
                        system = 3782656, 
                        system_admin = 0, 
                        system_internal = 122880, 
                        system_spare = 3659776, 
                        system_spare_unused = 3659776, 
                        system_spare_used = 0, 
                        total = 7152640, 
                        unmapped = 0, ), 
                    allocated_percentage = 0.23703678566580696, 
                    compaction = 8384.594860579551, 
                    compression = 1.337, 
                    data_reduction = 1.337, 
                    dedup = 1.337, 
                    failed = 2048, 
                    failed_percentage = 0.00006787023211619383, 
                    free = 23020544, 
                    free_initialized = 23020544, 
                    free_percentage = 0.7628953441020768, 
                    free_uninitialized = 1.337, 
                    over_provisioning = 0.08, 
                    total = 30175232, 
                    unavailable = 0, 
                    unavailable_percentage = 0, ),
                request_uri = '/api/v1/storage-systems/device-type1/7CE751P312/capacity-summary',
                resource_uri = '/api/v1/storage-systems/device-type1/7CE751P312/capacity-summary',
                ssd_capacity_summary = dscc.models.system_capacity_summary.systemCapacitySummary(
                    allocated = dscc.models.allocated.allocated(
                        cpgs = 0, 
                        cpgs_free = 0, 
                        cpgs_private = 0, 
                        cpgs_private_base = dscc.models.private.private(
                            reserved = 1.337, 
                            reserved_v_vols = 1.337, 
                            total = 1.337, ), 
                        cpgs_private_snap = dscc.models.private.private(
                            reserved = 1.337, 
                            reserved_v_vols = 1.337, 
                            total = 1.337, ), 
                        cpgs_shared = 0, 
                        legacy_volumes = 0, 
                        legacy_volumes_snap = 0, 
                        legacy_volumes_user = 0, 
                        system = 3782656, 
                        system_admin = 0, 
                        system_internal = 122880, 
                        system_spare = 3659776, 
                        system_spare_unused = 3659776, 
                        system_spare_used = 0, 
                        total = 7152640, 
                        unmapped = 0, ), 
                    allocated_percentage = 0.23703678566580696, 
                    compaction = 8384.594860579551, 
                    compression = 1.337, 
                    data_reduction = 1.337, 
                    dedup = 1.337, 
                    failed = 2048, 
                    failed_percentage = 0.00006787023211619383, 
                    free = 23020544, 
                    free_initialized = 23020544, 
                    free_percentage = 0.7628953441020768, 
                    free_uninitialized = 1.337, 
                    over_provisioning = 0.08, 
                    total = 30175232, 
                    unavailable = 0, 
                    unavailable_percentage = 0, ),
                system_id = '7CE751P312',
                utilization_summary = dscc.models.utilization_summary.utilizationSummary(
                    capacity_usage_data = dscc.models.device_type4utilization_summary_capacity_usage_data.DeviceType4utilizationSummary_capacityUsageData(
                        free_size_mi_b = 7240704, 
                        used_size_mi_b = 3072, ), 
                    provisioned_capacity = 16384, )
            )
        else:
            return Syscapacity(
        )
        """

    def testSyscapacity(self):
        """Test Syscapacity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
