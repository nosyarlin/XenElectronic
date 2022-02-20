# XenElectronicsWebStore.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCheckout**](DefaultApi.md#getCheckout) | **GET** /checkout/{checkoutId} | Get products and quantities for checkout
[**login**](DefaultApi.md#login) | **POST** /login | Authenticates the user
[**payment**](DefaultApi.md#payment) | **POST** /checkout/{checkoutId} | Informs server that payment has been made
[**saveCart**](DefaultApi.md#saveCart) | **PUT** /checkout | Saves cart items to database and create a checkout
[**search**](DefaultApi.md#search) | **GET** /search | Get products for sale

<a name="getCheckout"></a>
# **getCheckout**
> InlineResponse201 getCheckout(checkoutId)

Get products and quantities for checkout

See what products and how many of each product is in a checkout along with the userId the checkout is associated with

### Example
```javascript
import {XenElectronicsWebStore} from 'xen_electronics_web_store';

let apiInstance = new XenElectronicsWebStore.DefaultApi();
let checkoutId = 56; // Number | The order to read

apiInstance.getCheckout(checkoutId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkoutId** | **Number**| The order to read | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

<a name="login"></a>
# **login**
> InlineResponse2001 login(body)

Authenticates the user

Submit username and password through this endpoint. The server will return a cookie if username and password are correct

### Example
```javascript
import {XenElectronicsWebStore} from 'xen_electronics_web_store';

let apiInstance = new XenElectronicsWebStore.DefaultApi();
let body = new XenElectronicsWebStore.LoginBody(); // LoginBody | 

apiInstance.login(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginBody**](LoginBody.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

<a name="payment"></a>
# **payment**
> payment(body, checkoutId)

Informs server that payment has been made

Checkouts are created before payment is made. Use this endpoint to update the status on the checkout to &#x27;paid&#x27;

### Example
```javascript
import {XenElectronicsWebStore} from 'xen_electronics_web_store';

let apiInstance = new XenElectronicsWebStore.DefaultApi();
let body = "body_example"; // String | new status for checkout
let checkoutId = 56; // Number | The order to pay for

apiInstance.payment(body, checkoutId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**String**](String.md)| new status for checkout | 
 **checkoutId** | **Number**| The order to pay for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="saveCart"></a>
# **saveCart**
> InlineResponse201 saveCart(body)

Saves cart items to database and create a checkout

Saves what items this user is purchasing alongside the quantity of each item

### Example
```javascript
import {XenElectronicsWebStore} from 'xen_electronics_web_store';

let apiInstance = new XenElectronicsWebStore.DefaultApi();
let body = [new XenElectronicsWebStore.CheckoutBody()]; // [CheckoutBody] | The checkout to create

apiInstance.saveCart(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[CheckoutBody]**](CheckoutBody.md)| The checkout to create | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

<a name="search"></a>
# **search**
> [InlineResponse200] search(opts)

Get products for sale

Searches for products matching given filters.

### Example
```javascript
import {XenElectronicsWebStore} from 'xen_electronics_web_store';

let apiInstance = new XenElectronicsWebStore.DefaultApi();
let opts = { 
  'category': "category_example" // String | category of products for filter
};
apiInstance.search(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **String**| category of products for filter | [optional] 

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

