# jsonformat
Python program to ingest json and whitespace format it.

<sup>It also alphabetizes keys within each level!</sup>

_Be careful._ The formatted json will be written back to the file specified.

Usage: `python jsonformat.py filename`

Takes a file that looks like this:
```json
{ "id":5,"name":"something","price":12.50,"tags":["example","json"]}
```
and turns it into this:
```json
{
    "id": 5,
    "name": "something",
    "price": 12.5,
    "tags": [
        "example",
        "json"
    ]
}
```
