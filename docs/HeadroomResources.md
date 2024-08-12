# HeadroomResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_name** | **str** | Name of the resource | [optional] 
**series_data** | [**List[TimeSeriesData]**](TimeSeriesData.md) |  | [optional] 

## Example

```python
from dscc.models.headroom_resources import HeadroomResources

# TODO update the JSON string below
json = "{}"
# create an instance of HeadroomResources from a JSON string
headroom_resources_instance = HeadroomResources.from_json(json)
# print the JSON string representation of the object
print(HeadroomResources.to_json())

# convert the object into a dict
headroom_resources_dict = headroom_resources_instance.to_dict()
# create an instance of HeadroomResources from a dict
headroom_resources_from_dict = HeadroomResources.from_dict(headroom_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


