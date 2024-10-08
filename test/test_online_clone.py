# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.online_clone import OnlineClone

class TestOnlineClone(unittest.TestCase):
    """OnlineClone unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OnlineClone:
        """Test OnlineClone
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OnlineClone`
        """
        model = OnlineClone()
        if include_optional:
            return OnlineClone(
                auto_lun = True,
                destination_cpg = 'SSD_r6',
                destination_snapshot_cpg = 'SSD_r6',
                host_group_id = 'fd3244ef7f1ab8bd16500c7a41bdf8f8',
                lun = 0
            )
        else:
            return OnlineClone(
        )
        """

    def testOnlineClone(self):
        """Test OnlineClone"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
