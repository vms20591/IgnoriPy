```
#    _  _____                  _ _____       
#   (_)/ ____|                (_)  __ \      
#    _| |  __ _ __   ___  _ __ _| |__) |   _ 
#   | | | |_ | '_ \ / _ \| '__| |  ___/ | | |
#   | | |__| | | | | (_) | |  | | |   | |_| |
#   |_|\_____|_| |_|\___/|_|  |_|_|    \__, |
#                                       __/ |
#                                      |___/ 
```   

IgnoriPy is a script to quicky generate a `.gitignore` when starting new projects. This makes use of [gitignore](https://gitignore.io) under the hood to make it happen. 

**Note:** Be sure to check the generated `.gitignore` and modify them as needed.

### Installation

From source,

`python setup.py install` or,

`pip install .`

**Note:** Its better to keep every dependency in a virtual environment, like [virtualenv](https://virtualenv.pypa.io/en/stable/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

### Unit Tests

From source directory,

`python -m unittest discover`

### Usage

`ignoripy language`

### Examples

* Generate *gitignore* for *single* language,
  * *python* - `ignoripy python`
  * *java* - `ignoripy java`
* Generate *gitignore* for *multiple* languages,
  * *python* and *nodejs* - `ignoripy python,node`

### Available API's @ [gitignore](https://gitignore.io)

* https://gitignore.io/api/list - Lists all available language and ide's that has a *gitignore*
* https://gitignore.io/api/get/(language) - Returns *gitignore* for the passed in `language`, like
  * https://gitignore.io/api/python
  * https://gitignore.io/api/python,java

-------

### LICENSE

GNU GPL V3. Refer to the LICENSE file for details.
