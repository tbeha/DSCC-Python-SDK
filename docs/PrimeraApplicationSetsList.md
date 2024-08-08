# PrimeraApplicationSetsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PrimeraApplicationSets]**](PrimeraApplicationSets.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | RequestUri for applicationsets resources | [optional] 
**total** | **int** | Total Number of Application sets. | [optional] 

## Example

```python
from dscc.models.primera_application_sets_list import PrimeraApplicationSetsList

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraApplicationSetsList from a JSON string
primera_application_sets_list_instance = PrimeraApplicationSetsList.from_json(json)
# print the JSON string representation of the object
print(PrimeraApplicationSetsList.to_json())

# convert the object into a dict
primera_application_sets_list_dict = primera_application_sets_list_instance.to_dict()
# create an instance of PrimeraApplicationSetsList from a dict
primera_application_sets_list_from_dict = PrimeraApplicationSetsList.from_dict(primera_application_sets_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


