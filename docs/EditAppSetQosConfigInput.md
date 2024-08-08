# EditAppSetQosConfigInput

Edit QoS Configuration Input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | QoS Action | 
**bandwidth_max_limit_ki_b** | **float** | The maximum bandwidth limit permitted for the volume set associated with this policy. The bandwidth maximum limit must be between 0 and 9,007,199,254,740,991 KB/s. Pass -1 to unset the parameter | [optional] 
**enable** | **bool** | Enabling of QoS Configuration | [optional] 
**iops_max_limit** | **float** | The maximum IOPS limit permitted for the volume set associated with this policy. The IOPS maximum limit must be between 0 and 2,147,483,647 IO/s. Pass -1 to unset the parameter | [optional] 

## Example

```python
from dscc.models.edit_app_set_qos_config_input import EditAppSetQosConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of EditAppSetQosConfigInput from a JSON string
edit_app_set_qos_config_input_instance = EditAppSetQosConfigInput.from_json(json)
# print the JSON string representation of the object
print(EditAppSetQosConfigInput.to_json())

# convert the object into a dict
edit_app_set_qos_config_input_dict = edit_app_set_qos_config_input_instance.to_dict()
# create an instance of EditAppSetQosConfigInput from a dict
edit_app_set_qos_config_input_from_dict = EditAppSetQosConfigInput.from_dict(edit_app_set_qos_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


