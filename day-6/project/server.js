const http = require('http');
const url = require('url');
const fs = require('fs').promises;


const server = http.createServer((req,res)=>{

    const parsed_url = new URL(req.url, `http://${req.headers.host}`);
    const path = parsed_url.pathname;
    const method = req.method;

    if (path === '/' && method === 'GET') {
        res.writeHead(200);
        res.end('<h1>Welcome to home page</h1>');
    }else if(path === '/products' && method === "GET") {
        res.writeHead(200);
        res.end('<h1>Products fetched successfully.</h1>')
    }else if (path === '/products' && method === 'POST'){
        let data  = '';

        req.on(data, chunk => {
            data += chunk.tostring();
        });

        res.writeHead(201);
        res.end(JSON.stringify(data));
    }else if (path === '/content' && method === 'GET'){
        const getContent = async ()=>{
            try{
                const data = await fs.readFile('./sample.txt','utf-8');
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify(data));
            }catch(error){
                console.log(error);
            }
        };

        getContent();
    }else{
        res.writeHead(404);
        res.end('Not Found');
    }
});


const PORT = 4500;

server.listen(PORT,()=>{
    console.log(`application is running on port ${PORT}`);
});