# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.attach_detachv_vol_sc_input import AttachDetachvVolSCInput

class TestAttachDetachvVolSCInput(unittest.TestCase):
    """AttachDetachvVolSCInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttachDetachvVolSCInput:
        """Test AttachDetachvVolSCInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttachDetachvVolSCInput`
        """
        model = AttachDetachvVolSCInput()
        if include_optional:
            return AttachDetachvVolSCInput(
                action = 'ATTACH_VVOLSC',
                host_ids = ["c62b999dee0a4cb48c8805bfbc30b47d"],
                host_set_ids = ["a586833a8e1e4bb986d6073e682e6b12"]
            )
        else:
            return AttachDetachvVolSCInput(
        )
        """

    def testAttachDetachvVolSCInput(self):
        """Test AttachDetachvVolSCInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
