# stayforge
![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge)
![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg)
![PyPI Version](https://img.shields.io/pypi/v/stayforge)

### SDK

- [Python SDK](https://github.com/tokujun-t/stayforge-python)

We provided SDKs (currently only the Python version is provided).
Before deciding to call the API directly, you may wish to try the SDK to speed up your development.

![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)


### About Healthcheck

Healthcheck at `/api/healthcheck`. curl to check if the service is working.

```shell
curl -I http://<your service>/api/healthcheck
```
### Some Links

GitHub Repo
[https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)

Wiki
[https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki)


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 0.0.0-f3641a5
- Build date: 2024-12-19T14:22:39.350236Z[Etc/UTC]
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/tokujun-t/stayforge-python](https://github.com/tokujun-t/stayforge-python)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/tokujun-t/stayforge-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/tokujun-t/stayforge-python.git`)

Then import the package:
```python
import stayforge
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import stayforge
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import stayforge
from stayforge.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = stayforge.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.BranchesApi(api_client)
    api_branch_models_key_input = stayforge.ApiBranchModelsKeyInput() # ApiBranchModelsKeyInput | 

    try:
        # Create Key
        api_response = api_instance.create_key_api_branch_post(api_branch_models_key_input)
        print("The response of BranchesApi->create_key_api_branch_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BranchesApi->create_key_api_branch_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BranchesApi* | [**create_key_api_branch_post**](docs/BranchesApi.md#create_key_api_branch_post) | **POST** /api/branch/ | Create Key
*BranchesApi* | [**delete_key_api_branch_id_delete**](docs/BranchesApi.md#delete_key_api_branch_id_delete) | **DELETE** /api/branch/&lt;id&gt; | Delete Key
*BranchesApi* | [**get_key_api_branch_id_get**](docs/BranchesApi.md#get_key_api_branch_id_get) | **GET** /api/branch/&lt;id&gt; | Get Key
*BranchesApi* | [**get_keys_api_branch_get**](docs/BranchesApi.md#get_keys_api_branch_get) | **GET** /api/branch/ | Get Keys
*BranchesApi* | [**put_key_api_branch_id_put**](docs/BranchesApi.md#put_key_api_branch_id_put) | **PUT** /api/branch/&lt;id&gt; | Put Key
*KeyManagerApi* | [**create_key_api_key_post**](docs/KeyManagerApi.md#create_key_api_key_post) | **POST** /api/key/ | Create Key
*KeyManagerApi* | [**delete_key_api_key_id_delete**](docs/KeyManagerApi.md#delete_key_api_key_id_delete) | **DELETE** /api/key/&lt;id&gt; | Delete Key
*KeyManagerApi* | [**get_key_api_key_id_get**](docs/KeyManagerApi.md#get_key_api_key_id_get) | **GET** /api/key/&lt;id&gt; | Get Key
*KeyManagerApi* | [**get_key_by_num_api_key_num_num_get**](docs/KeyManagerApi.md#get_key_by_num_api_key_num_num_get) | **GET** /api/key/num/&lt;num&gt; | Get Key By Num
*KeyManagerApi* | [**put_key_api_key_id_put**](docs/KeyManagerApi.md#put_key_api_key_id_put) | **PUT** /api/key/&lt;id&gt; | Put Key
*OrdersApi* | [**create_order_api_order_post**](docs/OrdersApi.md#create_order_api_order_post) | **POST** /api/order/ | Create Order
*OrdersApi* | [**delete_order_api_order_delete_id_delete**](docs/OrdersApi.md#delete_order_api_order_delete_id_delete) | **DELETE** /api/order/_delete/&lt;id&gt; | Delete Order
*OrdersApi* | [**get_order_by_id_api_order_id_get**](docs/OrdersApi.md#get_order_by_id_api_order_id_get) | **GET** /api/order/&lt;id&gt; | Get Order By Id
*OrdersApi* | [**get_order_by_num_api_order_num_num_get**](docs/OrdersApi.md#get_order_by_num_api_order_num_num_get) | **GET** /api/order/num/&lt;num&gt; | Get Order By Num
*OrdersApi* | [**get_order_types_api_order_order_types_get**](docs/OrdersApi.md#get_order_types_api_order_order_types_get) | **GET** /api/order/order_types | Get Order Types
*PluginsManagerApi* | [**create_plugins_profile_api_plugins_manager_post**](docs/PluginsManagerApi.md#create_plugins_profile_api_plugins_manager_post) | **POST** /api/plugins_manager/ | Create Plugins Profile
*PluginsManagerApi* | [**delete_plugins_profile_api_plugins_manager_id_delete**](docs/PluginsManagerApi.md#delete_plugins_profile_api_plugins_manager_id_delete) | **DELETE** /api/plugins_manager/&lt;id&gt; | Delete Plugins Profile
*PluginsManagerApi* | [**get_plugins_profile_api_plugins_manager_get**](docs/PluginsManagerApi.md#get_plugins_profile_api_plugins_manager_get) | **GET** /api/plugins_manager/ | Get Plugins Profile
*PluginsManagerApi* | [**get_plugins_profile_api_plugins_manager_id_get**](docs/PluginsManagerApi.md#get_plugins_profile_api_plugins_manager_id_get) | **GET** /api/plugins_manager/&lt;id&gt; | Get Plugins Profile
*PluginsManagerApi* | [**put_plugins_profile_api_plugins_manager_id_put**](docs/PluginsManagerApi.md#put_plugins_profile_api_plugins_manager_id_put) | **PUT** /api/plugins_manager/&lt;id&gt; | Put Plugins Profile
*RoomTypesApi* | [**create_room_type_api_room_type_post**](docs/RoomTypesApi.md#create_room_type_api_room_type_post) | **POST** /api/room_type/ | Create Room Type
*RoomTypesApi* | [**delete_room_type_api_room_type_id_delete**](docs/RoomTypesApi.md#delete_room_type_api_room_type_id_delete) | **DELETE** /api/room_type/&lt;id&gt; | Delete Room Type
*RoomTypesApi* | [**get_room_type_api_room_type_id_get**](docs/RoomTypesApi.md#get_room_type_api_room_type_id_get) | **GET** /api/room_type/&lt;id&gt; | Get Room Type
*RoomTypesApi* | [**get_room_types_api_room_type_get**](docs/RoomTypesApi.md#get_room_types_api_room_type_get) | **GET** /api/room_type/ | Get Room Types
*RoomTypesApi* | [**put_room_type_api_room_type_id_put**](docs/RoomTypesApi.md#put_room_type_api_room_type_id_put) | **PUT** /api/room_type/&lt;id&gt; | Put Room Type
*RoomsApi* | [**create_room_api_room_post**](docs/RoomsApi.md#create_room_api_room_post) | **POST** /api/room/ | Create Room
*RoomsApi* | [**delete_room_api_room_id_delete**](docs/RoomsApi.md#delete_room_api_room_id_delete) | **DELETE** /api/room/&lt;id&gt; | Delete Room
*RoomsApi* | [**get_room_api_room_id_get**](docs/RoomsApi.md#get_room_api_room_id_get) | **GET** /api/room/&lt;id&gt; | Get Room
*RoomsApi* | [**get_rooms_api_room_get**](docs/RoomsApi.md#get_rooms_api_room_get) | **GET** /api/room/ | Get Rooms
*RoomsApi* | [**put_room_api_room_id_put**](docs/RoomsApi.md#put_room_api_room_id_put) | **PUT** /api/room/&lt;id&gt; | Put Room
*WebhooksManagerApi* | [**create_webhooks_profile_api_webhooks_manager_post**](docs/WebhooksManagerApi.md#create_webhooks_profile_api_webhooks_manager_post) | **POST** /api/webhooks_manager/ | Create Webhooks Profile
*WebhooksManagerApi* | [**delete_webhooks_profile_api_webhooks_manager_id_delete**](docs/WebhooksManagerApi.md#delete_webhooks_profile_api_webhooks_manager_id_delete) | **DELETE** /api/webhooks_manager/&lt;id&gt; | Delete Webhooks Profile
*WebhooksManagerApi* | [**get_webhooks_profile_api_webhooks_manager_get**](docs/WebhooksManagerApi.md#get_webhooks_profile_api_webhooks_manager_get) | **GET** /api/webhooks_manager/ | Get Webhooks Profile
*WebhooksManagerApi* | [**get_webhooks_profile_api_webhooks_manager_id_get**](docs/WebhooksManagerApi.md#get_webhooks_profile_api_webhooks_manager_id_get) | **GET** /api/webhooks_manager/&lt;id&gt; | Get Webhooks Profile
*WebhooksManagerApi* | [**put_webhooks_profile_api_webhooks_manager_id_put**](docs/WebhooksManagerApi.md#put_webhooks_profile_api_webhooks_manager_id_put) | **PUT** /api/webhooks_manager/&lt;id&gt; | Put Webhooks Profile


## Documentation For Models

 - [ApiBranchModelsKey](docs/ApiBranchModelsKey.md)
 - [ApiBranchModelsKeyInput](docs/ApiBranchModelsKeyInput.md)
 - [ApiBranchViewKeyResponses](docs/ApiBranchViewKeyResponses.md)
 - [ApiKeyManagerModelsKey](docs/ApiKeyManagerModelsKey.md)
 - [ApiKeyManagerModelsKeyInput](docs/ApiKeyManagerModelsKeyInput.md)
 - [ApiKeyManagerViewKeyResponses](docs/ApiKeyManagerViewKeyResponses.md)
 - [Guest](docs/Guest.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [IDDocument](docs/IDDocument.md)
 - [Order](docs/Order.md)
 - [OrderInput](docs/OrderInput.md)
 - [OrderResponses](docs/OrderResponses.md)
 - [Photocopy](docs/Photocopy.md)
 - [PluginsManager](docs/PluginsManager.md)
 - [PluginsManagerInput](docs/PluginsManagerInput.md)
 - [PluginsManagerResponses](docs/PluginsManagerResponses.md)
 - [Price](docs/Price.md)
 - [PriceMax](docs/PriceMax.md)
 - [PriceMin](docs/PriceMin.md)
 - [Room](docs/Room.md)
 - [RoomInput](docs/RoomInput.md)
 - [RoomResponses](docs/RoomResponses.md)
 - [RoomType](docs/RoomType.md)
 - [RoomTypeInput](docs/RoomTypeInput.md)
 - [RoomTypeResponses](docs/RoomTypeResponses.md)
 - [Stayforge](docs/Stayforge.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [WebhooksManager](docs/WebhooksManager.md)
 - [WebhooksManagerInput](docs/WebhooksManagerInput.md)
 - [WebhooksManagerResponses](docs/WebhooksManagerResponses.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

support@stayforge.io


