# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.volume_post import VolumePost

class TestVolumePost(unittest.TestCase):
    """VolumePost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VolumePost:
        """Test VolumePost
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VolumePost`
        """
        model = VolumePost()
        if include_optional:
            return VolumePost(
                comment = '',
                custom_name = 'snap1',
                expire_secs = 86400,
                name_pattern = 'PARENT_TIMESTAMP',
                read_only = False,
                retain_secs = 86400
            )
        else:
            return VolumePost(
                name_pattern = 'PARENT_TIMESTAMP',
        )
        """

    def testVolumePost(self):
        """Test VolumePost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
