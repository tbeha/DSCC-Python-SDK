# NimbleNsCtrlrNvmeCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial_number** | **str** | Serial number. | [optional] 
**size** | **int** | NVMe card cache size in bytes. | [optional] 
**state** | **str** | Online state. Possible values: &#39;valid&#39;, &#39;in use&#39;, &#39;failed&#39;. | [optional] 

## Example

```python
from dscc.models.nimble_ns_ctrlr_nvme_card import NimbleNsCtrlrNvmeCard

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNsCtrlrNvmeCard from a JSON string
nimble_ns_ctrlr_nvme_card_instance = NimbleNsCtrlrNvmeCard.from_json(json)
# print the JSON string representation of the object
print(NimbleNsCtrlrNvmeCard.to_json())

# convert the object into a dict
nimble_ns_ctrlr_nvme_card_dict = nimble_ns_ctrlr_nvme_card_instance.to_dict()
# create an instance of NimbleNsCtrlrNvmeCard from a dict
nimble_ns_ctrlr_nvme_card_from_dict = NimbleNsCtrlrNvmeCard.from_dict(nimble_ns_ctrlr_nvme_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


