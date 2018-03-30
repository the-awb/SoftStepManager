from PresetJSONParse import *
from SoftStepFileManagement import *

preset_object_list = parseJSONToObjects()

preset_index = int(input('Which preset do you want to print?')) - 1

preset = preset_object_list[preset_index]

generateParsedPresetCSV(preset)