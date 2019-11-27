using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Script.Serialization;

namespace Hackathon.N00BS.FormularioMvc.Controllers
{
    public class CorController : Controller
    {
        // GET: Cor
        public ActionResult Index()
        {
            var cores = 
                new JavaScriptSerializer().
                Deserialize<List<string>>(new FacilitadorWebApi("RetornarTodas", "Cores").Disparar());
            
            ViewBag.Cores = cores;
            
            return View();
        }
    }
}