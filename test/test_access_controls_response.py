# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.access_controls_response import AccessControlsResponse

class TestAccessControlsResponse(unittest.TestCase):
    """AccessControlsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessControlsResponse:
        """Test AccessControlsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessControlsResponse`
        """
        model = AccessControlsResponse()
        if include_optional:
            return AccessControlsResponse(
                items = ["volume.create","port.read"]
            )
        else:
            return AccessControlsResponse(
                items = ["volume.create","port.read"],
        )
        """

    def testAccessControlsResponse(self):
        """Test AccessControlsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
