from clld.db.models.common import (Value, ValueSet, Parameter, DomainElement,
                                   Language, Contribution, ValueSetReference, )
from clld.web.datatables.base import (DataTable, LinkCol, DetailsRowLinkCol,
                                      LinkToMapCol, Col)
from clld.web.datatables.value import RefsCol, ValueNameCol, ValueSetCol
from sqlalchemy.orm import joinedload

from kba.models import Word


# noinspection PyTypeChecker
class KbaValues(DataTable):
    __constraints__ = [Parameter, Contribution, Language]

    def base_query(self, query):
        query = query.join(ValueSet).options(
            joinedload(Value.valueset).joinedload(ValueSet.references).joinedload(ValueSetReference.source)
        )

        if self.language:
            query = query.join(ValueSet.parameter)
            return query.filter(ValueSet.language_pk == self.language.pk)

        if self.parameter:
            query = query.join(ValueSet.language)
            query = query.outerjoin(DomainElement).options(
                joinedload(Value.domainelement))
            return query.filter(ValueSet.parameter_pk == self.parameter.pk)

        if self.contribution:
            query = query.join(ValueSet.parameter)
            return query.filter(ValueSet.contribution_pk == self.contribution.pk)

        return query

    def col_defs(self):
        name_col = ValueNameCol(self, 'value')
        if self.parameter and self.parameter.domain:
            name_col.choices = [de.name for de in self.parameter.domain]

        res = [DetailsRowLinkCol(self, 'd')]

        if self.parameter:
            return res + [
                LinkCol(self,
                        'language',
                        model_col=Language.name,
                        get_object=lambda i: i.valueset.language),
                name_col,
                RefsCol(self, 'source'),
                LinkToMapCol(self, 'm', get_object=lambda i: i.valueset.language),
            ]

        if self.language:
            return res + [
                name_col,
                LinkCol(self,
                        'parameter',
                        sTitle=self.req.translate('Parameter'),
                        model_col=Parameter.name,
                        get_object=lambda i: i.valueset.parameter),
                # RefsCol(self, 'source'),
                Col(self, 'source orthography', model_col=Word.sourceorthography),
                Col(self, 'KBA orthography', model_col=Word.kbaorthography),
                Col(self, 'Word class', model_col=Word.wordclass),
                Col(self, 'Grammatical notes', model_col=Word.grammaticalnotes),
                Col(self, 'Idiolectal variant', model_col=Word.idiolectalvariant),
                Col(self, 'comment', model_col=Word.comment),
                # Col(self, 'original translation', model_col=Word.originaltranslation)
            ]

        return res + [
            name_col,
            ValueSetCol(self, 'valueset', bSearchable=False, bSortable=False),
        ]


def includeme(config):
    # config.register_datatable('languages', KbaLanguages)
    # config.register_datatable('units', KbaUnits)
    config.register_datatable('values', KbaValues)
