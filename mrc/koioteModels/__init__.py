import os
from koioteUtils import KoioteUtils

class KoioteModel():
    def __init__(self,name) -> None:
        self.model={
            'name':name,
            'fields':[]
        }
        print("Modelo {} creado!".format(name))
        self.util = KoioteUtils()
        model_lines = self.util.getLines(os.getcwd()+'/mrc/koioteModels/model_template.kit')
       
        model_lines = list(self.util.replaceNames(model_lines,name))
        
        #obtiene los modelos. Almacena en el objeto lista de pares nombre/tipo de dato y devuelve el texto a añadir en el modelo
        fields = self.askForFields()
        for idx,f in enumerate(fields):
            model_lines.insert(9+idx,f)
        
        print("*"*10)

        # for idx,line in enumerate( model_lines):
        #     print(idx,line)
        
        self.util.writeLines("results/models/{}.js".format(name.capitalize()),model_lines)
    
    def move_to_backend(self):
        src = "results/models/{}.js".format(self.model['name'].capitalize())
        dst = os.getcwd()+"/backend/models/{}.js".format(self.model['name'].capitalize())
        self.util.copy_file(src,dst)
            


  
    def askForFields(self):
        end=False
        lines=[]
        
        while(end==False):
            campo_actual={'name':'','type':''}
            print(campo_actual)
            print("Field name:")
            name=input()
            if name=='0':
                print("BYE")
                end=True
                break
            campo_actual['name']=name
            print("Tipo de dato")
            data_type=input().upper()
            campo_actual['type']=data_type
            self.model['fields'].append(campo_actual)
            lines+=["{}:".format(name) ,"{",
            "type: DataTypes.{}".format( data_type),
            "},"
            ]
        # print(lines)
        return lines
       

  


        
        