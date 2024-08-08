# InitiatorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Initiator]**](Initiator.md) |  | [optional] 
**page_limit** | **int** | Page Limit | [optional] 
**page_offset** | **int** | Page Offset | [optional] 
**request_uri** | **str** | requestUri for initiators | [optional] 
**total** | **int** | Number of host initiators | [optional] 

## Example

```python
from dscc.models.initiator_list import InitiatorList

# TODO update the JSON string below
json = "{}"
# create an instance of InitiatorList from a JSON string
initiator_list_instance = InitiatorList.from_json(json)
# print the JSON string representation of the object
print(InitiatorList.to_json())

# convert the object into a dict
initiator_list_dict = initiator_list_instance.to_dict()
# create an instance of InitiatorList from a dict
initiator_list_from_dict = InitiatorList.from_dict(initiator_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


