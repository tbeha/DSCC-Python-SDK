# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.primera_host_list import PrimeraHostList

class TestPrimeraHostList(unittest.TestCase):
    """PrimeraHostList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrimeraHostList:
        """Test PrimeraHostList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrimeraHostList`
        """
        model = PrimeraHostList()
        if include_optional:
            return PrimeraHostList(
                items = [
                    dscc.models.primera_host_list_obj.PrimeraHostListObj(
                        agent = dscc.models.host_agent.HostAgent(
                            ip_addr = '10.15.12.136', 
                            architecture = 'SAN', 
                            boot_from_san = 'yes', 
                            cluster_id = '113245', 
                            cluster_name = 'SAN-cluster', 
                            cluster_software = 'Linux', 
                            cluster_version = 'v1.0.0', 
                            host_apps = 'mysql', 
                            last_updated = dscc.models.host_agent_last_updated.HostAgent_lastUpdated(
                                ms = 101780, 
                                tz = '123545', ), 
                            multi_path_software = 'OS', 
                            multi_path_software_version = 'v1.0.0', 
                            os = 'Linux', 
                            os_patch = 'v1.0.0', 
                            os_version = 'v1.0.0', 
                            reported_name = 'slvs', ), 
                        associated_links = [
                            dscc.models.associated_links_inner.AssociatedLinks_inner(
                                resource_uri = '', 
                                type = '', )
                            ], 
                        common_resource_attributes = dscc.models.common_resource_attributes_hosts.commonResourceAttributesHosts(
                            cloud_state = 'CONNECTED', ), 
                        descriptors = dscc.models.host_descriptors.HostDescriptors(
                            ip_addr = '1.1.1.1', 
                            comment = 'Comments', 
                            contact = '1234567788e', 
                            location = 'US', 
                            model = 'AIX', 
                            os = 'Linux', ), 
                        displayname = 'Drive 0.SIDE_NONE.2.0', 
                        domain = 'slt', 
                        generation = 1652172502, 
                        host_id = 101780, 
                        hostpaths = [
                            dscc.models.primera_host_paths_for_primera_host.PrimeraHostPathsForPrimeraHost(
                                ip_addr = '1.1.1.1', 
                                address = '810009440c9ce5824', 
                                displayname = 'Drive 0.SIDE_NONE.2.0', 
                                domain = '-', 
                                driver_version = 'v1.0.0', 
                                firmware_version = 'v1.0.0', 
                                generation = 1652172206, 
                                host_id = 101780, 
                                host_name = 'test-host', 
                                host_speed = 100, 
                                id = '1223f5s', 
                                model = 'model_1', 
                                path_type = 'FC', 
                                port_pos = dscc.models.device_type4_host_path_list_obj_port_pos.DeviceType4HostPathListObj_portPos(
                                    node = 1, 
                                    port = 1, 
                                    slot = 1, ), 
                                resource_uri = '/v1/storage-systems/host-paths/dbce79b2612cde02a6e0be8934c330ec', 
                                sc_host_initiator_id = '1223f5s', 
                                switch_port_wwn = '5001438026e98a60', 
                                system_uid = '7CE727P35M', 
                                system_wwn = 'swK21', 
                                uri = '/api/v3/hostpaths/dbce79b2612cde02a6e0be8934c330ec', 
                                vendor = '-', )
                            ], 
                        id = '132b493352ca3141456333edf403be0c', 
                        initiator_chap_enabled = True, 
                        initiator_chap_name = 'chapName', 
                        initiator_encrypted_chap_secret = 'secret', 
                        min_lun_id = 10, 
                        name = 'test-host', 
                        persona = dscc.models.persona.Persona(
                            capabilities = [
                                ''
                                ], 
                            id = 101780, 
                            name = 'test-host', ), 
                        resource_uri = '/api/v3/hosts/2492b4e84f7536577a38be78f0da0c1a', 
                        sc_host_id = '132b493352ca3141456333edf403be0c', 
                        state = dscc.models.state.State(
                            detailed = dscc.models.device_type4_host_state_detailed.DeviceType4HostState_detailed(
                                args = [
                                    ''
                                    ], 
                                default = 'Host sltestish', 
                                key = 'HOST_NAME', 
                                localized_text = 'Localized text of the resource capabilities', ), 
                            overall_state = 'NORMAL', ), 
                        state_description = [
                            ''
                            ], 
                        state_val = 1, 
                        system_uid = 'swK21', 
                        system_wwn = 'swK21', 
                        target_chap_enabled = True, 
                        target_chap_name = 'sltest1', 
                        target_encrypted_chap_secret = 'Target Encrypted Chap Secret', 
                        ua_rep_lun = True, 
                        uri = '/api/v3/hosts/2492b4e84f7536577a38be78f0da0c1a', )
                    ],
                page_limit = 1,
                page_offset = 1,
                request_uri = '/api/v1/storage-systems/device-type1/host-paths',
                total = 1
            )
        else:
            return PrimeraHostList(
        )
        """

    def testPrimeraHostList(self):
        """Test PrimeraHostList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
