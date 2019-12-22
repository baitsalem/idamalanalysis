from idc import *
from idaapi import *
from idautils import *

from winapidata import *


class WinApiHandler():

    def __init__(self):

        self.winapi_tree = {}
        self.build_winapi_tree()

    def print_winapi_tree(self):
        """
        print self.winapi_tree in console for debug
        """

        for func in self.winapi_tree:
            print(self.winapi_tree[func][0])
            for ref in self.winapi_tree[func][1:]:
                print("     {}".format(ref))


    def build_winapi_tree(self):
        """
        Build winapi calling tree based on the list winapidat
        """
        
        for api_row in api_matrix:
        
    	    apis = api_row[1:]
    	    
            for api in apis:
               
                api_addr = get_name_ea_simple(api) 
            
                if ( api_addr == ida_idaapi.BADADDR ):
                    continue
                    
                api_addr_name = [hex(api_addr).lstrip("0x").rstrip("L"),api ]
                #print("{} : {}".format(api,api_addr_name))

                ref_addrs_to_api = CodeRefsTo(get_name_ea_simple(api),0)
                
                for ref_to_api in ref_addrs_to_api:

                    ref_to_api_func_name = get_func_name(ref_to_api)
                    ref_to_api_func_addr = hex(get_name_ea_simple(ref_to_api_func_name)).lstrip("0x").rstrip("L")

                    #print("{},{},{}".format(hex(ref_to_api).lstrip("0x").rstrip("L"),ref_to_api_func_name,ref_to_api_func_addr))
                    ref_to_api = hex(ref_to_api).lstrip("0x").rstrip("L")
                    
                    if ( ref_to_api_func_addr not in self.winapi_tree.keys()):
                        
                        self.winapi_tree[ref_to_api_func_addr] = [[ ref_to_api_func_addr, ref_to_api_func_name ]]
                        self.winapi_tree[ref_to_api_func_addr].append([ref_to_api,api])
                    else:
                        self.winapi_tree[ref_to_api_func_addr].append([ref_to_api,api])





#h = WinApiHandler()
#h.print_winapi_tree()



#if l not in func_name:
#   set_name(func_addr , l + '_' + func_name , SN_NOWARN)
