# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.policy import Policy

class TestPolicy(unittest.TestCase):
    """Policy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Policy:
        """Test Policy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Policy`
        """
        model = Policy()
        if include_optional:
            return Policy(
                file_service = True,
                host_dif3par = True,
                host_dif_std = True,
                no_cache = True,
                one_host = True,
                stale_snapshot = True,
                system = True,
                zero_detect = True,
                zero_fill = True
            )
        else:
            return Policy(
        )
        """

    def testPolicy(self):
        """Test Policy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
