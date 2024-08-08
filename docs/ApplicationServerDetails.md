# ApplicationServerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed application server objects | [optional] 
**hostname** | **str** | Application server hostname. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; Hypen and  colon are allowed after the first and before the last character. | [optional] 
**id** | **str** | Identifier for the application server. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of the volume. String of up to 64 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. | [optional] 
**server_type** | **str** | Application server type. Possible values: &#39;vss&#39;, &#39;vmware&#39;. | [optional] 
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
from dscc.models.application_server_details import ApplicationServerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationServerDetails from a JSON string
application_server_details_instance = ApplicationServerDetails.from_json(json)
# print the JSON string representation of the object
print(ApplicationServerDetails.to_json())

# convert the object into a dict
application_server_details_dict = application_server_details_instance.to_dict()
# create an instance of ApplicationServerDetails from a dict
application_server_details_from_dict = ApplicationServerDetails.from_dict(application_server_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


