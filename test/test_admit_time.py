# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.admit_time import AdmitTime

class TestAdmitTime(unittest.TestCase):
    """AdmitTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdmitTime:
        """Test AdmitTime
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdmitTime`
        """
        model = AdmitTime()
        if include_optional:
            return AdmitTime(
                ms = 1591599192000,
                tz = 'Asia/Calcutta'
            )
        else:
            return AdmitTime(
        )
        """

    def testAdmitTime(self):
        """Test AdmitTime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
