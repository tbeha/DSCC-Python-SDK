# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.api.vvolscs_api import VvolscsApi


class TestVvolscsApi(unittest.TestCase):
    """VvolscsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VvolscsApi()

    def tearDown(self) -> None:
        pass

    def test_device_type1_attach_detach_vol_sc(self) -> None:
        """Test case for device_type1_attach_detach_vol_sc

        Attach host to Storage container identified by {vvolscId} from Primera / Alletra 9K
        """
        pass

    def test_device_type1_createv_vol_sc(self) -> None:
        """Test case for device_type1_createv_vol_sc

        Creates VMware storage container on storage system Primera / Alletra 9K identified by {systemId}
        """
        pass

    def test_device_type1_edit_vol_sc(self) -> None:
        """Test case for device_type1_edit_vol_sc

        Edit Storage container identified by {vvolscId} from Primera / Alletra 9K
        """
        pass

    def test_device_type4_attach_vol_sc(self) -> None:
        """Test case for device_type4_attach_vol_sc

        Attach host to Storage container identified by {vvolscId} from HPE Alletra Storage MP
        """
        pass

    def test_device_type4_createv_vol_sc(self) -> None:
        """Test case for device_type4_createv_vol_sc

        Creates VMware storage container on storage system HPE Alletra Storage MP identified by {systemId}
        """
        pass

    def test_device_type4_detach_vol_sc(self) -> None:
        """Test case for device_type4_detach_vol_sc

        Detach host to Storage container identified by {vvolscId} from HPE Alletra Storage MP
        """
        pass


if __name__ == '__main__':
    unittest.main()
