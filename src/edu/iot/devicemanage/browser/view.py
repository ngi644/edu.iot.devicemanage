# encoding: utf-8

__author__ = 'nagai'


from Products.Five.browser import BrowserView
from edu.iot.devicemanage.interfaces import IDevice
from zope.interface import implementer
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


@implementer(IDevice)
class DeviceView(BrowserView):
    """

    """
    template_mlkcca = ViewPageTemplateFile('templates/device_view.pt')
    template_fb = ViewPageTemplateFile('templates/device_fb_view.pt')

    def __init__(self, context, request):
        super(DeviceView, self).__init__(context, request)

    def __call__(self):
        super(DeviceView, self).__call__()

        cloud_type = self.context.get_params().get('cloud_type', 'Milkcocoa')

        if cloud_type == 'Firebase':
            return self.template_fb()
        else:
            return self.template_mlkcca()

    def get_param(self):
        context = self.context
        params = context.get_params()
        if params['cloud_type'] == 'Milkcocoa':
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
        if params['cloud_type'] == 'Firebase':
            sc = '''
            <script type="text/javascript">
            let apiKey = '{}';
            let authDomain = '{}';
            let databaseURL = '{}';
            let storageBucket = '{}';
            let fb_projectId = '{}';
            let messagingSenderId = '{}';
            let device_id = '{}';
            </script>
            '''.format(params['fb_apiKey'], params['fb_authDomain'],
                       params['fb_databaseURL'], params['fb_projectId'], params['fb_storageBucket'],
                       params['fb_messagingSenderId'],
                       params['device_id'])
        return sc
