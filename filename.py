#     ".c":"c",
#     ".py":"python",
#     ".java":"java",
#     ".txt":"text",
#     ".css":"css",
#     ".cs":"c#",
#     ".js":"javascript",
#     ".pptx":"powerpoint presentation"
#the code has the above mentioned extensions included
fileName = input("enter the filename with extension: ")
file_extns= fileName.split(".")
x = repr(file_extns[-1])    
print(x)
if "py" in x :
    print("the extension  of the file is python")
elif "java" in x:
    print("the extension  of the file is java")
elif "css" in x:
    print("the extension of the file is css")
elif "txt" in x:
    print("the extension  of the file is a text file")
elif "cs" in x:
    print("the extension of the file is a c# file")
elif "c" in x :
    print("the extension of the file is a c file")
elif "js" in x :
    print("the extension  of the file is javascript")
elif "pptx" in x:
    print("the extension  of the file is powerpoint presentation")
elif "html" in x:
    print("the extension of the given file is html")
else :
    print("please check your input")