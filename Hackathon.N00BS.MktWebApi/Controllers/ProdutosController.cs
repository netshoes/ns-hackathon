using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Text.RegularExpressions;
using System.Web.Http;
using Hackathon.N00BS.MktWebApi.Models;

namespace Hackathon.N00BS.MktWebApi.Controllers
{
    public class ProdutosController : ApiController
    {
        [HttpPost]
        public IHttpActionResult Gravar(List<Comum.ProdutoModel> produtos) 
        {
            new Negocio.ProcessoNegocio().Processar(produtos);
            
            return Ok();
        }

        [HttpGet]
        public IHttpActionResult RetornarTodosBons() 
        {
            //http://localhost:50205/api/Produtos/RetornarTodosBons
            return Ok(new Negocio.ProcessoNegocio().RetornarProdutosBons());
        }

        [HttpGet]
        public IHttpActionResult RetornarTodosRuins()
        {
            return Ok(new Negocio.ProcessoNegocio().RetornarProdutosRuins());
        }
    }

    
}
