from collections import OrderedDict
class ConnectedDevice(object):
    _instance = None
    devices = {}
    groups = OrderedDict()
    groups['MX']=[]
    groups['SRX']=[]
    groups['QFX']=[]
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConnectedDevice, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
