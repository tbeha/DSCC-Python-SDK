# ScAssociatedLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_uri** | **str** | Resource URI | [optional] 
**type** | **str** | Resource Name | [optional] 

## Example

```python
from dscc.models.sc_associated_links_inner import ScAssociatedLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ScAssociatedLinksInner from a JSON string
sc_associated_links_inner_instance = ScAssociatedLinksInner.from_json(json)
# print the JSON string representation of the object
print(ScAssociatedLinksInner.to_json())

# convert the object into a dict
sc_associated_links_inner_dict = sc_associated_links_inner_instance.to_dict()
# create an instance of ScAssociatedLinksInner from a dict
sc_associated_links_inner_from_dict = ScAssociatedLinksInner.from_dict(sc_associated_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


