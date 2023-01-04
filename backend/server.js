import app from './app.js'
import { sequelize } from "./util/database.js";


// PARA CREAR LAS TABLAS

// FIN CREACIÓN DE TABLAS

async function main(){
    try {
        await sequelize.sync(
            // {force:false}
            )
        console.log("bien!")
    } catch (error) {
        
    }
    app.listen(3000)
    console.log('Server is listening....')
}

main();
