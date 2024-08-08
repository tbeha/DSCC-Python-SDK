# WitnessList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Witness]**](Witness.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | Request URI for quorum witness objects | [optional] 
**total** | **int** | Total number of witnesses. | [optional] 

## Example

```python
from dscc.models.witness_list import WitnessList

# TODO update the JSON string below
json = "{}"
# create an instance of WitnessList from a JSON string
witness_list_instance = WitnessList.from_json(json)
# print the JSON string representation of the object
print(WitnessList.to_json())

# convert the object into a dict
witness_list_dict = witness_list_instance.to_dict()
# create an instance of WitnessList from a dict
witness_list_from_dict = WitnessList.from_dict(witness_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


