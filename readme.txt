Creating a virtual environment
In the previous step we have downloaded the Python 3.7.2 interpreter, we can now use it to create an isolated virtual environment. This is very useful for software development, keeping each project completely isolated from the others.

To create a new virtual environment:
pyenv virtualenv 3.7.2 MY_VIRTUALENV_NAME

To list all your virtual environments:
pyenv virtualenvs

To activate a virtual environment:
pyenv activate MY_VIRTUALENV_NAME

To deactivate the currently active virtual environment:
pyenv deactivate

To remove an existing virtualenv use any of the following options:
pyenv uninstall MY_VIRTUALENV_NAME
pyenv virtualenv-delete MY_VIRTUALENV_NAME