import assign_form
import converter
import display
import sys
filename = str(sys.argv[1])
char = 'X'
try:
    char = str(sys.argv[2])
except:
    pass
converter.convert(filename, 4)
pixel_arr = assign_form.assign_form("sta_" + filename)
display.display(pixel_arr, char)