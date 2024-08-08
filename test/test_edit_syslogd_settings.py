# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.edit_syslogd_settings import EditSyslogdSettings

class TestEditSyslogdSettings(unittest.TestCase):
    """EditSyslogdSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditSyslogdSettings:
        """Test EditSyslogdSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditSyslogdSettings`
        """
        model = EditSyslogdSettings()
        if include_optional:
            return EditSyslogdSettings(
                syslogd_enabled = True,
                syslogd_port = 1080,
                syslogd_server = 'sysloghost-1.com',
                syslogd_servers = [
                    dscc.models.nimble_syslogd_server_info.NimbleSyslogdServerInfo(
                        syslog_port = 1080, 
                        syslog_server = 'sysloghost-1.com', )
                    ]
            )
        else:
            return EditSyslogdSettings(
        )
        """

    def testEditSyslogdSettings(self):
        """Test EditSyslogdSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
