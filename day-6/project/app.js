const express = require('express');

app = express();

app.use(express.json());

const PORT = 5000;

app.get("/", (req,res)=>{
    res.status(200).json({"message":"Welcome to home page."});
});

app.post("/products", (req,res) => {
    try{
        const {id,name,price} = req.body;
        res.status(201).json({"message":"The product data is saved.", "data":`Id:${id}, productname:${name}, productPrice:${price}`});
    }catch(error){
        res.status(500).json({"message":"Internal server error."});
    }
});

app.put("/products/:id", (req,res)=>{
    try{
        const {id} = req.params;

        if (id == 5){
            const {name,price} = req.body;
            res.status(200).json({"message":"The product gets updated.","Product":`Id:${id}, name:${name}, price:${price}`});
        }else{
            res.status(404).json({"message":"Product not found"});
        }
    }catch(error){
        res.status(500).json({"message":"Internal server error"});
    }
}); 


app.listen(PORT,()=>{
    console.log(`Application is running on the port : ${PORT}`);
});