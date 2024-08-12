# NimbleHostGroupDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[NimbleHostSummaryDetails]**](NimbleHostSummaryDetails.md) | List of hosts. | [optional] 
**sc_host_group_id** | **str** | Identifier for the host group in the Data Services Cloud Console (DSCC) | [optional] 
**sc_host_group_name** | **str** | Name of the Host Group in the Data Services Cloud Console (DSCC) | [optional] 
**user_created** | **bool** | Indicates whether it is user created hostgroup or discovered hostgroup. | [optional] 

## Example

```python
from dscc.models.nimble_host_group_detail import NimbleHostGroupDetail

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleHostGroupDetail from a JSON string
nimble_host_group_detail_instance = NimbleHostGroupDetail.from_json(json)
# print the JSON string representation of the object
print(NimbleHostGroupDetail.to_json())

# convert the object into a dict
nimble_host_group_detail_dict = nimble_host_group_detail_instance.to_dict()
# create an instance of NimbleHostGroupDetail from a dict
nimble_host_group_detail_from_dict = NimbleHostGroupDetail.from_dict(nimble_host_group_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


