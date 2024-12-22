# RichTextBlockList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bullet_list_marker** | **str** |  | [optional] 
**items** | [**List[RichTextListItem]**](RichTextListItem.md) |  | [optional] 
**ordered** | **bool** |  | 
**ordered_list_delimiter** | **str** |  | [optional] 
**ordered_list_starts_at** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.rich_text_block_list import RichTextBlockList

# TODO update the JSON string below
json = "{}"
# create an instance of RichTextBlockList from a JSON string
rich_text_block_list_instance = RichTextBlockList.from_json(json)
# print the JSON string representation of the object
print(RichTextBlockList.to_json())

# convert the object into a dict
rich_text_block_list_dict = rich_text_block_list_instance.to_dict()
# create an instance of RichTextBlockList from a dict
rich_text_block_list_from_dict = RichTextBlockList.from_dict(rich_text_block_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


