# InitiatorGroupFilterableFieldsWithoutFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_protocol** | **str** | Initiator group access protocol. Possible values: &#39;iscsi&#39;, &#39;fc&#39;. | [optional] 
**app_uuid** | **str** | Application identifier of initiator group. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed | [optional] 
**host_type** | **str** | Initiator group host type. Available options are auto and hpux. The default option is auto. This attribute will be applied to all the initiators in the initiator group. Initiators with different host OSes should not be kept in the same initiator group having a non-default host type attribute. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**id** | **str** | Identifier for initiator group. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of initiator group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 

## Example

```python
from dscc.models.initiator_group_filterable_fields_without_filter import InitiatorGroupFilterableFieldsWithoutFilter

# TODO update the JSON string below
json = "{}"
# create an instance of InitiatorGroupFilterableFieldsWithoutFilter from a JSON string
initiator_group_filterable_fields_without_filter_instance = InitiatorGroupFilterableFieldsWithoutFilter.from_json(json)
# print the JSON string representation of the object
print(InitiatorGroupFilterableFieldsWithoutFilter.to_json())

# convert the object into a dict
initiator_group_filterable_fields_without_filter_dict = initiator_group_filterable_fields_without_filter_instance.to_dict()
# create an instance of InitiatorGroupFilterableFieldsWithoutFilter from a dict
initiator_group_filterable_fields_without_filter_from_dict = InitiatorGroupFilterableFieldsWithoutFilter.from_dict(initiator_group_filterable_fields_without_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


