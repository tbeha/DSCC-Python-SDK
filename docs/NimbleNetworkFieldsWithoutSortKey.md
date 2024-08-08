# NimbleNetworkFieldsWithoutSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for network settings. | [optional] 
**name** | **str** | Name of the network configuration. Possible values: &#39;active&#39;, &#39;backup&#39;, &#39;draft&#39; | [optional] 
**role** | **str** | Role of network configuration. Possible values: &#39;active&#39;, &#39;backup&#39;, &#39;draft&#39; | [optional] 

## Example

```python
from dscc.models.nimble_network_fields_without_sort_key import NimbleNetworkFieldsWithoutSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNetworkFieldsWithoutSortKey from a JSON string
nimble_network_fields_without_sort_key_instance = NimbleNetworkFieldsWithoutSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleNetworkFieldsWithoutSortKey.to_json())

# convert the object into a dict
nimble_network_fields_without_sort_key_dict = nimble_network_fields_without_sort_key_instance.to_dict()
# create an instance of NimbleNetworkFieldsWithoutSortKey from a dict
nimble_network_fields_without_sort_key_from_dict = NimbleNetworkFieldsWithoutSortKey.from_dict(nimble_network_fields_without_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


