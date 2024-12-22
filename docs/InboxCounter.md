# InboxCounter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.inbox_counter import InboxCounter

# TODO update the JSON string below
json = "{}"
# create an instance of InboxCounter from a JSON string
inbox_counter_instance = InboxCounter.from_json(json)
# print the JSON string representation of the object
print(InboxCounter.to_json())

# convert the object into a dict
inbox_counter_dict = inbox_counter_instance.to_dict()
# create an instance of InboxCounter from a dict
inbox_counter_from_dict = InboxCounter.from_dict(inbox_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


