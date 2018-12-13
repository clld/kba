"""
This module will be available in templates as ``u``.

This module is also used to lookup custom template context providers, i.e.
functions following a special naming convention which are called to update
the template context before rendering resource's detail or index views.
"""

from clld.db.meta import DBSession
from clld.db.models import common
from kba import models


def dataset_detail_html(context=None, request=None, **kw):
    stats = {
        'wordlists': DBSession.query(common.Language.pk).count(),
        #'ethnologue_families': DBSession.query(
        #    models.Doculect.ethnologue_family).distinct().count(),
        #'glottolog_families': DBSession.query(
        #    models.Doculect.glottolog_family).distinct().count(),
        'iso_langs': DBSession.query(common.Identifier.name).filter(
            common.Identifier.type ==
            common.IdentifierType.iso.value).distinct().count(),
        'synsets': DBSession.execute(
            'select count(*) from (select distinct valueset_pk from '
            'value) as '
            's').fetchone()[0],
        'words': DBSession.query(common.Value.pk).count(),
        # 'missing_iso': len(missing_iso()),
        }
    return {k: '{0:,}'.format(n) for k, n in stats.items()}
