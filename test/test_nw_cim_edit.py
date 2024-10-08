# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nw_cim_edit import NwCimEdit

class TestNwCimEdit(unittest.TestCase):
    """NwCimEdit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NwCimEdit:
        """Test NwCimEdit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NwCimEdit`
        """
        model = NwCimEdit()
        if include_optional:
            return NwCimEdit(
                cim = dscc.models.nw_cim_edit_cim.nwCimEdit_cim(
                    cim_policy = True, 
                    enable_cim_service = True, 
                    http_state = True, 
                    https_state = True, 
                    id = '', 
                    slp_state = True, )
            )
        else:
            return NwCimEdit(
        )
        """

    def testNwCimEdit(self):
        """Test NwCimEdit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
