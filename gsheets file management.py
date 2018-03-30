import gspread
from oauth2client.service_account import ServiceAccountCredentials
from PresetJSONParse import *
from SoftStepFileManagement import *

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive'
    #'https://www.googleapis.com/auth/drive.file'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('SoftStepIntegration-a993219b4d70.json', scope)

gc = gspread.authorize(credentials)


wks = gc.open('Dummy Test').sheet1

#wks.add_worksheet('Gee Wizz',100,6)
for row in wks.row_values(1):
    print(row)

new_sheet = gc.create('Dummy Test 2').add_worksheet('1',10,10)

#
#
# preset_object_list = parseJSONToObjects()
#
# preset_index = int(input('Which preset do you want to print?')) - 1
#
# preset = preset_object_list[preset_index]
#
# generateParsedPresetCSV(preset)
#
#
#
# def generateParsedPresetCSV(preset):
#     location = '/Users/Willy/Google Drive/ArmedWithBow/Softstep Presets/Parsed Preset Files/'
#     file_name = location + 'parsed_' + preset.name + '.gsheet'
#     file = open(file_name,'w+')
#     file.write('PresetName'
#                + '\t' + 'PresetDisplayName'
#                + '\t' + 'Key'
#                + '\t' + 'KeyName'
#                + '\t' + 'Modline'
#                + '\t' + 'ModlineParameter'
#                + '\t' + 'ModlineValue'
#                + '\t' + 'GiveBitwigControl'
#                )
#     for x, y in preset.keys.items():
#         for m, mv in y.modlines.items():
#             for mod, value in mv.modline_dict.items():
#                 #print(preset.name, preset.display_name, y.name, mod, value)
#                 file.write('\n{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(preset.name,preset.display_name,y.name,y.display_configuration['display_name'],m,mod,value))
