import npyscreen
from collections import namedtuple

from bluemary.bluetooth.libbluetooth import BluetoothController

class BluetoothDevice:
    def __init__(self,name,ssid):
        self.name = name
        self.ssid = ssid



class BluetoothSummaryForm(npyscreen.Form):
    def create(self):
        self.connect = True
        bluetoothcontroller = BluetoothController.get_instance()
        paired_devices = bluetoothcontroller.get_paired_devices()
        connection_string = ""
        connection_device = bluetoothcontroller.get_connected_device_name()
        if connection_device != 'None':
            connection_string = 'Not Connected'
        else:
            connection_string = 'Connected ({})'.format(connection_device)
        self.title_widget = self.add(npyscreen.FixedText,name='title_widget',value='Summary')
        self.connected_status_widget = self.add(npyscreen.FixedText,name='connected_widget',value='Status - ' + connection_string)
        self.paired_widget_name = self.add(npyscreen.FixedText,name='paired_widget_name',value='Paired Devices')
        self.paired_widget = self.add(npyscreen.Pager,name='paired_widget',values=paired_devices,scroll_exit=True,max_height=5)
        self.mode_selector = self.add(npyscreen.SelectOne,name='mode_selector',values=['Connect','Remove'],scroll_exit=True)
    def afterEditing(self):
        if self.mode_selector.value:
            mode_value = int(self.mode_selector.value[0])
            if mode_value == 0:
                self.parentApp.setNextForm('CONNECT')
            if mode_value == 1:
                self.parentApp.setNextForm('UNPAIR')
        else:
            self.parentApp.setNextForm(None)



class BluetoothConnectForm(npyscreen.Form):
    def create(self):
        bluetooth_devices = BluetoothController.get_instance().get_bluetooth_devices()
        self.title_widget = self.add(npyscreen.FixedText,name='title_widget',value='Bluetooth Devices')
        self.bluetooth_devices = self.add(npyscreen.SelectOne,name='bluetooth_devices',values=bluetooth_devices,scroll_exit=True)
    def afterEditing(self):
        if self.bluetooth_devices.value:
            user_choice = int(self.bluetooth_devices.value[0])
            choices_available = BluetoothController.get_instance().get_bluetooth_devices()
            choosed_option = choices_available[user_choice]
            choosed_ssid = choosed_option.split()[0]
            BluetoothController.get_instance().connect_device(choosed_ssid)
        self.parentApp.setNextForm('MAIN')



class BluetoothUnpairForm(npyscreen.Form):
    def create(self):
        bluetooth_devices = BluetoothController.get_instance().get_bluetooth_devices()
        self.title_widget = self.add(npyscreen.FixedText,name='title_widget',value='Bluetooth Devices')
        self.bluetooth_devices = self.add(npyscreen.SelectOne,name='bluetooth_devices',values=bluetooth_devices,scroll_exit=True)
    def afterEditing(self):
        self.parentApp.setNextForm('MAIN')



class BlueMary(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN',BluetoothSummaryForm,name='Bluetooth Summary')
        self.addForm('CONNECT',BluetoothConnectForm,name='Bluetooth Connect')
        self.addForm('UNPAIR',BluetoothUnpairForm,name='Bluetooth Unpair/Remove')



def main():
    TestApp = BlueMary().run()

if __name__ == '__main__':
    main()
