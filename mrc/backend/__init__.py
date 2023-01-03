import subprocess
import os,pathlib
from koioteUtils import KoioteUtils

class BackendGenerator():
    def __init__(self) -> None:
        self.utils = KoioteUtils()
         #Crear directorio de backend
        path = os.getcwd()
        print("Current Directory", path)
        
        # prints parent directory
        previous_path =os.path.abspath(os.path.join(path, os.pardir))

        self.directory = '{}/backend'.format(previous_path)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)


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
    

      
