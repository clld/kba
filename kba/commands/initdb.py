"""

"""
import pathlib
import contextlib

import transaction
from clldutils import db
from clldutils import clilib
from clld.scripts.util import SessionContext, ExistingConfig, get_env_and_settings
from pycldf import Dataset

import kba
from kba.scripts.initializedb import main, prime_cache

PROJECT_DIR = pathlib.Path(kba.__file__).parent.parent


def register(parser):
    parser.add_argument(
        "--config-uri",
        action=ExistingConfig,
        help="ini file providing app config",
        default=str(PROJECT_DIR / 'development.ini'))
    parser.add_argument(
        '--doi',
        default=None,
    )
    parser.add_argument(
        '--prime-cache-only',
        action='store_true',
        default=False,
    )
    parser.add_argument(
        '--repos',
        default=pathlib.Path(PROJECT_DIR.parent / 'kba-data'),
        help='Clone of lexibank/kba',
        type=clilib.PathType,
    )
    parser.add_argument(
        '--glottolog',
        default=pathlib.Path(PROJECT_DIR.parent / '../glottolog/glottolog'),
        help='Clone of lexibank/kba',
        type=clilib.PathType,
    )


def run(args):
    args.env, settings = get_env_and_settings(args.config_uri)

    with contextlib.ExitStack() as stack:
        stack.enter_context(db.FreshDB.from_settings(settings, log=args.log))
        stack.enter_context(SessionContext(settings))
        args.cldf = Dataset.from_metadata(args.repos / 'cldf' / 'cldf-metadata.json')

        if not args.prime_cache_only:
            with transaction.manager:
                main(args)
        with transaction.manager:
            prime_cache(args)
