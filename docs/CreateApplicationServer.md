# CreateApplicationServer

Create Nimble application server input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Text description of application server. String of up to 255 printable ASCII characters. Defaults to the empty string. | [optional] 
**hostname** | **str** | Application server hostname. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; Hypen and  colon are allowed after the first and before the last character. | 
**metadata** | [**List[AppKeyValue]**](AppKeyValue.md) | Key-value pairs that augment an application server&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array. | [optional] 
**name** | **str** | Name of the volume. String of up to 64 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. | 
**password** | **str** | Application server password. A password with few constraints. A string of up to 255 characters. | [optional] 
**port** | **int** | Application server port number. Positive integer value up to 65535 representing TCP/IP port. Defaults to 65536. | [optional] 
**server_type** | **str** | Application server type. Defaults to &#39;vmware&#39;. Possible values are &#39;vss&#39; and &#39;vmware&#39;. | [optional] 
**username** | **str** | Application server username. String of up to 255 printable ASCII characters. | [optional] 

## Example

```python
from dscc.models.create_application_server import CreateApplicationServer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationServer from a JSON string
create_application_server_instance = CreateApplicationServer.from_json(json)
# print the JSON string representation of the object
print(CreateApplicationServer.to_json())

# convert the object into a dict
create_application_server_dict = create_application_server_instance.to_dict()
# create an instance of CreateApplicationServer from a dict
create_application_server_from_dict = CreateApplicationServer.from_dict(create_application_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


