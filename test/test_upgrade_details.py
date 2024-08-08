# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.upgrade_details import UpgradeDetails

class TestUpgradeDetails(unittest.TestCase):
    """UpgradeDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpgradeDetails:
        """Test UpgradeDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpgradeDetails`
        """
        model = UpgradeDetails()
        if include_optional:
            return UpgradeDetails(
                messages = [
                    dscc.models.nimble_error_with_arguments.NimbleErrorWithArguments(
                        code = 13, 
                        severity = 'info', 
                        text = 'Error occurred.', )
                    ],
                stage = 'finish',
                state = 'in_progress',
                type = 'offline'
            )
        else:
            return UpgradeDetails(
        )
        """

    def testUpgradeDetails(self):
        """Test UpgradeDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
