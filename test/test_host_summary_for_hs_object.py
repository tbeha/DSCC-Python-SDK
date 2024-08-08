# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.host_summary_for_hs_object import HostSummaryForHSObject

class TestHostSummaryForHSObject(unittest.TestCase):
    """HostSummaryForHSObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HostSummaryForHSObject:
        """Test HostSummaryForHSObject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HostSummaryForHSObject`
        """
        model = HostSummaryForHSObject()
        if include_optional:
            return HostSummaryForHSObject(
                id = '6848ef683c27403e96caa51816ddc72c',
                initiators = [
                    dscc.models.initiator_summary.InitiatorSummary(
                        address = '100008F1EABFE61C', 
                        id = 'd548ef683c27403e96caa51816ddc72c', 
                        ip_address = '15.212.100.100', 
                        name = 'init1', 
                        protocol = 'FC', 
                        systems = [
                            ''
                            ], )
                    ],
                ip_address = '15.212.100.100',
                is_mergable = True,
                is_vvol_host = True,
                marked_for_delete = True,
                name = 'host1',
                systems = [
                    ''
                    ],
                user_created = True
            )
        else:
            return HostSummaryForHSObject(
        )
        """

    def testHostSummaryForHSObject(self):
        """Test HostSummaryForHSObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
