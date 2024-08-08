# NimbleNsPoolSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of pool. | [optional] 
**name** | **str** | Name of pool. | [optional] 

## Example

```python
from dscc.models.nimble_ns_pool_summary import NimbleNsPoolSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNsPoolSummary from a JSON string
nimble_ns_pool_summary_instance = NimbleNsPoolSummary.from_json(json)
# print the JSON string representation of the object
print(NimbleNsPoolSummary.to_json())

# convert the object into a dict
nimble_ns_pool_summary_dict = nimble_ns_pool_summary_instance.to_dict()
# create an instance of NimbleNsPoolSummary from a dict
nimble_ns_pool_summary_from_dict = NimbleNsPoolSummary.from_dict(nimble_ns_pool_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


