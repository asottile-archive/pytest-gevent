[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/asottile.pytest-gevent?branchName=master)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=54&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/54/master.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=54&branchName=master)

pytest-gevent
=============

Ensure that gevent is properly patched when invoking pytest

## installation

`pip install pytest-gevent`

## usage

wherever you'd use `pytest`, use `pytest-gevent` instead.

### disabling specific patches

you can disable specific [gevent patches] through environment variables.  for
example, if you wanted to disable the `ssl` patch you would invoke:

```bash
PYTEST_GEVENT_PATCH_ALL_NO_SSL=1 pytest-gevent
```

[gevent patches]: http://www.gevent.org/api/gevent.monkey.html#gevent.monkey.patch_all

## how this works

this calls `gevent.monkey.patch_all(...)` and then `pytest.main()`

## alternatives

`gevent.monkey` provides a cli directly, though it's quite clunky to use

```bash
python -m gevent.monkey $(which pytest) ...
```
