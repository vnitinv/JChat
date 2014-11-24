class ConnectedDevice(object):
    _instance = None
    devices = []
    groups = {}
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConnectedDevice, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    #
    # def __init__(self):
    #     print 'construction'
    #     self.devices = []
    #     self.groups = {}
    #
    # @property
    # def connections(self):
    #     return self.devices
