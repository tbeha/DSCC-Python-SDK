# NimbleSpaceDomainList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleSpaceDomainListItemsInner]**](NimbleSpaceDomainListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for application-summary objects | [optional] 
**total** | **int** | Total number of applications. | [optional] 

## Example

```python
from dscc.models.nimble_space_domain_list import NimbleSpaceDomainList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSpaceDomainList from a JSON string
nimble_space_domain_list_instance = NimbleSpaceDomainList.from_json(json)
# print the JSON string representation of the object
print(NimbleSpaceDomainList.to_json())

# convert the object into a dict
nimble_space_domain_list_dict = nimble_space_domain_list_instance.to_dict()
# create an instance of NimbleSpaceDomainList from a dict
nimble_space_domain_list_from_dict = NimbleSpaceDomainList.from_dict(nimble_space_domain_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


