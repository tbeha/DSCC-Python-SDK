# DeviceType4NwCimEditCim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cim_policy** | **bool** | Specifies the CIM Policy of CIM server. | [optional] 
**enable_cim_service** | **bool** | Enable or disbale Cim service. | [optional] 
**http_state** | **bool** | Specifies whether HTTPState is enabled or disabled for CIM Server. Unsupported from version 10.4.0 and above | [optional] 
**https_state** | **bool** | Specifies whether HTTPS state is enabled or disabled for cim server. Unsupported from version 10.4.0 and above | [optional] 
**id** | **str** | Unique identifier of the CIM Server. | [optional] 
**slp_state** | **bool** | SLPport specification. | [optional] 

## Example

```python
from dscc.models.device_type4_nw_cim_edit_cim import DeviceType4NwCimEditCim

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4NwCimEditCim from a JSON string
device_type4_nw_cim_edit_cim_instance = DeviceType4NwCimEditCim.from_json(json)
# print the JSON string representation of the object
print(DeviceType4NwCimEditCim.to_json())

# convert the object into a dict
device_type4_nw_cim_edit_cim_dict = device_type4_nw_cim_edit_cim_instance.to_dict()
# create an instance of DeviceType4NwCimEditCim from a dict
device_type4_nw_cim_edit_cim_from_dict = DeviceType4NwCimEditCim.from_dict(device_type4_nw_cim_edit_cim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


