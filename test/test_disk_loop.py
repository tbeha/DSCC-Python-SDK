# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.disk_loop import DiskLoop

class TestDiskLoop(unittest.TestCase):
    """DiskLoop unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiskLoop:
        """Test DiskLoop
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiskLoop`
        """
        model = DiskLoop()
        if include_optional:
            return DiskLoop(
                degraded = False,
                disabled = False,
                port = dscc.models.disk_port_position.diskPortPosition(
                    node = 0, 
                    port = 2, 
                    slot = 0, ),
                primary = False
            )
        else:
            return DiskLoop(
        )
        """

    def testDiskLoop(self):
        """Test DiskLoop"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
