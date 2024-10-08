# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.api.ports_api import PortsApi


class TestPortsApi(unittest.TestCase):
    """PortsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PortsApi()

    def tearDown(self) -> None:
        pass

    def test_device_type1_fc_port_edit(self) -> None:
        """Test case for device_type1_fc_port_edit

        Edit ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        """
        pass

    def test_device_type1_iscsi_port_edit(self) -> None:
        """Test case for device_type1_iscsi_port_edit

        Edit iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        """
        pass

    def test_device_type1_iscsi_port_ping(self) -> None:
        """Test case for device_type1_iscsi_port_ping

        Ping iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        """
        pass

    def test_device_type1_ports_clear(self) -> None:
        """Test case for device_type1_ports_clear

        Clear the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        """
        pass

    def test_device_type1_ports_get_by_id(self) -> None:
        """Test case for device_type1_ports_get_by_id

        Get details of Primera / Alletra 9K Port identified by {id}
        """
        pass

    def test_device_type1_ports_list(self) -> None:
        """Test case for device_type1_ports_list

        Get details of Primera / Alletra 9K Ports
        """
        pass

    def test_device_type1_ports_performance_history_get(self) -> None:
        """Test case for device_type1_ports_performance_history_get

        Get details of performance metrics of Primera/ Alletra 9K host ports on storage system identified by {systemid}
        """
        pass

    def test_device_type1_rcip_port_edit(self) -> None:
        """Test case for device_type1_rcip_port_edit

        Edit rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        """
        pass

    def test_device_type1_rcip_port_ping(self) -> None:
        """Test case for device_type1_rcip_port_ping

        Ping rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        """
        pass

    def test_device_type2_edit_fc_port(self) -> None:
        """Test case for device_type2_edit_fc_port

        Edit Nimble FC Port of Nimble / Alletra 6K
        """
        pass

    def test_device_type2_get_all_fibre_channel_configs(self) -> None:
        """Test case for device_type2_get_all_fibre_channel_configs

        Get all fibre channel configs details of Nimble / Alletra 6K
        """
        pass

    def test_device_type2_get_all_fibre_channel_sessions(self) -> None:
        """Test case for device_type2_get_all_fibre_channel_sessions

        Get all fibre channel sessions details of Nimble / Alletra 6K
        """
        pass

    def test_device_type2_get_all_ports(self) -> None:
        """Test case for device_type2_get_all_ports

        Get all ports details of Nimble / Alletra 6K
        """
        pass

    def test_device_type2_get_fibre_channel_config_by_id(self) -> None:
        """Test case for device_type2_get_fibre_channel_config_by_id

        Get fibre channel configs details of Nimble / Alletra 6K identified by {fcConfigId}.
        """
        pass

    def test_device_type2_get_fibre_channel_session_by_id(self) -> None:
        """Test case for device_type2_get_fibre_channel_session_by_id

        Get fibre channel session details of Nimble / Alletra 6K identified by {fcSessionId}.
        """
        pass

    def test_device_type2_get_port_by_id(self) -> None:
        """Test case for device_type2_get_port_by_id

        Get details of Nimble / Alletra 6K Port identified by {portId}. Fibre_channel_interfaces attributes will be shown for Fibre_channel_interface ports. Network_interfaces attributes will be shown for Network_interface ports.
        """
        pass

    def test_device_type4_fc_port_edit(self) -> None:
        """Test case for device_type4_fc_port_edit

        Edit ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        """
        pass

    def test_device_type4_iscsi_port_edit(self) -> None:
        """Test case for device_type4_iscsi_port_edit

        Edit iscsi ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        """
        pass

    def test_device_type4_iscsi_port_ping(self) -> None:
        """Test case for device_type4_iscsi_port_ping

        Ping iscsi ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        """
        pass

    def test_device_type4_nvme_port_edit(self) -> None:
        """Test case for device_type4_nvme_port_edit

        Edit nvme ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        """
        pass

    def test_device_type4_nvme_port_ping(self) -> None:
        """Test case for device_type4_nvme_port_ping

        Ping nvme ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        """
        pass

    def test_device_type4_port_enable(self) -> None:
        """Test case for device_type4_port_enable

        Port enable disable identified by {id} from HPE Alletra Storage MP identified by {systemId}
        """
        pass

    def test_device_type4_ports_clear(self) -> None:
        """Test case for device_type4_ports_clear

        Clear the details of the ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        """
        pass

    def test_device_type4_ports_get_by_id(self) -> None:
        """Test case for device_type4_ports_get_by_id

        Get details of HPE Alletra Storage MP Port identified by {id}
        """
        pass

    def test_device_type4_ports_list(self) -> None:
        """Test case for device_type4_ports_list

        Get details of HPE Alletra Storage MP Ports
        """
        pass

    def test_device_type4_ports_performance_history_get(self) -> None:
        """Test case for device_type4_ports_performance_history_get

        Get details of performance metrics of host ports on storage system identified by {systemid}
        """
        pass

    def test_device_type4_rcip_port_edit(self) -> None:
        """Test case for device_type4_rcip_port_edit

        Edit rcip ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        """
        pass

    def test_device_type4_rcip_port_ping(self) -> None:
        """Test case for device_type4_rcip_port_ping

        Ping rcip ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        """
        pass

    def test_device_type4initialise_ports(self) -> None:
        """Test case for device_type4initialise_ports

        Initialize the details of the ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        """
        pass

    def test_get_device_type2_network_interface_by_id(self) -> None:
        """Test case for get_device_type2_network_interface_by_id

        Get all network interfaces details by Nimble / Alletra 6K identified  by {networkInterfaceId}
        """
        pass

    def test_get_device_type2_network_interfaces(self) -> None:
        """Test case for get_device_type2_network_interfaces

        Get all network interfaces details by Nimble / Alletra 6K
        """
        pass

    def test_initialise_ports(self) -> None:
        """Test case for initialise_ports

        Initialize the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        """
        pass

    def test_port_enable(self) -> None:
        """Test case for port_enable

        Port enable disable identified by {id} from Primera / Alletra 9K identified by {systemId}
        """
        pass


if __name__ == '__main__':
    unittest.main()
