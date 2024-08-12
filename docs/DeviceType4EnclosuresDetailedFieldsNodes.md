# DeviceType4EnclosuresDetailedFieldsNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4nodesLists]**](DeviceType4nodesLists.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of nodes | [optional] 

## Example

```python
from dscc.models.device_type4_enclosures_detailed_fields_nodes import DeviceType4EnclosuresDetailedFieldsNodes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosuresDetailedFieldsNodes from a JSON string
device_type4_enclosures_detailed_fields_nodes_instance = DeviceType4EnclosuresDetailedFieldsNodes.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosuresDetailedFieldsNodes.to_json())

# convert the object into a dict
device_type4_enclosures_detailed_fields_nodes_dict = device_type4_enclosures_detailed_fields_nodes_instance.to_dict()
# create an instance of DeviceType4EnclosuresDetailedFieldsNodes from a dict
device_type4_enclosures_detailed_fields_nodes_from_dict = DeviceType4EnclosuresDetailedFieldsNodes.from_dict(device_type4_enclosures_detailed_fields_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


