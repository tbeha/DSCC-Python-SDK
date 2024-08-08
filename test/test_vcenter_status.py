# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.vcenter_status import VcenterStatus

class TestVcenterStatus(unittest.TestCase):
    """VcenterStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VcenterStatus:
        """Test VcenterStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VcenterStatus`
        """
        model = VcenterStatus()
        if include_optional:
            return VcenterStatus(
                default = 'Ok',
                key = 'VMPERF_FAILED'
            )
        else:
            return VcenterStatus(
        )
        """

    def testVcenterStatus(self):
        """Test VcenterStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
