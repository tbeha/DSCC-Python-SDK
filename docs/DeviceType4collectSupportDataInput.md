# DeviceType4collectSupportDataInput

Trigger and collect support data collection on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Type of a collection. | [optional] 
**options** | **List[str]** | Options needed for the collection. If options are not specified, default values will be used.   INSPLORECOLLECTION can have any or all of \&quot;clidata\&quot;, \&quot;nodedata\&quot; and \&quot;tocdata\&quot;     Default options - [\&quot;clidata\&quot;,\&quot;nodedata\&quot;,\&quot;tocdata\&quot;]   PERFCOLLECTION should have 3 options,   * Iteration - a number between 1 to 1000 as a string,   * Interval - a number in seconds between 1 to 172800 as a string   * Type of collection -default or -comprehensive   Default options - [\&quot;60\&quot;,\&quot;10\&quot;,\&quot;-default\&quot;]  Other collection types won&#39;t require any options, if provided will be ignored. | [optional] 

## Example

```python
from dscc.models.device_type4collect_support_data_input import DeviceType4collectSupportDataInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4collectSupportDataInput from a JSON string
device_type4collect_support_data_input_instance = DeviceType4collectSupportDataInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4collectSupportDataInput.to_json())

# convert the object into a dict
device_type4collect_support_data_input_dict = device_type4collect_support_data_input_instance.to_dict()
# create an instance of DeviceType4collectSupportDataInput from a dict
device_type4collect_support_data_input_from_dict = DeviceType4collectSupportDataInput.from_dict(device_type4collect_support_data_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


