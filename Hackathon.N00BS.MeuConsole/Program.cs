using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Web.Script.Serialization;

namespace Hackathon.N00BS.MeuConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            var produtos = new List<Comum.ProdutoModel>
            {                
                new Comum.ProdutoModel
                {
                    CodigoBarras = "93147620",
                    Cor = "graphite",
                    Descricao = "Jaqueta com tecido acolchoado, que garante melhor conforto térmico. Tecnologias Water Resist e Wind Protection, com proteção contra vento e chuvas leves, bolsos laterais com zíper e punhos e barras com acabamento elástico.",
                    Marca = "Olimpicus",
                    Modelo = "Essential",
                    Preco = 199.99,
                    Tamanho = "S",
                    Data = DateTime.Now
                }
            };

            WebRequest webRequest = WebRequest.Create("http://localhost:50205/api/Produtos/Gravar");
            webRequest.Timeout = 7200000;
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

            Console.WriteLine("Acabou =)");
            Console.Read();
        }
    }
    public class FacilitadorWebApi
    {
        private string dominio = "http://localhost:59489/api/amigos/";
        private string action = string.Empty;

        public FacilitadorWebApi(string action)
        {
            this.action = action;
        }

        public string Disparar()
        {
            WebRequest webRequest = WebRequest.Create(dominio + action);
            webRequest.Method = "GET";
            HttpWebResponse httpWebResponse = null;
            httpWebResponse = (HttpWebResponse)webRequest.GetResponse();
            string resultado = string.Empty;

            using (Stream stream = httpWebResponse.GetResponseStream())
            {
                StreamReader streamReader = new StreamReader(stream);
                return streamReader.ReadToEnd();
            }
        }
    }
}
