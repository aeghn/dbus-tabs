#!/usr/bin/python3

# run with python -i, then use the get_tabs, activate and rename functions to use the dbus interface

import dbus
import json

bus = dbus.SessionBus()

browser_tabs_object = bus.get_object(
        'org.cubimon.BrowserTabs', '/org/cubimon/BrowserTabs')
browser_tabs_interface = dbus.Interface(
        browser_tabs_object, dbus_interface='org.cubimon.BrowserTabs')

getTabs = browser_tabs_interface.get_dbus_method('tabs')
activate = browser_tabs_interface.get_dbus_method('activate')
rename = browser_tabs_interface.get_dbus_method('rename')
getActiveTabId = browser_tabs_interface.get_dbus_method('activeTabId')

tabs = json.loads(getTabs())
for tabId, tabName in tabs.items():
    print(str(tabId) + ' - ' + tabName)
print('active tab id: ' + str(getActiveTabId()))


