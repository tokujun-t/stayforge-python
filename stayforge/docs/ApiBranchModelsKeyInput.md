# ApiBranchModelsKeyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the hotel key. By default, it combines a base name with a random town. | 
**postcode** | **str** | The postal code of the key location. | [optional] [default to '000-0000']
**address** | **str** | The full effective of the key, including administrative unit, city, town, and detailed location. | [optional] [default to '000-0000']
**telephone** | **str** | The contact telephone number for the key. | 

## Example

```python
from stayforge.models.api_branch_models_key_input import ApiBranchModelsKeyInput

# TODO update the JSON string below
json = "{}"
# create an instance of ApiBranchModelsKeyInput from a JSON string
api_branch_models_key_input_instance = ApiBranchModelsKeyInput.from_json(json)
# print the JSON string representation of the object
print(ApiBranchModelsKeyInput.to_json())

# convert the object into a dict
api_branch_models_key_input_dict = api_branch_models_key_input_instance.to_dict()
# create an instance of ApiBranchModelsKeyInput from a dict
api_branch_models_key_input_from_dict = ApiBranchModelsKeyInput.from_dict(api_branch_models_key_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

