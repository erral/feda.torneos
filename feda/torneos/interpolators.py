from zope.component import adapts
from zope.interface import implements
from plone.stringinterp.adapters import BaseSubstitution as Base
from plone.stringinterp.interfaces import IStringInterpolator
from plone.stringinterp.adapters import DateSubstitution

from feda.torneos.torneo import ITorneo
from feda.torneos import MessageFactory as _

class BaseSubstitution(Base):
    implements(IStringInterpolator)


class DateStartSubstitution(DateSubstitution):
    adapts(ITorneo)

    category = _(u'Torneo')
    description = _(u'Start date of the tournament')

    def safe_call(self):
        return self.formatDate(self.context.start_date)

class DateEndSubstitution(DateSubstitution):
    adapts(ITorneo)

    category = _(u'Torneo')
    description = _(u'End date of the tournament')

    def safe_call(self):
        return self.formatDate(self.context.end_date)

class SystemSubstitution(Base):
    adapts(ITorneo)

    category = _(u'Torneo')
    description = _(u'System of play')

    def safe_call(self):
        return self.context.system

class CitySubstitution(Base):
    adapts(ITorneo)

    category = _(u'Torneo')
    description = _(u'City')

    def safe_call(self):
        return self.context.city


class CASubstitution(Base):
    adapts(ITorneo)

    category = _(u'Torneo')
    description = _(u'Chief arbiter')

    def safe_call(self):
        return self.context.chief_arbiter

class RatingTypeSubstitution(Base):
    adapts(ITorneo)

    category = _(u'Torneo')
    description = _(u'Rating type')

    def safe_call(self):
        return self.context.rating_type
