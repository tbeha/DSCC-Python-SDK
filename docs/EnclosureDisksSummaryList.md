# EnclosureDisksSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EnclosureDiskList]**](EnclosureDiskList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure cards object | [optional] 
**total** | **int** | Number of enclosure cards | [optional] 

## Example

```python
from dscc.models.enclosure_disks_summary_list import EnclosureDisksSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureDisksSummaryList from a JSON string
enclosure_disks_summary_list_instance = EnclosureDisksSummaryList.from_json(json)
# print the JSON string representation of the object
print(EnclosureDisksSummaryList.to_json())

# convert the object into a dict
enclosure_disks_summary_list_dict = enclosure_disks_summary_list_instance.to_dict()
# create an instance of EnclosureDisksSummaryList from a dict
enclosure_disks_summary_list_from_dict = EnclosureDisksSummaryList.from_dict(enclosure_disks_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


