# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.api.host_initiator_groups_api import HostInitiatorGroupsApi


class TestHostInitiatorGroupsApi(unittest.TestCase):
    """HostInitiatorGroupsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HostInitiatorGroupsApi()

    def tearDown(self) -> None:
        pass

    def test_bulk_merge_host_group(self) -> None:
        """Test case for bulk_merge_host_group

        Bulk merge hosts into user created host
        """
        pass

    def test_device_type2_get_all_host_initiator_groups(self) -> None:
        """Test case for device_type2_get_all_host_initiator_groups

        Get all nimble host initiator groups details by Nimble / Alletra 6K
        """
        pass

    def test_device_type2_get_host_initiator_group_by_id(self) -> None:
        """Test case for device_type2_get_host_initiator_group_by_id

        Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}
        """
        pass

    def test_device_type2_host_initiator_group_create(self) -> None:
        """Test case for device_type2_host_initiator_group_create

        Create Nimble / Alletra 6K initiator group in system identified by {systemId}
        """
        pass

    def test_device_type2_remove_host_initiator_group_by_id(self) -> None:
        """Test case for device_type2_remove_host_initiator_group_by_id

        Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K
        """
        pass

    def test_device_type2_update_host_initiator_group_by_id(self) -> None:
        """Test case for device_type2_update_host_initiator_group_by_id

        Update initiator-groups identified by {hostInitiatorGroupId}
        """
        pass

    def test_find_bulk_merge_candidates_for_host_groups(self) -> None:
        """Test case for find_bulk_merge_candidates_for_host_groups

        Get the list of host groups which have duplicates
        """
        pass

    def test_host_group_create(self) -> None:
        """Test case for host_group_create

        Create a host group
        """
        pass

    def test_host_group_delete(self) -> None:
        """Test case for host_group_delete

        Delete a host group by {hostGroupId}
        """
        pass

    def test_host_group_get_by_id(self) -> None:
        """Test case for host_group_get_by_id

        Get the host group details by {hostGroupId}
        """
        pass

    def test_host_group_list(self) -> None:
        """Test case for host_group_list

        Get the list of host groups
        """
        pass

    def test_host_group_merge(self) -> None:
        """Test case for host_group_merge

        Merge a host group
        """
        pass

    def test_host_group_update_by_id(self) -> None:
        """Test case for host_group_update_by_id

        Update host group by {hostGroupId}
        """
        pass


if __name__ == '__main__':
    unittest.main()
