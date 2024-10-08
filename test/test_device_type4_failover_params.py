# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_failover_params import DeviceType4FailoverParams

class TestDeviceType4FailoverParams(unittest.TestCase):
    """DeviceType4FailoverParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4FailoverParams:
        """Test DeviceType4FailoverParams
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4FailoverParams`
        """
        model = DeviceType4FailoverParams()
        if include_optional:
            return DeviceType4FailoverParams(
                force_pp_failover = True,
                no_snapshot = True,
                skip_promote = True,
                target_name = 's1511'
            )
        else:
            return DeviceType4FailoverParams(
        )
        """

    def testDeviceType4FailoverParams(self):
        """Test DeviceType4FailoverParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
