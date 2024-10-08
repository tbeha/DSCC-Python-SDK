# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_telemetry_status import DeviceType4TelemetryStatus

class TestDeviceType4TelemetryStatus(unittest.TestCase):
    """DeviceType4TelemetryStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4TelemetryStatus:
        """Test DeviceType4TelemetryStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4TelemetryStatus`
        """
        model = DeviceType4TelemetryStatus()
        if include_optional:
            return DeviceType4TelemetryStatus(
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type4/{uid}","type":"systems"}],
                collection_server = '',
                connectivity_status = 'NORMAL',
                connectivity_test_time = dscc.models.device_type4_telemetry_status_connectivity_test_time.DeviceType4TelemetryStatus_connectivityTestTime(
                    ms = 1599631885, 
                    tz = 'Asia/Kolkata', ),
                details = [
                    dscc.models.device_type4details_inner.DeviceType4details_inner(
                        args = [
                            dscc.models.device_type4details_inner_args_inner.DeviceType4details_inner_args_inner(
                                ms = 1599631885, 
                                tz = 'Asia/Kolkata', )
                            ], 
                        default = '', 
                        key = '', )
                    ],
                id = '',
                last_file_sent = '',
                last_file_transfer_time = dscc.models.device_type4_telemetry_status_last_file_transfer_time.DeviceType4TelemetryStatus_lastFileTransferTime(
                    ms = 1599631885, 
                    tz = 'Asia/Kolkata', ),
                last_successful_connectivity_test_time = dscc.models.device_type4_telemetry_status_last_successful_connectivity_test_time.DeviceType4TelemetryStatus_lastSuccessfulConnectivityTestTime(
                    ms = 1599631885, 
                    tz = 'Asia/Kolkata', ),
                proxy_connectivity = 'NORMAL',
                r_da_configured = 'NORMAL',
                r_da_status = 'NORMAL',
                r_sv_s_status = 'NORMAL',
                r_ts_status = 'NORMAL',
                request_uri = '/api/v1/storage-systems/device-type4/7CE751P312/telemetryStatus',
                resource_uri = '/api/v1/storage-systems/device-type4/7CE751P312/telemetryStatus',
                rolled_up_status = 'NORMAL',
                shared_volume_status = 'NORMAL',
                transfer_status = 'NORMAL'
            )
        else:
            return DeviceType4TelemetryStatus(
        )
        """

    def testDeviceType4TelemetryStatus(self):
        """Test DeviceType4TelemetryStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
