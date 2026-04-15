import express from 'express';
import portsRouter from './routes/ports.routes.js';
import {errorHandler} from './utils/apiError.js';

const app = express();

app.use(express.json());

const PORT = 3000;

app.use((req,_res,next)=>{
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
    next();
});


app.get("/", (_req,res)=>{
    res.status(200).json({"message":"welcome to Home page."});
});


app.use('/ports',portsRouter);

app.use((_req,res)=>{
    res.status(404).json({success:false,"error":"Routes not found"});
});

app.use(errorHandler);


app.listen(PORT, ()=>{
    console.log(`ports api is running on http://localhost:${PORT}`);
});