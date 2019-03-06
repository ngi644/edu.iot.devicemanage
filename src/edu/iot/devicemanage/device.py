# encoding: utf-8

__author__ = 'nagai'

from plone.dexterity.content import Item


class Device(Item):
    """A device class"""

    def get_params(self):
        """
        """
        parent = self.__parent__
        params = parent.get_params()
        params['device_id'] = self.device_id
        params['device_name'] = self.title
        return params
