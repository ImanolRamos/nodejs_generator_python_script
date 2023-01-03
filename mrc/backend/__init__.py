import subprocess
import os,pathlib
from koioteUtils import KoioteUtils
from dotenv import dotenv_values

class BackendGenerator():
    def __init__(self) -> None:
        self.config = dotenv_values(".env")
        
        

        self.utils = KoioteUtils()
         #Crear directorio de backend
        path = os.getcwd()
        self.current_path = path
        print("Current Directory", path)
        
        # prints parent directory
        previous_path =os.path.abspath(os.path.join(path, os.pardir))

        self.directory = '{}/backend'.format(previous_path)

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        
        #Copiar .env
        self.utils.copy_file(self.current_path+"/.env",self.directory+"/.env")

        #Carpetas que deben existir en el backend
        paths = [self.directory+"/controllers",
        self.directory+"/models",
        self.directory+"/routes",
        self.directory+"/utils"]

        self.utils.regenerate_directories(paths,self.directory)
        


    def create_nodejs(self):
        os.chdir(self.directory)
        subprocess.call(["npm","init","es6"])

    def install_dependencies(self):
        os.chdir(self.directory)
        #morgann pg pg-hstore sequelie sequelize-cli
        modulos = ["express","morgan","pg","pg-hstore", "sequelize", "sequelize-cli"]
        for m in modulos:
            subprocess.call(["npm","install",m])
    
    #Creates app.js
    def create_app(self):
        os.chdir(self.directory)
        path = "{}/app.js".format(self.directory)
        print(path)
        headers = [
            "import express from 'express'\n",
            "//IMPORT ROUTES\n"
            "const app = express();\n",
            "//middlewares\n",
            "app.use(express.json());//para entender ejemplos json en body\n",
            "//USE ROUTES\n"
            "export default app;\n"
        ]

        for h in headers:print(h)

        self.utils.writeLines(path,headers)
    
    #Creates server.js
    def create_server(self):
        
        lines = self.utils.getLines(self.current_path+"/koioteServer/server_template.kit")
        lines = self.utils.replaceAnyField(lines,"port", self.config['SERVER_PORT'])
        self.utils.writeLines(self.directory+"/server.js",lines)

    
    def create_util_database(self):
        database_path = self.directory+"/utils"
        self.utils.copy_file(
            src=self.current_path+"/koioteDatabase/database_template.kit",
            dst=database_path+"/database.js")
        

      
