import os
import subprocess
import sys

import pytest

import pytest_gevent


def test_patch_all_kwargs_noop():
    assert pytest_gevent._patch_all_kwargs({}) == {}


def test_patch_all_kwargs_empty_ignored():
    m = {'GEVENT_PYTEST_PATCH_ALL_NO_SSL': ''}
    assert pytest_gevent._patch_all_kwargs(m) == {}


def test_patch_all_kwargs():
    m = {
        'GEVENT_PYTEST_PATCH_ALL_NO_SSL': '1',
        'GEVENT_PYTEST_PATCH_ALL_NO_TIME': '1',
    }
    assert pytest_gevent._patch_all_kwargs(m) == {'ssl': False, 'time': False}


@pytest.fixture
def run_test(tmp_path):
    def _run_test(s, env=None):
        t = tmp_path.joinpath('t.py')
        t.write_text(s)
        env = env or {}
        cmd = (
            sys.executable, '-mcoverage', 'run', '--concurrency=gevent',
            '-m', 'pytest_gevent', t,
        )
        subprocess.check_call(cmd, env={**os.environ, **env})
    return _run_test


def test_gevent_patched(run_test):
    run_test(
        'import ssl\n'
        'def test():\n'
        '    assert ssl.SSLContext.__module__.startswith("gevent.")\n',
    )


def test_gevent_patch_disabled(run_test):
    run_test(
        'import ssl\n'
        'def test():\n'
        '    assert not ssl.SSLContext.__module__.startswith("gevent.")\n',
        env={'GEVENT_PYTEST_PATCH_ALL_NO_SSL': '1'},
    )
