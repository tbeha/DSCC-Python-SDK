# NimbleNetworkFieldsWithSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for network settings. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the network configuration. Possible values: &#39;active&#39;, &#39;backup&#39;, &#39;draft&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**role** | **str** | Role of network configuration. Possible values: &#39;active&#39;, &#39;backup&#39;, &#39;draft&#39;.  &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.nimble_network_fields_with_sort_key import NimbleNetworkFieldsWithSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNetworkFieldsWithSortKey from a JSON string
nimble_network_fields_with_sort_key_instance = NimbleNetworkFieldsWithSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleNetworkFieldsWithSortKey.to_json())

# convert the object into a dict
nimble_network_fields_with_sort_key_dict = nimble_network_fields_with_sort_key_instance.to_dict()
# create an instance of NimbleNetworkFieldsWithSortKey from a dict
nimble_network_fields_with_sort_key_from_dict = NimbleNetworkFieldsWithSortKey.from_dict(nimble_network_fields_with_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


