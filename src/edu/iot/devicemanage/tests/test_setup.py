# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from edu.iot.devicemanage.testing import EDU_IOT_DEVICEMANAGE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that edu.iot.devicemanage is properly installed."""

    layer = EDU_IOT_DEVICEMANAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if edu.iot.devicemanage is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'edu.iot.devicemanage'))

    def test_browserlayer(self):
        """Test that IEduIotDevicemanageLayer is registered."""
        from edu.iot.devicemanage.interfaces import (
            IEduIotDevicemanageLayer)
        from plone.browserlayer import utils
        self.assertIn(IEduIotDevicemanageLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EDU_IOT_DEVICEMANAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['edu.iot.devicemanage'])

    def test_product_uninstalled(self):
        """Test if edu.iot.devicemanage is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'edu.iot.devicemanage'))

    def test_browserlayer_removed(self):
        """Test that IEduIotDevicemanageLayer is removed."""
        from edu.iot.devicemanage.interfaces import \
            IEduIotDevicemanageLayer
        from plone.browserlayer import utils
        self.assertNotIn(IEduIotDevicemanageLayer, utils.registered_layers())
