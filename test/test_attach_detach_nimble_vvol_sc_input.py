# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.attach_detach_nimble_vvol_sc_input import AttachDetachNimbleVvolSCInput

class TestAttachDetachNimbleVvolSCInput(unittest.TestCase):
    """AttachDetachNimbleVvolSCInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttachDetachNimbleVvolSCInput:
        """Test AttachDetachNimbleVvolSCInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttachDetachNimbleVvolSCInput`
        """
        model = AttachDetachNimbleVvolSCInput()
        if include_optional:
            return AttachDetachNimbleVvolSCInput(
                action = 'ATTACH_VVOLSC',
                host_initiator_group_ids = ["b58856f40db14f109186810b61bf72e9"],
                host_initiators_ids = ["7c021a70a50e4437a13bd08542a75667"]
            )
        else:
            return AttachDetachNimbleVvolSCInput(
        )
        """

    def testAttachDetachNimbleVvolSCInput(self):
        """Test AttachDetachNimbleVvolSCInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
