# README #

PyPI link: https://pypi.python.org/pypi/aemessenger/

### Project description ###

A simple Python messenger for learning sockets, threads, PyQT5, SQLAlchemy, etc...

### Install ###

```pip install aemessenger```

or

```pip3 install aemessenger```

### Usage ###

Server: ```python3 -m aemessenger.server``` or just ```server```


Qt Client: ```python3 -m aemessenger.gui_client``` or just ```client```

#### Sample logins ####
```Now any login will work actually```

### Note to self ###
Build: ```python3 setup.py bdist_wheel```

Install local: ```pip3 install ./dist/aemessenger-0.1-py3-none-any.whl```

Upload: ```twine upload dist/*```

Uninstall: ```pip3 uninstall aemessenger```
