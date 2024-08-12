# CappedObjData

QoS policy cap details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ObjData]**](ObjData.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | total number of cap data | [optional] 

## Example

```python
from dscc.models.capped_obj_data import CappedObjData

# TODO update the JSON string below
json = "{}"
# create an instance of CappedObjData from a JSON string
capped_obj_data_instance = CappedObjData.from_json(json)
# print the JSON string representation of the object
print(CappedObjData.to_json())

# convert the object into a dict
capped_obj_data_dict = capped_obj_data_instance.to_dict()
# create an instance of CappedObjData from a dict
capped_obj_data_from_dict = CappedObjData.from_dict(capped_obj_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


