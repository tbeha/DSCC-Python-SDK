# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_associated_links_inner import DeviceType4AssociatedLinksInner

class TestDeviceType4AssociatedLinksInner(unittest.TestCase):
    """DeviceType4AssociatedLinksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4AssociatedLinksInner:
        """Test DeviceType4AssociatedLinksInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4AssociatedLinksInner`
        """
        model = DeviceType4AssociatedLinksInner()
        if include_optional:
            return DeviceType4AssociatedLinksInner(
                resource_uri = '',
                type = ''
            )
        else:
            return DeviceType4AssociatedLinksInner(
        )
        """

    def testDeviceType4AssociatedLinksInner(self):
        """Test DeviceType4AssociatedLinksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
