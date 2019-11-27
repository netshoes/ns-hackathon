using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hackathon.N00BS.Dado
{
    public class CorDado : ADataBase
    {
        public CorDado():base("cores")
        {

        }
        
        public List<string> GetAll() 
        {
            var cores = new List<string>();

            var results = client.ExecuteQuery("select* from dadosBrutos.cores", parameters: null);

            foreach (var row in results)
            {
                cores.Add(row["cor"].ToString());
            }           

            return cores;
        }

        public bool ExisteEssaCor(string corDigitada)
        {
            bool existe = false;

            var results = client.ExecuteQuery(
                "select count(*) from dadosBrutos.cores where cor = @cor",
                parameters: 
                new List<Google.Cloud.BigQuery.V2.BigQueryParameter> 
                { 
                    new Google.Cloud.BigQuery.V2.BigQueryParameter(
                        "cor",
                        Google.Cloud.BigQuery.V2.BigQueryDbType.String, corDigitada)  });

            foreach (var row in results)
            {
                existe = Convert.ToInt32(row[0]) >= 1;
                break;
            }

            return existe;
        }
    }
}
