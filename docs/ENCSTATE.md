# ENCSTATE

State of the resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailed** | **str** | Array of the detailed states of the resource | [optional] 
**overall** | **str** | Overall state of the resource. &#x60;Sort: stateOverall&#x60; | [optional] 

## Example

```python
from dscc.models.encstate import ENCSTATE

# TODO update the JSON string below
json = "{}"
# create an instance of ENCSTATE from a JSON string
encstate_instance = ENCSTATE.from_json(json)
# print the JSON string representation of the object
print(ENCSTATE.to_json())

# convert the object into a dict
encstate_dict = encstate_instance.to_dict()
# create an instance of ENCSTATE from a dict
encstate_from_dict = ENCSTATE.from_dict(encstate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


