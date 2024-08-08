# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_move_volume_to_another_pool_input import NimbleMoveVolumeToAnotherPoolInput

class TestNimbleMoveVolumeToAnotherPoolInput(unittest.TestCase):
    """NimbleMoveVolumeToAnotherPoolInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleMoveVolumeToAnotherPoolInput:
        """Test NimbleMoveVolumeToAnotherPoolInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleMoveVolumeToAnotherPoolInput`
        """
        model = NimbleMoveVolumeToAnotherPoolInput()
        if include_optional:
            return NimbleMoveVolumeToAnotherPoolInput(
                dest_pool_id = '0a00000000000004d3000000000000000000000001'
            )
        else:
            return NimbleMoveVolumeToAnotherPoolInput(
                dest_pool_id = '0a00000000000004d3000000000000000000000001',
        )
        """

    def testNimbleMoveVolumeToAnotherPoolInput(self):
        """Test NimbleMoveVolumeToAnotherPoolInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
