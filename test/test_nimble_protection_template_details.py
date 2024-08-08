# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_protection_template_details import NimbleProtectionTemplateDetails

class TestNimbleProtectionTemplateDetails(unittest.TestCase):
    """NimbleProtectionTemplateDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleProtectionTemplateDetails:
        """Test NimbleProtectionTemplateDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleProtectionTemplateDetails`
        """
        model = NimbleProtectionTemplateDetails()
        if include_optional:
            return NimbleProtectionTemplateDetails(
                agent_username = 'myobject-5',
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817","type":"storage-systems"}],
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'null',
                customer_id = 'string',
                description = 'Provides hourly snapshots retained for 2 days, daily snapshots retained for 30 days, and weekly snapshots retained for 52 weeks.',
                full_name = 'Retain-48Hourly-30Daily-52Weekly',
                generation = 0,
                repl_priority = 'normal',
                resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817',
                schedule_list = [
                    dscc.models.nimble_ns_schedule.NimbleNsSchedule(
                        active = False, 
                        at_time = 0, 
                        days = 'all', 
                        disable_appsync = True, 
                        downstream_partner = 'abc', 
                        downstream_partner_id = '0c1c9973433673c3db000000000000000000000008', 
                        downstream_partner_name = 'abc', 
                        id = '0c1c9973433673c3db000000000000000000000008', 
                        mfa_protected = True, 
                        name = 'daily', 
                        num_retain = 30, 
                        num_retain_replica = 0, 
                        period = 1, 
                        period_unit = 'days', 
                        repl_alert_thres = 86400, 
                        replicate_every = 0, 
                        schedule_id = '0c1c9973433673c3db000000000000000000000008', 
                        schedule_name = 'daily', 
                        schedule_type = 'regular', 
                        skip_db_consistency_check = False, 
                        snap_verify = True, 
                        until_time = 86399, )
                    ],
                search_name = 'Retain-48Hourly-30Daily-52Weekly',
                type = 'string',
                vcenter_username = 'myobject-5'
            )
        else:
            return NimbleProtectionTemplateDetails(
        )
        """

    def testNimbleProtectionTemplateDetails(self):
        """Test NimbleProtectionTemplateDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
