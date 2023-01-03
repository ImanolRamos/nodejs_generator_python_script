from koioteModels import KoioteModel
from koioteControllers import KoioteController
from koioteRoutes import KoioteRoute
from backend import BackendGenerator



#Create backend
mBackendGenerator = BackendGenerator()
# mBackendGenerator.create_nodejs()
# mBackendGenerator.install_dependencies()

#Create database utils
mBackendGenerator.create_util_database()

#Creates app.js
mBackendGenerator.create_app()

#Creates server.js
mBackendGenerator.create_server()



# end=False
# while end==False:
#     print("Nombre del modelo:")
#     name= input()
#     if name=='0':
#         end=True
#         break
#     #Create model
#     mKoioteModel = KoioteModel(name)

#     #Create controller
#     mKoioteController = KoioteController(mKoioteModel.model)
#     mKoioteController.getAndUpdateFieldString()

#     #Create route
#     mKoioteRoute = KoioteRoute(mKoioteModel.model)



