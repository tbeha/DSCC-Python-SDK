# ObjData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**target_name** | **str** | target name | [optional] 
**target_type** | **str** | target type | [optional] 
**timestampms** | **List[int]** |  | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.obj_data import ObjData

# TODO update the JSON string below
json = "{}"
# create an instance of ObjData from a JSON string
obj_data_instance = ObjData.from_json(json)
# print the JSON string representation of the object
print(ObjData.to_json())

# convert the object into a dict
obj_data_dict = obj_data_instance.to_dict()
# create an instance of ObjData from a dict
obj_data_from_dict = ObjData.from_dict(obj_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


