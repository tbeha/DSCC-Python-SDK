# DeviceType4enclosureCardMemoryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_card_id** | **int** | ID of enclosure card. | [optional] 
**enclosure_card_mem_type** | **str** | Enclosure card memory type. | [optional] 
**enclosure_card_uid** | **str** | Unique Identifier of the enclosure card. | [optional] 
**enclosure_id** | **int** | ID of the enclosure | [optional] 
**enclosure_uid** | **str** | Unique Identifier of the enclosure. | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | id | [optional] 
**index** | **int** | Slot id of the physical memory | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the enclosure memory card. | [optional] 
**rcd** | **str** | RCD of the physical memory | [optional] 
**size** | **int** | Size of the physical memory of KiB | [optional] 
**speed** | **int** | Speed | [optional] 
**system_id** | **str** | systemId | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_card_memory_details import DeviceType4enclosureCardMemoryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureCardMemoryDetails from a JSON string
device_type4enclosure_card_memory_details_instance = DeviceType4enclosureCardMemoryDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureCardMemoryDetails.to_json())

# convert the object into a dict
device_type4enclosure_card_memory_details_dict = device_type4enclosure_card_memory_details_instance.to_dict()
# create an instance of DeviceType4enclosureCardMemoryDetails from a dict
device_type4enclosure_card_memory_details_from_dict = DeviceType4enclosureCardMemoryDetails.from_dict(device_type4enclosure_card_memory_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


