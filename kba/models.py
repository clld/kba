from clld import interfaces
from clld.db.meta import CustomModelMixin
from clld.db.models.common import Language, Value
from sqlalchemy import (Column, Unicode, Integer, ForeignKey, )
from zope.interface import implementer


@implementer(interfaces.ILanguage)
class KbaLanguage(CustomModelMixin, Language):
    pk = Column(Integer, ForeignKey('language.pk'), primary_key=True)


@implementer(interfaces.IValue)
class Word(CustomModelMixin, Value):
    pk = Column(Integer, ForeignKey('value.pk'), primary_key=True)
    # ipa = Column(Unicode)
    # reference = Column(Unicode)
    # alternative = Column(Unicode)
    comment = Column(Unicode)
    # sound = Column(Unicode)
    # original = Column(Unicode)
