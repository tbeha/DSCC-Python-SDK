# CommonResourceAttributesHosts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_state** | **str** | Cloud connectivity status of the system where the host resource belongs | [optional] 

## Example

```python
from dscc.models.common_resource_attributes_hosts import CommonResourceAttributesHosts

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResourceAttributesHosts from a JSON string
common_resource_attributes_hosts_instance = CommonResourceAttributesHosts.from_json(json)
# print the JSON string representation of the object
print(CommonResourceAttributesHosts.to_json())

# convert the object into a dict
common_resource_attributes_hosts_dict = common_resource_attributes_hosts_instance.to_dict()
# create an instance of CommonResourceAttributesHosts from a dict
common_resource_attributes_hosts_from_dict = CommonResourceAttributesHosts.from_dict(common_resource_attributes_hosts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


