from clld import interfaces
from clld.db.meta import CustomModelMixin
from clld.db.models.common import Language, Value, ValueSet
from sqlalchemy import (Column, Unicode, Integer, ForeignKey, )
from zope.interface import implementer


@implementer(interfaces.ILanguage)
class KbaLanguage(CustomModelMixin, Language):
    pk = Column(Integer, ForeignKey('language.pk'), primary_key=True)


@implementer(interfaces.IValue)
class Word(CustomModelMixin, Value):
    pk = Column(Integer, ForeignKey('value.pk'), primary_key=True)
    comment = Column(Unicode)
    originaltranslation = Column(Unicode)

