
## Installation

```bash
pip install git+http://east-control.com:9000/pockestra/python-mpath.git
```

```bash
pip uninstall mpath
```

## Example

```python
from mpath import mpath
```

```python
path = mpath('/var/www/some.txt')
path.get_path()
>>> /var/www/some.txt
path.get_dirname()
>>> /var/www
path.get_filename()
>>> some.txt
path.get_basename()
>>> some
path.get_extension()
>>> .txt
path.get_split()
>>> ['/var/www', 'test', '.txt']
path.get_split(depth=2)
>>> ['/', 'var', 'www', 'test', '.txt']
```

```python
path = mpath('/var/www/some.txt')
path.set_extension('doc')
path.get_path()
>>> /var/www/some.doc
path.set_dirname('dir')
path.get_path()
>>> /var/dir/some.doc
path.set_basename('base')
path.get_path()
>>> /var/dir/base.doc
path.set_filename('file.ext')
path.get_path()
>>> /var/dir/file.ext
path.revert()
path.get_path()
>>> /var/www/some.doc
```

```python
mpath('path').get_md5()
>>> cdd9a7db9a674169497378bda160772a
```

```python
mpath('path').search_subpath('*', file=False, directory=True)
```

```python
mpath('path').remove(message=True)
>>> removing path
```

```python
mpath('path').remove_empty(parent=0)
```

```python
mpath('path').initialize(own='www-data:www-data', mod='744', forced=True, message=True)
>>> removing path
>>> creating path
```

```python
mpath('path').change_ownmod(own='www-data:www-data', mod='744', recursive=False)
```

## Repository

```bash
git clone http://east-control.com:9000/pockestra/python-mpath.git
```
