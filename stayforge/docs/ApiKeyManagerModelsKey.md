# ApiKeyManagerModelsKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '676b3247868770ac5f209f0d']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**url** | **str** | The name of the hotel key. By default, it combines a base name with a random town. | 
**num** | **str** | Order number | [optional] [default to '']
**effective_at** | **str** | Effective at | [optional] [default to '2024-12-24T22:14:31.976272Z']
**ineffective_at** | **str** | Ineffective at | [optional] [default to '2024-12-25T22:14:31.976299Z']

## Example

```python
from stayforge.models.api_key_manager_models_key import ApiKeyManagerModelsKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyManagerModelsKey from a JSON string
api_key_manager_models_key_instance = ApiKeyManagerModelsKey.from_json(json)
# print the JSON string representation of the object
print(ApiKeyManagerModelsKey.to_json())

# convert the object into a dict
api_key_manager_models_key_dict = api_key_manager_models_key_instance.to_dict()
# create an instance of ApiKeyManagerModelsKey from a dict
api_key_manager_models_key_from_dict = ApiKeyManagerModelsKey.from_dict(api_key_manager_models_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


