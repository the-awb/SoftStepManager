
"""All config files"""
#fileLib = ['hosted_setlist', 'hosted_softstepadvanced', 'setlist', 'settings', 'softstepadvanced']
"""
activePresets = 'hosted_setlist.json'
presetDefinitions = 'hosted_softstepadvanced.json'
"""

def getSourceFile(source_file_type):
    location = '/Applications/SoftStep Advanced Editor.app/Contents/Resources/presets/'
    source_file_type = source_file_type
    if source_file_type == 'presets':
        file = location + 'hosted_softstepadvanced.json'
        print('Opening: ', file)
        return open(file).read()
    if source_file_type == 'setlist':
        file = location + 'hosted_setlist.json'
        print('Opening: ', file)
        return open(file).read()
    else:
        print("That file isn't defined yet")

def generateParsedPresetCSV(preset):
    location = '/Users/Willy/Google Drive/ArmedWithBow/Softstep Presets/Parsed Preset Files/'
    file_name = location + 'parsed_' + preset.name + '.gsheet'
    file = open(file_name,'w+')
    file.write('PresetName'
               + '\t' + 'PresetDisplayName'
               + '\t' + 'Key'
               + '\t' + 'KeyName'
               + '\t' + 'Modline'
               + '\t' + 'ModlineParameter'
               + '\t' + 'ModlineValue'
               + '\t' + 'GiveBitwigControl'
               )
    for x, y in preset.keys.items():
        for m, mv in y.modlines.items():
            for mod, value in mv.modline_dict.items():
                #print(preset.name, preset.display_name, y.name, mod, value)
                file.write('\n{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(preset.name,preset.display_name,y.name,y.display_configuration['display_name'],m,mod,value))

#openSourceFile(activePresets)
