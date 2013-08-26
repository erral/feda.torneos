from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from feda.torneos import MessageFactory as _


tournament_systems = SimpleVocabulary(
    [SimpleTerm(value=u'IS', title=_(u'Individual Swiss')),
     SimpleTerm(value=u'IRR', title=_(u'Individual Round Robin')),
     SimpleTerm(value=u'IDRR', title=_(u'Individual Double Round Robin')),
     SimpleTerm(value=u'TS', title=_(u'Team Swiss')),
     SimpleTerm(value=u'TRR', title=_(u'Team Round Robin')),
     SimpleTerm(value=u'O', title=_(u'Other (explain in comments)'))


     ]
    )

rating_types = SimpleVocabulary(
    [SimpleTerm(value=u'standard', title=_(u'Standard chess')),
     SimpleTerm(value=u'rapid', title=_(u'Rapid chess')),
     SimpleTerm(value=u'blitz', title=_(u'Blitz chess')),


     ]
    )

# Interface class; used to define content-type schema.
class ITorneo(form.Schema):
    """
    Description of the Example Type
    """
    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/torneo.xml to define the content type
    # and add directives here as necessary.

    city = schema.TextLine(
        title=_(u'City'),
        required=True,
        )

    number_of_players = schema.Int(
        title=_(u'Number of expected players'),
        required=True,
        )

    system = schema.Choice(
        title=_(u'System of play'),
        vocabulary=tournament_systems,
        required=True,
        )

    start_date = schema.Date(
        title=_(u'Start date'),
        required=True,
        )

    end_date = schema.Date(
        title=_(u'End date'),
        required=True,
        )

    chief_arbiter = schema.Int(
        title=_(u'Chief arbiter'),
        description=_("Enter arbiter's FIDE ID"),
        required=True,
        )

    deputy_arbiters = schema.List(
        title=_(u'Deputy arbiters'),
        value_type=schema.Int(title=_(u'Deputy arbiter')),
        required=False,
        )

    organizer_id = schema.Int(
        title=_(u"Organizer's FIDE ID"),
        description=_("Enter only if the organizer has a FIDE ID"),
        required=False,
        )

    organizer_name = schema.TextLine(
        title=_(u"Organizer's Name"),
        description=_("Enter only if the organizer does not have a FIDE ID"),
        required=False,
        )

    rating_type = schema.Choice(
        title=_(u'Rating type'),
        vocabulary=rating_types,
        required=True,
        )

    invoice_name = schema.TextLine(
        title=_(u'Name for the invoice'),
        required=True
        )

    invoice_nif_cif = schema.TextLine(
        title=_(u'NIF/CIF'),
        required=True
        )

    invoice_address = schema.TextLine(
        title=_(u'Address for the invoice'),
        required=True
        )

    invoice_city = schema.TextLine(
        title=_(u'City'),
        required=True
        )

    invoice_postal_code = schema.TextLine(
        title=_(u'Postal code'),
        required=True
        )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.
class Torneo(dexterity.Container):
    grok.implements(ITorneo)
    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# templates called torneoview.pt .
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@view" appended unless specified otherwise
# using grok.name below.
# This will make this view the default view for your content-type

grok.templatedir('templates')


class TorneoView(grok.View):
    grok.context(ITorneo)
    grok.require('zope2.View')
    grok.name('view')
