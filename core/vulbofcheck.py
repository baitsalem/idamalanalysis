from idautils import *
from idaapi import *

from idc import *

ea = ida_ida.inf_get_min_ea()

for funcea in Functions(get_segm_start(ea), get_segm_end(ea)):
    functionName = get_func_name(funcea)
    if "strcpy" in functionName :
        print ("Function : {}".format(functionName))
        for ref in CodeRefsTo(funcea, 1):
            print ("Reference to {} : {}-{}".format(functionName,hex(ref), idc.generate_disasm_line(ref,0)))
            if "call" in idc.generate_disasm_line(ref,0):
                print("it is a call")


#ea = idc.get_name_ea_simple("CreateFileA")
#if ea != idaapi.BADADDR:    
 #   for ref in idautils.CodeRefsTo(ea, 1):
  #      print hex(ref), idc.generate_disasm_line(ref,0)
