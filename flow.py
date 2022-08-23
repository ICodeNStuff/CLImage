import assign_form
import converter
import display
import os
import sys
filename = str(sys.argv[1])
char = 'X'
try:
    char = str(sys.argv[2])
except:
    pass
quality_multiplier = 4
try:
    quality_multiplier = int(sys.argv[3])
except:
    pass
converter.convert(filename, quality_multiplier)
pixel_arr = assign_form.assign_form("sta_" + filename)
display.display(pixel_arr, char)
os.remove("sta_" + filename)
