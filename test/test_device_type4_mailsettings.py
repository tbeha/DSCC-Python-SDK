# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_mailsettings import DeviceType4Mailsettings

class TestDeviceType4Mailsettings(unittest.TestCase):
    """DeviceType4Mailsettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4Mailsettings:
        """Test DeviceType4Mailsettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4Mailsettings`
        """
        model = DeviceType4Mailsettings()
        if include_optional:
            return DeviceType4Mailsettings(
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type4/7CE751P312","type":"systems"}],
                authentication_required = 'enabled',
                common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'data-ops-manager/storage-systems/device-type4/SGH014XGSP/settings/system-settings',
                customer_id = 'fc5f41652a53497e88cdcebc715cc1cq',
                friendly_cert = dscc.models.device_type4friendly_certificate.DeviceType4friendlyCertificate(
                    valid_from = dscc.models.device_type4friendly_certificate_valid_from.DeviceType4friendlyCertificate_ValidFrom(
                        ms = 1552301131000, 
                        tz = 'UTC', ), 
                    valid_until = dscc.models.device_type4friendly_certificate_valid_until.DeviceType4friendlyCertificate_ValidUntil(
                        ms = 1615416331000, 
                        tz = 'UTC', ), 
                    issued_to = 'example.hpe.com', 
                    issuer = 'CA', ),
                generation = 1627540911681,
                mail_host_domain = 'hpe.com',
                mail_host_server = 'example.hpe.com',
                port = 25,
                request_uri = '/api/v1/storage-systems/device-type4/7CE751P312/mailsettings',
                sender_email_id = 'someone@maildomain.com',
                type = 'mail-settings',
                username = 'username'
            )
        else:
            return DeviceType4Mailsettings(
        )
        """

    def testDeviceType4Mailsettings(self):
        """Test DeviceType4Mailsettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
