# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from edu.iot.devicemanage import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.autoform import directives
from plone.supermodel.directives import fieldset
from plone.supermodel.directives import primary
from plone.supermodel import model
from zope.schema.vocabulary import SimpleVocabulary


def _vocab():
    vs_type = ['Milkcocoa', 'Firebase']
    vocab_list = [SimpleVocabulary.createTerm(name, str(id), name) for id, name in enumerate(vs_type)]
    return SimpleVocabulary(vocab_list)


SV_TYPE = _vocab()


class IEduIotDevicemanageLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IDevice(model.Schema):
    """

    """
    device_id = schema.TextLine(title=_(u"Device ID"), required=True)
    sensor_type = schema.TextLine(title=_(u"Sensor Type"), required=True)


class IDeviceManage(model.Schema):
    """

    """

    cloud_type = schema.Choice(
        source=SV_TYPE,
        title=_(u'cloud_type_title', default=u'Cloud type'),
        description=_(u'help_cloud_type', default=u''),
        required=True,)

    fieldset('Firebase',
             label=u'Firebase Settings',
             fields=['fb_apiKey', 'fb_authDomain', 'fb_databaseURL', 'fb_storageBucket', 'fb_messagingSenderId']
             )

    fb_apiKey = schema.TextLine(title=_(u"FB API Key"), required=False)
    fb_authDomain = schema.TextLine(title=_(u"FB Auth Domain"), required=False)
    fb_databaseURL = schema.TextLine(title=_(u"FB Database URL"), required=False)
    fb_projectId = schema.TextLine(title=_(u"FB Project Id"), required=False)
    fb_storageBucket = schema.TextLine(title=_(u"FB Storage Bucket"), required=False)
    fb_messagingSenderId = schema.TextLine(title=_(u"FB Messaging SenderId"), required=False)


    fieldset('Milkcocoa',
             label=u'Milkcocoa Settings',
             fields=['app_id', 'datastore', 'api_key', 'api_secret']
             )

    app_id = schema.TextLine(title=_(u"Application ID"), required=False)
    datastore = schema.TextLine(title=_(u"Datastore"), required=False)
    api_key = schema.TextLine(title=_(u"API Key"), required=False)
    api_secret = schema.TextLine(title=_(u"API Secret"), required=False)

    fieldset('WiFi',
             label=u'WiFi Settings',
             fields=['ssid', 'passphrase']
             )

    ssid = schema.TextLine(title=_(u"SSID"), required=True)
    passphrase = schema.TextLine(title=_(u"Passphrase"), required=True)
