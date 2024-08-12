# CommonFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int** | Time when this application server was created. Seconds since last epoch i.e. 00:00 January 1, 1970 | [optional] 
**customer_id** | **str** | customerId | [optional] 
**description** | **str** | Text description of application server. String of up to 255 printable ASCII characters. Defaults to the empty string. | [optional] 
**generation** | **int** | generation | [optional] 
**last_modified** | **int** | Time when this application server was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**metadata** | [**List[AppKeyValue]**](AppKeyValue.md) | Key-value pairs that augment an application server&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array. | [optional] 
**port** | **int** | Application server port number. Positive integer value up to 65535 representing TCP/IP port. Defaults to 65536. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**type** | **str** | type | [optional] 
**username** | **str** | Application server username. String of up to 255 printable ASCII characters. | [optional] 

## Example

```python
from dscc.models.common_fields import CommonFields

# TODO update the JSON string below
json = "{}"
# create an instance of CommonFields from a JSON string
common_fields_instance = CommonFields.from_json(json)
# print the JSON string representation of the object
print(CommonFields.to_json())

# convert the object into a dict
common_fields_dict = common_fields_instance.to_dict()
# create an instance of CommonFields from a dict
common_fields_from_dict = CommonFields.from_dict(common_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


