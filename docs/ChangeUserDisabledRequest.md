# ChangeUserDisabledRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | 
**user_id** | **str** |  | 

## Example

```python
from openapi_client.models.change_user_disabled_request import ChangeUserDisabledRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeUserDisabledRequest from a JSON string
change_user_disabled_request_instance = ChangeUserDisabledRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeUserDisabledRequest.to_json())

# convert the object into a dict
change_user_disabled_request_dict = change_user_disabled_request_instance.to_dict()
# create an instance of ChangeUserDisabledRequest from a dict
change_user_disabled_request_from_dict = ChangeUserDisabledRequest.from_dict(change_user_disabled_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


