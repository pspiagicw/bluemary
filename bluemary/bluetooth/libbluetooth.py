import subprocess
import threading

BLUETOOTH_POWERON_COMMAND = "bluetoothctl power on"
BLUETOOTH_GET_INTERFACE = "bluetoothctl list"
BLUETOOTH_CONNECT_COMMAND = "bluetoothctl connect {}"
BLUETOOTH_DISCONNECT_COMMAND = "bluetoothctl disconnect {}"
BLUETOOTH_PAIR_COMMAND = "bluetoothctl pair {}"
BLUETOOTH_REMOVE_COMMAND = "bluetoothctl remove {}"
BLUETOOTH_TRUST_COMMAND = "bluetoothctl trust {}"
BLUETOOTH_UNTRUST_COMMAND = "bluetoothctl untrust {}"
BLUETOOTH_SCAN_ON = "bluetoothctl scan on"
BLUETOOTH_DEVICE_LIST = "bluetoothctl devices"
BLUETOOTH_CONTROLLER_LIST = "bluetoothctl list"
BLUETOOTH_INFO_COMMAND = "bluetoothctl info {}"
BLUETOOTH_PAIRED_DEVICES = "bluetoothctl paired-devices"


class BluetoothController:
    instance = None
    scan_on = True
    connected_device = None
    @staticmethod
    def thread_start_scan():
        def start_scan():
            result = subprocess.Popen(BLUETOOTH_SCAN_ON.split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        x = threading.Thread(target=start_scan,args=())
        x.start()
    def get_connected_device_name(self):
        if self.connected_device:
            return self.connected_devices
        return 'None'
    def connected_status(self):
        if self.connected_device:
            return True
        return False
    def connect_device(self,device):
        self.pair_device(device)
        result = subprocess.Popen(BLUETOOTH_CONNECT_COMMAND.format(device).split())
        self.connected_device = device
    def diconnect_device(self,device):
        result = subprocess.Popen(BLUETOOTH_DISCONNECT_COMMAND.format(device).split())
    def pair_device(self,device):
        result = subprocess.run(BLUETOOTH_PAIR_COMMAND.format(device).split())
    def remove_device(self,device):
        result = subprocess.run(BLUETOOTH_REMOVE_COMMAND.format(device).split())
    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = cls.__new__(cls)
            cls.thread_start_scan()
        return cls.instance
    def bluetooth_scan_on(self):
        self.scan_on = True
    def get_bluetooth_devices(self):
        if self.scan_on:
            result = subprocess.run(BLUETOOTH_DEVICE_LIST.split(),stdout=subprocess.PIPE)
            out = result.stdout.decode()
            with open('log.txt','a') as logfile:
                logfile.write(out)
            device_list = out.split(sep='\n')
            bluetooth_devices = list()
            for device_line in device_list[:-1]:
                device_line = device_line.split()
                with open('log.txt','a') as logfile:
                    logfile.write(str(device_line))
                bluetooth_devices.append(device_line[1] + ' - ' + device_line[2])
            return bluetooth_devices
    def get_paired_devices(self):
        if self.scan_on:
            result = subprocess.run(BLUETOOTH_PAIRED_DEVICES.split(),stdout=subprocess.PIPE)
            out = result.stdout.decode()
            with open('log.txt','a') as logfile:
                logfile.write(out)
            device_list = out.split(sep='\n')
            bluetooth_devices = list()
            for device_line in device_list[:-1]:
                device_line = device_line.split()
                with open('log.txt','a') as logfile:
                    logfile.write(str(device_line))
                bluetooth_devices.append(device_line[1] + ' - ' + device_line[2])
            return bluetooth_devices
    def get_connection_status(self):
        return 'Connected'
