# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.edit_replication_partner import EditReplicationPartner

class TestEditReplicationPartner(unittest.TestCase):
    """EditReplicationPartner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditReplicationPartner:
        """Test EditReplicationPartner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditReplicationPartner`
        """
        model = EditReplicationPartner()
        if include_optional:
            return EditReplicationPartner(
                control_port = 1024,
                data_port = 1024,
                description = '99.9999% availability',
                remote_partner_id = '005319ed73385876a4000000000000000000000006',
                repl_hostname = '15.213.204.121',
                source = dscc.models.edit_source_partner.EditSourcePartner(
                    hostname = '15.213.204.163', 
                    name = 'replicationPartner1', 
                    subnet_label = 'myobject-5', 
                    subnet_type = 'mgmt', ),
                subnet_label = 'myobject-5',
                subnet_type = 'mgmt',
                target = dscc.models.edit_target_partner.EditTargetPartner(
                    hostname = '15.213.204.164', 
                    name = 'replicationPartner2', 
                    subnet_label = 'myobject-5', 
                    subnet_type = 'mgmt', ),
                target_system_id = '005319ed73385876a4000000000000000000000001',
                throttles = [
                    dscc.models.replication_throttle.ReplicationThrottle(
                        days = 'example day', 
                        description = 'Throttle one', 
                        name = 'Throttle1', 
                        thr_at_time = 10800, 
                        thr_bandwidth = 14, 
                        thr_until_time = 14400, )
                    ]
            )
        else:
            return EditReplicationPartner(
        )
        """

    def testEditReplicationPartner(self):
        """Test EditReplicationPartner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
