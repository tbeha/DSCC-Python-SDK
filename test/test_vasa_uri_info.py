# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.vasa_uri_info import VasaUriInfo

class TestVasaUriInfo(unittest.TestCase):
    """VasaUriInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VasaUriInfo:
        """Test VasaUriInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VasaUriInfo`
        """
        model = VasaUriInfo()
        if include_optional:
            return VasaUriInfo(
                is_valid = 1,
                uri = 'https://xppa6614.in.rdlabs.hpecorp.net:9997/vasa'
            )
        else:
            return VasaUriInfo(
        )
        """

    def testVasaUriInfo(self):
        """Test VasaUriInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
