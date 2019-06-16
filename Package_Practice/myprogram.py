from Package_Practice.PackagePractice import myfunc
from Package_Practice.Main import MainScript
from Package_Practice.Main.Subfolder import MySubscript


myfunc()
MainScript.main_report()
MySubscript.sub_report()

########################################################################################################################
# Detects if the code is being run directly (True) or if is being imported (False)
if __name__ ==  '__main__':
    pass
'''
Could be cool if importing packages that have debugging script that isnt run if being imported or something
'''