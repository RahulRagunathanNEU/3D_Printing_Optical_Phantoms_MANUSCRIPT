## Written by Rahul Ragunathan 03FEB23
#NORTHEASTERN UNIVERSITY

### classes to import
import tkinter as tk
import os
import re
###

from tkinter import filedialog
root=tk.Tk()
root.withdraw()
# current dir
dir_path = os.path.dirname(os.path.realpath(__file__))


inp_file_path = filedialog.askopenfilename(initialdir=dir_path,filetypes=[("gcode","*.gcode")])  # #input file name, gcode we will work on-- HAS TO BE GCODE
f = open("post_processed.gcode", "w") # make empty post processed file
f.close()
## open input file-- run post processing on gcode-- 


# 2 steps replacement -- refer to https://flexiple.com/python/python-regex-replace/
search_regex = re.compile("G0 (.*) X([\d.]*) Y([\d.]*)(.*?)$")
search_regex2 = re.compile("G0 X([\d.]*) Y([\d.]*)")

data=[]
f = open("post_processed.gcode", "a") # open for appending
with open(inp_file_path, 'r') as file : # reads INPUT File to memory
    for i_num,line in enumerate(file): # line by line 

         line=str(line)
         new_str=line
         #new_str=re.sub(search_regex,str('G0 \1 X\2\4\nG0 Y\3'),line)
         #new_str=re.sub(search_regex2,str('G0 \1 X\2\nG0 Y\3'),new_str)
         t=search_regex.search(line)
         t2=search_regex2.search(line)


         if t:
    #print(t.groups())
            new_str=('G0 %s X%s%s\nG0 Y%s\n' % (t.group(1),t.group(2),t.group(4), t.group(3)))

         if t2:
    #print(t2.groups())
            new_str=('G0 X%s\nG0 Y%s\n' % (t2.group(1),t2.group(2)))



         #print(id(new_str))
         
         f.write(new_str)
         #f.write("Testing %d \n" %4)
         
         




         #filedata = file.read()
f.close()


#print(search_regex.search(filedata)) ## prints out if there is a m(.*)atch
#print(search_regex3.search(filedata))
# Replacing
#new_str=re.sub(search_regex,'G0 \1 X\2\4\nG0 Y\3',filedata)
#new_str2=re.sub(search_regex3,'G0 \1 X\2\nG0 Y\3',new_str)

#print(new_str)







##

