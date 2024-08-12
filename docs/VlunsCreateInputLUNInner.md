# VlunsCreateInputLUNInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun** | **int** | Logical Unit Number | [optional] 
**host_group_id** | **str** | Host group Id | [optional] 

## Example

```python
from dscc.models.vluns_create_input_lun_inner import VlunsCreateInputLUNInner

# TODO update the JSON string below
json = "{}"
# create an instance of VlunsCreateInputLUNInner from a JSON string
vluns_create_input_lun_inner_instance = VlunsCreateInputLUNInner.from_json(json)
# print the JSON string representation of the object
print(VlunsCreateInputLUNInner.to_json())

# convert the object into a dict
vluns_create_input_lun_inner_dict = vluns_create_input_lun_inner_instance.to_dict()
# create an instance of VlunsCreateInputLUNInner from a dict
vluns_create_input_lun_inner_from_dict = VlunsCreateInputLUNInner.from_dict(vluns_create_input_lun_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


