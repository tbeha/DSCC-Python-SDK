# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.create_volume_input import CreateVolumeInput

class TestCreateVolumeInput(unittest.TestCase):
    """CreateVolumeInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateVolumeInput:
        """Test CreateVolumeInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateVolumeInput`
        """
        model = CreateVolumeInput()
        if include_optional:
            return CreateVolumeInput(
                comments = 'test',
                count = 2,
                data_reduction = True,
                name = '<resource_name>',
                size_mib = 16384,
                snap_cpg = 'SSD_r6',
                snapshot_alloc_warning = 5,
                user_alloc_warning = 5,
                user_cpg = 'SSD_r6'
            )
        else:
            return CreateVolumeInput(
                name = '<resource_name>',
                size_mib = 16384,
                user_cpg = 'SSD_r6',
        )
        """

    def testCreateVolumeInput(self):
        """Test CreateVolumeInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
