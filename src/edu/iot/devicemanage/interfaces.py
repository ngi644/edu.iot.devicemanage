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

    fieldset('Milkcocoa',
             label=u'Milkcocoa Settings',
             fields=['app_id', 'datastore', 'api_key', 'api_secret']
             )

    app_id = schema.TextLine(title=_(u"Application ID"), required=True)
    datastore = schema.TextLine(title=_(u"Datastore"), required=True)
    api_key = schema.TextLine(title=_(u"API Key"), required=True)
    api_secret = schema.TextLine(title=_(u"API Secret"), required=True)

    fieldset('WiFi',
             label=u'WiFi Settings',
             fields=['ssid', 'passphrase']
             )

    ssid = schema.TextLine(title=_(u"SSID"), required=True)
    passphrase = schema.TextLine(title=_(u"Passphrase"), required=True)
