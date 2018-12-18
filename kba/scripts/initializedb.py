from __future__ import unicode_literals

import sys

from clld.db.meta import DBSession
from clld.db.models import common
from clld.scripts.util import initializedb, Data, add_language_codes
from clld_glottologfamily_plugin.util import load_families
from pathlib import Path
from pycldf.dataset import Wordlist

import kba
from kba import models

GLOTTOLOG_REPOS = Path(kba.__file__).parent.parent.joinpath('data', 'glottolog')


def main(args):
    _ = args
    data = Data()
    cldf_data = Wordlist.from_metadata('data/cldf/cldf-metadata.json')

    # TODO: Editors/Contributors
    dataset = common.Dataset(id=kba.__name__, name="KBA",
                             publisher_name="Max Planck Institute for the "
                                            "Science of Human History",
                             publisher_place="Jena",
                             publisher_url="http://www.shh.mpg.de",
                             license="http://creativecommons.org/licenses/by"
                                     "/4.0/", domain='kba.clld.org',
                             jsondata={'license_icon': 'cc-by.png',
                                       'license_name': 'Creative Commons '
                                                       'Attribution 4.0 '
                                                       'International '
                                                       'License'})

    DBSession.add(dataset)

    for language in cldf_data['LanguageTable']:
        lang = data.add(models.KbaLanguage, language['ID'], id=language['ID'],
                        name=language['Name'])
        add_language_codes(data, lang, None, glottocode=language['Glottocode'])

    # TODO: Concepticon
    for parameter in cldf_data['ParameterTable']:
        data.add(common.Parameter, parameter['ID'], id=parameter['ID'],
                 name='{0} ({1})'.format(parameter['Name'], parameter['ID']))

    for form in cldf_data['FormTable']:
        valueset_id = '{0}-{1}'.format(form['Parameter_ID'],
                                       form['Language_ID'])
        valueset = data['ValueSet'].get(valueset_id)

        # Unless we already have something in the VS:
        if not valueset:
            vs = data.add(common.ValueSet, valueset_id, id=valueset_id,
                          language=data['KbaLanguage'][form['Language_ID']],
                          parameter=data['Parameter'][form['Parameter_ID']])

        DBSession.add(models.Word(id=form['ID'], name=form['Form'],
                                  comment=form.get('Comment'),
                                  valueset=vs))

    load_families(data,
                  [(l.glottocode, l) for l in data['KbaLanguage'].values()],
                  glottolog_repos=GLOTTOLOG_REPOS,
                  isolates_icon='tcccccc')


def prime_cache(args):
    """If data needs to be denormalized for lookup, do that here.
    This procedure should be separate from the db initialization, because
    it will have to be run periodically whenever data has been updated.
    """
    print(args)


if __name__ == '__main__':  # pragma: no cover
    initializedb(create=main, prime_cache=prime_cache)
    sys.exit(0)
