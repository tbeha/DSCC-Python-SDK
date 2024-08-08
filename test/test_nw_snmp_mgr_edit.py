# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nw_snmp_mgr_edit import NwSnmpMgrEdit

class TestNwSnmpMgrEdit(unittest.TestCase):
    """NwSnmpMgrEdit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NwSnmpMgrEdit:
        """Test NwSnmpMgrEdit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NwSnmpMgrEdit`
        """
        model = NwSnmpMgrEdit()
        if include_optional:
            return NwSnmpMgrEdit(
                manager_ip = '15.218.169.163',
                notify = 'STANDARD',
                port = 162,
                retry = 2,
                timeout_secs = 162,
                user = 'user1',
                version = 2
            )
        else:
            return NwSnmpMgrEdit(
        )
        """

    def testNwSnmpMgrEdit(self):
        """Test NwSnmpMgrEdit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
