using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Script.Serialization;

namespace Hackathon.N00BS.FormularioMvc2.Controllers
{
    public class CorController : Controller
    {
        // GET: Cor
        public ActionResult Index()
        {
            
            
            string x = new FacilitadorWebApi("RetornarTodas", "Cores").Disparar();

            var cores = new JavaScriptSerializer().Deserialize<List<string>>(x);

            ViewBag.Cores = cores;

            return View();
        }
    }
}