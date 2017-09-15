# encoding: utf-8

__author__ = 'nagai'

from plone.dexterity.content import Container


class DeviceManage(Container):
    """A device manage class"""

    def get_params(self, cloud_type='milkcocoa'):
        """
        Connection Param
        """
        if cloud_type == 'milkcocoa':
            return dict(app_id=self.app_id,
                               datastore=self.datastore,
                               api_key=self.api_key,
                               api_secret=self.api_secret)
        return dict()
