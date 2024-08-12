# CreatevVolSCInput

Request body for creating VMware Storage Container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Storage Container Comment | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**host_ids** | **List[str]** | Host IDs | [optional] 
**host_set_ids** | **List[str]** | Host Set IDs | [optional] 
**keep** | **bool** | Indicates if a volume set with existing volumes to be marked as a VMware storage container | [optional] 
**members** | **List[str]** | Names of the set members | [optional] 
**name** | **str** | Storage Container Name. | 

## Example

```python
from dscc.models.createv_vol_sc_input import CreatevVolSCInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreatevVolSCInput from a JSON string
createv_vol_sc_input_instance = CreatevVolSCInput.from_json(json)
# print the JSON string representation of the object
print(CreatevVolSCInput.to_json())

# convert the object into a dict
createv_vol_sc_input_dict = createv_vol_sc_input_instance.to_dict()
# create an instance of CreatevVolSCInput from a dict
createv_vol_sc_input_from_dict = CreatevVolSCInput.from_dict(createv_vol_sc_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


