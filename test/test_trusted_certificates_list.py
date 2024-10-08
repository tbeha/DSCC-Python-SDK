# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.trusted_certificates_list import TrustedCertificatesList

class TestTrustedCertificatesList(unittest.TestCase):
    """TrustedCertificatesList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrustedCertificatesList:
        """Test TrustedCertificatesList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrustedCertificatesList`
        """
        model = TrustedCertificatesList()
        if include_optional:
            return TrustedCertificatesList(
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                commonname = 'c3-hp-eskm-01',
                detail = dscc.models.trusted_certificate_details_detail.trustedCertificateDetails_detail(
                    default = 'Valid Certificate', 
                    key = 'CERTIFICATE_VALID', ),
                domain = 'hpe.com',
                enddate = dscc.models.trusted_certificate_details_enddate.trustedCertificateDetails_enddate(
                    ms = 1611599192000, 
                    tz = 'Local', ),
                fingerprint = '2e92f97ad86fdcfff295841fefe20a1d71944923',
                hash = '47efc91a.0',
                id = '99691e493067b2b2acf1774fc0ccc011',
                issuer = 'CN=c3-hp-eskm-01',
                isvalid = True,
                key_usage = '',
                pem = '-----BEGIN CERTIFICATE REQUEST-----abc----END CERTIFICATE REQUEST-----',
                serial = '0',
                signaturetype = 'self-signed',
                startdate = dscc.models.trusted_certificate_details_startdate.trustedCertificateDetails_startdate(
                    ms = 1591789652000, 
                    tz = 'Local', ),
                subject = 'CN=c3-hp-eskm-01',
                system_id = '7CE809P009',
                type = 'other',
                uri = '/api/v3/trustcerts/99691e493067b2b2acf1774fc0ccc011'
            )
        else:
            return TrustedCertificatesList(
        )
        """

    def testTrustedCertificatesList(self):
        """Test TrustedCertificatesList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
