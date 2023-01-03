import express from 'express'
//IMPORT ROUTES
const app = express();
//middlewares
app.use(express.json());//para entender ejemplos json en body
//USE ROUTES
export default app;
