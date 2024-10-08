# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.edit_date_timezone_settings import EditDateTimezoneSettings

class TestEditDateTimezoneSettings(unittest.TestCase):
    """EditDateTimezoneSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditDateTimezoneSettings:
        """Test EditDateTimezoneSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditDateTimezoneSettings`
        """
        model = EditDateTimezoneSettings()
        if include_optional:
            return EditDateTimezoneSettings(
                var_date = 1598267193,
                ntp_server = '0.abc.pool.ntp.org',
                timezone = 'America/Los_Angeles'
            )
        else:
            return EditDateTimezoneSettings(
        )
        """

    def testEditDateTimezoneSettings(self):
        """Test EditDateTimezoneSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
