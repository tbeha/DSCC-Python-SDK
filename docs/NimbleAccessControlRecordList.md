# NimbleAccessControlRecordList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleAccessControlRecordListItemsInner]**](NimbleAccessControlRecordListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for Access Control Record objects | [optional] 
**total** | **int** | Total number of Access Control Records. | [optional] 

## Example

```python
from dscc.models.nimble_access_control_record_list import NimbleAccessControlRecordList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleAccessControlRecordList from a JSON string
nimble_access_control_record_list_instance = NimbleAccessControlRecordList.from_json(json)
# print the JSON string representation of the object
print(NimbleAccessControlRecordList.to_json())

# convert the object into a dict
nimble_access_control_record_list_dict = nimble_access_control_record_list_instance.to_dict()
# create an instance of NimbleAccessControlRecordList from a dict
nimble_access_control_record_list_from_dict = NimbleAccessControlRecordList.from_dict(nimble_access_control_record_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


