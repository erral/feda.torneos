from feda.torneos.torneo import ITorneo
from zope.component import adapts
from zope.interface import implements
from collective.contentrules.mailadapter.interfaces import IRecipientsResolver
from Acquisition import aq_inner
from plone import api


class EnviarAFFAA(object):
    implements(IRecipientsResolver)
    adapts(ITorneo)

    def __init__(self, context):
        self.context = context

    def recipients(self):
        context = aq_inner(self.context)

        state = api.content.get_state(obj=context)
        current_user = api.user.get_current()
        emails = [current_user.getProperty('email')]

        if state == 'registro-autona3mico':
            emails.append('larreategi+euskadi@gmail.com')

        return emails
