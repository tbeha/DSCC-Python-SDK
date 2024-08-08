# VlunsCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun** | [**List[VlunsCreateInputLUNInner]**](VlunsCreateInputLUNInner.md) | Custom LUN Id for multiple host groups | [optional] 
**auto_lun** | **bool** | Auto Lun | [optional] 
**host_group_ids** | **List[Optional[str]]** | HostGroups | 
**max_auto_lun** | **int** | Number of volumes. | [optional] 
**no_vcn** | **bool** | No VCN | [optional] 
**override** | **bool** | Override | [optional] 
**position** | **str** | Position. This field is deprecated. | [optional] 
**proximity** | **str** | Host proximity setting for Active Peer Persistence configuration. Supported values are - PRIMARY, SECONDARY and ALL. Default proximity is PRIMARY. | [optional] 

## Example

```python
from dscc.models.vluns_create_input import VlunsCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VlunsCreateInput from a JSON string
vluns_create_input_instance = VlunsCreateInput.from_json(json)
# print the JSON string representation of the object
print(VlunsCreateInput.to_json())

# convert the object into a dict
vluns_create_input_dict = vluns_create_input_instance.to_dict()
# create an instance of VlunsCreateInput from a dict
vluns_create_input_from_dict = VlunsCreateInput.from_dict(vluns_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


