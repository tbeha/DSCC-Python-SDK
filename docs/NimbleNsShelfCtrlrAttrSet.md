# NimbleNsShelfCtrlrAttrSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cached_serial** | **str** | Cached serial. | [optional] 
**disk_serials** | **str** | Comma separated list of disk serials connected to this logical controller. | [optional] 
**disk_types** | **str** | Comma separated list of disk types (H for HDD, S for SSD). | [optional] 
**hw_state** | **str** | The hardware state for this logical controller. Possible values:&#39;discovering&#39;, &#39;disconnected&#39;, &#39;void&#39;,&#39;ready&#39;,&#39;faulty&#39;. | [optional] 
**session_serial** | **str** | Session serial. | [optional] 
**sw_type** | **str** | The software type of this logical controller. Possible values:&#39;Disk Shelf&#39;, &#39;unknown shelf software type&#39;, &#39;All Flash Shelf&#39;,&#39;Head Shelf&#39;. | [optional] 

## Example

```python
from dscc.models.nimble_ns_shelf_ctrlr_attr_set import NimbleNsShelfCtrlrAttrSet

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNsShelfCtrlrAttrSet from a JSON string
nimble_ns_shelf_ctrlr_attr_set_instance = NimbleNsShelfCtrlrAttrSet.from_json(json)
# print the JSON string representation of the object
print(NimbleNsShelfCtrlrAttrSet.to_json())

# convert the object into a dict
nimble_ns_shelf_ctrlr_attr_set_dict = nimble_ns_shelf_ctrlr_attr_set_instance.to_dict()
# create an instance of NimbleNsShelfCtrlrAttrSet from a dict
nimble_ns_shelf_ctrlr_attr_set_from_dict = NimbleNsShelfCtrlrAttrSet.from_dict(nimble_ns_shelf_ctrlr_attr_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


