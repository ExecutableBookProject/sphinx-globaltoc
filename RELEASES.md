# Instructions for creating a new release

Sphinx-GlobalTOC is [hosted on the pypi repository](https://pypi.org/project/sphinx-globaltoc/).
To create a new release of sphinx-globaltoc, you need to do these things:

## Before you start

1. Ensure that you have push access to the [sphinx-globaltoc pypi repository](https://pypi.org/project/sphinx-globaltoc/)
2. Install [the twine package](https://twine.readthedocs.io/en/latest/). This is a package that helps you
   bundle and push new Python package distributions to pip.

## To create the release

To create a new release, [open an issue](https://github.com/ExecutableBookProject/sphinx-globaltoc/issues/new) to keep
track of the to-do list for the release. Copy/paste the following markdown into the issue
and check off the boxes as you complete items:


```
- [ ] Ensure that the [sphinx-globaltoc version number](https://github.com/ExecutableBookProject/sphinx-globaltoc/blob/master/jupyter_book/__init__.py)
   is correct, and remove the `dev0` part of the version number.
   Make a PR with the new number and merge into master.
- [ ] Create a new distribution for sphinx-globaltoc by
   [following the twine release instructions](https://twine.readthedocs.io/en/latest/#using-twine)
- [ ] Confirm that the new version of sphinx-globaltoc [is posted to pypi](https://pypi.org/project/sphinx-globaltoc/)
- [ ] Bump the [sphinx-globaltoc version number](https://github.com/ExecutableBookProject/sphinx-globaltoc/blob/master/jupyter_book/__init__.py) to
   the next minor (or major) release and append `dev0` to the end.
- [ ] Celebrate! You've just released a new version of sphinx-globaltoc!
```
