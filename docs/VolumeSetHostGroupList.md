# VolumeSetHostGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**host_group_name** | **str** | Host group name | [optional] 
**hosts** | [**List[VolumeSetHostProximityInfo]**](VolumeSetHostProximityInfo.md) |  | [optional] 
**system_id** | **str** | Unique ID or serial number of the system. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.volume_set_host_group_list import VolumeSetHostGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeSetHostGroupList from a JSON string
volume_set_host_group_list_instance = VolumeSetHostGroupList.from_json(json)
# print the JSON string representation of the object
print(VolumeSetHostGroupList.to_json())

# convert the object into a dict
volume_set_host_group_list_dict = volume_set_host_group_list_instance.to_dict()
# create an instance of VolumeSetHostGroupList from a dict
volume_set_host_group_list_from_dict = VolumeSetHostGroupList.from_dict(volume_set_host_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


