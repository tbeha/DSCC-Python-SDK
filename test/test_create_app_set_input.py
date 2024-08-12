# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.create_app_set_input import CreateAppSetInput

class TestCreateAppSetInput(unittest.TestCase):
    """CreateAppSetInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAppSetInput:
        """Test CreateAppSetInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAppSetInput`
        """
        model = CreateAppSetInput()
        if include_optional:
            return CreateAppSetInput(
                app_set_business_unit = 'HPE',
                app_set_comments = 'Edit appset',
                app_set_importance = 'MEDIUM',
                app_set_name = 'Appset_134',
                app_set_type = 'ORACLE_LOG',
                create_app_set_qos_config_input = dscc.models.create_app_set_qos_config_input.CreateAppSetQosConfigInput(
                    bandwidth_max_limit_ki_b = 100, 
                    enable = True, 
                    iops_max_limit = 1, ),
                custom_app_type = 'CustomWorkload_123',
                members = ["vol1","vol2"]
            )
        else:
            return CreateAppSetInput(
                app_set_name = 'Appset_134',
                app_set_type = 'ORACLE_LOG',
        )
        """

    def testCreateAppSetInput(self):
        """Test CreateAppSetInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
