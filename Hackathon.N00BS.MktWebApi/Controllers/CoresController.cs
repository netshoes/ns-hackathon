using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace Hackathon.N00BS.MktWebApi.Controllers
{
    public class CoresController : ApiController
    {
        [HttpGet]
        public IHttpActionResult RetornarTodas() 
        {
            return Ok(new Negocio.ProcessoNegocio().RetornarCores());
        }
    }
}
