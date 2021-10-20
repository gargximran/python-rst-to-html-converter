## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Run Flask
### Run flask for develop
```
$ python app.py
```
In flask, Default port is `5000`

Endpoint:  `http://127.0.0.1:5000/rsttohtml`


example curl
```
curl --location --request POST 'http://127.0.0.1:5000/rsttohtml' \
--header 'Content-Type: application/json' \
--data-raw '{"data":"*This is paragraph*"}'
```