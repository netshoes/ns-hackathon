using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using System.Web.Script.Serialization;

namespace Hackathon.N00BS.FormularioMvc2.Controllers
{
    public class ProdutoController : Controller
    {
        // GET: Produto
        public ActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Salvar(Comum.ProdutoModel modelo) 
        {
            var produtos = new List<Comum.ProdutoModel>();
            {
                new Comum.ProdutoModel
                {
                    CodigoBarras = modelo.CodigoBarras,
                    Cor = modelo.Cor,
                    Descricao = modelo.Descricao,
                    Marca = modelo.Marca,
                    Modelo = modelo.Modelo,
                    Preco = modelo.Preco,
                    Tamanho = modelo.Tamanho,
                    Data = DateTime.Now
                };
            };

            WebRequest webRequest = WebRequest.Create("http://localhost:50205/api/Produtos/Gravar");
            webRequest.Method = "POST";
            webRequest.ContentType = "application/json";

            string jsonParaEnvio = new JavaScriptSerializer().Serialize(produtos);

            using (StreamWriter streamWriter = new StreamWriter(webRequest.GetRequestStream()))
            {
                streamWriter.Write(jsonParaEnvio);
                streamWriter.Flush();
                streamWriter.Close();

                HttpWebResponse response = (HttpWebResponse)webRequest.GetResponse();

                using (StreamReader streamReader = new StreamReader(response.GetResponseStream()))
                {
                    var resultado = streamReader.ReadToEnd();
                }
            }

            return View();
        }

        public ActionResult ListarBons() 
        {
            string retorno = new FacilitadorWebApi("RetornarTodosBons", "Produtos").Disparar();

            var bons = new JavaScriptSerializer().Deserialize<List<Comum.ProdutoModel>>(retorno);

            ViewBag.Bons = bons;

            return View();
        }

        public ActionResult ListarRuins() 
        {
            string retorno = new FacilitadorWebApi("RetornarTodosRuins", "Produtos").Disparar();

            var ruins = new JavaScriptSerializer().Deserialize<List<Comum.ProdutoModel>>(retorno);

            ViewBag.Bons = ruins;

            return View();
        }
    }
}