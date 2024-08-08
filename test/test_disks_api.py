# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.api.disks_api import DisksApi


class TestDisksApi(unittest.TestCase):
    """DisksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DisksApi()

    def tearDown(self) -> None:
        pass

    def test_device_type2_disk_edit(self) -> None:
        """Test case for device_type2_disk_edit

        Edit details of Nimble / Alletra 6K disk identified by {diskId}
        """
        pass

    def test_device_type2_get_all_disks(self) -> None:
        """Test case for device_type2_get_all_disks

        Get all disks details by Nimble / Alletra 6K
        """
        pass

    def test_device_type2_get_disk_by_id(self) -> None:
        """Test case for device_type2_get_disk_by_id

        Get details of Nimble / Alletra 6K disk identified by {diskId}
        """
        pass


if __name__ == '__main__':
    unittest.main()
