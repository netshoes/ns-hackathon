//////////////////////////////////////////////////////
// Módulos
const express   = require("express");
const request   = require("request-promise-native");
const validador = require("./lib/validador.js");
const src_root  = "./htdocs";
const _debug    = false;
const MATCH_URI = "http://127.0.0.1:8002/matchData";

const HTTP_OK   = 200;
const HTTP_NOTF = 404;
const HTTP_BADR = 400;
const HTTP_SERR = 500; 

//////////////////////////////////////////////////////
// Setup do server
let port = process.env.PORT || 8001;
app = new express();

let json_op  = {};
json_op.type = "application/json";

//////////////////////////////////////////////////////
// Funções de rotas

function naoEncontrado(req, res)
{
    res.status(HTTP_NOTF);
    res.send("404 Not found");
    res.end();
}

async function fazMatch(req, res)
{
    let dados_validados = {};
    let resultado_match = {};

    try
    {
        let dados       = req.query;
        dados_validados = validador(dados);

        if(_debug)
        {
            console.log(req.headers);
            console.log(dados_validados);
        }

        resultado_match = await chamaMatchAPI(dados_validados);
    }
    catch(err)
    {

        console.log(err);

        let err_response = {};
        
        res.status(HTTP_SERR);
        res.send("Internal Server Error - GG");
        res.end();
        return;
    }

    let final_objects = resultado_match.body;

    if(final_objects.err == true)
    {
        res.status(HTTP_OK);
        res.send("Não foi possível realizar sua consulta no momento, tente novamente mais tarde.");
        res.end();
        return;
    }

    res.status(HTTP_OK);
    res.send(JSON.parse(resultado_match.body));
    res.end();
}

async function chamaMatchAPI(dados)
{
    let resultado_match = {};

    let query = "?";
    let keys  = Object.keys(dados);
    for(let i = 0; i < keys.length; i++)
    {
        query += keys[i] + "=" + dados[keys[i]] + "&";
    }

    console.log(query);

    if(_debug)
    {
        console.log(query);
        for(let i = 0; i < keys.length; i++)
        {
            resultado_match[keys[i]] = dados[keys[i]];
        }

        return resultado_match;
    }

    try
    {
        let uri = MATCH_URI + "/" + query
        resultado_match = await request
        ({ 
            method: 'GET', 
            uri: uri,
            resolveWithFullResponse: true  
        });
    }
    catch(err)
    {
        throw err;
    }

    return resultado_match;
}

//////////////////////////////////////////////////////
// Rotas
let router = express.Router();

router.get("/fazMatch", fazMatch);

//////////////////////////////////////////////////////
// Execução

//pilha de middlewares
app.use(express.json(json_op));
app.use(router);
app.use(express.static(src_root));
app.use(naoEncontrado);

//espera
app.listen(port);



