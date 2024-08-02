Certainly! Let's enhance the README file by adding details about request and response methods and attributes for
the `requests` module.

---

# HTTP Requests in Python: `requests` and `urllib`

## Introduction

The `requests` and `urllib` modules in Python facilitate making HTTP requests to web servers. Each module offers unique
features and levels of abstraction to suit different needs.

### Table of Contents

1. [Requests Module](#requests-module)
   - [Common Arguments and Keyword Arguments](#common-arguments-requests)
   - [Example Usage](#example-usage-requests)
   - [Error Handling](#error-handling-requests)
   - [Sessions and More Features](#sessions-requests)
   - [Request and Response Methods and Attributes](#request-response-methods-requests)
2. [Urllib Module](#urllib-module)
   - [Common Classes and Functions](#common-classes-urllib)
   - [Example Usage](#example-usage-urllib)
   - [Error Handling](#error-handling-urllib)
   - [Sessions and More Features](#sessions-urllib)
3. [Conclusion](#conclusion)

---

## Requests Module <a name="requests-module"></a>

The `requests` module in Python allows sending HTTP requests with ease.

### Common Arguments and Keyword Arguments <a name="common-arguments-requests"></a>

#### URL (Positional Argument)

- **url**: The URL for the request.

#### Keyword Arguments

- **params**: (optional) Dictionary, list of tuples, or bytes to send in the query string.
- **data**: (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body.
- **json**: (optional) JSON serializable Python object to send in the body.
- **headers**: (optional) Dictionary of HTTP headers.
- **cookies**: (optional) Dictionary or CookieJar object.
- **files**: (optional) Dictionary of 'filename': file-like-objects for multipart encoding upload.
- **auth**: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
- **timeout**: (optional) Timeout in seconds for the server to send data before giving up.
- **allow_redirects**: (optional) Boolean to follow redirects.
- **proxies**: (optional) Dictionary mapping protocol to the URL of the proxy.
- **verify**: (optional) Boolean or string. Control SSL certificate verification.
- **stream**: (optional) If False, response content will be immediately downloaded.
- **cert**: (optional) String or tuple specifying SSL certificate file or ('cert', 'key') tuple.

### Example Usage <a name="example-usage-requests"></a>

#### GET Request with Parameters

```python
import requests

response = requests.get(
   'https://api.example.com/data',
   params={'key1': 'value1', 'key2': 'value2'},
   headers={'Authorization': 'Bearer YOUR_TOKEN'}
)
print(response.json())
```

#### POST Request with JSON Data

```python
import requests

response = requests.post(
   'https://api.example.com/data',
   json={'key1': 'value1', 'key2': 'value2'}
)
print(response.status_code)
print(response.json())
```

#### Error Handling <a name="error-handling-requests"></a>

Handle exceptions like connection errors and HTTP errors:

```python
import requests

try:
   response = requests.get('https://api.example.com/data')
   response.raise_for_status()  # Raise HTTPError for bad responses
except requests.exceptions.HTTPError as http_err:
   print(f'HTTP error occurred: {http_err}')
except requests.exceptions.ConnectionError as conn_err:
   print(f'Connection error occurred: {conn_err}')
except requests.exceptions.RequestException as req_err:
   print(f'Request error occurred: {req_err}')
```

### Sessions and More Features <a name="sessions-requests"></a>

#### Session Management

Use a session for persistent settings like cookies and headers:

```python
import requests

session = requests.Session()
session.headers.update({'User-Agent': 'my-app/0.0.1'})

response = session.get('https://httpbin.org/get')
print(response.text)

session.close()  # Close session
```

#### Custom Headers and Parameters

Set custom headers and parameters in requests:

```python
import requests

headers = {'User-Agent': 'my-app/0.0.1'}
params = {'key': 'value'}

response = requests.get('https://httpbin.org/get', headers=headers, params=params)
print(response.text)
```

#### Detailed Examples for Each Keyword Argument

##### Example with `params`

```python
import requests

response = requests.get('https://httpbin.org/get', params={'key': 'value'})
print(response.json())
```

##### Example with `data` (for `POST` requests)

```python
import requests

response = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(response.json())
```

##### Example with `json`

```python
import requests

response = requests.post('https://httpbin.org/post', json={'key': 'value'})
print(response.json())
```

##### Example with `headers`

```python
import requests

headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get('https://httpbin.org/get', headers=headers)
print(response.text)
```

##### Example with `cookies`

```python
import requests

cookies = {'session_id': '12345'}
response = requests.get('https://httpbin.org/get', cookies=cookies)
print(response.text)
```

##### Example with `files`

```python
import requests

files = {'file': open('file.txt', 'rb')}
response = requests.post('https://httpbin.org/post', files=files)
print(response.text)
```

##### Example with `auth`

```python
import requests
from requests.auth import HTTPBasicAuth

response = requests.get('https://api.example.com/data', auth=HTTPBasicAuth('username', 'password'))
print(response.json())
```

##### Example with `timeout`

```python
import requests

try:
   response = requests.get('https://api.example.com/data', timeout=5)
   print(response.json())
except requests.exceptions.Timeout:
   print('Request timed out')
```

##### Example with `allow_redirects`

```python
import requests

response = requests.get('https://api.example.com/data', allow_redirects=False)
print(response.status_code)
```

##### Example with `proxies`

```python
import requests

proxies = {
   'http': 'http://10.10.1.10:3128',
   'https': 'http://10.10.1.10:1080'
}
response = requests.get('https://api.example.com/data', proxies=proxies)
print(response.json())
```

##### Example with `verify`

```python
import requests

response = requests.get('https://api.example.com/data', verify='/path/to/certfile.pem')
print(response.json())
```

##### Example with `stream`

```python
import requests

response = requests.get('https://api.example.com/data', stream=True)
print(response.raw.read(10))  # Read first 10 bytes of the response content
```

##### Example with `cert`

```python
import requests

response = requests.get('https://api.example.com/data', cert=('/path/client.cert', '/path/client.key'))
print(response.json())
```

### Request and Response Methods and Attributes <a name="request-response-methods-requests"></a>

#### Request Methods

- **requests.get(url, **kwargs)**: Sends a GET request.
- **requests.post(url, **kwargs)**: Sends a POST request.
- **requests.put(url, **kwargs)**: Sends a PUT request.
- **requests.delete(url, **kwargs)**: Sends a DELETE request.
- **requests.head(url, **kwargs)**: Sends a HEAD request.
- **requests.options(url, **kwargs)**: Sends an OPTIONS request.
- **requests.patch(url, **kwargs)**: Sends a PATCH request.

Example:

```python
import requests

response = requests.put('https://httpbin.org/put', data={'key': 'value'})
print(response.status_code)
print(response.json())
```

#### Response Attributes

- **response.status_code**: The HTTP status code.
- **response.headers**: Dictionary of response headers.
- **response.text**: The content of the response, in unicode.
- **response.content**: The content of the response, in bytes.
- **response.json()**: A method to parse the JSON content.
- **response.url**: The final URL location of the response.
- **response.history**: A list of response objects from redirects.
- **response.elapsed**: The time elapsed between sending the request and the arrival of the response.

Example:

```python
import requests

response = requests.get('https://api.example.com/data')
print(f'Status Code: {response.status_code}')
print(f'Headers: {response.headers}')
print(f'Content: {response.text}')
print(f'JSON: {response.json()}')
print(f'URL: {response.url}')
print(f'History: {response.history}')
print(f'Elapsed Time: {response.elapsed}')
```

---

## Urllib Module <a name="urllib-module"></a>

The `urllib` module provides a lower-level interface for making HTTP requests.

### Common Classes and Functions <a name="common-classes-urllib"></a>

#### `urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)`

- **url**: The URL to be opened.
- **data**: (optional

) Data to be sent as a POST request.

- **timeout**: (optional) Timeout in seconds for blocking operations.
- **cafile**: (optional) Path to a file of concatenated CA certificates.
- **capath**: (optional) Path to a directory containing CA certificates.
- **cadefault**: Deprecated and ignored.
- **context**: (optional) An `ssl.SSLContext` object for TLS/SSL settings.

### Example Usage <a name="example-usage-urllib"></a>

#### GET Request

```python
import urllib.request

response = urllib.request.urlopen('https://api.example.com/data')
print(response.read().decode('utf-8'))
```

#### POST Request with Data

```python
import urllib.request
import urllib.parse

data = urllib.parse.urlencode({'key1': 'value1', 'key2': 'value2'}).encode('utf-8')
response = urllib.request.urlopen('https://api.example.com/data', data=data)
print(response.read().decode('utf-8'))
```

#### Error Handling <a name="error-handling-urllib"></a>

Handle exceptions like HTTP errors and URL errors:

```python
import urllib.request
import urllib.error

try:
   response = urllib.request.urlopen('https://api.example.com/data')
   print(response.read().decode('utf-8'))
except urllib.error.HTTPError as http_err:
   print(f'HTTP error occurred: {http_err.code}')
except urllib.error.URLError as url_err:
   print(f'URL error occurred: {url_err.reason}')
except Exception as e:
   print(f'Other error occurred: {str(e)}')
```

### Sessions and More Features <a name="sessions-urllib"></a>

#### Cookie Handling

Manage cookies with `http.cookiejar` and `urllib.request`:

```python
import urllib.request
import http.cookiejar

cookie_jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

response = opener.open('https://httpbin.org/cookies/set?name=value')
for cookie in cookie_jar:
   print(f'Cookie: {cookie.name}={cookie.value}')
```

#### Custom Headers and Parameters

Set headers and parameters manually in `urllib` requests:

```python
import urllib.request

headers = {'User-Agent': 'my-app/0.0.1'}
params = urllib.parse.urlencode({'key': 'value'}).encode('utf-8')

request = urllib.request.Request('https://httpbin.org/get', headers=headers, data=params)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
```

#### Detailed Examples for Each Keyword Argument

##### Example with `data`

```python
import urllib.request
import urllib.parse

data = urllib.parse.urlencode({'key': 'value'}).encode('utf-8')
response = urllib.request.urlopen('https://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))
```

##### Example with `timeout`

```python
import urllib.request

try:
   response = urllib.request.urlopen('https://api.example.com/data', timeout=5)
   print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
   print(f'URLError occurred: {e.reason}')
```

##### Example with `cafile` and `capath`

```python
import urllib.request

response = urllib.request.urlopen('https://api.example.com/data', cafile='/path/to/cafile.pem',
                                  capath='/path/to/capath')
print(response.read().decode('utf-8'))
```

##### Example with `context`

```python
import urllib.request
import ssl

context = ssl.create_default_context()
response = urllib.request.urlopen('https://api.example.com/data', context=context)
print(response.read().decode('utf-8'))
```

---

## Conclusion <a name="conclusion"></a>

Both `requests` and `urllib` modules provide capabilities for making HTTP requests in Python. Choose `requests` for a
higher-level interface with convenient methods for session management and JSON handling. Use `urllib` for more control
over low-level HTTP operations.

---

This README provides a comprehensive guide to using `requests` and `urllib` in Python for HTTP requests, including
sessions handling, error handling, and example code snippets. Adjust examples and sections as needed for your specific
project requirements.
