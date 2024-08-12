# NimbleProtectionTemplateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleProtectionTemplateListItemsInner]**](NimbleProtectionTemplateListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for Protection Template objects | [optional] 
**total** | **int** | Total number of Protection Templates. | [optional] 

## Example

```python
from dscc.models.nimble_protection_template_list import NimbleProtectionTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleProtectionTemplateList from a JSON string
nimble_protection_template_list_instance = NimbleProtectionTemplateList.from_json(json)
# print the JSON string representation of the object
print(NimbleProtectionTemplateList.to_json())

# convert the object into a dict
nimble_protection_template_list_dict = nimble_protection_template_list_instance.to_dict()
# create an instance of NimbleProtectionTemplateList from a dict
nimble_protection_template_list_from_dict = NimbleProtectionTemplateList.from_dict(nimble_protection_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


