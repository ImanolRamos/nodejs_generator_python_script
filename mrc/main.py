from koioteModels import KoioteModel
from koioteControllers import KoioteController
from koioteRoutes import KoioteRoute
from backend import BackendGenerator

#Create backend
mBackendGenerator = BackendGenerator()
# mBackendGenerator.create_nodejs()
# mBackendGenerator.install_dependencies()

#Creates app.js
mBackendGenerator.create_app()

#Creates server.js



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



