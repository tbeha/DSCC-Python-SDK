# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_system_latency_factors_latency_bands_read_inner import DeviceType4SystemLatencyFactorsLatencyBandsReadInner

class TestDeviceType4SystemLatencyFactorsLatencyBandsReadInner(unittest.TestCase):
    """DeviceType4SystemLatencyFactorsLatencyBandsReadInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4SystemLatencyFactorsLatencyBandsReadInner:
        """Test DeviceType4SystemLatencyFactorsLatencyBandsReadInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4SystemLatencyFactorsLatencyBandsReadInner`
        """
        model = DeviceType4SystemLatencyFactorsLatencyBandsReadInner()
        if include_optional:
            return DeviceType4SystemLatencyFactorsLatencyBandsReadInner(
                end_time = 1669880791,
                start_time = 1669880791,
                top_factors = [
                    ''
                    ]
            )
        else:
            return DeviceType4SystemLatencyFactorsLatencyBandsReadInner(
        )
        """

    def testDeviceType4SystemLatencyFactorsLatencyBandsReadInner(self):
        """Test DeviceType4SystemLatencyFactorsLatencyBandsReadInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
