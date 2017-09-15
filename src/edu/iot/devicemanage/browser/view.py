# encoding: utf-8

__author__ = 'nagai'


from Products.Five.browser import BrowserView
from edu.iot.devicemanage.interfaces import IDevice
from zope.interface import implementer
from zope.interface import implements


@implementer(IDevice)
class DeviceView(BrowserView):
    """

    """

    def __init__(self, context, request):
        super(DeviceView, self).__init__(context, request)

    def get_param(self):
        context = self.context
        params = context.get_params()
        sc = '''
        <script type="text/javascript">
        let app_id = '{}.mlkcca.com';
        let app_ds = '{}';
        let app_key = '{}';
        let app_pass = '{}';
        let device_id = '{}';
        </script>
        '''.format(params['app_id'], params['datastore'],
                   params['api_key'], params['api_secret'],
                   params['device_id'])
        return sc
