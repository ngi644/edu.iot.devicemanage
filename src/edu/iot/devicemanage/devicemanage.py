# encoding: utf-8

__author__ = 'nagai'

from plone.dexterity.content import Container


class DeviceManage(Container):
    """A device manage class"""

    def get_params(self):
        """
        Connection Param
        """
        if self.cloud_type == 'Milkcocoa':
            return dict(cloud_type=self.cloud_type,
                        app_id=self.app_id,
                        datastore=self.datastore,
                        api_key=self.api_key,
                        api_secret=self.api_secret)
        if self.cloud_type == 'Firebase':
            return dict(cloud_type=self.cloud_type,
                        fb_apiKey=self.fb_apiKey,
                        fb_authDomain=self.fb_authDomain,
                        fb_databaseURL=self.fb_databaseURL,
                        fb_projectId=self.fb_projectId,
                        fb_storageBucket=self.fb_storageBucket,
                        fb_messagingSenderId=self.fb_messagingSenderId,
                        )
        return dict()
