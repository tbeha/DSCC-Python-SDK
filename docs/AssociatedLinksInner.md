# AssociatedLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_uri** | **str** | Resource Uri | [optional] 
**type** | **str** | Resource Name | [optional] 

## Example

```python
from dscc.models.associated_links_inner import AssociatedLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedLinksInner from a JSON string
associated_links_inner_instance = AssociatedLinksInner.from_json(json)
# print the JSON string representation of the object
print(AssociatedLinksInner.to_json())

# convert the object into a dict
associated_links_inner_dict = associated_links_inner_instance.to_dict()
# create an instance of AssociatedLinksInner from a dict
associated_links_inner_from_dict = AssociatedLinksInner.from_dict(associated_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


