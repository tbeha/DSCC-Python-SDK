# DisksSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DisksList]**](DisksList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed disks object | [optional] 
**total** | **int** | Number of disks | [optional] 

## Example

```python
from dscc.models.disks_summary_list import DisksSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DisksSummaryList from a JSON string
disks_summary_list_instance = DisksSummaryList.from_json(json)
# print the JSON string representation of the object
print(DisksSummaryList.to_json())

# convert the object into a dict
disks_summary_list_dict = disks_summary_list_instance.to_dict()
# create an instance of DisksSummaryList from a dict
disks_summary_list_from_dict = DisksSummaryList.from_dict(disks_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


