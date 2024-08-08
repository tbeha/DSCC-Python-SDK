# NimbleInitiatorGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleInitiatorGroup]**](NimbleInitiatorGroup.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed initiator groups object | [optional] 
**total** | **int** | Total number of initiator groups. | [optional] 

## Example

```python
from dscc.models.nimble_initiator_group_list import NimbleInitiatorGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleInitiatorGroupList from a JSON string
nimble_initiator_group_list_instance = NimbleInitiatorGroupList.from_json(json)
# print the JSON string representation of the object
print(NimbleInitiatorGroupList.to_json())

# convert the object into a dict
nimble_initiator_group_list_dict = nimble_initiator_group_list_instance.to_dict()
# create an instance of NimbleInitiatorGroupList from a dict
nimble_initiator_group_list_from_dict = NimbleInitiatorGroupList.from_dict(nimble_initiator_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


