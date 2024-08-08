# FleetVolumeSetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FleetVolumeset]**](FleetVolumeset.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | RequestUri for applicationsets resources | [optional] 
**total** | **int** | Total Number of volume sets. | [optional] 

## Example

```python
from dscc.models.fleet_volume_set_list import FleetVolumeSetList

# TODO update the JSON string below
json = "{}"
# create an instance of FleetVolumeSetList from a JSON string
fleet_volume_set_list_instance = FleetVolumeSetList.from_json(json)
# print the JSON string representation of the object
print(FleetVolumeSetList.to_json())

# convert the object into a dict
fleet_volume_set_list_dict = fleet_volume_set_list_instance.to_dict()
# create an instance of FleetVolumeSetList from a dict
fleet_volume_set_list_from_dict = FleetVolumeSetList.from_dict(fleet_volume_set_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


