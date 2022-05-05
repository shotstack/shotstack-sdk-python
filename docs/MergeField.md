# MergeField

A merge field consists of a key; `find`, and a value; `replace`. Merge fields can be used to replace placeholders within the JSON edit to create re-usable templates. Placeholders should be a string with double brace delimiters, i.e. `\"{{NAME}}\"`. A placeholder can be used for any value within the JSON edit.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**find** | **str** | The string to find &lt;u&gt;without&lt;/u&gt; delimiters. | 
**replace** | **bool, date, datetime, dict, float, int, list, str, none_type** | The replacement value. The replacement can be any valid JSON type - string, boolean, number, etc... | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


