# DeviceType4EnclosureConnectorDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**connector** | **int** | Connector on slot on IOM in Cage for connection | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**current_speed** | **str** | Current speed of connection | [optional] 
**customer_id** | **str** | customerId | [optional] 
**disabled** | **str** | Disabled for connection | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | [**DeviceType4ElementStatusCode**](DeviceType4ElementStatusCode.md) |  | [optional] 
**enclosure_card_id** | **int** | ID of the enclosure card | [optional] 
**enclosure_card_pci_uid** | **str** | UID of the enclosure card PCI card | [optional] 
**enclosure_card_uid** | **str** | Unique Identifier of the enclosure card | [optional] 
**enclosure_id** | **int** | ID of the enclosure | [optional] 
**enclosure_name** | **str** | Name of the enclosure. | [optional] 
**enclosure_uid** | **str** | Unique Identifier of the enclosure. &#x60;Filter&#x60; | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**ipv4_address** | **str** | ip v4 address of connection | [optional] 
**ipv6_address** | **str** | ip v6 address of connection | [optional] 
**label** | **str** | Connection label | [optional] 
**link_speed** | **str** | Link speed for connection | [optional] 
**locate** | **str** | Locate for connection | [optional] 
**mac_address** | **str** | mac address of connection | [optional] 
**node_port** | [**DeviceType4EnclosureConnectorDetailsNodePort**](DeviceType4EnclosureConnectorDetailsNodePort.md) |  | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure connector object | [optional] 
**slot** | **int** | Slot on IOM in Cage for connection | [optional] 
**system_id** | **str** | Id of the array | [optional] 
**type** | **str** | Type of connection | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_connector_details import DeviceType4EnclosureConnectorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureConnectorDetails from a JSON string
device_type4_enclosure_connector_details_instance = DeviceType4EnclosureConnectorDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureConnectorDetails.to_json())

# convert the object into a dict
device_type4_enclosure_connector_details_dict = device_type4_enclosure_connector_details_instance.to_dict()
# create an instance of DeviceType4EnclosureConnectorDetails from a dict
device_type4_enclosure_connector_details_from_dict = DeviceType4EnclosureConnectorDetails.from_dict(device_type4_enclosure_connector_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


