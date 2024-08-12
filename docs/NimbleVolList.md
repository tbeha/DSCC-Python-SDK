# NimbleVolList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_category** | **str** | Application category that the volume belongs to. | [optional] 
**full_name** | **str** | Fully qualified name of volume. | [optional] 
**id** | **str** | ID of volume. | [optional] 
**lun** | **int** | LUN of volume. Secondary LUN if this is Virtual Volume. | [optional] 
**name** | **str** | Name of volume | [optional] 

## Example

```python
from dscc.models.nimble_vol_list import NimbleVolList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleVolList from a JSON string
nimble_vol_list_instance = NimbleVolList.from_json(json)
# print the JSON string representation of the object
print(NimbleVolList.to_json())

# convert the object into a dict
nimble_vol_list_dict = nimble_vol_list_instance.to_dict()
# create an instance of NimbleVolList from a dict
nimble_vol_list_from_dict = NimbleVolList.from_dict(nimble_vol_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


