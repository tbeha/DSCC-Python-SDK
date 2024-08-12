# NimbleHostGroupDetails

Host group details for the volumes to be exported for data access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_group_id** | **str** | Identifier for the host group. | [optional] 
**lun** | **int** | Custom LUN ID for the host group. Specify integer in the range 0 to 2047. | [optional] 

## Example

```python
from dscc.models.nimble_host_group_details import NimbleHostGroupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleHostGroupDetails from a JSON string
nimble_host_group_details_instance = NimbleHostGroupDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleHostGroupDetails.to_json())

# convert the object into a dict
nimble_host_group_details_dict = nimble_host_group_details_instance.to_dict()
# create an instance of NimbleHostGroupDetails from a dict
nimble_host_group_details_from_dict = NimbleHostGroupDetails.from_dict(nimble_host_group_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


