# C:/Users/mkovach/Documents/Pfuncs/winAddr_format.py
# remember to put an 'r' before the path input to this function, like
# winAddr_format(r'example\path\etc')

def winAddr_format(winIn):
    wintOut = winIn.replace("\\", "/")
    return wintOut
    #print(wintOut)