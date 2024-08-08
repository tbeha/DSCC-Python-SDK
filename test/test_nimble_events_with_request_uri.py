# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_events_with_request_uri import NimbleEventsWithRequestUri

class TestNimbleEventsWithRequestUri(unittest.TestCase):
    """NimbleEventsWithRequestUri unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleEventsWithRequestUri:
        """Test NimbleEventsWithRequestUri
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleEventsWithRequestUri`
        """
        model = NimbleEventsWithRequestUri()
        if include_optional:
            return NimbleEventsWithRequestUri(
                request_uri = 'api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817/events/2a0df0fe6f7dc7bb16000000000000000000004007',
                alarm_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                category = 'hardware',
                event_type = 10,
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                scope = 'AC-109084',
                severity = 'info',
                target = 'volumes in performance policy default',
                target_type = 'array',
                timestamp = 3400,
                activity = 'Created snapshot % of volume %',
                associated_links = [{resourceUri=/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817, type=storage-systems}],
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'null',
                customer_id = 'string',
                generation = 0,
                resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817',
                summary = '',
                type = 'string'
            )
        else:
            return NimbleEventsWithRequestUri(
        )
        """

    def testNimbleEventsWithRequestUri(self):
        """Test NimbleEventsWithRequestUri"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
