import os
from typing import Mapping

K = 'GEVENT_PYTEST_PATCH_ALL_NO_'


def _patch_all_kwargs(environ: Mapping[str, str]) -> Mapping[str, bool]:
    return {
        k[len(K):].lower(): False
        for k, v in environ.items()
        if k.startswith(K) and v
    }


def main() -> int:
    import gevent.monkey
    gevent.monkey.patch_all(**_patch_all_kwargs(os.environ))

    import pytest
    return pytest.main()


if __name__ == '__main__':
    exit(main())
