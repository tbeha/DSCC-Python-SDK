# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.drift_buckets_inner import DriftBucketsInner

class TestDriftBucketsInner(unittest.TestCase):
    """DriftBucketsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DriftBucketsInner:
        """Test DriftBucketsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DriftBucketsInner`
        """
        model = DriftBucketsInner()
        if include_optional:
            return DriftBucketsInner(
                bucket_name = 128,
                bucket_unit = 'KiB',
                magnitude = 1.64
            )
        else:
            return DriftBucketsInner(
        )
        """

    def testDriftBucketsInner(self):
        """Test DriftBucketsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
