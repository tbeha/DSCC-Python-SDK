# HostChapDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[HostChapObject]**](HostChapObject.md) |  | [optional] 
**request_uri** | **str** | requestUri for host initiators | [optional] 
**total** | **int** | Number of hosts | [optional] 

## Example

```python
from dscc.models.host_chap_details import HostChapDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostChapDetails from a JSON string
host_chap_details_instance = HostChapDetails.from_json(json)
# print the JSON string representation of the object
print(HostChapDetails.to_json())

# convert the object into a dict
host_chap_details_dict = host_chap_details_instance.to_dict()
# create an instance of HostChapDetails from a dict
host_chap_details_from_dict = HostChapDetails.from_dict(host_chap_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


