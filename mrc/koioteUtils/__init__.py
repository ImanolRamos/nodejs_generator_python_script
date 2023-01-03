"""
Aplicativo para crear modelos, controladores y rutas
"""
import os

class KoioteUtils:
    def __init__(self) -> None:
        """
        cargar modelo .kit
        """
        print("Creado util de koiote!")
        self.current_path = os.getcwd()
        print(self.current_path)
        
    def getLines(self,path):
        
        data=[]
        # with is like your try .. finally block in this case
        with open(path, 'r') as file:
            # read a list of lines into data
            data = file.readlines()
        
        return data
    
    def replaceNames(self,lines,name):
        lines = map(lambda s: s.replace("{{name_capitalized}}",name.capitalize()),lines)
        lines = map(lambda s: s.replace("{{name}}",name),lines)
        return lines
        
    
    def replaceFields(self,lines,fields):
        lines = map(lambda s: s.replace("{{fields}}",fields),lines)
        return lines


    def writeLines(self,path,lines):
        f = open(path, "w")
        f.writelines(lines)
        f.close()

    def appendLines(self,path,lines):
        f = open(path, "a")
        f.writelines(lines)
        f.close()

    

  

        