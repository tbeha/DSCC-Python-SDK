# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.service_ports_list import ServicePortsList

class TestServicePortsList(unittest.TestCase):
    """ServicePortsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicePortsList:
        """Test ServicePortsList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServicePortsList`
        """
        model = ServicePortsList()
        if include_optional:
            return ServicePortsList(
                items = [
                    dscc.models.service_ports.servicePorts(
                        common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                            cloud_state = 'CONNECTED', ), 
                        customer_id = 'string', 
                        domain = 'domain_name', 
                        generation = 0, 
                        id = 'f5306b97759d80aab4bb5dcdf28dfff3', 
                        ipv4address = '169.254.77.160', 
                        ipv4netmask = '255.255.0.0', 
                        ipv6address = 'fe80::cbf3:360d:9ad:996a', 
                        ipv6vnetmask = '64', 
                        mode = 'Service', 
                        name = 'Name_1', 
                        node = '0', 
                        resource_uri = '/v1/storage-systems/device-type1/7CE751P312/nodes/0/serviceports', 
                        system_id = '7CE751P312', 
                        type = 'string', )
                    ],
                page_limit = 1,
                page_offset = 1,
                request_uri = '/v1/storage-systems/device-type1/{systemUid}/nodes/serviceports',
                total = 2
            )
        else:
            return ServicePortsList(
        )
        """

    def testServicePortsList(self):
        """Test ServicePortsList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
