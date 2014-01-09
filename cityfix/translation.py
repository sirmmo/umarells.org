from modeltranslation.translator import translator, TranslationOptions
from .models import *

class NamedItemTranslation(TranslationOptions):
    fields = ('name',)

translator.register(FixType, NamedItemTranslation)
translator.register(Operator, NamedItemTranslation)
translator.register(Infrastructure, NamedItemTranslation)
translator.register(SiteType, NamedItemTranslation)