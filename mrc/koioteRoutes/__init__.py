from koioteUtils import KoioteUtils

class KoioteRoute():
    def __init__(self,modelo) -> None:
        self.modelo=modelo
        self.util = KoioteUtils()
        self.lines = self.util.getLines('koioteRoutes/route_template.kit')
        self.lines = list(self.util.replaceNames(self.lines,self.modelo['name']))
        self.util.writeLines('results/routes/{}.routes.js'.format(modelo['name']),self.lines)
    
   