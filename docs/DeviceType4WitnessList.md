# DeviceType4WitnessList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4Witness]**](DeviceType4Witness.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | Request URI for quorum witness objects | [optional] 
**total** | **int** | Total number of witnesses. | [optional] 

## Example

```python
from dscc.models.device_type4_witness_list import DeviceType4WitnessList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4WitnessList from a JSON string
device_type4_witness_list_instance = DeviceType4WitnessList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4WitnessList.to_json())

# convert the object into a dict
device_type4_witness_list_dict = device_type4_witness_list_instance.to_dict()
# create an instance of DeviceType4WitnessList from a dict
device_type4_witness_list_from_dict = DeviceType4WitnessList.from_dict(device_type4_witness_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


