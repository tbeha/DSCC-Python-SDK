# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.common_resource_attributes_primera_host import CommonResourceAttributesPrimeraHost

class TestCommonResourceAttributesPrimeraHost(unittest.TestCase):
    """CommonResourceAttributesPrimeraHost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonResourceAttributesPrimeraHost:
        """Test CommonResourceAttributesPrimeraHost
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonResourceAttributesPrimeraHost`
        """
        model = CommonResourceAttributesPrimeraHost()
        if include_optional:
            return CommonResourceAttributesPrimeraHost(
                cloud_state = 'CONNECTED'
            )
        else:
            return CommonResourceAttributesPrimeraHost(
        )
        """

    def testCommonResourceAttributesPrimeraHost(self):
        """Test CommonResourceAttributesPrimeraHost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
