# PrimeraVolumesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PrimeraVolumeDetailsList]**](PrimeraVolumeDetailsList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed volume object | [optional] 
**total** | **int** | Total number of volumes. | [optional] 

## Example

```python
from dscc.models.primera_volumes_list import PrimeraVolumesList

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraVolumesList from a JSON string
primera_volumes_list_instance = PrimeraVolumesList.from_json(json)
# print the JSON string representation of the object
print(PrimeraVolumesList.to_json())

# convert the object into a dict
primera_volumes_list_dict = primera_volumes_list_instance.to_dict()
# create an instance of PrimeraVolumesList from a dict
primera_volumes_list_from_dict = PrimeraVolumesList.from_dict(primera_volumes_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


