from clld.web.assets import environment
from clldutils.path import Path

import kba


environment.append_path(
    Path(kba.__file__).parent.joinpath('static').as_posix(),
    url='/kba:static/')
environment.load_path = list(reversed(environment.load_path))
