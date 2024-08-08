# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.api.audit_event_api import AuditEventApi


class TestAuditEventApi(unittest.TestCase):
    """AuditEventApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuditEventApi()

    def tearDown(self) -> None:
        pass

    def test_device_type2_get_events(self) -> None:
        """Test case for device_type2_get_events

        Get all events of Nimble / Alletra 6K
        """
        pass

    def test_device_type2_get_events_using_event_id(self) -> None:
        """Test case for device_type2_get_events_using_event_id

        Get all events of Nimble / Alletra 6K identified by {eventId}
        """
        pass


if __name__ == '__main__':
    unittest.main()
