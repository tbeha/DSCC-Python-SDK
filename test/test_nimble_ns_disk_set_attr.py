# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_ns_disk_set_attr import NimbleNsDiskSetAttr

class TestNimbleNsDiskSetAttr(unittest.TestCase):
    """NimbleNsDiskSetAttr unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleNsDiskSetAttr:
        """Test NimbleNsDiskSetAttr
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleNsDiskSetAttr`
        """
        model = NimbleNsDiskSetAttr()
        if include_optional:
            return NimbleNsDiskSetAttr(
                ave_mb_ps = 0,
                ave_segment_ps = 0,
                ave_ttc = 0,
                driveset = 0,
                is_capacity_valid = False,
                is_flash_shelf = False,
                pause_state = 0,
                pct_completion = 0,
                raw_cache_capacity = 34359738368,
                raw_capacity = 476741369856,
                sw_state = 'online',
                usable_cache_capacity = 244695092429,
                usable_capacity = 244695092429
            )
        else:
            return NimbleNsDiskSetAttr(
        )
        """

    def testNimbleNsDiskSetAttr(self):
        """Test NimbleNsDiskSetAttr"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
