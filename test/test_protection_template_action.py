# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.protection_template_action import ProtectionTemplateAction

class TestProtectionTemplateAction(unittest.TestCase):
    """ProtectionTemplateAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProtectionTemplateAction:
        """Test ProtectionTemplateAction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProtectionTemplateAction`
        """
        model = ProtectionTemplateAction()
        if include_optional:
            return ProtectionTemplateAction(
                protection_template_id = '3a0df0fe6f7dc7bb16000000000000000000003467'
            )
        else:
            return ProtectionTemplateAction(
        )
        """

    def testProtectionTemplateAction(self):
        """Test ProtectionTemplateAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
