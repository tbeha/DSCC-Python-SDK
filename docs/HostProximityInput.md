# HostProximityInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | Name of the host of which proximity setting is getting changed. | 
**proximity** | **str** | Host proximity setting for Active Peer Persistence configuration. Supported values are - PRIMARY, SECONDARY and ALL | 

## Example

```python
from dscc.models.host_proximity_input import HostProximityInput

# TODO update the JSON string below
json = "{}"
# create an instance of HostProximityInput from a JSON string
host_proximity_input_instance = HostProximityInput.from_json(json)
# print the JSON string representation of the object
print(HostProximityInput.to_json())

# convert the object into a dict
host_proximity_input_dict = host_proximity_input_instance.to_dict()
# create an instance of HostProximityInput from a dict
host_proximity_input_from_dict = HostProximityInput.from_dict(host_proximity_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


