# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_remove_certificates_input import DeviceType4RemoveCertificatesInput

class TestDeviceType4RemoveCertificatesInput(unittest.TestCase):
    """DeviceType4RemoveCertificatesInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4RemoveCertificatesInput:
        """Test DeviceType4RemoveCertificatesInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4RemoveCertificatesInput`
        """
        model = DeviceType4RemoveCertificatesInput()
        if include_optional:
            return DeviceType4RemoveCertificatesInput(
                certificates = [
                    dscc.models.device_type4_remove_certificate_input.DeviceType4RemoveCertificateInput(
                        certificate = '99691e493067b2b2acf1774fc0ccc011', )
                    ]
            )
        else:
            return DeviceType4RemoveCertificatesInput(
                certificates = [
                    dscc.models.device_type4_remove_certificate_input.DeviceType4RemoveCertificateInput(
                        certificate = '99691e493067b2b2acf1774fc0ccc011', )
                    ],
        )
        """

    def testDeviceType4RemoveCertificatesInput(self):
        """Test DeviceType4RemoveCertificatesInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
