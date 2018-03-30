import datetime


class Modline:
    def __init__(self, modline_name):
        self.modline_name = modline_name
        self.modline_dict = {
            'bankmsb': None,
            'cc': None,
            'channel': None,
            'delay': None,
            'destination': None,
            'device': None,
            'displayLinked': None,
            'enable': None,
            'gain': None,
            'initmode': None,
            'initvalue': None,
            'ledgreen': None,
            'ledred': None,
            'max': None,
            'min': None,
            'mmcfunction': None,
            'mmcid': None,
            'note': None,
            'offset': None,
            'oscroute': None,
            'slew': None,
            'source': None,
            'table': None,
            'velocity': None
        }

class Key:
    def __init__(self, name, key_type, mod_one=None, mod_two=None, mod_three=None, mod_four=None, mod_five=None, mod_six=None):
        self.name = name
        self.type = key_type
        self.display_configuration = {
            'counter_max': None,
            'counter_min': None,
            'counter_wrap': None,
            'display_mode': None,
            'display_name': None,
            'prefix': None
        }
        self.modlines = {
            'modline1': Modline(modline_name='modline1'),
            'modline2': Modline(modline_name='modline2'),
            'modline3': Modline(modline_name='modline3'),
            'modline4': Modline(modline_name='modline4'),
            'modline5': Modline(modline_name='modline5'),
            'modline6': Modline(modline_name='modline6'),
        }
        self.date_imported = datetime.datetime.now()


class Preset:
    def __init__(self, file_name, name, display_name, activation_message=None):
        self.file_name = file_name
        self.name = name
        self.display_name = display_name
        self.activation_message = activation_message
        self.keys = {
            '1': Key('1', 'numeric'),
            '2': Key('2', 'numeric'),
            '3': Key('3', 'numeric'),
            '4': Key('4', 'numeric'),
            '5': Key('5', 'numeric'),
            '6': Key('6', 'numeric'),
            '7': Key('7', 'numeric'),
            '8': Key('8', 'numeric'),
            '9': Key('9', 'numeric'),
            '10': Key('10', 'numeric'),
            'nav': Key('nav', 'nav')
        }

