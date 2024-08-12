# FieldsWithFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Application server hostname. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; Hypen and  colon are allowed after the first and before the last character. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier for the application server. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the volume. String of up to 64 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. &#x60;Filter, Sort&#x60; | [optional] 
**server_type** | **str** | Application server type. Possible values: &#39;vss&#39;, &#39;vmware&#39;. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.fields_with_filter import FieldsWithFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FieldsWithFilter from a JSON string
fields_with_filter_instance = FieldsWithFilter.from_json(json)
# print the JSON string representation of the object
print(FieldsWithFilter.to_json())

# convert the object into a dict
fields_with_filter_dict = fields_with_filter_instance.to_dict()
# create an instance of FieldsWithFilter from a dict
fields_with_filter_from_dict = FieldsWithFilter.from_dict(fields_with_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


