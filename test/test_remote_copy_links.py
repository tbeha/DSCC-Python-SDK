# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.remote_copy_links import RemoteCopyLinks

class TestRemoteCopyLinks(unittest.TestCase):
    """RemoteCopyLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoteCopyLinks:
        """Test RemoteCopyLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemoteCopyLinks`
        """
        model = RemoteCopyLinks()
        if include_optional:
            return RemoteCopyLinks(
                items = [
                    dscc.models.remote_copy_link.RemoteCopyLink(
                        ipc = 'RCs12', 
                        display_name = 'sp2bh_1_3_1', 
                        domain = 'domain1', 
                        id = '5a5ce66d4814a5e5156de428abb0a58a', 
                        name = 'sp2bh_1_3_1', 
                        partner_name = 'RCPartner12', 
                        port = '1079', 
                        port_pos = null, 
                        rc_link_id = 1, 
                        remote_address = '20230002AC020CEG', 
                        remote_id = '6b5ce66d4814a5e5156de428abb0a79a', 
                        remote_port_pos = null, 
                        remote_state = 'UNKNOWN', 
                        remote_status = 'Down', 
                        source_address = '20230002AC020CEF', 
                        state = 'UNKNOWN', 
                        status = 'Down', 
                        system_id = 'SGH000XWEE', 
                        system_wwn = '2FF70002AC020CEF', 
                        throughput_k_byte_sec = 1024, 
                        type = 2, )
                    ],
                total = 1
            )
        else:
            return RemoteCopyLinks(
        )
        """

    def testRemoteCopyLinks(self):
        """Test RemoteCopyLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
