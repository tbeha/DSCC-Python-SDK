# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.import_certificate_input import ImportCertificateInput

class TestImportCertificateInput(unittest.TestCase):
    """ImportCertificateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportCertificateInput:
        """Test ImportCertificateInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportCertificateInput`
        """
        model = ImportCertificateInput()
        if include_optional:
            return ImportCertificateInput(
                authority_chain = '-----BEGIN CERTIFICATE REQUEST-----abc----END CERTIFICATE REQUEST----- \n-----BEGIN CERTIFICATE REQUEST-----pqr----END CERTIFICATE REQUEST-----',
                certificate = '-----BEGIN CERTIFICATE REQUEST-----abc----END CERTIFICATE REQUEST-----'
            )
        else:
            return ImportCertificateInput(
                authority_chain = '-----BEGIN CERTIFICATE REQUEST-----abc----END CERTIFICATE REQUEST----- \n-----BEGIN CERTIFICATE REQUEST-----pqr----END CERTIFICATE REQUEST-----',
                certificate = '-----BEGIN CERTIFICATE REQUEST-----abc----END CERTIFICATE REQUEST-----',
        )
        """

    def testImportCertificateInput(self):
        """Test ImportCertificateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
