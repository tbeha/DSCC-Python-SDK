# DeviceType4PortDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**card_type** | [**DeviceType4cardType**](DeviceType4cardType.md) |  | [optional] 
**var_class** | **int** | Fibre Channel class (can be either 2 or 3) | [optional] 
**class2** | **str** | Class2 state and configuration | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**config** | **str** | Configuration state of port | [optional] 
**config_mode** | **str** | Connection mode of the port | [optional] 
**connection_type** | **str** | port connection type | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**devices** | [**List[DeviceType4connectedDevicesInner]**](DeviceType4connectedDevicesInner.md) |  | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_card_id** | **int** | ID of the enclosure card | [optional] 
**enclosure_card_pci_uid** | **str** | UID of the enclosure card PCI card | [optional] 
**enclosure_card_pcid** | **int** | ID of the enclosure card PCI card | [optional] 
**enclosure_card_uid** | **str** | Unique Identifier of the enclosure card | [optional] 
**enclosure_id** | **int** | ID of the enclosure | [optional] 
**enclosure_uid** | **str** | Unique Identifier of the enclosure | [optional] 
**failover_status** | **str** | Failover status of this port and the partner | [optional] 
**fc_data** | [**DeviceType4portFC**](DeviceType4portFC.md) |  | [optional] 
**fw_version** | **str** | Firmware version | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**initiator_ports** | [**DeviceType4initiatorPort**](DeviceType4initiatorPort.md) |  | [optional] 
**interrupt_coalesce** | **str** | Interrupt Coalesce | [optional] 
**ip_data** | [**DeviceType4portIP**](DeviceType4portIP.md) |  | [optional] 
**iscsi_data** | [**DeviceType4portISCSI**](DeviceType4portISCSI.md) |  | [optional] 
**label** | **str** | Label | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**mode** | **str** | Current mode the port is in | [optional] 
**mode_change** | **str** | Indicates if the mode change is allowed or prohibited | [optional] 
**name** | **str** | Name of the resource | [optional] 
**node_card_id** | **str** | Unique Identifier of the node adapter card | [optional] 
**node_id** | **str** | Unique Identifier of the node | [optional] 
**nvme_data** | [**DeviceType4PortNVMe**](DeviceType4PortNVMe.md) |  | [optional] 
**partner** | [**DeviceType4partnerPort**](DeviceType4partnerPort.md) |  | [optional] 
**port_sfp** | [**DeviceType4portSfp**](DeviceType4portSfp.md) |  | [optional] 
**port_type** | **str** | Type of the port based on the device it is connected to | [optional] 
**position** | [**DeviceType4portPosition**](DeviceType4portPosition.md) |  | [optional] 
**protocol** | **str** | Current protocol the port is in | [optional] 
**request_uri** | **str** | requestUri for detailed ports object | [optional] 
**resource_uri** | **str** | resourceUri for detailed ports object | [optional] 
**revision** | **str** | Revision of the Host Bus Adapter | [optional] 
**smart_san** | **str** | Smart SAN status | [optional] 
**speed_actual** | **str** | Actual speed that port is running at | [optional] 
**speed_configured** | **str** | Speed that is configured to run as | [optional] 
**speed_max** | **str** | Maximum speed that port can run at | [optional] 
**speed_min** | **str** | Minimum speed that port can run at | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**state_description** | **List[Optional[str]]** | Detailed descriptions of the port state | [optional] 
**system_id** | **str** | SystemUid / SerialNumber of the array | [optional] 
**tgt_mode_write_opt** | **str** | Target mode write optimization setting | [optional] 
**type** | **str** | type | [optional] 
**unique_wwn** | **str** | Unique WWN setting | [optional] 
**virtual_ports** | [**List[DeviceType4PortDetailsVirtualPortsInner]**](DeviceType4PortDetailsVirtualPortsInner.md) | Virtual ports | [optional] 
**vlans** | [**List[DeviceType4vlan]**](DeviceType4vlan.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_port_details import DeviceType4PortDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortDetails from a JSON string
device_type4_port_details_instance = DeviceType4PortDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortDetails.to_json())

# convert the object into a dict
device_type4_port_details_dict = device_type4_port_details_instance.to_dict()
# create an instance of DeviceType4PortDetails from a dict
device_type4_port_details_from_dict = DeviceType4PortDetails.from_dict(device_type4_port_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


