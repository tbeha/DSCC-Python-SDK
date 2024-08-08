# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_export_app_set_post_host_group_data_map_inner import DeviceType4ExportAppSetPostHostGroupDataMapInner

class TestDeviceType4ExportAppSetPostHostGroupDataMapInner(unittest.TestCase):
    """DeviceType4ExportAppSetPostHostGroupDataMapInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4ExportAppSetPostHostGroupDataMapInner:
        """Test DeviceType4ExportAppSetPostHostGroupDataMapInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4ExportAppSetPostHostGroupDataMapInner`
        """
        model = DeviceType4ExportAppSetPostHostGroupDataMapInner()
        if include_optional:
            return DeviceType4ExportAppSetPostHostGroupDataMapInner(
                host_group_id = 'cb17544e9347145d22a0fac608831053',
                nvme_transport_type = 'TCP'
            )
        else:
            return DeviceType4ExportAppSetPostHostGroupDataMapInner(
        )
        """

    def testDeviceType4ExportAppSetPostHostGroupDataMapInner(self):
        """Test DeviceType4ExportAppSetPostHostGroupDataMapInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
