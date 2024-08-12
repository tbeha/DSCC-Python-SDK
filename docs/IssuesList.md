# IssuesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[IssueDetails]**](IssueDetails.md) |  | 
**page_limit** | **int** | The number of items retrieved from the pageOffset | 
**page_offset** | **int** | The offset specified in the offset query parameter. | 
**total** | **int** | The total count of objects in the result set. | 

## Example

```python
from dscc.models.issues_list import IssuesList

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesList from a JSON string
issues_list_instance = IssuesList.from_json(json)
# print the JSON string representation of the object
print(IssuesList.to_json())

# convert the object into a dict
issues_list_dict = issues_list_instance.to_dict()
# create an instance of IssuesList from a dict
issues_list_from_dict = IssuesList.from_dict(issues_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


