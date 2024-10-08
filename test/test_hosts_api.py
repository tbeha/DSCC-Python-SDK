# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.api.hosts_api import HostsApi


class TestHostsApi(unittest.TestCase):
    """HostsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HostsApi()

    def tearDown(self) -> None:
        pass

    def test_device_type1_get_all_hosts(self) -> None:
        """Test case for device_type1_get_all_hosts

        Get details of Primera / Alletra 9K Hosts
        """
        pass

    def test_device_type1_get_host_by_id(self) -> None:
        """Test case for device_type1_get_host_by_id

        Get details of Primera / Alletra 9K Host identified by {HostId}
        """
        pass

    def test_device_type4_get_all_hosts(self) -> None:
        """Test case for device_type4_get_all_hosts

        Get details of HPE Alletra Storage MP Hosts
        """
        pass

    def test_device_type4_get_host_by_id(self) -> None:
        """Test case for device_type4_get_host_by_id

        Get details of HPE Alletra Storage MP Host identified by {HostId}
        """
        pass


if __name__ == '__main__':
    unittest.main()
