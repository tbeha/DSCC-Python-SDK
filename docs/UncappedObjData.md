# UncappedObjData

QoS policy uncap details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ObjData]**](ObjData.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | total number of uncapped data | [optional] 

## Example

```python
from dscc.models.uncapped_obj_data import UncappedObjData

# TODO update the JSON string below
json = "{}"
# create an instance of UncappedObjData from a JSON string
uncapped_obj_data_instance = UncappedObjData.from_json(json)
# print the JSON string representation of the object
print(UncappedObjData.to_json())

# convert the object into a dict
uncapped_obj_data_dict = uncapped_obj_data_instance.to_dict()
# create an instance of UncappedObjData from a dict
uncapped_obj_data_from_dict = UncappedObjData.from_dict(uncapped_obj_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


