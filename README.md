# sanitize_filepaths

A Pythonic generating safe and clean file paths for various sysadmin tasks

## Quick start

```bash
$ git clone https://github.com/verbalhanglider/sanitize_filepaths
$ cd sanitize_filepaths
$ python -m venv venv
$ source venv/bin/activate
$ python setup.py install
```

## Examples

```python
>>> from tdfilepathsanization.makers import PathMaker
>>> new_path = PathMaker("/home/verbalhanglider/bob")
>>> new_path.create()
'/home/verbalhanglider/bob'
```