# DeviceType4EditAppSetQosConfigInput

Edit QoS Configuration Input (Applicable for OS version 10.4.0 and above)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | QoS Action | 
**bandwidth_max_limit_ki_b** | **float** | The maximum bandwidth limit permitted for the volume set associated with this policy. The bandwidth maximum limit must be between 0 and 9,007,199,254,740,991 KB/s. Pass -1 to unset the parameter | [optional] 
**enable** | **bool** | Enabling of QoS Configuration | [optional] 
**enable_sr_alert** | **bool** | Sets the SR alert with the criterion name as the vvset name based on the max limits being set on the QoS parameters. If provided, the SR alert criterion will be created or updated based on updated parameters. | [optional] 
**iops_max_limit** | **float** | The maximum IOPS limit permitted for the volume set associated with this policy. The IOPS maximum limit must be between 0 and 2,147,483,647 IO/s. Pass -1 to unset the parameter | [optional] 
**per_tb** | **bool** | Sets the maximum IOPS limit or/and bandwidth limit for QoS throttling based on the number of terabytes configured for the volumes in the volume set on which QoS rule is configured.  By default, this option is off. Once per_tb is set, it cannot be unset. | [optional] 

## Example

```python
from dscc.models.device_type4_edit_app_set_qos_config_input import DeviceType4EditAppSetQosConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EditAppSetQosConfigInput from a JSON string
device_type4_edit_app_set_qos_config_input_instance = DeviceType4EditAppSetQosConfigInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EditAppSetQosConfigInput.to_json())

# convert the object into a dict
device_type4_edit_app_set_qos_config_input_dict = device_type4_edit_app_set_qos_config_input_instance.to_dict()
# create an instance of DeviceType4EditAppSetQosConfigInput from a dict
device_type4_edit_app_set_qos_config_input_from_dict = DeviceType4EditAppSetQosConfigInput.from_dict(device_type4_edit_app_set_qos_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


