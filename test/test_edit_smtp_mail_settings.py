# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.edit_smtp_mail_settings import EditSmtpMailSettings

class TestEditSmtpMailSettings(unittest.TestCase):
    """EditSmtpMailSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditSmtpMailSettings:
        """Test EditSmtpMailSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditSmtpMailSettings`
        """
        model = EditSmtpMailSettings()
        if include_optional:
            return EditSmtpMailSettings(
                smtp_port = 25,
                smtp_server = 'example.hpe.com'
            )
        else:
            return EditSmtpMailSettings(
        )
        """

    def testEditSmtpMailSettings(self):
        """Test EditSmtpMailSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
