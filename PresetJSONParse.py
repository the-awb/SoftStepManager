from SoftStepObjects import *
from SoftStepFileManagement import *
import json
import re

#TODO: nav_modlinemode not being parsed or set anywhere

"""Regex lists"""

# Ignore bad values
undefined_modline = 'modline\d_$'

# Sort by type
display_config_generic = 'nav_(?!modline)|\d+_key'
modline_generic = 'nav_modline\d|key\d+'


# Parser split
display_value_split = '(\d+|nav)_(?:key_)?(\w+)'
modline_value_split = '(\d+|nav)_(modline(\d))_(\w+)'

def parseJSONToObjects():
    preset_file = getSourceFile('presets')

    ss_dict = json.loads(preset_file)

    preset_list = []

    i = 0

    for k, v in ss_dict.items():
        file_name = k
        preset_name = v['preset_name']
        preset_display_name = v['preset_displayname']
        new_preset = Preset(file_name=file_name, name=preset_name, display_name=preset_display_name)
        preset_list.append(new_preset)
        for param, value in v.items():
            #print(new_preset.name, param, value)
            if re.search(undefined_modline,param) is None:
                if re.match(display_config_generic,param):
                    elements = re.split(display_value_split, param)
                    ss_key = elements[1]
                    display_param_name = elements[2]
                    display_param_value = value
                    new_preset.keys[ss_key].display_configuration[display_param_name] = display_param_value
                elif re.match(modline_generic, param):# and i == 19:
                    elements = re.split(modline_value_split, param)
                    ss_key = elements[1]    #the key number
                    modline_name = elements[2]  # the literal name of the modline
                    modline_num = elements[3]
                    param_name = elements[4] # the name of the parameter
                    new_preset.keys[ss_key].modlines[modline_name].modline_dict[param_name] = value


    """Prints a message to show how Presets found"""

    print('Found %s Presets in the SoftStep Hosted Preset folder:' % (preset_list.__len__()))
    i = 0
    for preset in preset_list:
        i += 1
        print('\t {} : {}'.format(i, preset.name))
    #
    # for preset in preset_list:
    #     for x, y in preset.keys.items():
    #         for m, mv in y.modlines.items():
    #             print(preset.name, preset.display_name,y.name,mv.modline_dict)

    return preset_list

