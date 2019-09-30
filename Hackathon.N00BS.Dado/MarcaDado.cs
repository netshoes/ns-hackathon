using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hackathon.N00BS.Dado
{
    public class MarcaDado : ADataBase
    {
        public MarcaDado() : base("DadosMarca")
        {

        }

        public List<string> GetAll()
        {
            var marcas = new List<string>();

            var results = client.ExecuteQuery("select * from dadosBrutos.DadosMarca", parameters: null);

            foreach (var row in results)
            {
                marcas.Add(row[0].ToString());
            }

            return marcas;
        }

        public bool ExisteEssaMarca(string marcaDigitada)
        {
            bool existe = false;

            var results = client.ExecuteQuery(
                "select count(*) from dadosBrutos.DadosMarca where Marcas = @marca",
                parameters:
                new List<Google.Cloud.BigQuery.V2.BigQueryParameter>
                {
                    new Google.Cloud.BigQuery.V2.BigQueryParameter(
                        "marca",
                        Google.Cloud.BigQuery.V2.BigQueryDbType.String, marcaDigitada)  });

            foreach (var row in results)
            {
                existe = Convert.ToInt32(row[0]) >= 1;
                break;
            }

            return existe;
        }
    }
}
