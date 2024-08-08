# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.sys_locate_input import SysLocateInput

class TestSysLocateInput(unittest.TestCase):
    """SysLocateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SysLocateInput:
        """Test SysLocateInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SysLocateInput`
        """
        model = SysLocateInput()
        if include_optional:
            return SysLocateInput(
                locate_enabled = True
            )
        else:
            return SysLocateInput(
        )
        """

    def testSysLocateInput(self):
        """Test SysLocateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
