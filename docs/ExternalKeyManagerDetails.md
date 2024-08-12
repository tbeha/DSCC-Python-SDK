# ExternalKeyManagerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed external key manager objects | [optional] 
**id** | **str** | Identifier for the External key manager. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of External key manager. | [optional] [default to 'default']
**active** | **bool** | Indicates if the external key manager is active or not | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**description** | **str** | String of up to 255 printable ASCII characters. Example: &#39;99.9999% availability&#39;. | [optional] 
**hostname** | **str** | Hostname of the external key manager | [optional] 
**port** | **int** | Positive integer value up to 65535 representing External key manager port. | [optional] 
**protocol** | **str** | Possible values: &#39;KMIP1_0&#39;, &#39;KMIP1_1&#39;, &#39;KMIP1_2&#39;, &#39;KMIP1_3&#39;. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**status** | **str** | status | [optional] 
**username** | **str** | External key manager username. String of up to 255 printable ASCII characters. | [optional] 

## Example

```python
from dscc.models.external_key_manager_details import ExternalKeyManagerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKeyManagerDetails from a JSON string
external_key_manager_details_instance = ExternalKeyManagerDetails.from_json(json)
# print the JSON string representation of the object
print(ExternalKeyManagerDetails.to_json())

# convert the object into a dict
external_key_manager_details_dict = external_key_manager_details_instance.to_dict()
# create an instance of ExternalKeyManagerDetails from a dict
external_key_manager_details_from_dict = ExternalKeyManagerDetails.from_dict(external_key_manager_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


