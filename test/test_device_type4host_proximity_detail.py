# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4host_proximity_detail import DeviceType4hostProximityDetail

class TestDeviceType4hostProximityDetail(unittest.TestCase):
    """DeviceType4hostProximityDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4hostProximityDetail:
        """Test DeviceType4hostProximityDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4hostProximityDetail`
        """
        model = DeviceType4hostProximityDetail()
        if include_optional:
            return DeviceType4hostProximityDetail(
                is_remote_array_support_replication = True,
                is_source_array_support_replication = True,
                local_system = 'CS2-A630-SVQ8',
                proximity_value = 'PRIMARY',
                remote_system = 's2937'
            )
        else:
            return DeviceType4hostProximityDetail(
        )
        """

    def testDeviceType4hostProximityDetail(self):
        """Test DeviceType4hostProximityDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
