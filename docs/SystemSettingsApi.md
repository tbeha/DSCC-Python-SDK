# dscc.SystemSettingsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_trusted_certificates**](SystemSettingsApi.md#add_trusted_certificates) | **POST** /api/v1/storage-systems/device-type1/{systemId}/trust-certificates | Add trusted certificates for storage system Primera / Alletra 9K identified by {systemId}
[**alert_contacts_create**](SystemSettingsApi.md#alert_contacts_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/alert-contacts | Add Alert/Mail contact details
[**alert_contacts_delete**](SystemSettingsApi.md#alert_contacts_delete) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/alert-contacts/{id} | Delete Alert/Email contact of storage system Primera / Alletra 9K identified by {id}
[**alert_contacts_update**](SystemSettingsApi.md#alert_contacts_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/alert-contacts/{id} | Edit Alert/Email contact details of storage system Primera / Alletra 9K identified by {id}
[**device_type1_alert_contacts_get_by_id**](SystemSettingsApi.md#device_type1_alert_contacts_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/alert-contacts/{id} | Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}
[**device_type1_alert_contacts_list**](SystemSettingsApi.md#device_type1_alert_contacts_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/alert-contacts | Get alert-contact details for a storage system Primera / Alletra 9K
[**device_type1_certificates_get_by_id**](SystemSettingsApi.md#device_type1_certificates_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/certificates/{id} | Get array certificates by Primera / Alletra 9K identified by {id}
[**device_type1_certificates_list**](SystemSettingsApi.md#device_type1_certificates_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/certificates | Get array certificates by Primera / Alletra 9K
[**device_type1_delete_quorum_witness**](SystemSettingsApi.md#device_type1_delete_quorum_witness) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/system-settings/quorum-witness/{replicationPartnerId} | Delete quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_delete_v_center_settings**](SystemSettingsApi.md#device_type1_delete_v_center_settings) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/vm-manager-settings/{vcenterSettingId} | Delete vcenter setting identified by {vcenterSettingId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_get_quorum_witness**](SystemSettingsApi.md#device_type1_get_quorum_witness) | **GET** /api/v1/storage-systems/device-type1/{systemId}/system-settings/quorum-witness | Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_get_quorum_witness_with_id**](SystemSettingsApi.md#device_type1_get_quorum_witness_with_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/system-settings/quorum-witness/{replicationPartnerId} | Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_get_replication_partner_with_id**](SystemSettingsApi.md#device_type1_get_replication_partner_with_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/system-settings/replication-partners/{replicationPartnerId} | Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_get_replication_partners**](SystemSettingsApi.md#device_type1_get_replication_partners) | **GET** /api/v1/storage-systems/device-type1/{systemId}/system-settings/replication-partners | Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_mail_settings_get**](SystemSettingsApi.md#device_type1_mail_settings_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/mail-settings | Get the system&#39;s SMTP/Mail server settigs
[**device_type1_network_service_cim_get**](SystemSettingsApi.md#device_type1_network_service_cim_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/network-services/cim | Get CIM Network-Service details for a storage system Primera / Alletra 9K
[**device_type1_network_service_configure_vasa_service**](SystemSettingsApi.md#device_type1_network_service_configure_vasa_service) | **POST** /api/v1/storage-systems/device-type1/{systemId}/network-services/vasa/{vasaId}/services | Configures vasa service for the specified id.
[**device_type1_network_service_snmp_mgr_get_by_id**](SystemSettingsApi.md#device_type1_network_service_snmp_mgr_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/network-services/snmp-mgr/{id} | Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
[**device_type1_network_service_snmp_mgr_list**](SystemSettingsApi.md#device_type1_network_service_snmp_mgr_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/network-services/snmp-mgr | Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
[**device_type1_network_service_vasa_configure**](SystemSettingsApi.md#device_type1_network_service_vasa_configure) | **POST** /api/v1/storage-systems/device-type1/{systemId}/network-services/vasa/{vasaId} | Configures vasa service for the specified id.
[**device_type1_network_service_vasa_get**](SystemSettingsApi.md#device_type1_network_service_vasa_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/network-services/vasa | Get VASA Network-Service details for a storage system Primera / Alletra 9K
[**device_type1_network_settings_get**](SystemSettingsApi.md#device_type1_network_settings_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/network-settings | Get Network-Settings details for a storage system Primera / Alletra 9K
[**device_type1_node_service_ports_get_by_id**](SystemSettingsApi.md#device_type1_node_service_ports_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/service-ports | Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }
[**device_type1_node_service_ports_list**](SystemSettingsApi.md#device_type1_node_service_ports_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/service-ports | Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}
[**device_type1_post_quorum_witness**](SystemSettingsApi.md#device_type1_post_quorum_witness) | **POST** /api/v1/storage-systems/device-type1/{systemId}/system-settings/quorum-witness | Create quorum witness on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_post_remove_replication_partners**](SystemSettingsApi.md#device_type1_post_remove_replication_partners) | **POST** /api/v1/storage-systems/device-type1/{systemId}/system-settings/replication-partners/remove | Delete replication partner from storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_post_replication_partners**](SystemSettingsApi.md#device_type1_post_replication_partners) | **POST** /api/v1/storage-systems/device-type1/{systemId}/system-settings/replication-partners | Create replication partners on Primera / Alletra 9K identified by {systemId}
[**device_type1_post_v_center_settings**](SystemSettingsApi.md#device_type1_post_v_center_settings) | **POST** /api/v1/storage-systems/device-type1/{systemId}/vm-manager-settings | Add vCenter settings to storage system Primera / Alletra 9K
[**device_type1_put_quorum_witness**](SystemSettingsApi.md#device_type1_put_quorum_witness) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/system-settings/quorum-witness/{replicationPartnerId} | Edit quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_put_replication_partner**](SystemSettingsApi.md#device_type1_put_replication_partner) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/system-settings/replication-partners/{replicationPartnerId} | Edit replication partner identified by {replicationPartnerId} on Primera / Alletra 9K identified by {systemId}
[**device_type1_put_v_center_settings**](SystemSettingsApi.md#device_type1_put_v_center_settings) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/vm-manager-settings/{vcenterSettingId} | Edit vCenter setting identified by {vcenterSettingId} on Primera / Alletra 9K identified by {systemId}
[**device_type1_remote_copy_links_performance_history_get**](SystemSettingsApi.md#device_type1_remote_copy_links_performance_history_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/remotecopylinks-performance | Get details of performance metrics of Primera/ Alletra 9K remote copy links on storage system identified by {systemid}
[**device_type1_storage_container_delete_by_id**](SystemSettingsApi.md#device_type1_storage_container_delete_by_id) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/system-settings/management-services/vvolscs/{vvolscId} | Delete storage container of  storage system Primera / Alletra 9K identified by {id}
[**device_type1_storage_container_get**](SystemSettingsApi.md#device_type1_storage_container_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/system-settings/management-services/vvolscs | Get Storage Container details for a storage system Primera / Alletra 9K
[**device_type1_support_data_collect**](SystemSettingsApi.md#device_type1_support_data_collect) | **POST** /api/v1/storage-systems/device-type1/{systemId}/collect-support-data | Trigger a collection on the storage system Primera / Alletra 9K
[**device_type1_support_settings_get**](SystemSettingsApi.md#device_type1_support_settings_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/support-settings | Get support settings for a storage system Primera / Alletra 9K
[**device_type1_system_settings_list**](SystemSettingsApi.md#device_type1_system_settings_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/system-settings | Get the system settings configuration details
[**device_type1_telemetry_get**](SystemSettingsApi.md#device_type1_telemetry_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/telemetry | Get telemetry status for a storage system Primera / Alletra 9K
[**device_type1_trusted_certificates_get_by_id**](SystemSettingsApi.md#device_type1_trusted_certificates_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/trust-certificates/{id} | Get certificates trusted by Primera / Alletra 9K identified by {id}
[**device_type1_trusted_certificates_list**](SystemSettingsApi.md#device_type1_trusted_certificates_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/trust-certificates | Get certificates trusted by Primera / Alletra 9K
[**device_type1_vm_manager_settings_get_by_id**](SystemSettingsApi.md#device_type1_vm_manager_settings_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/vm-manager-settings/{vcenterSettingId} | Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K
[**device_type1_vm_manager_settings_list**](SystemSettingsApi.md#device_type1_vm_manager_settings_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/vm-manager-settings | Get vcenter settings for a storage system Primera / Alletra 9K
[**device_type2_application_server_create**](SystemSettingsApi.md#device_type2_application_server_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/application-servers | Create Nimble / Alletra 6K application server in system identified by {systemId}
[**device_type2_application_server_edit**](SystemSettingsApi.md#device_type2_application_server_edit) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/application-servers/{applicationServerId} | Modify Nimble / Alletra 6K application server in system identified by {systemId}
[**device_type2_create_replication_partners**](SystemSettingsApi.md#device_type2_create_replication_partners) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners | Create replication partner pair for Nimble / Alletra 6K
[**device_type2_create_witness**](SystemSettingsApi.md#device_type2_create_witness) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/witnesses | Create a new witness configuration Nimble / Alletra 6K
[**device_type2_edit_mail_settings**](SystemSettingsApi.md#device_type2_edit_mail_settings) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/mail-settings | Edit Nimble Mail Settings of Nimble / Alletra 6K
[**device_type2_edit_network_setting_by_id**](SystemSettingsApi.md#device_type2_edit_network_setting_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/network-settings/{networkSettingId} | Edit Nimble / Alletra 6K network setting identified by {networkSettingId}
[**device_type2_edit_replication_partners_by_id**](SystemSettingsApi.md#device_type2_edit_replication_partners_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/{replicationpartnerId} | Edit a replication partner for Nimble / Alletra 6K given by replicationpartnerId
[**device_type2_edit_system_settings**](SystemSettingsApi.md#device_type2_edit_system_settings) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/system-settings | Edit system settings of Nimble / Alletra 6K
[**device_type2_get_all_application_servers**](SystemSettingsApi.md#device_type2_get_all_application_servers) | **GET** /api/v1/storage-systems/device-type2/{systemId}/application-servers | Get all application servers details by Nimble / Alletra 6K
[**device_type2_get_all_network_settings**](SystemSettingsApi.md#device_type2_get_all_network_settings) | **GET** /api/v1/storage-systems/device-type2/{systemId}/network-settings | Get all network settings details by Nimble / Alletra 6K
[**device_type2_get_application_server_by_id**](SystemSettingsApi.md#device_type2_get_application_server_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/application-servers/{applicationServerId} | Get details of Nimble / Alletra 6K application server identified by {applicationServerId}
[**device_type2_get_network_setting_by_id**](SystemSettingsApi.md#device_type2_get_network_setting_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/network-settings/{networkSettingId} | Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}
[**device_type2_get_replication_partners**](SystemSettingsApi.md#device_type2_get_replication_partners) | **GET** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners | Get all replication-partners details for Nimble / Alletra 6K
[**device_type2_get_replication_partners_by_id**](SystemSettingsApi.md#device_type2_get_replication_partners_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/{replicationpartnerId} | Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}
[**device_type2_get_witnesses**](SystemSettingsApi.md#device_type2_get_witnesses) | **GET** /api/v1/storage-systems/device-type2/{systemId}/system-settings/witnesses | Get all witness configuration details by Nimble / Alletra 6K
[**device_type2_get_witnesses_by_id**](SystemSettingsApi.md#device_type2_get_witnesses_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/system-settings/witnesses/{witnessId} | Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}
[**device_type2_pause_replication_partner**](SystemSettingsApi.md#device_type2_pause_replication_partner) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/actions/pause | Pause the replication pair of Nimble / Alletra 6K
[**device_type2_remove_application_server_by_id**](SystemSettingsApi.md#device_type2_remove_application_server_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/application-servers/{applicationServerId} | Remove application server identified by {applicationServerId} from Nimble / Alletra 6K
[**device_type2_remove_replication_partner**](SystemSettingsApi.md#device_type2_remove_replication_partner) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/remove | Remove list of replication partner for Nimble / Alletra 6K
[**device_type2_remove_witnesses_by_id**](SystemSettingsApi.md#device_type2_remove_witnesses_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/system-settings/witnesses/{witnessId} | Remove witness identified by {witnessId} from Nimble / Alletra 6K
[**device_type2_resume_replication_partner**](SystemSettingsApi.md#device_type2_resume_replication_partner) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/actions/resume | Resume the replication pair of Nimble / Alletra 6K
[**device_type2_send_auto_support**](SystemSettingsApi.md#device_type2_send_auto_support) | **POST** /api/v1/storage-systems/device-type2/{systemId}/autosupport/actions/send | Send auto support information of Nimble / Alletra 6K identified by {systemId}
[**device_type2_test_replication_configuration**](SystemSettingsApi.md#device_type2_test_replication_configuration) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/actions/test | Test the replication partner pair of Nimble / Alletra 6K
[**device_type2_test_witnesses_by_id**](SystemSettingsApi.md#device_type2_test_witnesses_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/witnesses/{witnessId}/actions/test | Test and validate the witness configuration between the host identified by {witnessId} from Nimble / Alletra 6K identified by {systemId}
[**device_type4_add_trusted_certificates**](SystemSettingsApi.md#device_type4_add_trusted_certificates) | **POST** /api/v1/storage-systems/device-type4/{systemId}/trust-certificates | Add trusted certificates for storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_alert_contacts_create**](SystemSettingsApi.md#device_type4_alert_contacts_create) | **POST** /api/v1/storage-systems/device-type4/{systemId}/alert-contacts | Add Alert/Mail contact details
[**device_type4_alert_contacts_delete**](SystemSettingsApi.md#device_type4_alert_contacts_delete) | **DELETE** /api/v1/storage-systems/device-type4/{systemId}/alert-contacts/{id} | Delete Alert/Email contact of storage system HPE Alletra Storage MP identified by {id}
[**device_type4_alert_contacts_get_by_id**](SystemSettingsApi.md#device_type4_alert_contacts_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/alert-contacts/{id} | Get alert-contact details for a storage system HPE Alletra Storage MP identified by {id}
[**device_type4_alert_contacts_list**](SystemSettingsApi.md#device_type4_alert_contacts_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/alert-contacts | Get alert-contact details for a storage system HPE Alletra Storage MP
[**device_type4_alert_contacts_update**](SystemSettingsApi.md#device_type4_alert_contacts_update) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/alert-contacts/{id} | Edit Alert/Email contact details of storage system HPE Alletra Storage MP identified by {id}
[**device_type4_certificates_get_by_id**](SystemSettingsApi.md#device_type4_certificates_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/certificates/{id} | Get array certificates by HPE Alletra Storage MP identified by {id}
[**device_type4_certificates_list**](SystemSettingsApi.md#device_type4_certificates_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/certificates | Get array certificates by HPE Alletra Storage MP
[**device_type4_delete_quorum_witness**](SystemSettingsApi.md#device_type4_delete_quorum_witness) | **DELETE** /api/v1/storage-systems/device-type4/{systemId}/system-settings/quorum-witness/{replicationPartnerId} | Delete quorum witness identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_delete_v_center_settings**](SystemSettingsApi.md#device_type4_delete_v_center_settings) | **DELETE** /api/v1/storage-systems/device-type4/{systemId}/vm-manager-settings/{vcenterSettingId} | Delete vcenter setting identified by {vcenterSettingId} on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_enclosure_powers_sustainability**](SystemSettingsApi.md#device_type4_enclosure_powers_sustainability) | **GET** /api/v1/storage-systems/device-type4/{systemId}/sustainabilityMetrics | Get details of sustainability metrics of enclosure and system power supplies in Watts on storage system identified by {systemid}
[**device_type4_get_quorum_witness**](SystemSettingsApi.md#device_type4_get_quorum_witness) | **GET** /api/v1/storage-systems/device-type4/{systemId}/system-settings/quorum-witness | Get quorum witness configuration details from storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_get_quorum_witness_with_id**](SystemSettingsApi.md#device_type4_get_quorum_witness_with_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/system-settings/quorum-witness/{replicationPartnerId} | Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_get_replication_partner_with_id**](SystemSettingsApi.md#device_type4_get_replication_partner_with_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/system-settings/replication-partners/{replicationPartnerId} | Get details of replication partner identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_get_replication_partners**](SystemSettingsApi.md#device_type4_get_replication_partners) | **GET** /api/v1/storage-systems/device-type4/{systemId}/system-settings/replication-partners | Get details of replication partners on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_mail_settings_associate**](SystemSettingsApi.md#device_type4_mail_settings_associate) | **POST** /api/v1/storage-systems/device-type4/{systemId}/mail-settings | Add SMTP/Mail server settigs
[**device_type4_mail_settings_delete**](SystemSettingsApi.md#device_type4_mail_settings_delete) | **DELETE** /api/v1/storage-systems/device-type4/{systemId}/mail-settings | Delete SMTP/mail server settings
[**device_type4_mail_settings_get**](SystemSettingsApi.md#device_type4_mail_settings_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/mail-settings | Get the system&#39;s SMTP/Mail server settigs
[**device_type4_mail_settings_update**](SystemSettingsApi.md#device_type4_mail_settings_update) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/mail-settings | Edit SMTP/Mail server settigs
[**device_type4_network_service_cim_get**](SystemSettingsApi.md#device_type4_network_service_cim_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/network-services/cim | Get CIM Network-Service details for a storage system HPE Alletra Storage MP
[**device_type4_network_service_cim_update**](SystemSettingsApi.md#device_type4_network_service_cim_update) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/network-services/cim | Edit CIM network service configuration
[**device_type4_network_service_configure_vasa_service**](SystemSettingsApi.md#device_type4_network_service_configure_vasa_service) | **POST** /api/v1/storage-systems/device-type4/{systemId}/network-services/vasa/{vasaId}/services | Configures vasa service for the specified id.
[**device_type4_network_service_snmp_mgr_create**](SystemSettingsApi.md#device_type4_network_service_snmp_mgr_create) | **POST** /api/v1/storage-systems/device-type4/{systemId}/network-services/snmp-mgr | Add SNMP Manager settings
[**device_type4_network_service_snmp_mgr_delete**](SystemSettingsApi.md#device_type4_network_service_snmp_mgr_delete) | **DELETE** /api/v1/storage-systems/device-type4/{systemId}/network-services/snmp-mgr/{id} | Delete SNMP manager settings identified by {id}
[**device_type4_network_service_snmp_mgr_get_by_id**](SystemSettingsApi.md#device_type4_network_service_snmp_mgr_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/network-services/snmp-mgr/{id} | Get a specific SNMP-Manager Network-Service details for a storage system HPE Alletra Storage MP
[**device_type4_network_service_snmp_mgr_list**](SystemSettingsApi.md#device_type4_network_service_snmp_mgr_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/network-services/snmp-mgr | Get SNMP-Manager Network-Service details for a storage system HPE Alletra Storage MP
[**device_type4_network_service_snmp_mgr_update**](SystemSettingsApi.md#device_type4_network_service_snmp_mgr_update) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/network-services/snmp-mgr/{id} | Edit SNMP Manager settings for the specified Id
[**device_type4_network_service_vasa_configure**](SystemSettingsApi.md#device_type4_network_service_vasa_configure) | **POST** /api/v1/storage-systems/device-type4/{systemId}/network-services/vasa/{vasaId} | Configures vasa service for the specified id.
[**device_type4_network_service_vasa_get**](SystemSettingsApi.md#device_type4_network_service_vasa_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/network-services/vasa | Get VASA Network-Service details for a storage system Primera / Alletra 9K
[**device_type4_network_settings_associate**](SystemSettingsApi.md#device_type4_network_settings_associate) | **POST** /api/v1/storage-systems/device-type4/{systemId}/network-settings | Post Network-Settings details for a storage system HPE Alletra Storage MP
[**device_type4_network_settings_get**](SystemSettingsApi.md#device_type4_network_settings_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/network-settings | Get Network-Settings details for a storage system HPE Alletra Storage MP
[**device_type4_node_service_ports_get_by_id**](SystemSettingsApi.md#device_type4_node_service_ports_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/nodes/{nodeId}/service-ports | Get service ports for nodes of all storage systems of HPE Alletra Storage MP identified by {systemId} and {nodeId }
[**device_type4_node_service_ports_list**](SystemSettingsApi.md#device_type4_node_service_ports_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/nodes/service-ports | Get service ports for nodes of all storage systems of HPE Alletra Storage MP identified by {systemId}
[**device_type4_post_certificate**](SystemSettingsApi.md#device_type4_post_certificate) | **POST** /api/v1/storage-systems/device-type4/{systemId}/certificates | Create certificate on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_post_quorum_witness**](SystemSettingsApi.md#device_type4_post_quorum_witness) | **POST** /api/v1/storage-systems/device-type4/{systemId}/system-settings/quorum-witness | Create quorum witness on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_post_remove_replication_partners**](SystemSettingsApi.md#device_type4_post_remove_replication_partners) | **POST** /api/v1/storage-systems/device-type4/{systemId}/system-settings/replication-partners/remove | Delete replication partner from storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_post_replication_partners**](SystemSettingsApi.md#device_type4_post_replication_partners) | **POST** /api/v1/storage-systems/device-type4/{systemId}/system-settings/replication-partners | Create replication partners on HPE Alletra Storage MP identified by {systemId}
[**device_type4_post_v_center_settings**](SystemSettingsApi.md#device_type4_post_v_center_settings) | **POST** /api/v1/storage-systems/device-type4/{systemId}/vm-manager-settings | Add vCenter settings to storage system HPE Alletra Storage MP
[**device_type4_put_certificate**](SystemSettingsApi.md#device_type4_put_certificate) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/certificates/{id} | Import certificate identified by {id} on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_put_quorum_witness**](SystemSettingsApi.md#device_type4_put_quorum_witness) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/system-settings/quorum-witness/{replicationPartnerId} | Edit quorum witness identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_put_replication_partner**](SystemSettingsApi.md#device_type4_put_replication_partner) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/system-settings/replication-partners/{replicationPartnerId} | Edit replication partner identified by {replicationPartnerId} on HPE Alletra Storage MP identified by {systemId}
[**device_type4_put_v_center_settings**](SystemSettingsApi.md#device_type4_put_v_center_settings) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/vm-manager-settings/{vcenterSettingId} | Edit vCenter setting identified by {vcenterSettingId} on HPE Alletra Storage MP identified by {systemId}
[**device_type4_remote_copy_links_performance_history_get**](SystemSettingsApi.md#device_type4_remote_copy_links_performance_history_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/remotecopylinks-performance | Get details of performance metrics of remote copy links on storage system identified by {systemid}
[**device_type4_remove_certificates**](SystemSettingsApi.md#device_type4_remove_certificates) | **POST** /api/v1/storage-systems/device-type4/{systemId}/certificates/remove | Delete certificates from storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_remove_trusted_certificates**](SystemSettingsApi.md#device_type4_remove_trusted_certificates) | **POST** /api/v1/storage-systems/device-type4/{systemId}/trust-certificates/remove | Delete trusted certificates from storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_set_license**](SystemSettingsApi.md#device_type4_set_license) | **POST** /api/v1/storage-systems/device-type4/{systemId}/licenses | Set license of the storage system identified by {systemId}
[**device_type4_snmp_users_get_by_id**](SystemSettingsApi.md#device_type4_snmp_users_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/network-services/snmp-users/{id} | Get SNMP users identified by {id}
[**device_type4_snmp_users_list**](SystemSettingsApi.md#device_type4_snmp_users_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/network-services/snmp-users | Get SNMP users
[**device_type4_storage_container_delete_by_id**](SystemSettingsApi.md#device_type4_storage_container_delete_by_id) | **DELETE** /api/v1/storage-systems/device-type4/{systemId}/system-settings/management-services/vvolscs/{vvolscId} | Delete storage container of storage system HPE Alletra Storage MP identified by {id}
[**device_type4_storage_container_edit_by_id**](SystemSettingsApi.md#device_type4_storage_container_edit_by_id) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/system-settings/management-services/vvolscs/{vvolscId} | Edit storage container of storage system HPE Alletra Storage MP identified by {id}
[**device_type4_storage_container_get**](SystemSettingsApi.md#device_type4_storage_container_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/system-settings/management-services/vvolscs | Get Storage Container details for a storage system HPE Alletra Storage MP
[**device_type4_support_data_collect**](SystemSettingsApi.md#device_type4_support_data_collect) | **POST** /api/v1/storage-systems/device-type4/{systemId}/collect-support-data | Trigger a collection on the storage system HPE Alletra Storage MP
[**device_type4_support_settings_associate**](SystemSettingsApi.md#device_type4_support_settings_associate) | **POST** /api/v1/storage-systems/device-type4/{systemId}/support-settings | Add support settings for a storage system HPE Alletra Storage MP
[**device_type4_support_settings_get**](SystemSettingsApi.md#device_type4_support_settings_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/support-settings | Get support settings for a storage system HPE Alletra Storage MP
[**device_type4_support_settings_update**](SystemSettingsApi.md#device_type4_support_settings_update) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/support-settings | Edit support settings for a storage system HPE Alletra Storage MP
[**device_type4_system_settings_associate**](SystemSettingsApi.md#device_type4_system_settings_associate) | **POST** /api/v1/storage-systems/device-type4/{systemId}/system-settings | Edit system settings configuration
[**device_type4_system_settings_list**](SystemSettingsApi.md#device_type4_system_settings_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/system-settings | Get the system settings configuration details
[**device_type4_system_settings_update**](SystemSettingsApi.md#device_type4_system_settings_update) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/system-settings | Edit system settings configuration
[**device_type4_telemetry_get**](SystemSettingsApi.md#device_type4_telemetry_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/telemetry | Get telemetry status for a storage system HPE Alletra Storage MP
[**device_type4_trusted_certificates_get_by_id**](SystemSettingsApi.md#device_type4_trusted_certificates_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/trust-certificates/{id} | Get certificates trusted by HPE Alletra Storage MP identified by {id}
[**device_type4_trusted_certificates_list**](SystemSettingsApi.md#device_type4_trusted_certificates_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/trust-certificates | Get certificates trusted by HPE Alletra Storage MP
[**device_type4_vm_manager_settings_get_by_id**](SystemSettingsApi.md#device_type4_vm_manager_settings_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/vm-manager-settings/{vcenterSettingId} | Get vcenter setting detail for a given vcenter setting of a storage system HPE Alletra Storage MP
[**device_type4_vm_manager_settings_list**](SystemSettingsApi.md#device_type4_vm_manager_settings_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/vm-manager-settings | Get vcenter settings for a storage system HPE Alletra Storage MP
[**mail_settings_associate**](SystemSettingsApi.md#mail_settings_associate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/mail-settings | Add SMTP/Mail server settigs
[**mail_settings_delete**](SystemSettingsApi.md#mail_settings_delete) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/mail-settings | Delete SMTP/mail server settings
[**mail_settings_update**](SystemSettingsApi.md#mail_settings_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/mail-settings | Edit SMTP/Mail server settigs
[**network_service_cim_update**](SystemSettingsApi.md#network_service_cim_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/network-services/cim | Edit CIM network service configuration
[**network_service_snmp_mgr_create**](SystemSettingsApi.md#network_service_snmp_mgr_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/network-services/snmp-mgr | Add SNMP Manager settings
[**network_service_snmp_mgr_delete**](SystemSettingsApi.md#network_service_snmp_mgr_delete) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/network-services/snmp-mgr/{id} | Delete SNMP manager settings identified by {id}
[**network_service_snmp_mgr_update**](SystemSettingsApi.md#network_service_snmp_mgr_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/network-services/snmp-mgr/{id} | Edit SNMP Manager settings for the specified Id
[**network_settings_associate**](SystemSettingsApi.md#network_settings_associate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/network-settings | Post Network-Settings details for a storage system Primera / Alletra 9K
[**post_certificate**](SystemSettingsApi.md#post_certificate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/certificates | Create certificate on storage system Primera / Alletra 9K identified by {systemId}
[**put_certificate**](SystemSettingsApi.md#put_certificate) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/certificates/{id} | Import certificate identified by {id} on storage system Primera / Alletra 9K identified by {systemId}
[**remove_certificates**](SystemSettingsApi.md#remove_certificates) | **POST** /api/v1/storage-systems/device-type1/{systemId}/certificates/remove | Delete certificates from storage system Primera / Alletra 9K identified by {systemId}
[**remove_trusted_certificates**](SystemSettingsApi.md#remove_trusted_certificates) | **POST** /api/v1/storage-systems/device-type1/{systemId}/trust-certificates/remove | Delete trusted certificates from storage system Primera / Alletra 9K identified by {systemId}
[**support_settings_associate**](SystemSettingsApi.md#support_settings_associate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/support-settings | Add support settings for a storage system Primera / Alletra 9K
[**support_settings_update**](SystemSettingsApi.md#support_settings_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/support-settings | Edit support settings for a storage system Primera / Alletra 9K
[**system_settings_associate**](SystemSettingsApi.md#system_settings_associate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/system-settings | Edit system settings configuration
[**system_settings_update**](SystemSettingsApi.md#system_settings_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/system-settings | Edit system settings configuration


# **add_trusted_certificates**
> TaskResponse add_trusted_certificates(system_id, add_trusted_certificate_input)

Add trusted certificates for storage system Primera / Alletra 9K identified by {systemId}

Add trusted certificates for storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.add_trusted_certificate_input import AddTrustedCertificateInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    add_trusted_certificate_input = dscc.AddTrustedCertificateInput() # AddTrustedCertificateInput | 

    try:
        # Add trusted certificates for storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.add_trusted_certificates(system_id, add_trusted_certificate_input)
        print("The response of SystemSettingsApi->add_trusted_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->add_trusted_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **add_trusted_certificate_input** | [**AddTrustedCertificateInput**](AddTrustedCertificateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_contacts_create**
> TaskResponse alert_contacts_create(system_id, alert_contact_input)

Add Alert/Mail contact details

Add Alert/Mail contact details

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.alert_contact_input import AlertContactInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    alert_contact_input = dscc.AlertContactInput() # AlertContactInput | 

    try:
        # Add Alert/Mail contact details
        api_response = api_instance.alert_contacts_create(system_id, alert_contact_input)
        print("The response of SystemSettingsApi->alert_contacts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->alert_contacts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **alert_contact_input** | [**AlertContactInput**](AlertContactInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_contacts_delete**
> TaskResponse alert_contacts_delete(system_id, id)

Delete Alert/Email contact of storage system Primera / Alletra 9K identified by {id}

Delete Alert/Email contact of storage system Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a4c78226-69cd-b9e7-af3e-445ca8f8a655' # str | Unique Identifier of the alert contact

    try:
        # Delete Alert/Email contact of storage system Primera / Alletra 9K identified by {id}
        api_response = api_instance.alert_contacts_delete(system_id, id)
        print("The response of SystemSettingsApi->alert_contacts_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->alert_contacts_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Unique Identifier of the alert contact | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_contacts_update**
> TaskResponse alert_contacts_update(system_id, id, alert_contact_input)

Edit Alert/Email contact details of storage system Primera / Alletra 9K identified by {id}

Edit Alert/Email contact details of storage system Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.alert_contact_input import AlertContactInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a4c78226-69cd-b9e7-af3e-445ca8f8a655' # str | Unique Identifier of the alert contact
    alert_contact_input = dscc.AlertContactInput() # AlertContactInput | 

    try:
        # Edit Alert/Email contact details of storage system Primera / Alletra 9K identified by {id}
        api_response = api_instance.alert_contacts_update(system_id, id, alert_contact_input)
        print("The response of SystemSettingsApi->alert_contacts_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->alert_contacts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Unique Identifier of the alert contact | 
 **alert_contact_input** | [**AlertContactInput**](AlertContactInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_alert_contacts_get_by_id**
> AlertContactsDetailsList device_type1_alert_contacts_get_by_id(system_id, id, select=select)

Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}

Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.alert_contacts_details_list import AlertContactsDetailsList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a4c78226-69cd-b9e7-af3e-445ca8f8a655' # str | Unique Identifier of the alert contact
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}
        api_response = api_instance.device_type1_alert_contacts_get_by_id(system_id, id, select=select)
        print("The response of SystemSettingsApi->device_type1_alert_contacts_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_alert_contacts_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Unique Identifier of the alert contact | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**AlertContactsDetailsList**](AlertContactsDetailsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_alert_contacts_list**
> AlertContacts device_type1_alert_contacts_list(system_id, limit=limit, offset=offset, select=select)

Get alert-contact details for a storage system Primera / Alletra 9K

Get alert-contact details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.alert_contacts import AlertContacts
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get alert-contact details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_alert_contacts_list(system_id, limit=limit, offset=offset, select=select)
        print("The response of SystemSettingsApi->device_type1_alert_contacts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_alert_contacts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**AlertContacts**](AlertContacts.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_certificates_get_by_id**
> CertificateDetails device_type1_certificates_get_by_id(system_id, id, select=select)

Get array certificates by Primera / Alletra 9K identified by {id}

Get array certificates by Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.certificate_details import CertificateDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '99691e493067b2b2acf1774fc0ccc011' # str | ID of the certificate
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get array certificates by Primera / Alletra 9K identified by {id}
        api_response = api_instance.device_type1_certificates_get_by_id(system_id, id, select=select)
        print("The response of SystemSettingsApi->device_type1_certificates_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_certificates_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the certificate | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**CertificateDetails**](CertificateDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_certificates_list**
> CertificatesSummaryList device_type1_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)

Get array certificates by Primera / Alletra 9K

Get array certificates by Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.certificates_summary_list import CertificatesSummaryList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'service eq qw-client' # str | Lucene query to filter Certificates by Key. (optional)

    try:
        # Get array certificates by Primera / Alletra 9K
        api_response = api_instance.device_type1_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)
        print("The response of SystemSettingsApi->device_type1_certificates_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_certificates_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Certificates by Key. | [optional] 

### Return type

[**CertificatesSummaryList**](CertificatesSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_delete_quorum_witness**
> TaskResponse device_type1_delete_quorum_witness(system_id, replication_partner_id)

Delete quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Delete quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner

    try:
        # Delete quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_delete_quorum_witness(system_id, replication_partner_id)
        print("The response of SystemSettingsApi->device_type1_delete_quorum_witness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_delete_quorum_witness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_delete_v_center_settings**
> TaskResponse device_type1_delete_v_center_settings(system_id, vcenter_setting_id)

Delete vcenter setting identified by {vcenterSettingId} on storage system Primera / Alletra 9K identified by {systemId}

Delete vcenter setting identified by {vcenterSettingId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vcenter_setting_id = '7e92269a-12d1-35b4-60e8-5919edfc5475' # str | UID(vcenterSettingId) of the storage system

    try:
        # Delete vcenter setting identified by {vcenterSettingId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_delete_v_center_settings(system_id, vcenter_setting_id)
        print("The response of SystemSettingsApi->device_type1_delete_v_center_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_delete_v_center_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vcenter_setting_id** | **str**| UID(vcenterSettingId) of the storage system | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_quorum_witness**
> WitnessList device_type1_get_quorum_witness(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}

Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.witness_list import WitnessList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq afb4961e47212e5bc88dd35db5be5c83' # str | oData query to filter witness by key. (optional)
    sort = 'id desc' # str | oData query to sort witness resource by key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_quorum_witness(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SystemSettingsApi->device_type1_get_quorum_witness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_get_quorum_witness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter witness by key. | [optional] 
 **sort** | **str**| oData query to sort witness resource by key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**WitnessList**](WitnessList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_quorum_witness_with_id**
> WitnessDetails device_type1_get_quorum_witness_with_id(system_id, replication_partner_id, select=select)

Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.witness_details import WitnessDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_quorum_witness_with_id(system_id, replication_partner_id, select=select)
        print("The response of SystemSettingsApi->device_type1_get_quorum_witness_with_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_get_quorum_witness_with_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**WitnessDetails**](WitnessDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_replication_partner_with_id**
> ReplicationPartnerDetails device_type1_get_replication_partner_with_id(system_id, replication_partner_id, select=select)

Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.replication_partner_details import ReplicationPartnerDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_replication_partner_with_id(system_id, replication_partner_id, select=select)
        print("The response of SystemSettingsApi->device_type1_get_replication_partner_with_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_get_replication_partner_with_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ReplicationPartnerDetails**](ReplicationPartnerDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_replication_partners**
> ReplicationPartnersList device_type1_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)

Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}

Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.replication_partners_list import ReplicationPartnersList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemId eq 7CE751P312' # str | oData query to filter replication partners by key. (optional)
    sort = 'systemId desc' # str | oData query to sort nodes resource by key. (optional)
    include_indirect_partners = true # bool | Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)
        print("The response of SystemSettingsApi->device_type1_get_replication_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_get_replication_partners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter replication partners by key. | [optional] 
 **sort** | **str**| oData query to sort nodes resource by key. | [optional] 
 **include_indirect_partners** | **bool**| Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ReplicationPartnersList**](ReplicationPartnersList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_mail_settings_get**
> Mailsettings device_type1_mail_settings_get(system_id, select=select)

Get the system's SMTP/Mail server settigs

Get the system's SMTP/Mail server settigs

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.mailsettings import Mailsettings
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get the system's SMTP/Mail server settigs
        api_response = api_instance.device_type1_mail_settings_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type1_mail_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_mail_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**Mailsettings**](Mailsettings.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - System settings configuration information <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_cim_get**
> NetworkServicesCim device_type1_network_service_cim_get(system_id, select=select)

Get CIM Network-Service details for a storage system Primera / Alletra 9K

Get CIM Network-Service details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.network_services_cim import NetworkServicesCim
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get CIM Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_cim_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type1_network_service_cim_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_service_cim_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NetworkServicesCim**](NetworkServicesCim.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_configure_vasa_service**
> TaskResponse device_type1_network_service_configure_vasa_service(system_id, vasa_id, vasa_service_config)

Configures vasa service for the specified id.

Enables, disable and updates the cert management mode for vasa services on a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.vasa_service_config import VasaServiceConfig
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vasa_id = 'a9c455bf98fc1a6bdb90b824e3ac20b8' # str | ID of the VASA service
    vasa_service_config = dscc.VasaServiceConfig() # VasaServiceConfig | 

    try:
        # Configures vasa service for the specified id.
        api_response = api_instance.device_type1_network_service_configure_vasa_service(system_id, vasa_id, vasa_service_config)
        print("The response of SystemSettingsApi->device_type1_network_service_configure_vasa_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_service_configure_vasa_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vasa_id** | **str**| ID of the VASA service | 
 **vasa_service_config** | [**VasaServiceConfig**](VasaServiceConfig.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_snmp_mgr_get_by_id**
> NetworkServicesSnmp device_type1_network_service_snmp_mgr_get_by_id(system_id, id, select=select)

Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.network_services_snmp import NetworkServicesSnmp
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the SNMP manager
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_snmp_mgr_get_by_id(system_id, id, select=select)
        print("The response of SystemSettingsApi->device_type1_network_service_snmp_mgr_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_service_snmp_mgr_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the SNMP manager | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NetworkServicesSnmp**](NetworkServicesSnmp.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | SNMP Manager object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_snmp_mgr_list**
> NetworkServicesSnmp device_type1_network_service_snmp_mgr_list(system_id, limit=limit, offset=offset, select=select)

Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.network_services_snmp import NetworkServicesSnmp
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_snmp_mgr_list(system_id, limit=limit, offset=offset, select=select)
        print("The response of SystemSettingsApi->device_type1_network_service_snmp_mgr_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_service_snmp_mgr_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NetworkServicesSnmp**](NetworkServicesSnmp.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_vasa_configure**
> TaskResponse device_type1_network_service_vasa_configure(system_id, vasa_id, vasa_config)

Configures vasa service for the specified id.

Enables, disable or reset vasa service on a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.vasa_config import VasaConfig
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vasa_id = 'a9c455bf98fc1a6bdb90b824e3ac20b8' # str | ID of the VASA service
    vasa_config = dscc.VasaConfig() # VasaConfig | 

    try:
        # Configures vasa service for the specified id.
        api_response = api_instance.device_type1_network_service_vasa_configure(system_id, vasa_id, vasa_config)
        print("The response of SystemSettingsApi->device_type1_network_service_vasa_configure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_service_vasa_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vasa_id** | **str**| ID of the VASA service | 
 **vasa_config** | [**VasaConfig**](VasaConfig.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_vasa_get**
> NetworkServicesVasa device_type1_network_service_vasa_get(system_id, select=select)

Get VASA Network-Service details for a storage system Primera / Alletra 9K

Get VASA Network-Service details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.network_services_vasa import NetworkServicesVasa
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get VASA Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_vasa_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type1_network_service_vasa_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_service_vasa_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NetworkServicesVasa**](NetworkServicesVasa.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_settings_get**
> NetworkSettings device_type1_network_settings_get(system_id, select=select)

Get Network-Settings details for a storage system Primera / Alletra 9K

Get Network-Settings details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.network_settings import NetworkSettings
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get Network-Settings details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_settings_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type1_network_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NetworkSettings**](NetworkSettings.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_node_service_ports_get_by_id**
> ServicePortsList device_type1_node_service_ports_get_by_id(node_id, system_id, limit=limit, offset=offset, filter=filter, select=select)

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.service_ports_list import ServicePortsList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    node_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | Primary ID of the node
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'ipv4address eq \"169.254.77.160\"' # str | oData query to filter systems by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }
        api_response = api_instance.device_type1_node_service_ports_get_by_id(node_id, system_id, limit=limit, offset=offset, filter=filter, select=select)
        print("The response of SystemSettingsApi->device_type1_node_service_ports_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_node_service_ports_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Primary ID of the node | 
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter systems by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ServicePortsList**](ServicePortsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_node_service_ports_list**
> ServicePortsList device_type1_node_service_ports_list(system_id, limit=limit, offset=offset, filter=filter, select=select)

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.service_ports_list import ServicePortsList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'ipv4address eq \"169.254.77.160\"' # str | oData query to filter systems by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_node_service_ports_list(system_id, limit=limit, offset=offset, filter=filter, select=select)
        print("The response of SystemSettingsApi->device_type1_node_service_ports_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_node_service_ports_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter systems by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ServicePortsList**](ServicePortsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_quorum_witness**
> TaskResponse device_type1_post_quorum_witness(system_id, create_quorum_witness_input)

Create quorum witness on storage system Primera / Alletra 9K identified by {systemId}

Create quorum witness on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_quorum_witness_input import CreateQuorumWitnessInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    create_quorum_witness_input = dscc.CreateQuorumWitnessInput() # CreateQuorumWitnessInput | 

    try:
        # Create quorum witness on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_post_quorum_witness(system_id, create_quorum_witness_input)
        print("The response of SystemSettingsApi->device_type1_post_quorum_witness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_post_quorum_witness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **create_quorum_witness_input** | [**CreateQuorumWitnessInput**](CreateQuorumWitnessInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_remove_replication_partners**
> TaskResponse device_type1_post_remove_replication_partners(system_id, remove_replication_partners_input)

Delete replication partner from storage system Primera / Alletra 9K identified by {systemId}

Delete replication partner from storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.remove_replication_partners_input import RemoveReplicationPartnersInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    remove_replication_partners_input = dscc.RemoveReplicationPartnersInput() # RemoveReplicationPartnersInput | 

    try:
        # Delete replication partner from storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_post_remove_replication_partners(system_id, remove_replication_partners_input)
        print("The response of SystemSettingsApi->device_type1_post_remove_replication_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_post_remove_replication_partners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **remove_replication_partners_input** | [**RemoveReplicationPartnersInput**](RemoveReplicationPartnersInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_replication_partners**
> TaskResponse device_type1_post_replication_partners(system_id, create_replication_partners_input)

Create replication partners on Primera / Alletra 9K identified by {systemId}

Create replication partners on Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_replication_partners_input import CreateReplicationPartnersInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    create_replication_partners_input = dscc.CreateReplicationPartnersInput() # CreateReplicationPartnersInput | 

    try:
        # Create replication partners on Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_post_replication_partners(system_id, create_replication_partners_input)
        print("The response of SystemSettingsApi->device_type1_post_replication_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_post_replication_partners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **create_replication_partners_input** | [**CreateReplicationPartnersInput**](CreateReplicationPartnersInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_v_center_settings**
> TaskResponse device_type1_post_v_center_settings(system_id, v_center_settings_input)

Add vCenter settings to storage system Primera / Alletra 9K

Add vCenter settings to storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.v_center_settings_input import VCenterSettingsInput
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    v_center_settings_input = dscc.VCenterSettingsInput() # VCenterSettingsInput | 

    try:
        # Add vCenter settings to storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_post_v_center_settings(system_id, v_center_settings_input)
        print("The response of SystemSettingsApi->device_type1_post_v_center_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_post_v_center_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **v_center_settings_input** | [**VCenterSettingsInput**](VCenterSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_put_quorum_witness**
> TaskResponse device_type1_put_quorum_witness(system_id, replication_partner_id, edit_quorum_witness_input)

Edit quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Edit quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.edit_quorum_witness_input import EditQuorumWitnessInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner
    edit_quorum_witness_input = dscc.EditQuorumWitnessInput() # EditQuorumWitnessInput | 

    try:
        # Edit quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_put_quorum_witness(system_id, replication_partner_id, edit_quorum_witness_input)
        print("The response of SystemSettingsApi->device_type1_put_quorum_witness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_put_quorum_witness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **edit_quorum_witness_input** | [**EditQuorumWitnessInput**](EditQuorumWitnessInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_put_replication_partner**
> TaskResponse device_type1_put_replication_partner(system_id, replication_partner_id, edit_replication_partner_input)

Edit replication partner identified by {replicationPartnerId} on Primera / Alletra 9K identified by {systemId}

Edit replication partner identified by {replicationPartnerId} on Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.edit_replication_partner_input import EditReplicationPartnerInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner
    edit_replication_partner_input = dscc.EditReplicationPartnerInput() # EditReplicationPartnerInput | 

    try:
        # Edit replication partner identified by {replicationPartnerId} on Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_put_replication_partner(system_id, replication_partner_id, edit_replication_partner_input)
        print("The response of SystemSettingsApi->device_type1_put_replication_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_put_replication_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **edit_replication_partner_input** | [**EditReplicationPartnerInput**](EditReplicationPartnerInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_put_v_center_settings**
> TaskResponse device_type1_put_v_center_settings(system_id, vcenter_setting_id, edit_v_center_settings_input)

Edit vCenter setting identified by {vcenterSettingId} on Primera / Alletra 9K identified by {systemId}

Edit vCenter setting identified by {vcenterSettingId} on Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.edit_v_center_settings_input import EditVCenterSettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vcenter_setting_id = '7e92269a-12d1-35b4-60e8-5919edfc5475' # str | UID(vcenterSettingId) of the storage system
    edit_v_center_settings_input = dscc.EditVCenterSettingsInput() # EditVCenterSettingsInput | 

    try:
        # Edit vCenter setting identified by {vcenterSettingId} on Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_put_v_center_settings(system_id, vcenter_setting_id, edit_v_center_settings_input)
        print("The response of SystemSettingsApi->device_type1_put_v_center_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_put_v_center_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vcenter_setting_id** | **str**| UID(vcenterSettingId) of the storage system | 
 **edit_v_center_settings_input** | [**EditVCenterSettingsInput**](EditVCenterSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_remote_copy_links_performance_history_get**
> RcLinkPerformanceHistoryData device_type1_remote_copy_links_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)

Get details of performance metrics of Primera/ Alletra 9K remote copy links on storage system identified by {systemid}

Get details of performance metrics of Primera/ Alletra 9K remote copy links on storage system identified by {systemid}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.rc_link_performance_history_data import RcLinkPerformanceHistoryData
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    report_type = 'Canned,Custom,Def,ApiUser' # str | parameter will be set to report type requested. For api users, set parameter as ApiUser (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    compare_by = 'top eq 5 and metrics eq READ_IOPS' # str | compareBy will define top and compare metrics for which query has to be made (optional)
    group_by = 'VV_NAME,HOST_NAME,LUN,deviceName' # str | groupBy will define comma separated groupby parameters (optional)
    metric_type = 'IOPS,LATENCY,THROUGHPUT,IOSIZE,QLEN,AVG_BUSY,powerConsumption' # str | metricType will define comma separated metrics (optional)
    filter = 'vvname in (vvname1,vvname2,vvname3) ,deviceName in (cage1)' # str | filter will define objects to be filtered (optional)

    try:
        # Get details of performance metrics of Primera/ Alletra 9K remote copy links on storage system identified by {systemid}
        api_response = api_instance.device_type1_remote_copy_links_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)
        print("The response of SystemSettingsApi->device_type1_remote_copy_links_performance_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_remote_copy_links_performance_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **report_type** | **str**| parameter will be set to report type requested. For api users, set parameter as ApiUser | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 
 **compare_by** | **str**| compareBy will define top and compare metrics for which query has to be made | [optional] 
 **group_by** | **str**| groupBy will define comma separated groupby parameters | [optional] 
 **metric_type** | **str**| metricType will define comma separated metrics | [optional] 
 **filter** | **str**| filter will define objects to be filtered | [optional] 

### Return type

[**RcLinkPerformanceHistoryData**](RcLinkPerformanceHistoryData.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_storage_container_delete_by_id**
> TaskResponse device_type1_storage_container_delete_by_id(system_id, vvolsc_id)

Delete storage container of  storage system Primera / Alletra 9K identified by {id}

Delete storage container of storage system Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vvolsc_id = 'd09b59cd7bd07a4e9559e78dcea07498' # str | Storage container UID

    try:
        # Delete storage container of  storage system Primera / Alletra 9K identified by {id}
        api_response = api_instance.device_type1_storage_container_delete_by_id(system_id, vvolsc_id)
        print("The response of SystemSettingsApi->device_type1_storage_container_delete_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_storage_container_delete_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vvolsc_id** | **str**| Storage container UID | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_storage_container_get**
> NetworkServicesVvolscs device_type1_storage_container_get(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get Storage Container details for a storage system Primera / Alletra 9K

Get Storage Container details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.network_services_vvolscs import NetworkServicesVvolscs
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get Storage Container details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_storage_container_get(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SystemSettingsApi->device_type1_storage_container_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_storage_container_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NetworkServicesVvolscs**](NetworkServicesVvolscs.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_support_data_collect**
> TaskResponse device_type1_support_data_collect(system_id, collect_support_data_input)

Trigger a collection on the storage system Primera / Alletra 9K

Trigger a collection on the storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.collect_support_data_input import CollectSupportDataInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    collect_support_data_input = [dscc.CollectSupportDataInput()] # List[CollectSupportDataInput] | 

    try:
        # Trigger a collection on the storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_support_data_collect(system_id, collect_support_data_input)
        print("The response of SystemSettingsApi->device_type1_support_data_collect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_support_data_collect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **collect_support_data_input** | [**List[CollectSupportDataInput]**](CollectSupportDataInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_support_settings_get**
> SupportSetting device_type1_support_settings_get(system_id, select=select)

Get support settings for a storage system Primera / Alletra 9K

Get support settings for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.support_setting import SupportSetting
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get support settings for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_support_settings_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type1_support_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_support_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SupportSetting**](SupportSetting.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_settings_list**
> SystemConfigParams device_type1_system_settings_list(system_id, select=select)

Get the system settings configuration details

Get the system settings configuration details

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.system_config_params import SystemConfigParams
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get the system settings configuration details
        api_response = api_instance.device_type1_system_settings_list(system_id, select=select)
        print("The response of SystemSettingsApi->device_type1_system_settings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_system_settings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SystemConfigParams**](SystemConfigParams.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - System settings configuration information <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_telemetry_get**
> TelemetryStatus device_type1_telemetry_get(system_id, select=select)

Get telemetry status for a storage system Primera / Alletra 9K

Get telemetry status for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.telemetry_status import TelemetryStatus
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get telemetry status for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_telemetry_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type1_telemetry_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_telemetry_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**TelemetryStatus**](TelemetryStatus.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_trusted_certificates_get_by_id**
> TrustedCertificateDetails device_type1_trusted_certificates_get_by_id(system_id, id, select=select)

Get certificates trusted by Primera / Alletra 9K identified by {id}

Get certificates trusted by Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.trusted_certificate_details import TrustedCertificateDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '99691e493067b2b2acf1774fc0ccc011' # str | ID of the certificate
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get certificates trusted by Primera / Alletra 9K identified by {id}
        api_response = api_instance.device_type1_trusted_certificates_get_by_id(system_id, id, select=select)
        print("The response of SystemSettingsApi->device_type1_trusted_certificates_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_trusted_certificates_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the certificate | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**TrustedCertificateDetails**](TrustedCertificateDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_trusted_certificates_list**
> TrustedCertificatesSummaryList device_type1_trusted_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)

Get certificates trusted by Primera / Alletra 9K

Get certificates trusted by Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.trusted_certificates_summary_list import TrustedCertificatesSummaryList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'other' # str | Lucene query to filter Certificates by Key. (optional)

    try:
        # Get certificates trusted by Primera / Alletra 9K
        api_response = api_instance.device_type1_trusted_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)
        print("The response of SystemSettingsApi->device_type1_trusted_certificates_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_trusted_certificates_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Certificates by Key. | [optional] 

### Return type

[**TrustedCertificatesSummaryList**](TrustedCertificatesSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vm_manager_settings_get_by_id**
> VcenterSettingDetail device_type1_vm_manager_settings_get_by_id(system_id, vcenter_setting_id, select=select)

Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K

Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.vcenter_setting_detail import VcenterSettingDetail
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vcenter_setting_id = '7e92269a-12d1-35b4-60e8-5919edfc5475' # str | UID(vcenterSettingId) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_vm_manager_settings_get_by_id(system_id, vcenter_setting_id, select=select)
        print("The response of SystemSettingsApi->device_type1_vm_manager_settings_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_vm_manager_settings_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vcenter_setting_id** | **str**| UID(vcenterSettingId) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**VcenterSettingDetail**](VcenterSettingDetail.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vm_manager_settings_list**
> VcenterSettingsSumarryList device_type1_vm_manager_settings_list(system_id, select=select, limit=limit, offset=offset)

Get vcenter settings for a storage system Primera / Alletra 9K

Get vcenter settings for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.vcenter_settings_sumarry_list import VcenterSettingsSumarryList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)

    try:
        # Get vcenter settings for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_vm_manager_settings_list(system_id, select=select, limit=limit, offset=offset)
        print("The response of SystemSettingsApi->device_type1_vm_manager_settings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type1_vm_manager_settings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 

### Return type

[**VcenterSettingsSumarryList**](VcenterSettingsSumarryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_application_server_create**
> TaskResponse device_type2_application_server_create(system_id, create_application_server)

Create Nimble / Alletra 6K application server in system identified by {systemId}

Create Nimble / Alletra 6K application server in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_application_server import CreateApplicationServer
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    create_application_server = dscc.CreateApplicationServer() # CreateApplicationServer | 

    try:
        # Create Nimble / Alletra 6K application server in system identified by {systemId}
        api_response = api_instance.device_type2_application_server_create(system_id, create_application_server)
        print("The response of SystemSettingsApi->device_type2_application_server_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_application_server_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **create_application_server** | [**CreateApplicationServer**](CreateApplicationServer.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_application_server_edit**
> TaskResponse device_type2_application_server_edit(system_id, application_server_id, edit_application_server)

Modify Nimble / Alletra 6K application server in system identified by {systemId}

Modify Nimble / Alletra 6K application server in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.edit_application_server import EditApplicationServer
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    application_server_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of application server. A 42 digit hexadecimal number.
    edit_application_server = dscc.EditApplicationServer() # EditApplicationServer | 

    try:
        # Modify Nimble / Alletra 6K application server in system identified by {systemId}
        api_response = api_instance.device_type2_application_server_edit(system_id, application_server_id, edit_application_server)
        print("The response of SystemSettingsApi->device_type2_application_server_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_application_server_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **application_server_id** | **str**| Identifier of application server. A 42 digit hexadecimal number. | 
 **edit_application_server** | [**EditApplicationServer**](EditApplicationServer.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_create_replication_partners**
> TaskResponse device_type2_create_replication_partners(system_id, nimble_create_replication_partner_input)

Create replication partner pair for Nimble / Alletra 6K

Create replication partner pair for Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_replication_partner_input import NimbleCreateReplicationPartnerInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_replication_partner_input = dscc.NimbleCreateReplicationPartnerInput() # NimbleCreateReplicationPartnerInput | 

    try:
        # Create replication partner pair for Nimble / Alletra 6K
        api_response = api_instance.device_type2_create_replication_partners(system_id, nimble_create_replication_partner_input)
        print("The response of SystemSettingsApi->device_type2_create_replication_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_create_replication_partners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_replication_partner_input** | [**NimbleCreateReplicationPartnerInput**](NimbleCreateReplicationPartnerInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_create_witness**
> TaskResponse device_type2_create_witness(system_id, nimble_create_witness_input)

Create a new witness configuration Nimble / Alletra 6K

Create a new witness configuration Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_witness_input import NimbleCreateWitnessInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_witness_input = dscc.NimbleCreateWitnessInput() # NimbleCreateWitnessInput | 

    try:
        # Create a new witness configuration Nimble / Alletra 6K
        api_response = api_instance.device_type2_create_witness(system_id, nimble_create_witness_input)
        print("The response of SystemSettingsApi->device_type2_create_witness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_create_witness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_witness_input** | [**NimbleCreateWitnessInput**](NimbleCreateWitnessInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_mail_settings**
> TaskResponse device_type2_edit_mail_settings(system_id, nimble_mail_setting_input)

Edit Nimble Mail Settings of Nimble / Alletra 6K

Edit Nimble Mail Settings of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_mail_setting_input import NimbleMailSettingInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_mail_setting_input = dscc.NimbleMailSettingInput() # NimbleMailSettingInput | 

    try:
        # Edit Nimble Mail Settings of Nimble / Alletra 6K
        api_response = api_instance.device_type2_edit_mail_settings(system_id, nimble_mail_setting_input)
        print("The response of SystemSettingsApi->device_type2_edit_mail_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_edit_mail_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_mail_setting_input** | [**NimbleMailSettingInput**](NimbleMailSettingInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_network_setting_by_id**
> TaskResponse device_type2_edit_network_setting_by_id(system_id, network_setting_id, nimble_edit_network_settings)

Edit Nimble / Alletra 6K network setting identified by {networkSettingId}

Edit Nimble / Alletra 6K network setting identified by {networkSettingId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_network_settings import NimbleEditNetworkSettings
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    network_setting_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of network setting. A 42 digit hexadecimal number.
    nimble_edit_network_settings = dscc.NimbleEditNetworkSettings() # NimbleEditNetworkSettings | 

    try:
        # Edit Nimble / Alletra 6K network setting identified by {networkSettingId}
        api_response = api_instance.device_type2_edit_network_setting_by_id(system_id, network_setting_id, nimble_edit_network_settings)
        print("The response of SystemSettingsApi->device_type2_edit_network_setting_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_edit_network_setting_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **network_setting_id** | **str**| Identifier of network setting. A 42 digit hexadecimal number. | 
 **nimble_edit_network_settings** | [**NimbleEditNetworkSettings**](NimbleEditNetworkSettings.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_replication_partners_by_id**
> TaskResponse device_type2_edit_replication_partners_by_id(system_id, replicationpartner_id, nimble_edit_replication_partner_input)

Edit a replication partner for Nimble / Alletra 6K given by replicationpartnerId

Edit a replication partner for Nimble / Alletra 6K given by replicationpartnerId

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_replication_partner_input import NimbleEditReplicationPartnerInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    replicationpartner_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of replicationpartner. A 42 digit hexadecimal number.
    nimble_edit_replication_partner_input = dscc.NimbleEditReplicationPartnerInput() # NimbleEditReplicationPartnerInput | 

    try:
        # Edit a replication partner for Nimble / Alletra 6K given by replicationpartnerId
        api_response = api_instance.device_type2_edit_replication_partners_by_id(system_id, replicationpartner_id, nimble_edit_replication_partner_input)
        print("The response of SystemSettingsApi->device_type2_edit_replication_partners_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_edit_replication_partners_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **replicationpartner_id** | **str**| Identifier of replicationpartner. A 42 digit hexadecimal number. | 
 **nimble_edit_replication_partner_input** | [**NimbleEditReplicationPartnerInput**](NimbleEditReplicationPartnerInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_system_settings**
> TaskResponse device_type2_edit_system_settings(system_id, nimble_edit_system_settings)

Edit system settings of Nimble / Alletra 6K

Edit system settings of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_system_settings import NimbleEditSystemSettings
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_edit_system_settings = dscc.NimbleEditSystemSettings() # NimbleEditSystemSettings | 

    try:
        # Edit system settings of Nimble / Alletra 6K
        api_response = api_instance.device_type2_edit_system_settings(system_id, nimble_edit_system_settings)
        print("The response of SystemSettingsApi->device_type2_edit_system_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_edit_system_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_edit_system_settings** | [**NimbleEditSystemSettings**](NimbleEditSystemSettings.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_application_servers**
> ApplicationServersList device_type2_get_all_application_servers(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all application servers details by Nimble / Alletra 6K

Get all application servers details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.application_servers_list import ApplicationServersList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter application servers by Key. (optional)
    sort = 'name desc' # str | oData query to sort application servers by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all application servers details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_application_servers(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SystemSettingsApi->device_type2_get_all_application_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_all_application_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter application servers by Key. | [optional] 
 **sort** | **str**| oData query to sort application servers by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ApplicationServersList**](ApplicationServersList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_network_settings**
> NimbleNetworkSettingsList device_type2_get_all_network_settings(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all network settings details by Nimble / Alletra 6K

Get all network settings details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_network_settings_list import NimbleNetworkSettingsList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter network settings by Key. (optional)
    sort = 'name desc' # str | oData query to sort network settings resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all network settings details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_network_settings(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SystemSettingsApi->device_type2_get_all_network_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_all_network_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter network settings by Key. | [optional] 
 **sort** | **str**| oData query to sort network settings resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleNetworkSettingsList**](NimbleNetworkSettingsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage group object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_application_server_by_id**
> ApplicationServerDetails device_type2_get_application_server_by_id(system_id, application_server_id, select=select)

Get details of Nimble / Alletra 6K application server identified by {applicationServerId}

Get details of Nimble / Alletra 6K application server identified by {applicationServerId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.application_server_details import ApplicationServerDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    application_server_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of application server. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K application server identified by {applicationServerId}
        api_response = api_instance.device_type2_get_application_server_by_id(system_id, application_server_id, select=select)
        print("The response of SystemSettingsApi->device_type2_get_application_server_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_application_server_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **application_server_id** | **str**| Identifier of application server. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ApplicationServerDetails**](ApplicationServerDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_network_setting_by_id**
> NimbleNetworkSettingsDetailsWithRequestUri device_type2_get_network_setting_by_id(system_id, network_setting_id, select=select)

Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}

Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_network_settings_details_with_request_uri import NimbleNetworkSettingsDetailsWithRequestUri
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    network_setting_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of network setting. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}
        api_response = api_instance.device_type2_get_network_setting_by_id(system_id, network_setting_id, select=select)
        print("The response of SystemSettingsApi->device_type2_get_network_setting_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_network_setting_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **network_setting_id** | **str**| Identifier of network setting. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleNetworkSettingsDetailsWithRequestUri**](NimbleNetworkSettingsDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | network settings object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_replication_partners**
> NimbleReplicationPartnersList device_type2_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)

Get all replication-partners details for Nimble / Alletra 6K

Get all replication-partners details for Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_replication_partners_list import NimbleReplicationPartnersList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter replication partners by Key. (optional)
    sort = 'name desc' # str | oData query to sort replication partner resource by Key. (optional)
    include_indirect_partners = true # bool | Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all replication-partners details for Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)
        print("The response of SystemSettingsApi->device_type2_get_replication_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_replication_partners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter replication partners by Key. | [optional] 
 **sort** | **str**| oData query to sort replication partner resource by Key. | [optional] 
 **include_indirect_partners** | **bool**| Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleReplicationPartnersList**](NimbleReplicationPartnersList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_replication_partners_by_id**
> NimbleReplicationPartnerDetails device_type2_get_replication_partners_by_id(system_id, replicationpartner_id, select=select)

Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}

Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_replication_partner_details import NimbleReplicationPartnerDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    replicationpartner_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of replicationpartner. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}
        api_response = api_instance.device_type2_get_replication_partners_by_id(system_id, replicationpartner_id, select=select)
        print("The response of SystemSettingsApi->device_type2_get_replication_partners_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_replication_partners_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **replicationpartner_id** | **str**| Identifier of replicationpartner. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleReplicationPartnerDetails**](NimbleReplicationPartnerDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_witnesses**
> NimbleWitnessesList device_type2_get_witnesses(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all witness configuration details by Nimble / Alletra 6K

Get all witness configuration details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_witnesses_list import NimbleWitnessesList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004007' # str | Lucene query to filter witnesses by Key. (optional)
    sort = 'name desc' # str | oData query to sort witnesses resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all witness configuration details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_witnesses(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SystemSettingsApi->device_type2_get_witnesses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_witnesses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter witnesses by Key. | [optional] 
 **sort** | **str**| oData query to sort witnesses resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleWitnessesList**](NimbleWitnessesList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_witnesses_by_id**
> NimbleWitnessDetails device_type2_get_witnesses_by_id(system_id, witness_id, select=select)

Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}

Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_witness_details import NimbleWitnessDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    witness_id = '2a0df0fe6f7dc7bb16000000000000000000004007' # str | Identifier of witness. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}
        api_response = api_instance.device_type2_get_witnesses_by_id(system_id, witness_id, select=select)
        print("The response of SystemSettingsApi->device_type2_get_witnesses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_witnesses_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **witness_id** | **str**| Identifier of witness. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleWitnessDetails**](NimbleWitnessDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_pause_replication_partner**
> TaskResponse device_type2_pause_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)

Pause the replication pair of Nimble / Alletra 6K

Pause the replication pair of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.pause_resume_nimble_replication_partner_pair_input import PauseResumeNimbleReplicationPartnerPairInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    pause_resume_nimble_replication_partner_pair_input = dscc.PauseResumeNimbleReplicationPartnerPairInput() # PauseResumeNimbleReplicationPartnerPairInput | 

    try:
        # Pause the replication pair of Nimble / Alletra 6K
        api_response = api_instance.device_type2_pause_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)
        print("The response of SystemSettingsApi->device_type2_pause_replication_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_pause_replication_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **pause_resume_nimble_replication_partner_pair_input** | [**PauseResumeNimbleReplicationPartnerPairInput**](PauseResumeNimbleReplicationPartnerPairInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_application_server_by_id**
> TaskResponse device_type2_remove_application_server_by_id(system_id, application_server_id)

Remove application server identified by {applicationServerId} from Nimble / Alletra 6K

Remove application server identified by {applicationServerId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    application_server_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of application server. A 42 digit hexadecimal number.

    try:
        # Remove application server identified by {applicationServerId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_application_server_by_id(system_id, application_server_id)
        print("The response of SystemSettingsApi->device_type2_remove_application_server_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_remove_application_server_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **application_server_id** | **str**| Identifier of application server. A 42 digit hexadecimal number. | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_replication_partner**
> TaskResponse device_type2_remove_replication_partner(system_id, remove_replication_partners)

Remove list of replication partner for Nimble / Alletra 6K

Remove list of replication partner for Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.remove_replication_partners import RemoveReplicationPartners
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    remove_replication_partners = dscc.RemoveReplicationPartners() # RemoveReplicationPartners | 

    try:
        # Remove list of replication partner for Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_replication_partner(system_id, remove_replication_partners)
        print("The response of SystemSettingsApi->device_type2_remove_replication_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_remove_replication_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **remove_replication_partners** | [**RemoveReplicationPartners**](RemoveReplicationPartners.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_witnesses_by_id**
> TaskResponse device_type2_remove_witnesses_by_id(system_id, witness_id)

Remove witness identified by {witnessId} from Nimble / Alletra 6K

Remove witness identified by {witnessId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    witness_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of witness. A 42 digit hexadecimal number.

    try:
        # Remove witness identified by {witnessId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_witnesses_by_id(system_id, witness_id)
        print("The response of SystemSettingsApi->device_type2_remove_witnesses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_remove_witnesses_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **witness_id** | **str**| Identifier of witness. A 42 digit hexadecimal number. | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_resume_replication_partner**
> TaskResponse device_type2_resume_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)

Resume the replication pair of Nimble / Alletra 6K

Resume the replication pair of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.pause_resume_nimble_replication_partner_pair_input import PauseResumeNimbleReplicationPartnerPairInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    pause_resume_nimble_replication_partner_pair_input = dscc.PauseResumeNimbleReplicationPartnerPairInput() # PauseResumeNimbleReplicationPartnerPairInput | 

    try:
        # Resume the replication pair of Nimble / Alletra 6K
        api_response = api_instance.device_type2_resume_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)
        print("The response of SystemSettingsApi->device_type2_resume_replication_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_resume_replication_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **pause_resume_nimble_replication_partner_pair_input** | [**PauseResumeNimbleReplicationPartnerPairInput**](PauseResumeNimbleReplicationPartnerPairInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_send_auto_support**
> TaskResponse device_type2_send_auto_support(system_id)

Send auto support information of Nimble / Alletra 6K identified by {systemId}

Send auto support information of Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system

    try:
        # Send auto support information of Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_send_auto_support(system_id)
        print("The response of SystemSettingsApi->device_type2_send_auto_support:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_send_auto_support: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_test_replication_configuration**
> TaskResponseReplication device_type2_test_replication_configuration(system_id, pause_resume_nimble_replication_partner_pair_input)

Test the replication partner pair of Nimble / Alletra 6K

Test the replication partner pair of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.pause_resume_nimble_replication_partner_pair_input import PauseResumeNimbleReplicationPartnerPairInput
from dscc.models.task_response_replication import TaskResponseReplication
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    pause_resume_nimble_replication_partner_pair_input = dscc.PauseResumeNimbleReplicationPartnerPairInput() # PauseResumeNimbleReplicationPartnerPairInput | 

    try:
        # Test the replication partner pair of Nimble / Alletra 6K
        api_response = api_instance.device_type2_test_replication_configuration(system_id, pause_resume_nimble_replication_partner_pair_input)
        print("The response of SystemSettingsApi->device_type2_test_replication_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_test_replication_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **pause_resume_nimble_replication_partner_pair_input** | [**PauseResumeNimbleReplicationPartnerPairInput**](PauseResumeNimbleReplicationPartnerPairInput.md)|  | 

### Return type

[**TaskResponseReplication**](TaskResponseReplication.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_test_witnesses_by_id**
> NimbleTestWitnessResponse device_type2_test_witnesses_by_id(system_id, witness_id)

Test and validate the witness configuration between the host identified by {witnessId} from Nimble / Alletra 6K identified by {systemId}

Test and validate the witness configuration between the host identified by {witnessId} from Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_test_witness_response import NimbleTestWitnessResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    witness_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of witness. A 42 digit hexadecimal number.

    try:
        # Test and validate the witness configuration between the host identified by {witnessId} from Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_test_witnesses_by_id(system_id, witness_id)
        print("The response of SystemSettingsApi->device_type2_test_witnesses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type2_test_witnesses_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **witness_id** | **str**| Identifier of witness. A 42 digit hexadecimal number. | 

### Return type

[**NimbleTestWitnessResponse**](NimbleTestWitnessResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_add_trusted_certificates**
> TaskResponse device_type4_add_trusted_certificates(system_id, add_trusted_certificate_input)

Add trusted certificates for storage system HPE Alletra Storage MP identified by {systemId}

Add trusted certificates for storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.add_trusted_certificate_input import AddTrustedCertificateInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    add_trusted_certificate_input = dscc.AddTrustedCertificateInput() # AddTrustedCertificateInput | 

    try:
        # Add trusted certificates for storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_add_trusted_certificates(system_id, add_trusted_certificate_input)
        print("The response of SystemSettingsApi->device_type4_add_trusted_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_add_trusted_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **add_trusted_certificate_input** | [**AddTrustedCertificateInput**](AddTrustedCertificateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_alert_contacts_create**
> TaskResponse device_type4_alert_contacts_create(system_id, device_type4_alert_contact_input)

Add Alert/Mail contact details

Add Alert/Mail contact details

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_alert_contact_input import DeviceType4AlertContactInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_alert_contact_input = dscc.DeviceType4AlertContactInput() # DeviceType4AlertContactInput | 

    try:
        # Add Alert/Mail contact details
        api_response = api_instance.device_type4_alert_contacts_create(system_id, device_type4_alert_contact_input)
        print("The response of SystemSettingsApi->device_type4_alert_contacts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_alert_contacts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_alert_contact_input** | [**DeviceType4AlertContactInput**](DeviceType4AlertContactInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_alert_contacts_delete**
> TaskResponse device_type4_alert_contacts_delete(system_id, id)

Delete Alert/Email contact of storage system HPE Alletra Storage MP identified by {id}

Delete Alert/Email contact of storage system HPE Alletra Storage MP identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a4c78226-69cd-b9e7-af3e-445ca8f8a655' # str | Unique Identifier of the alert contact

    try:
        # Delete Alert/Email contact of storage system HPE Alletra Storage MP identified by {id}
        api_response = api_instance.device_type4_alert_contacts_delete(system_id, id)
        print("The response of SystemSettingsApi->device_type4_alert_contacts_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_alert_contacts_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Unique Identifier of the alert contact | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_alert_contacts_get_by_id**
> DeviceType4AlertContactsDetailsList device_type4_alert_contacts_get_by_id(system_id, id, select=select)

Get alert-contact details for a storage system HPE Alletra Storage MP identified by {id}

Get alert-contact details for a storage system HPE Alletra Storage MP identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_alert_contacts_details_list import DeviceType4AlertContactsDetailsList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a4c78226-69cd-b9e7-af3e-445ca8f8a655' # str | Unique Identifier of the alert contact
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get alert-contact details for a storage system HPE Alletra Storage MP identified by {id}
        api_response = api_instance.device_type4_alert_contacts_get_by_id(system_id, id, select=select)
        print("The response of SystemSettingsApi->device_type4_alert_contacts_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_alert_contacts_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Unique Identifier of the alert contact | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4AlertContactsDetailsList**](DeviceType4AlertContactsDetailsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_alert_contacts_list**
> DeviceType4AlertContacts device_type4_alert_contacts_list(system_id, limit=limit, offset=offset, select=select)

Get alert-contact details for a storage system HPE Alletra Storage MP

Get alert-contact details for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_alert_contacts import DeviceType4AlertContacts
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get alert-contact details for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_alert_contacts_list(system_id, limit=limit, offset=offset, select=select)
        print("The response of SystemSettingsApi->device_type4_alert_contacts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_alert_contacts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4AlertContacts**](DeviceType4AlertContacts.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_alert_contacts_update**
> TaskResponse device_type4_alert_contacts_update(system_id, id, device_type4_alert_contact_input)

Edit Alert/Email contact details of storage system HPE Alletra Storage MP identified by {id}

Edit Alert/Email contact details of storage system HPE Alletra Storage MP identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_alert_contact_input import DeviceType4AlertContactInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a4c78226-69cd-b9e7-af3e-445ca8f8a655' # str | Unique Identifier of the alert contact
    device_type4_alert_contact_input = dscc.DeviceType4AlertContactInput() # DeviceType4AlertContactInput | 

    try:
        # Edit Alert/Email contact details of storage system HPE Alletra Storage MP identified by {id}
        api_response = api_instance.device_type4_alert_contacts_update(system_id, id, device_type4_alert_contact_input)
        print("The response of SystemSettingsApi->device_type4_alert_contacts_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_alert_contacts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Unique Identifier of the alert contact | 
 **device_type4_alert_contact_input** | [**DeviceType4AlertContactInput**](DeviceType4AlertContactInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_certificates_get_by_id**
> DeviceType4CertificateDetails device_type4_certificates_get_by_id(system_id, id, select=select)

Get array certificates by HPE Alletra Storage MP identified by {id}

Get array certificates by HPE Alletra Storage MP identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_certificate_details import DeviceType4CertificateDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '99691e493067b2b2acf1774fc0ccc011' # str | ID of the certificate
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get array certificates by HPE Alletra Storage MP identified by {id}
        api_response = api_instance.device_type4_certificates_get_by_id(system_id, id, select=select)
        print("The response of SystemSettingsApi->device_type4_certificates_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_certificates_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the certificate | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4CertificateDetails**](DeviceType4CertificateDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_certificates_list**
> DeviceType4CertificatesSummaryList device_type4_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)

Get array certificates by HPE Alletra Storage MP

Get array certificates by HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_certificates_summary_list import DeviceType4CertificatesSummaryList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'service eq qw-client' # str | Lucene query to filter Certificates by Key. (optional)

    try:
        # Get array certificates by HPE Alletra Storage MP
        api_response = api_instance.device_type4_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)
        print("The response of SystemSettingsApi->device_type4_certificates_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_certificates_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Certificates by Key. | [optional] 

### Return type

[**DeviceType4CertificatesSummaryList**](DeviceType4CertificatesSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_delete_quorum_witness**
> TaskResponse device_type4_delete_quorum_witness(system_id, replication_partner_id)

Delete quorum witness identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}

Delete quorum witness identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner

    try:
        # Delete quorum witness identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_delete_quorum_witness(system_id, replication_partner_id)
        print("The response of SystemSettingsApi->device_type4_delete_quorum_witness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_delete_quorum_witness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_delete_v_center_settings**
> TaskResponse device_type4_delete_v_center_settings(system_id, vcenter_setting_id)

Delete vcenter setting identified by {vcenterSettingId} on storage system HPE Alletra Storage MP identified by {systemId}

Delete vcenter setting identified by {vcenterSettingId} on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vcenter_setting_id = '7e92269a-12d1-35b4-60e8-5919edfc5475' # str | UID(vcenterSettingId) of the storage system

    try:
        # Delete vcenter setting identified by {vcenterSettingId} on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_delete_v_center_settings(system_id, vcenter_setting_id)
        print("The response of SystemSettingsApi->device_type4_delete_v_center_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_delete_v_center_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vcenter_setting_id** | **str**| UID(vcenterSettingId) of the storage system | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_enclosure_powers_sustainability**
> DeviceType4SysPowerSustainabilityMerticData device_type4_enclosure_powers_sustainability(system_id, range=range, time_interval_min=time_interval_min, group_by=group_by, metric_type=metric_type, filter=filter)

Get details of sustainability metrics of enclosure and system power supplies in Watts on storage system identified by {systemid}

Get details of sustainability metrics of enclosure and system power supplies in Watts on storage system identified by {systemid}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_sys_power_sustainability_mertic_data import DeviceType4SysPowerSustainabilityMerticData
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    group_by = 'VV_NAME,HOST_NAME,LUN,deviceName' # str | groupBy will define comma separated groupby parameters (optional)
    metric_type = 'IOPS,LATENCY,THROUGHPUT,IOSIZE,QLEN,AVG_BUSY,powerConsumption' # str | metricType will define comma separated metrics (optional)
    filter = 'vvname in (vvname1,vvname2,vvname3) ,deviceName in (cage1)' # str | filter will define objects to be filtered (optional)

    try:
        # Get details of sustainability metrics of enclosure and system power supplies in Watts on storage system identified by {systemid}
        api_response = api_instance.device_type4_enclosure_powers_sustainability(system_id, range=range, time_interval_min=time_interval_min, group_by=group_by, metric_type=metric_type, filter=filter)
        print("The response of SystemSettingsApi->device_type4_enclosure_powers_sustainability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_enclosure_powers_sustainability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 
 **group_by** | **str**| groupBy will define comma separated groupby parameters | [optional] 
 **metric_type** | **str**| metricType will define comma separated metrics | [optional] 
 **filter** | **str**| filter will define objects to be filtered | [optional] 

### Return type

[**DeviceType4SysPowerSustainabilityMerticData**](DeviceType4SysPowerSustainabilityMerticData.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_get_quorum_witness**
> DeviceType4WitnessList device_type4_get_quorum_witness(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get quorum witness configuration details from storage system HPE Alletra Storage MP identified by {systemId}

Get quorum witness configuration details from storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_witness_list import DeviceType4WitnessList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq afb4961e47212e5bc88dd35db5be5c83' # str | oData query to filter witness by key. (optional)
    sort = 'id desc' # str | oData query to sort witness resource by key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get quorum witness configuration details from storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_get_quorum_witness(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SystemSettingsApi->device_type4_get_quorum_witness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_get_quorum_witness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter witness by key. | [optional] 
 **sort** | **str**| oData query to sort witness resource by key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4WitnessList**](DeviceType4WitnessList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_get_quorum_witness_with_id**
> DeviceType4WitnessDetails device_type4_get_quorum_witness_with_id(system_id, replication_partner_id, select=select)

Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}

Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_witness_details import DeviceType4WitnessDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_get_quorum_witness_with_id(system_id, replication_partner_id, select=select)
        print("The response of SystemSettingsApi->device_type4_get_quorum_witness_with_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_get_quorum_witness_with_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4WitnessDetails**](DeviceType4WitnessDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_get_replication_partner_with_id**
> DeviceType4ReplicationPartnerDetails device_type4_get_replication_partner_with_id(system_id, replication_partner_id, select=select)

Get details of replication partner identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}

Get details of replication partner identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_replication_partner_details import DeviceType4ReplicationPartnerDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of replication partner identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_get_replication_partner_with_id(system_id, replication_partner_id, select=select)
        print("The response of SystemSettingsApi->device_type4_get_replication_partner_with_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_get_replication_partner_with_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4ReplicationPartnerDetails**](DeviceType4ReplicationPartnerDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_get_replication_partners**
> DeviceType4ReplicationPartnersList device_type4_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)

Get details of replication partners on storage system HPE Alletra Storage MP identified by {systemId}

Get details of replication partners on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_replication_partners_list import DeviceType4ReplicationPartnersList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemId eq 7CE751P312' # str | oData query to filter replication partners by key. (optional)
    sort = 'name desc' # str | oData query to sort nodes resource by key. (optional)
    include_indirect_partners = true # bool | Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of replication partners on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)
        print("The response of SystemSettingsApi->device_type4_get_replication_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_get_replication_partners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter replication partners by key. | [optional] 
 **sort** | **str**| oData query to sort nodes resource by key. | [optional] 
 **include_indirect_partners** | **bool**| Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4ReplicationPartnersList**](DeviceType4ReplicationPartnersList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_mail_settings_associate**
> TaskResponse device_type4_mail_settings_associate(system_id, device_type4_mailsettings_input)

Add SMTP/Mail server settigs

Add SMTP/Mail server settigs

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_mailsettings_input import DeviceType4MailsettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_mailsettings_input = dscc.DeviceType4MailsettingsInput() # DeviceType4MailsettingsInput | 

    try:
        # Add SMTP/Mail server settigs
        api_response = api_instance.device_type4_mail_settings_associate(system_id, device_type4_mailsettings_input)
        print("The response of SystemSettingsApi->device_type4_mail_settings_associate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_mail_settings_associate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_mailsettings_input** | [**DeviceType4MailsettingsInput**](DeviceType4MailsettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_mail_settings_delete**
> TaskResponse device_type4_mail_settings_delete(system_id)

Delete SMTP/mail server settings

Delete SMTP/mail server settings

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Delete SMTP/mail server settings
        api_response = api_instance.device_type4_mail_settings_delete(system_id)
        print("The response of SystemSettingsApi->device_type4_mail_settings_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_mail_settings_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_mail_settings_get**
> DeviceType4Mailsettings device_type4_mail_settings_get(system_id, select=select)

Get the system's SMTP/Mail server settigs

Get the system's SMTP/Mail server settigs

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_mailsettings import DeviceType4Mailsettings
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get the system's SMTP/Mail server settigs
        api_response = api_instance.device_type4_mail_settings_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type4_mail_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_mail_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4Mailsettings**](DeviceType4Mailsettings.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - System settings configuration information <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_mail_settings_update**
> TaskResponse device_type4_mail_settings_update(system_id, device_type4_mailsettings_input)

Edit SMTP/Mail server settigs

Edit SMTP/Mail server settigs

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_mailsettings_input import DeviceType4MailsettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_mailsettings_input = dscc.DeviceType4MailsettingsInput() # DeviceType4MailsettingsInput | 

    try:
        # Edit SMTP/Mail server settigs
        api_response = api_instance.device_type4_mail_settings_update(system_id, device_type4_mailsettings_input)
        print("The response of SystemSettingsApi->device_type4_mail_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_mail_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_mailsettings_input** | [**DeviceType4MailsettingsInput**](DeviceType4MailsettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_service_cim_get**
> DeviceType4NetworkServicesCim device_type4_network_service_cim_get(system_id, select=select)

Get CIM Network-Service details for a storage system HPE Alletra Storage MP

Get CIM Network-Service details for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_network_services_cim import DeviceType4NetworkServicesCim
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get CIM Network-Service details for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_network_service_cim_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type4_network_service_cim_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_service_cim_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4NetworkServicesCim**](DeviceType4NetworkServicesCim.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_service_cim_update**
> TaskResponse device_type4_network_service_cim_update(system_id, device_type4_nw_cim_edit)

Edit CIM network service configuration

Edit CIM network service configuration

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_nw_cim_edit import DeviceType4NwCimEdit
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_nw_cim_edit = dscc.DeviceType4NwCimEdit() # DeviceType4NwCimEdit | 

    try:
        # Edit CIM network service configuration
        api_response = api_instance.device_type4_network_service_cim_update(system_id, device_type4_nw_cim_edit)
        print("The response of SystemSettingsApi->device_type4_network_service_cim_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_service_cim_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_nw_cim_edit** | [**DeviceType4NwCimEdit**](DeviceType4NwCimEdit.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_service_configure_vasa_service**
> TaskResponse device_type4_network_service_configure_vasa_service(system_id, vasa_id, device_type4_vasa_service_config)

Configures vasa service for the specified id.

Enables, disable and updates the cert management mode for vasa services on a HPE Alletra Storage MP storage system

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_vasa_service_config import DeviceType4VasaServiceConfig
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vasa_id = 'a9c455bf98fc1a6bdb90b824e3ac20b8' # str | ID of the VASA service
    device_type4_vasa_service_config = dscc.DeviceType4VasaServiceConfig() # DeviceType4VasaServiceConfig | 

    try:
        # Configures vasa service for the specified id.
        api_response = api_instance.device_type4_network_service_configure_vasa_service(system_id, vasa_id, device_type4_vasa_service_config)
        print("The response of SystemSettingsApi->device_type4_network_service_configure_vasa_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_service_configure_vasa_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vasa_id** | **str**| ID of the VASA service | 
 **device_type4_vasa_service_config** | [**DeviceType4VasaServiceConfig**](DeviceType4VasaServiceConfig.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_service_snmp_mgr_create**
> TaskResponse device_type4_network_service_snmp_mgr_create(system_id, device_type4_nw_add_snmp_mgr)

Add SNMP Manager settings

Add SNMP Manager settings

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_nw_add_snmp_mgr import DeviceType4NwAddSnmpMgr
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_nw_add_snmp_mgr = dscc.DeviceType4NwAddSnmpMgr() # DeviceType4NwAddSnmpMgr | 

    try:
        # Add SNMP Manager settings
        api_response = api_instance.device_type4_network_service_snmp_mgr_create(system_id, device_type4_nw_add_snmp_mgr)
        print("The response of SystemSettingsApi->device_type4_network_service_snmp_mgr_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_service_snmp_mgr_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_nw_add_snmp_mgr** | [**DeviceType4NwAddSnmpMgr**](DeviceType4NwAddSnmpMgr.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_service_snmp_mgr_delete**
> TaskResponse device_type4_network_service_snmp_mgr_delete(system_id, id)

Delete SNMP manager settings identified by {id}

Delete SNMP manager settings identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the SNMP manager

    try:
        # Delete SNMP manager settings identified by {id}
        api_response = api_instance.device_type4_network_service_snmp_mgr_delete(system_id, id)
        print("The response of SystemSettingsApi->device_type4_network_service_snmp_mgr_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_service_snmp_mgr_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the SNMP manager | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_service_snmp_mgr_get_by_id**
> DeviceType4NetworkServicesSnmp device_type4_network_service_snmp_mgr_get_by_id(system_id, id, select=select)

Get a specific SNMP-Manager Network-Service details for a storage system HPE Alletra Storage MP

Get a specific SNMP-Manager Network-Service details for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_network_services_snmp import DeviceType4NetworkServicesSnmp
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the SNMP manager
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get a specific SNMP-Manager Network-Service details for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_network_service_snmp_mgr_get_by_id(system_id, id, select=select)
        print("The response of SystemSettingsApi->device_type4_network_service_snmp_mgr_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_service_snmp_mgr_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the SNMP manager | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4NetworkServicesSnmp**](DeviceType4NetworkServicesSnmp.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | SNMP Manager object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_service_snmp_mgr_list**
> DeviceType4NetworkServicesSnmp device_type4_network_service_snmp_mgr_list(system_id, limit=limit, offset=offset, select=select)

Get SNMP-Manager Network-Service details for a storage system HPE Alletra Storage MP

Get SNMP-Manager Network-Service details for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_network_services_snmp import DeviceType4NetworkServicesSnmp
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get SNMP-Manager Network-Service details for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_network_service_snmp_mgr_list(system_id, limit=limit, offset=offset, select=select)
        print("The response of SystemSettingsApi->device_type4_network_service_snmp_mgr_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_service_snmp_mgr_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4NetworkServicesSnmp**](DeviceType4NetworkServicesSnmp.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_service_snmp_mgr_update**
> TaskResponse device_type4_network_service_snmp_mgr_update(system_id, id, device_type4_nw_snmp_mgr_edit)

Edit SNMP Manager settings for the specified Id

Edit SNMP Manager settings for the specified Id

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_nw_snmp_mgr_edit import DeviceType4NwSnmpMgrEdit
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the SNMP manager
    device_type4_nw_snmp_mgr_edit = dscc.DeviceType4NwSnmpMgrEdit() # DeviceType4NwSnmpMgrEdit | 

    try:
        # Edit SNMP Manager settings for the specified Id
        api_response = api_instance.device_type4_network_service_snmp_mgr_update(system_id, id, device_type4_nw_snmp_mgr_edit)
        print("The response of SystemSettingsApi->device_type4_network_service_snmp_mgr_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_service_snmp_mgr_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the SNMP manager | 
 **device_type4_nw_snmp_mgr_edit** | [**DeviceType4NwSnmpMgrEdit**](DeviceType4NwSnmpMgrEdit.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_service_vasa_configure**
> TaskResponse device_type4_network_service_vasa_configure(system_id, vasa_id, device_type4_vasa_config)

Configures vasa service for the specified id.

Enables or disable vasa service  on a HPE Alletra Storage MP storage system

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_vasa_config import DeviceType4VasaConfig
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vasa_id = 'a9c455bf98fc1a6bdb90b824e3ac20b8' # str | ID of the VASA service
    device_type4_vasa_config = dscc.DeviceType4VasaConfig() # DeviceType4VasaConfig | 

    try:
        # Configures vasa service for the specified id.
        api_response = api_instance.device_type4_network_service_vasa_configure(system_id, vasa_id, device_type4_vasa_config)
        print("The response of SystemSettingsApi->device_type4_network_service_vasa_configure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_service_vasa_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vasa_id** | **str**| ID of the VASA service | 
 **device_type4_vasa_config** | [**DeviceType4VasaConfig**](DeviceType4VasaConfig.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_service_vasa_get**
> DeviceType4NetworkServicesVasa device_type4_network_service_vasa_get(system_id, select=select)

Get VASA Network-Service details for a storage system Primera / Alletra 9K

Get VASA Network-Service details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_network_services_vasa import DeviceType4NetworkServicesVasa
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get VASA Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type4_network_service_vasa_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type4_network_service_vasa_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_service_vasa_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4NetworkServicesVasa**](DeviceType4NetworkServicesVasa.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_settings_associate**
> TaskResponse device_type4_network_settings_associate(system_id, device_type4_edit_network_settings_input)

Post Network-Settings details for a storage system HPE Alletra Storage MP

Post Network-Settings details for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_edit_network_settings_input import DeviceType4EditNetworkSettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_edit_network_settings_input = dscc.DeviceType4EditNetworkSettingsInput() # DeviceType4EditNetworkSettingsInput | 

    try:
        # Post Network-Settings details for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_network_settings_associate(system_id, device_type4_edit_network_settings_input)
        print("The response of SystemSettingsApi->device_type4_network_settings_associate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_settings_associate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_edit_network_settings_input** | [**DeviceType4EditNetworkSettingsInput**](DeviceType4EditNetworkSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_network_settings_get**
> DeviceType4networkSettings device_type4_network_settings_get(system_id, select=select)

Get Network-Settings details for a storage system HPE Alletra Storage MP

Get Network-Settings details for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4network_settings import DeviceType4networkSettings
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get Network-Settings details for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_network_settings_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type4_network_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_network_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4networkSettings**](DeviceType4networkSettings.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_node_service_ports_get_by_id**
> DeviceType4ServicePortsList device_type4_node_service_ports_get_by_id(node_id, system_id, limit=limit, offset=offset, filter=filter, select=select)

Get service ports for nodes of all storage systems of HPE Alletra Storage MP identified by {systemId} and {nodeId }

Get service ports for nodes of all storage systems of HPE Alletra Storage MP identified by {systemId} and {nodeId }

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_service_ports_list import DeviceType4ServicePortsList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    node_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | Primary ID of the node
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'ipv4address eq \"169.254.77.160\"' # str | oData query to filter systems by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get service ports for nodes of all storage systems of HPE Alletra Storage MP identified by {systemId} and {nodeId }
        api_response = api_instance.device_type4_node_service_ports_get_by_id(node_id, system_id, limit=limit, offset=offset, filter=filter, select=select)
        print("The response of SystemSettingsApi->device_type4_node_service_ports_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_node_service_ports_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Primary ID of the node | 
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter systems by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4ServicePortsList**](DeviceType4ServicePortsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_node_service_ports_list**
> DeviceType4ServicePortsList device_type4_node_service_ports_list(system_id, limit=limit, offset=offset, filter=filter, select=select)

Get service ports for nodes of all storage systems of HPE Alletra Storage MP identified by {systemId}

Get service ports for nodes of all storage systems of HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_service_ports_list import DeviceType4ServicePortsList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'ipv4address eq \"169.254.77.160\"' # str | oData query to filter systems by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get service ports for nodes of all storage systems of HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_node_service_ports_list(system_id, limit=limit, offset=offset, filter=filter, select=select)
        print("The response of SystemSettingsApi->device_type4_node_service_ports_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_node_service_ports_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter systems by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4ServicePortsList**](DeviceType4ServicePortsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_post_certificate**
> TaskResponse device_type4_post_certificate(system_id, device_type4_create_certificate_input)

Create certificate on storage system HPE Alletra Storage MP identified by {systemId}

Create certificate on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_create_certificate_input import DeviceType4CreateCertificateInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_create_certificate_input = dscc.DeviceType4CreateCertificateInput() # DeviceType4CreateCertificateInput | 

    try:
        # Create certificate on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_post_certificate(system_id, device_type4_create_certificate_input)
        print("The response of SystemSettingsApi->device_type4_post_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_post_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_create_certificate_input** | [**DeviceType4CreateCertificateInput**](DeviceType4CreateCertificateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_post_quorum_witness**
> TaskResponse device_type4_post_quorum_witness(system_id, device_type4_create_quorum_witness_input)

Create quorum witness on storage system HPE Alletra Storage MP identified by {systemId}

Create quorum witness on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_create_quorum_witness_input import DeviceType4CreateQuorumWitnessInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_create_quorum_witness_input = dscc.DeviceType4CreateQuorumWitnessInput() # DeviceType4CreateQuorumWitnessInput | 

    try:
        # Create quorum witness on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_post_quorum_witness(system_id, device_type4_create_quorum_witness_input)
        print("The response of SystemSettingsApi->device_type4_post_quorum_witness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_post_quorum_witness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_create_quorum_witness_input** | [**DeviceType4CreateQuorumWitnessInput**](DeviceType4CreateQuorumWitnessInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_post_remove_replication_partners**
> TaskResponse device_type4_post_remove_replication_partners(system_id, device_type4_remove_replication_partners_input)

Delete replication partner from storage system HPE Alletra Storage MP identified by {systemId}

Delete replication partner from storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_remove_replication_partners_input import DeviceType4RemoveReplicationPartnersInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_remove_replication_partners_input = dscc.DeviceType4RemoveReplicationPartnersInput() # DeviceType4RemoveReplicationPartnersInput | 

    try:
        # Delete replication partner from storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_post_remove_replication_partners(system_id, device_type4_remove_replication_partners_input)
        print("The response of SystemSettingsApi->device_type4_post_remove_replication_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_post_remove_replication_partners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_remove_replication_partners_input** | [**DeviceType4RemoveReplicationPartnersInput**](DeviceType4RemoveReplicationPartnersInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_post_replication_partners**
> TaskResponse device_type4_post_replication_partners(system_id, device_type4_create_replication_partners_input)

Create replication partners on HPE Alletra Storage MP identified by {systemId}

Create replication partners on HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_create_replication_partners_input import DeviceType4CreateReplicationPartnersInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_create_replication_partners_input = dscc.DeviceType4CreateReplicationPartnersInput() # DeviceType4CreateReplicationPartnersInput | 

    try:
        # Create replication partners on HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_post_replication_partners(system_id, device_type4_create_replication_partners_input)
        print("The response of SystemSettingsApi->device_type4_post_replication_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_post_replication_partners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_create_replication_partners_input** | [**DeviceType4CreateReplicationPartnersInput**](DeviceType4CreateReplicationPartnersInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_post_v_center_settings**
> TaskResponse device_type4_post_v_center_settings(system_id, device_type4v_center_settings_input)

Add vCenter settings to storage system HPE Alletra Storage MP

Add vCenter settings to storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4v_center_settings_input import DeviceType4vCenterSettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4v_center_settings_input = dscc.DeviceType4vCenterSettingsInput() # DeviceType4vCenterSettingsInput | 

    try:
        # Add vCenter settings to storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_post_v_center_settings(system_id, device_type4v_center_settings_input)
        print("The response of SystemSettingsApi->device_type4_post_v_center_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_post_v_center_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4v_center_settings_input** | [**DeviceType4vCenterSettingsInput**](DeviceType4vCenterSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_put_certificate**
> TaskResponse device_type4_put_certificate(system_id, id, device_type4_import_certificate_input)

Import certificate identified by {id} on storage system HPE Alletra Storage MP identified by {systemId}

Import certificate identified by {id} on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_import_certificate_input import DeviceType4ImportCertificateInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '99691e493067b2b2acf1774fc0ccc011' # str | ID of the certificate
    device_type4_import_certificate_input = dscc.DeviceType4ImportCertificateInput() # DeviceType4ImportCertificateInput | 

    try:
        # Import certificate identified by {id} on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_put_certificate(system_id, id, device_type4_import_certificate_input)
        print("The response of SystemSettingsApi->device_type4_put_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_put_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the certificate | 
 **device_type4_import_certificate_input** | [**DeviceType4ImportCertificateInput**](DeviceType4ImportCertificateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_put_quorum_witness**
> TaskResponse device_type4_put_quorum_witness(system_id, replication_partner_id, device_type4_edit_quorum_witness_input)

Edit quorum witness identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}

Edit quorum witness identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_edit_quorum_witness_input import DeviceType4EditQuorumWitnessInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner
    device_type4_edit_quorum_witness_input = dscc.DeviceType4EditQuorumWitnessInput() # DeviceType4EditQuorumWitnessInput | 

    try:
        # Edit quorum witness identified by {replicationPartnerId} on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_put_quorum_witness(system_id, replication_partner_id, device_type4_edit_quorum_witness_input)
        print("The response of SystemSettingsApi->device_type4_put_quorum_witness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_put_quorum_witness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **device_type4_edit_quorum_witness_input** | [**DeviceType4EditQuorumWitnessInput**](DeviceType4EditQuorumWitnessInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_put_replication_partner**
> TaskResponse device_type4_put_replication_partner(system_id, replication_partner_id, device_type4_edit_replication_partner_input)

Edit replication partner identified by {replicationPartnerId} on HPE Alletra Storage MP identified by {systemId}

Edit replication partner identified by {replicationPartnerId} on HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_edit_replication_partner_input import DeviceType4EditReplicationPartnerInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner
    device_type4_edit_replication_partner_input = dscc.DeviceType4EditReplicationPartnerInput() # DeviceType4EditReplicationPartnerInput | 

    try:
        # Edit replication partner identified by {replicationPartnerId} on HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_put_replication_partner(system_id, replication_partner_id, device_type4_edit_replication_partner_input)
        print("The response of SystemSettingsApi->device_type4_put_replication_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_put_replication_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **device_type4_edit_replication_partner_input** | [**DeviceType4EditReplicationPartnerInput**](DeviceType4EditReplicationPartnerInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_put_v_center_settings**
> TaskResponse device_type4_put_v_center_settings(system_id, vcenter_setting_id, device_type4_edit_v_center_settings_input)

Edit vCenter setting identified by {vcenterSettingId} on HPE Alletra Storage MP identified by {systemId}

Edit vCenter setting identified by {vcenterSettingId} on HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_edit_v_center_settings_input import DeviceType4EditVCenterSettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vcenter_setting_id = '7e92269a-12d1-35b4-60e8-5919edfc5475' # str | UID(vcenterSettingId) of the storage system
    device_type4_edit_v_center_settings_input = dscc.DeviceType4EditVCenterSettingsInput() # DeviceType4EditVCenterSettingsInput | 

    try:
        # Edit vCenter setting identified by {vcenterSettingId} on HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_put_v_center_settings(system_id, vcenter_setting_id, device_type4_edit_v_center_settings_input)
        print("The response of SystemSettingsApi->device_type4_put_v_center_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_put_v_center_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vcenter_setting_id** | **str**| UID(vcenterSettingId) of the storage system | 
 **device_type4_edit_v_center_settings_input** | [**DeviceType4EditVCenterSettingsInput**](DeviceType4EditVCenterSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_remote_copy_links_performance_history_get**
> DeviceType4RcLinkPerformanceHistoryData device_type4_remote_copy_links_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)

Get details of performance metrics of remote copy links on storage system identified by {systemid}

Get details of performance metrics of remote copy links on storage system identified by {systemid}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_rc_link_performance_history_data import DeviceType4RcLinkPerformanceHistoryData
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    report_type = 'Canned,Custom,Def,ApiUser' # str | parameter will be set to report type requested. For api users, set parameter as ApiUser (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    compare_by = 'top eq 5 and metrics eq READ_IOPS' # str | compareBy will define top and compare metrics for which query has to be made (optional)
    group_by = 'VV_NAME,HOST_NAME,LUN,deviceName' # str | groupBy will define comma separated groupby parameters (optional)
    metric_type = 'IOPS,LATENCY,THROUGHPUT,IOSIZE,QLEN,AVG_BUSY,powerConsumption' # str | metricType will define comma separated metrics (optional)
    filter = 'vvname in (vvname1,vvname2,vvname3) ,deviceName in (cage1)' # str | filter will define objects to be filtered (optional)

    try:
        # Get details of performance metrics of remote copy links on storage system identified by {systemid}
        api_response = api_instance.device_type4_remote_copy_links_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)
        print("The response of SystemSettingsApi->device_type4_remote_copy_links_performance_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_remote_copy_links_performance_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **report_type** | **str**| parameter will be set to report type requested. For api users, set parameter as ApiUser | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 
 **compare_by** | **str**| compareBy will define top and compare metrics for which query has to be made | [optional] 
 **group_by** | **str**| groupBy will define comma separated groupby parameters | [optional] 
 **metric_type** | **str**| metricType will define comma separated metrics | [optional] 
 **filter** | **str**| filter will define objects to be filtered | [optional] 

### Return type

[**DeviceType4RcLinkPerformanceHistoryData**](DeviceType4RcLinkPerformanceHistoryData.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_remove_certificates**
> TaskResponse device_type4_remove_certificates(system_id, device_type4_remove_certificates_input)

Delete certificates from storage system HPE Alletra Storage MP identified by {systemId}

Delete certificates from storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_remove_certificates_input import DeviceType4RemoveCertificatesInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_remove_certificates_input = dscc.DeviceType4RemoveCertificatesInput() # DeviceType4RemoveCertificatesInput | 

    try:
        # Delete certificates from storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_remove_certificates(system_id, device_type4_remove_certificates_input)
        print("The response of SystemSettingsApi->device_type4_remove_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_remove_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_remove_certificates_input** | [**DeviceType4RemoveCertificatesInput**](DeviceType4RemoveCertificatesInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_remove_trusted_certificates**
> TaskResponse device_type4_remove_trusted_certificates(system_id, remove_trusted_certificates_input)

Delete trusted certificates from storage system HPE Alletra Storage MP identified by {systemId}

Delete trusted certificates from storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.remove_trusted_certificates_input import RemoveTrustedCertificatesInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    remove_trusted_certificates_input = dscc.RemoveTrustedCertificatesInput() # RemoveTrustedCertificatesInput | 

    try:
        # Delete trusted certificates from storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_remove_trusted_certificates(system_id, remove_trusted_certificates_input)
        print("The response of SystemSettingsApi->device_type4_remove_trusted_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_remove_trusted_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **remove_trusted_certificates_input** | [**RemoveTrustedCertificatesInput**](RemoveTrustedCertificatesInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_set_license**
> TaskResponse device_type4_set_license(system_id, device_type4_set_license)

Set license of the storage system identified by {systemId}

Set license of the storage system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_set_license import DeviceType4SetLicense
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_set_license = dscc.DeviceType4SetLicense() # DeviceType4SetLicense | 

    try:
        # Set license of the storage system identified by {systemId}
        api_response = api_instance.device_type4_set_license(system_id, device_type4_set_license)
        print("The response of SystemSettingsApi->device_type4_set_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_set_license: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_set_license** | [**DeviceType4SetLicense**](DeviceType4SetLicense.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_snmp_users_get_by_id**
> DeviceType4SnmpUsersDetails device_type4_snmp_users_get_by_id(system_id, id, select=select)

Get SNMP users identified by {id}

Get SNMP users identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_snmp_users_details import DeviceType4SnmpUsersDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the SNMP manager
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get SNMP users identified by {id}
        api_response = api_instance.device_type4_snmp_users_get_by_id(system_id, id, select=select)
        print("The response of SystemSettingsApi->device_type4_snmp_users_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_snmp_users_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the SNMP manager | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SnmpUsersDetails**](DeviceType4SnmpUsersDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_snmp_users_list**
> DeviceType4SnmpUsersList device_type4_snmp_users_list(system_id, limit=limit, offset=offset, select=select, filter=filter, sort=sort)

Get SNMP users

Get SNMP users

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_snmp_users_list import DeviceType4SnmpUsersList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter snmpusers resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort snmpusers resource by Key. (optional)

    try:
        # Get SNMP users
        api_response = api_instance.device_type4_snmp_users_list(system_id, limit=limit, offset=offset, select=select, filter=filter, sort=sort)
        print("The response of SystemSettingsApi->device_type4_snmp_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_snmp_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **filter** | **str**| oData query to filter snmpusers resource by Key. | [optional] 
 **sort** | **str**| oData query to sort snmpusers resource by Key. | [optional] 

### Return type

[**DeviceType4SnmpUsersList**](DeviceType4SnmpUsersList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_storage_container_delete_by_id**
> TaskResponse device_type4_storage_container_delete_by_id(system_id, vvolsc_id)

Delete storage container of storage system HPE Alletra Storage MP identified by {id}

Delete storage container of storage system HPE Alletra Storage MP identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vvolsc_id = 'd09b59cd7bd07a4e9559e78dcea07498' # str | Storage container UID

    try:
        # Delete storage container of storage system HPE Alletra Storage MP identified by {id}
        api_response = api_instance.device_type4_storage_container_delete_by_id(system_id, vvolsc_id)
        print("The response of SystemSettingsApi->device_type4_storage_container_delete_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_storage_container_delete_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vvolsc_id** | **str**| Storage container UID | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_storage_container_edit_by_id**
> TaskResponse device_type4_storage_container_edit_by_id(system_id, vvolsc_id, device_type4_editv_vol_sc_input)

Edit storage container of storage system HPE Alletra Storage MP identified by {id}

Edit storage container of storage system HPE Alletra Storage MP identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_editv_vol_sc_input import DeviceType4EditvVolSCInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vvolsc_id = 'd09b59cd7bd07a4e9559e78dcea07498' # str | Storage container UID
    device_type4_editv_vol_sc_input = dscc.DeviceType4EditvVolSCInput() # DeviceType4EditvVolSCInput | 

    try:
        # Edit storage container of storage system HPE Alletra Storage MP identified by {id}
        api_response = api_instance.device_type4_storage_container_edit_by_id(system_id, vvolsc_id, device_type4_editv_vol_sc_input)
        print("The response of SystemSettingsApi->device_type4_storage_container_edit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_storage_container_edit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vvolsc_id** | **str**| Storage container UID | 
 **device_type4_editv_vol_sc_input** | [**DeviceType4EditvVolSCInput**](DeviceType4EditvVolSCInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_storage_container_get**
> DeviceType4Vvolscs device_type4_storage_container_get(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get Storage Container details for a storage system HPE Alletra Storage MP

Get Storage Container details for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_vvolscs import DeviceType4Vvolscs
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get Storage Container details for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_storage_container_get(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SystemSettingsApi->device_type4_storage_container_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_storage_container_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4Vvolscs**](DeviceType4Vvolscs.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_support_data_collect**
> TaskResponse device_type4_support_data_collect(system_id, device_type4collect_support_data_input)

Trigger a collection on the storage system HPE Alletra Storage MP

Trigger a collection on the storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4collect_support_data_input import DeviceType4collectSupportDataInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4collect_support_data_input = [dscc.DeviceType4collectSupportDataInput()] # List[DeviceType4collectSupportDataInput] | 

    try:
        # Trigger a collection on the storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_support_data_collect(system_id, device_type4collect_support_data_input)
        print("The response of SystemSettingsApi->device_type4_support_data_collect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_support_data_collect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4collect_support_data_input** | [**List[DeviceType4collectSupportDataInput]**](DeviceType4collectSupportDataInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_support_settings_associate**
> TaskResponse device_type4_support_settings_associate(system_id, device_type4_support_settings_input)

Add support settings for a storage system HPE Alletra Storage MP

Add support settings for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_support_settings_input import DeviceType4SupportSettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_support_settings_input = dscc.DeviceType4SupportSettingsInput() # DeviceType4SupportSettingsInput | 

    try:
        # Add support settings for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_support_settings_associate(system_id, device_type4_support_settings_input)
        print("The response of SystemSettingsApi->device_type4_support_settings_associate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_support_settings_associate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_support_settings_input** | [**DeviceType4SupportSettingsInput**](DeviceType4SupportSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_support_settings_get**
> DeviceType4SupportSetting device_type4_support_settings_get(system_id, select=select)

Get support settings for a storage system HPE Alletra Storage MP

Get support settings for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_support_setting import DeviceType4SupportSetting
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get support settings for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_support_settings_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type4_support_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_support_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SupportSetting**](DeviceType4SupportSetting.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_support_settings_update**
> TaskResponse device_type4_support_settings_update(system_id, device_type4_support_settings_input)

Edit support settings for a storage system HPE Alletra Storage MP

Edit support settings for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_support_settings_input import DeviceType4SupportSettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_support_settings_input = dscc.DeviceType4SupportSettingsInput() # DeviceType4SupportSettingsInput | 

    try:
        # Edit support settings for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_support_settings_update(system_id, device_type4_support_settings_input)
        print("The response of SystemSettingsApi->device_type4_support_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_support_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_support_settings_input** | [**DeviceType4SupportSettingsInput**](DeviceType4SupportSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_system_settings_associate**
> TaskResponse device_type4_system_settings_associate(system_id, device_type4_system_config_params_edit_input)

Edit system settings configuration

Edit system settings configuration. Only one type of system settings i.e. either \"authMode or dateTime or installationSites or name or ntpAddresses or remoteSyslogSettings or srinfo or supportContact or systemParameters\" is allowed to be configured at a time.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_system_config_params_edit_input import DeviceType4SystemConfigParamsEditInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_system_config_params_edit_input = dscc.DeviceType4SystemConfigParamsEditInput() # DeviceType4SystemConfigParamsEditInput | 

    try:
        # Edit system settings configuration
        api_response = api_instance.device_type4_system_settings_associate(system_id, device_type4_system_config_params_edit_input)
        print("The response of SystemSettingsApi->device_type4_system_settings_associate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_system_settings_associate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_system_config_params_edit_input** | [**DeviceType4SystemConfigParamsEditInput**](DeviceType4SystemConfigParamsEditInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_system_settings_list**
> DeviceType4SystemConfigParams device_type4_system_settings_list(system_id, select=select)

Get the system settings configuration details

Get the system settings configuration details

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_system_config_params import DeviceType4SystemConfigParams
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get the system settings configuration details
        api_response = api_instance.device_type4_system_settings_list(system_id, select=select)
        print("The response of SystemSettingsApi->device_type4_system_settings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_system_settings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SystemConfigParams**](DeviceType4SystemConfigParams.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - System settings configuration information <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_system_settings_update**
> TaskResponse device_type4_system_settings_update(system_id, device_type4_system_config_params_edit_input)

Edit system settings configuration

Edit system settings configuration. Only one type of system settings i.e. either \"authMode or dateTime or installationSites or name or ntpAddresses or remoteSyslogSettings or srinfo or supportContact or systemParameters\" is allowed to be configured at a time.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_system_config_params_edit_input import DeviceType4SystemConfigParamsEditInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_system_config_params_edit_input = dscc.DeviceType4SystemConfigParamsEditInput() # DeviceType4SystemConfigParamsEditInput | 

    try:
        # Edit system settings configuration
        api_response = api_instance.device_type4_system_settings_update(system_id, device_type4_system_config_params_edit_input)
        print("The response of SystemSettingsApi->device_type4_system_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_system_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_system_config_params_edit_input** | [**DeviceType4SystemConfigParamsEditInput**](DeviceType4SystemConfigParamsEditInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_telemetry_get**
> DeviceType4TelemetryStatus device_type4_telemetry_get(system_id, select=select)

Get telemetry status for a storage system HPE Alletra Storage MP

Get telemetry status for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_telemetry_status import DeviceType4TelemetryStatus
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get telemetry status for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_telemetry_get(system_id, select=select)
        print("The response of SystemSettingsApi->device_type4_telemetry_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_telemetry_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4TelemetryStatus**](DeviceType4TelemetryStatus.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_trusted_certificates_get_by_id**
> TrustedCertificateDetails device_type4_trusted_certificates_get_by_id(system_id, id, select=select)

Get certificates trusted by HPE Alletra Storage MP identified by {id}

Get certificates trusted by HPE Alletra Storage MP identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.trusted_certificate_details import TrustedCertificateDetails
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '99691e493067b2b2acf1774fc0ccc011' # str | ID of the certificate
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get certificates trusted by HPE Alletra Storage MP identified by {id}
        api_response = api_instance.device_type4_trusted_certificates_get_by_id(system_id, id, select=select)
        print("The response of SystemSettingsApi->device_type4_trusted_certificates_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_trusted_certificates_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the certificate | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**TrustedCertificateDetails**](TrustedCertificateDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_trusted_certificates_list**
> TrustedCertificatesSummaryList device_type4_trusted_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)

Get certificates trusted by HPE Alletra Storage MP

Get certificates trusted by HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.trusted_certificates_summary_list import TrustedCertificatesSummaryList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'other' # str | Lucene query to filter Certificates by Key. (optional)

    try:
        # Get certificates trusted by HPE Alletra Storage MP
        api_response = api_instance.device_type4_trusted_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)
        print("The response of SystemSettingsApi->device_type4_trusted_certificates_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_trusted_certificates_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Certificates by Key. | [optional] 

### Return type

[**TrustedCertificatesSummaryList**](TrustedCertificatesSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_vm_manager_settings_get_by_id**
> DeviceType4vcenterSettingDetail device_type4_vm_manager_settings_get_by_id(system_id, vcenter_setting_id, select=select)

Get vcenter setting detail for a given vcenter setting of a storage system HPE Alletra Storage MP

Get vcenter setting detail for a given vcenter setting of a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4vcenter_setting_detail import DeviceType4vcenterSettingDetail
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vcenter_setting_id = '7e92269a-12d1-35b4-60e8-5919edfc5475' # str | UID(vcenterSettingId) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get vcenter setting detail for a given vcenter setting of a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_vm_manager_settings_get_by_id(system_id, vcenter_setting_id, select=select)
        print("The response of SystemSettingsApi->device_type4_vm_manager_settings_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_vm_manager_settings_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vcenter_setting_id** | **str**| UID(vcenterSettingId) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4vcenterSettingDetail**](DeviceType4vcenterSettingDetail.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_vm_manager_settings_list**
> DeviceType4VcenterSettingsSumarryList device_type4_vm_manager_settings_list(system_id, select=select, limit=limit, offset=offset)

Get vcenter settings for a storage system HPE Alletra Storage MP

Get vcenter settings for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_vcenter_settings_sumarry_list import DeviceType4VcenterSettingsSumarryList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)

    try:
        # Get vcenter settings for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_vm_manager_settings_list(system_id, select=select, limit=limit, offset=offset)
        print("The response of SystemSettingsApi->device_type4_vm_manager_settings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->device_type4_vm_manager_settings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 

### Return type

[**DeviceType4VcenterSettingsSumarryList**](DeviceType4VcenterSettingsSumarryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_settings_associate**
> TaskResponse mail_settings_associate(system_id, mailsettings_input)

Add SMTP/Mail server settigs

Add SMTP/Mail server settigs

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.mailsettings_input import MailsettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    mailsettings_input = dscc.MailsettingsInput() # MailsettingsInput | 

    try:
        # Add SMTP/Mail server settigs
        api_response = api_instance.mail_settings_associate(system_id, mailsettings_input)
        print("The response of SystemSettingsApi->mail_settings_associate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->mail_settings_associate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **mailsettings_input** | [**MailsettingsInput**](MailsettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_settings_delete**
> TaskResponse mail_settings_delete(system_id)

Delete SMTP/mail server settings

Delete SMTP/mail server settings

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Delete SMTP/mail server settings
        api_response = api_instance.mail_settings_delete(system_id)
        print("The response of SystemSettingsApi->mail_settings_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->mail_settings_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_settings_update**
> TaskResponse mail_settings_update(system_id, mailsettings_input)

Edit SMTP/Mail server settigs

Edit SMTP/Mail server settigs

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.mailsettings_input import MailsettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    mailsettings_input = dscc.MailsettingsInput() # MailsettingsInput | 

    try:
        # Edit SMTP/Mail server settigs
        api_response = api_instance.mail_settings_update(system_id, mailsettings_input)
        print("The response of SystemSettingsApi->mail_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->mail_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **mailsettings_input** | [**MailsettingsInput**](MailsettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_cim_update**
> TaskResponse network_service_cim_update(system_id, nw_cim_edit)

Edit CIM network service configuration

Edit CIM network service configuration

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nw_cim_edit import NwCimEdit
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    nw_cim_edit = dscc.NwCimEdit() # NwCimEdit | 

    try:
        # Edit CIM network service configuration
        api_response = api_instance.network_service_cim_update(system_id, nw_cim_edit)
        print("The response of SystemSettingsApi->network_service_cim_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->network_service_cim_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **nw_cim_edit** | [**NwCimEdit**](NwCimEdit.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_snmp_mgr_create**
> TaskResponse network_service_snmp_mgr_create(system_id, nw_add_snmp_mgr)

Add SNMP Manager settings

Add SNMP Manager settings

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nw_add_snmp_mgr import NwAddSnmpMgr
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    nw_add_snmp_mgr = dscc.NwAddSnmpMgr() # NwAddSnmpMgr | 

    try:
        # Add SNMP Manager settings
        api_response = api_instance.network_service_snmp_mgr_create(system_id, nw_add_snmp_mgr)
        print("The response of SystemSettingsApi->network_service_snmp_mgr_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->network_service_snmp_mgr_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **nw_add_snmp_mgr** | [**NwAddSnmpMgr**](NwAddSnmpMgr.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_snmp_mgr_delete**
> TaskResponse network_service_snmp_mgr_delete(system_id, id)

Delete SNMP manager settings identified by {id}

Delete SNMP manager settings identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the SNMP manager

    try:
        # Delete SNMP manager settings identified by {id}
        api_response = api_instance.network_service_snmp_mgr_delete(system_id, id)
        print("The response of SystemSettingsApi->network_service_snmp_mgr_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->network_service_snmp_mgr_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the SNMP manager | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_snmp_mgr_update**
> TaskResponse network_service_snmp_mgr_update(system_id, id, nw_snmp_mgr_edit)

Edit SNMP Manager settings for the specified Id

Edit SNMP Manager settings for the specified Id

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nw_snmp_mgr_edit import NwSnmpMgrEdit
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the SNMP manager
    nw_snmp_mgr_edit = dscc.NwSnmpMgrEdit() # NwSnmpMgrEdit | 

    try:
        # Edit SNMP Manager settings for the specified Id
        api_response = api_instance.network_service_snmp_mgr_update(system_id, id, nw_snmp_mgr_edit)
        print("The response of SystemSettingsApi->network_service_snmp_mgr_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->network_service_snmp_mgr_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the SNMP manager | 
 **nw_snmp_mgr_edit** | [**NwSnmpMgrEdit**](NwSnmpMgrEdit.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_settings_associate**
> TaskResponse network_settings_associate(system_id, edit_network_settings_input)

Post Network-Settings details for a storage system Primera / Alletra 9K

Post Network-Settings details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.edit_network_settings_input import EditNetworkSettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    edit_network_settings_input = dscc.EditNetworkSettingsInput() # EditNetworkSettingsInput | 

    try:
        # Post Network-Settings details for a storage system Primera / Alletra 9K
        api_response = api_instance.network_settings_associate(system_id, edit_network_settings_input)
        print("The response of SystemSettingsApi->network_settings_associate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->network_settings_associate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **edit_network_settings_input** | [**EditNetworkSettingsInput**](EditNetworkSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_certificate**
> TaskResponse post_certificate(system_id, create_certificate_input)

Create certificate on storage system Primera / Alletra 9K identified by {systemId}

Create certificate on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_certificate_input import CreateCertificateInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    create_certificate_input = dscc.CreateCertificateInput() # CreateCertificateInput | 

    try:
        # Create certificate on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.post_certificate(system_id, create_certificate_input)
        print("The response of SystemSettingsApi->post_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->post_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **create_certificate_input** | [**CreateCertificateInput**](CreateCertificateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_certificate**
> TaskResponse put_certificate(system_id, id, import_certificate_input)

Import certificate identified by {id} on storage system Primera / Alletra 9K identified by {systemId}

Import certificate identified by {id} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.import_certificate_input import ImportCertificateInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '99691e493067b2b2acf1774fc0ccc011' # str | ID of the certificate
    import_certificate_input = dscc.ImportCertificateInput() # ImportCertificateInput | 

    try:
        # Import certificate identified by {id} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.put_certificate(system_id, id, import_certificate_input)
        print("The response of SystemSettingsApi->put_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->put_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the certificate | 
 **import_certificate_input** | [**ImportCertificateInput**](ImportCertificateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_certificates**
> TaskResponse remove_certificates(system_id, remove_certificates_input)

Delete certificates from storage system Primera / Alletra 9K identified by {systemId}

Delete certificates from storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.remove_certificates_input import RemoveCertificatesInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    remove_certificates_input = dscc.RemoveCertificatesInput() # RemoveCertificatesInput | 

    try:
        # Delete certificates from storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.remove_certificates(system_id, remove_certificates_input)
        print("The response of SystemSettingsApi->remove_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->remove_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **remove_certificates_input** | [**RemoveCertificatesInput**](RemoveCertificatesInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_trusted_certificates**
> TaskResponse remove_trusted_certificates(system_id, remove_trusted_certificates_input)

Delete trusted certificates from storage system Primera / Alletra 9K identified by {systemId}

Delete trusted certificates from storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.remove_trusted_certificates_input import RemoveTrustedCertificatesInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    remove_trusted_certificates_input = dscc.RemoveTrustedCertificatesInput() # RemoveTrustedCertificatesInput | 

    try:
        # Delete trusted certificates from storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.remove_trusted_certificates(system_id, remove_trusted_certificates_input)
        print("The response of SystemSettingsApi->remove_trusted_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->remove_trusted_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **remove_trusted_certificates_input** | [**RemoveTrustedCertificatesInput**](RemoveTrustedCertificatesInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_settings_associate**
> TaskResponse support_settings_associate(system_id, support_settings_input)

Add support settings for a storage system Primera / Alletra 9K

Add support settings for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.support_settings_input import SupportSettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    support_settings_input = dscc.SupportSettingsInput() # SupportSettingsInput | 

    try:
        # Add support settings for a storage system Primera / Alletra 9K
        api_response = api_instance.support_settings_associate(system_id, support_settings_input)
        print("The response of SystemSettingsApi->support_settings_associate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->support_settings_associate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **support_settings_input** | [**SupportSettingsInput**](SupportSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_settings_update**
> TaskResponse support_settings_update(system_id, support_settings_input)

Edit support settings for a storage system Primera / Alletra 9K

Edit support settings for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.support_settings_input import SupportSettingsInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    support_settings_input = dscc.SupportSettingsInput() # SupportSettingsInput | 

    try:
        # Edit support settings for a storage system Primera / Alletra 9K
        api_response = api_instance.support_settings_update(system_id, support_settings_input)
        print("The response of SystemSettingsApi->support_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->support_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **support_settings_input** | [**SupportSettingsInput**](SupportSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_associate**
> TaskResponse system_settings_associate(system_id, system_config_params_edit_input)

Edit system settings configuration

Edit system settings configuration

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.system_config_params_edit_input import SystemConfigParamsEditInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    system_config_params_edit_input = dscc.SystemConfigParamsEditInput() # SystemConfigParamsEditInput | 

    try:
        # Edit system settings configuration
        api_response = api_instance.system_settings_associate(system_id, system_config_params_edit_input)
        print("The response of SystemSettingsApi->system_settings_associate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->system_settings_associate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **system_config_params_edit_input** | [**SystemConfigParamsEditInput**](SystemConfigParamsEditInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_update**
> TaskResponse system_settings_update(system_id, system_config_params_edit_input)

Edit system settings configuration

Edit system settings configuration

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.system_config_params_edit_input import SystemConfigParamsEditInput
from dscc.models.task_response import TaskResponse
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.SystemSettingsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    system_config_params_edit_input = dscc.SystemConfigParamsEditInput() # SystemConfigParamsEditInput | 

    try:
        # Edit system settings configuration
        api_response = api_instance.system_settings_update(system_id, system_config_params_edit_input)
        print("The response of SystemSettingsApi->system_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSettingsApi->system_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **system_config_params_edit_input** | [**SystemConfigParamsEditInput**](SystemConfigParamsEditInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

