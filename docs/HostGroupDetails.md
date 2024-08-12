# HostGroupDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[HostDetails]**](HostDetails.md) | Hosts | [optional] 
**id** | **str** | uid | [optional] 
**name** | **str** | name | [optional] 

## Example

```python
from dscc.models.host_group_details import HostGroupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostGroupDetails from a JSON string
host_group_details_instance = HostGroupDetails.from_json(json)
# print the JSON string representation of the object
print(HostGroupDetails.to_json())

# convert the object into a dict
host_group_details_dict = host_group_details_instance.to_dict()
# create an instance of HostGroupDetails from a dict
host_group_details_from_dict = HostGroupDetails.from_dict(host_group_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


