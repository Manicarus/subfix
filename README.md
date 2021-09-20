# Subfix

A simple subtitle encoding fixer.

Subfix is a utility package which helps to convert subtitle file encodings.

# Features

- Single File Conversion
- Batch Conversion

# Installing

**Install using pip**:

**`pip install subfixio`**

# Developing

1. (Optional) Set up virtual environment using venv

    1. Create virtual environment

    `python -m venv <your venv directory>`

    2. Activate virtual environment

    `source <your venv directory>/activate`

2. Install subfix

    `pip install -e <your subfix directory>`
    
    (Instead) Under virtual environment
    
    `python -m pip install -e <your subfix directory>`

# Uninstalling

`pip uninstall subfixio`

# Example:

*Terminal:*
```
subfix -x smi
```

converts all `.smi` files and puts them into `patched` directory that is created under current working directory

*Single:*
```python
from subfix.converter.manager import converter_manager


converter_manager.convert('/home/user/movies/system-crasher-2019/english_sub.srt')
```
*Batch:*
```python
from subfix.converter.manager import converter_manager


converter_manager.batch_convert('/home/user/movies/system-crasher-2019')
```
*Both methods accept extra optional inputs to customize the conversion.*
<br>
*Read the docstrings for more information on extra options.*