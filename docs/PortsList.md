# PortsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**card_type** | [**CardType**](CardType.md) |  | [optional] 
**var_class** | **int** | Fibre Channel class (can be either 2 or 3) | [optional] 
**class2** | **str** | Class2 state and configuration | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**config** | **str** | Configuration state of port | [optional] 
**config_mode** | **str** | Connection mode of the port | [optional] 
**connection_type** | **str** | port connection type | [optional] 
**customer_id** | **str** | customerId | [optional] 
**devices** | [**List[DeviceType4connectedDevicesInner]**](DeviceType4connectedDevicesInner.md) |  | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**failover_status** | **str** | Failover status of this port and the partner &#x60;Filter, Sort&#x60; | [optional] 
**fc_data** | [**PortFC**](PortFC.md) |  | [optional] 
**fw_version** | **str** | Firmware version | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource &#x60;Filter&#x60; | [optional] 
**initiator_ports** | [**InitiatorPort**](InitiatorPort.md) |  | [optional] 
**interrupt_coalesce** | **str** | Interrupt Coalesce | [optional] 
**ip_data** | [**PortIP**](PortIP.md) |  | [optional] 
**iscsi_data** | [**PortISCSI**](PortISCSI.md) |  | [optional] 
**label** | **str** | Label &#x60;Filter, Sort&#x60; | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**mode** | **str** | Current mode the port is in &#x60;Filter, Sort&#x60; | [optional] 
**mode_change** | **str** | Indicates if the mode change is allowed or prohibited | [optional] 
**name** | **str** | Name of the resource &#x60;Filter, Sort&#x60; | [optional] 
**node_card_id** | **str** | Unique Identifier of the node adapter card | [optional] 
**node_id** | **str** | Unique Identifier of the node &#x60;Filter&#x60; | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**port_sfp** | [**PortSfp**](PortSfp.md) |  | [optional] 
**port_type** | **str** | Type of the port based on the device it is connected to &#x60;Filter, Sort&#x60; | [optional] 
**position** | [**PortPosition**](PortPosition.md) |  | [optional] 
**protocol** | **str** | Current protocol the port is in &#x60;Filter, Sort&#x60; | [optional] 
**resource_uri** | **str** | resourceUri for detailed port object | [optional] 
**revision** | **str** | Revision of the Host Bus Adapter | [optional] 
**smart_san** | **str** | Smart SAN status | [optional] 
**speed_actual** | **str** | Actual speed that port is running at  &#x60;Filter&#x60; | [optional] 
**speed_configured** | **str** | Speed that is configured to run as | [optional] 
**speed_max** | **str** | Maximum speed that port can run at | [optional] 
**speed_min** | **str** | Minimum speed that port can run at | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**state_description** | **List[Optional[str]]** | Detailed descriptions of the port state | [optional] 
**system_id** | **str** | SystemUid/SerialNumber of the array. | [optional] 
**tgt_mode_write_opt** | **str** | Target mode write optimization setting | [optional] 
**type** | **str** | type | [optional] 
**unique_wwn** | **str** | Unique WWN setting | [optional] 
**vlans** | [**List[Vlan]**](Vlan.md) |  | [optional] 

## Example

```python
from dscc.models.ports_list import PortsList

# TODO update the JSON string below
json = "{}"
# create an instance of PortsList from a JSON string
ports_list_instance = PortsList.from_json(json)
# print the JSON string representation of the object
print(PortsList.to_json())

# convert the object into a dict
ports_list_dict = ports_list_instance.to_dict()
# create an instance of PortsList from a dict
ports_list_from_dict = PortsList.from_dict(ports_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


