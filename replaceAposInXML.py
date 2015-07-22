import os, time
from xml.dom.minidom import parse
from Tkinter import *
from tkFileDialog import askdirectory

def getpath():
    Tk().withdraw()

    options = {}
    options['initialdir'] = "B:\DTP DEPARTMENT\_Projects MOCA"
    options['title'] = 'ESM Files Investigation'

    fp = askdirectory(**options)
    return fp

def replaceText(node, newText):
    if node.firstChild.nodeType != node.TEXT_NODE:
        raise Exception("node does not contain text")
    
    node.firstChild.replaceWholeText(newText)
    
def replaceApos(fastText):
    newFastText = fastText.replace("'", " ")
#    print newFastText
    replaceText(fast, newFastText)
    file_handle = open(f, "wb")
    
dir = getpath()
    
i = 0
for file in os.listdir(dir):
    print "Checking " + file
    if file.endswith(".xml"):
        f = os.path.join(dir,file)
        xmldoc = parse(f)
        fasts = xmldoc.getElementsByTagName("fast")
        
        for fast in fasts:
            ftext = fast.firstChild.data
#            print f + "\t" + ftext
            if "'" in ftext:
                replaceApos(ftext)
                with open(f, "wb") as modifiedfile:
                    xmldoc.writexml(modifiedfile)
                i += 1    
                print "\n!!!  -->  %s  modified.\n" %file
            else:
                pass
    
print "%s fast links changed" %i
            
print "=" * 150
print "TASK COMPLETED"

time.sleep(10)