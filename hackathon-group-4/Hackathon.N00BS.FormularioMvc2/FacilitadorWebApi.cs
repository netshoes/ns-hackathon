using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Web;

namespace Hackathon.N00BS.FormularioMvc2
{
    public class FacilitadorWebApi
    {
        private string dominio = "http://localhost:50205/api/";
        private string action = string.Empty;

        public FacilitadorWebApi(string action, string controller)
        {
            this.action = "/"+action;
            this.dominio += controller;
        }

        public string Disparar()
        {
            try
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
            catch (Exception e)
            {

                throw;
            }
            
            
        }
    }
}