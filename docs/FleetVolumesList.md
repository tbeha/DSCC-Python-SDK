# FleetVolumesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FleetVolumeDetailsList]**](FleetVolumeDetailsList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed volume object | [optional] 
**total** | **int** | Number of volumes. | [optional] 

## Example

```python
from dscc.models.fleet_volumes_list import FleetVolumesList

# TODO update the JSON string below
json = "{}"
# create an instance of FleetVolumesList from a JSON string
fleet_volumes_list_instance = FleetVolumesList.from_json(json)
# print the JSON string representation of the object
print(FleetVolumesList.to_json())

# convert the object into a dict
fleet_volumes_list_dict = fleet_volumes_list_instance.to_dict()
# create an instance of FleetVolumesList from a dict
fleet_volumes_list_from_dict = FleetVolumesList.from_dict(fleet_volumes_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


