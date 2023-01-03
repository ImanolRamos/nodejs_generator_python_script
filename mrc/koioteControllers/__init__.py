from koioteUtils import KoioteUtils

class KoioteController():
    def __init__(self,modelo) -> None:
        self.modelo = modelo
        print("Controller created!")
        print(self.modelo)
        print("*"*10)
        self.util = KoioteUtils()
        self.lines = self.util.getLines('koioteControllers/controller_template.kit')
        self.lines = list(self.util.replaceNames(self.lines,self.modelo['name']))
        print("Controller:")
        for sl in self.lines:
            print(sl)
        
        # lines = list(self.util.replaceFields(lines,fields))
    
    def getAndUpdateFieldString(self):
        fields=''
        for f in self.modelo["fields"]:
            l = f['name']+","
            print(l)
            fields += l

        self.lines = list(self.util.replaceFields(self.lines,fields))
        for sl in self.lines:
            print(sl)
            
        self.util.writeLines('results/controllers/{}.controller.js'.format(self.modelo['name']),self.lines)