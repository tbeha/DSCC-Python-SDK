# HostDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | uid | [optional] 
**name** | **str** | name | [optional] 

## Example

```python
from dscc.models.host_details import HostDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostDetails from a JSON string
host_details_instance = HostDetails.from_json(json)
# print the JSON string representation of the object
print(HostDetails.to_json())

# convert the object into a dict
host_details_dict = host_details_instance.to_dict()
# create an instance of HostDetails from a dict
host_details_from_dict = HostDetails.from_dict(host_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


