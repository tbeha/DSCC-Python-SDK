# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.primera_protection_policy import PrimeraProtectionPolicy

class TestPrimeraProtectionPolicy(unittest.TestCase):
    """PrimeraProtectionPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrimeraProtectionPolicy:
        """Test PrimeraProtectionPolicy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrimeraProtectionPolicy`
        """
        model = PrimeraProtectionPolicy()
        if include_optional:
            return PrimeraProtectionPolicy(
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                customer_id = 'string',
                generation = 0,
                policy = dscc.models.primera_protection_policy_policy.PrimeraProtectionPolicy_policy(
                    auto_recover = True, 
                    auto_synchronize = True, 
                    is_protection_policy_configured = True, 
                    no_automatic_synchronization = False, 
                    non_zero_rto_config = 'ActiveSync', 
                    over_period_alert = True, 
                    remote = dscc.models.remote.remote(), 
                    rpo_secs = 600, 
                    secondary_remote = dscc.models.secondary_remote.secondaryRemote(), 
                    zero_rto_config = 'PP', ),
                protection_policy_type = 'sync',
                schedules = dscc.models.primera_protection_policy_schedules.PrimeraProtectionPolicy_schedules(
                    items = [
                        dscc.models.primera_schedule.PrimeraSchedule(
                            at_time = 8, 
                            customer_id = 'fc5f41652a53497e88cdcebc715cc1cf', 
                            day_of_month = 4, 
                            days = 'sunday,monday', 
                            expire_secs = 86400, 
                            generation = 123, 
                            id = 'fa43500317062d6f025ec9ca54bab123', 
                            is_alert_enabled = True, 
                            is_paused = True, 
                            is_remote = True, 
                            is_system_task = False, 
                            name = 'Every_1_hour_on_sunday_monday', 
                            next_run_time = 1622873100, 
                            period = 1, 
                            period_unit = 'hours', 
                            retain_secs = 3600, 
                            status = 'Active', 
                            system_wwn = '2FF70002AC020CEF', 
                            type = 'schedules', 
                            until_time = 15, 
                            user = '3paradm', )
                        ], 
                    total = 1, ),
                type = 'string'
            )
        else:
            return PrimeraProtectionPolicy(
        )
        """

    def testPrimeraProtectionPolicy(self):
        """Test PrimeraProtectionPolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
