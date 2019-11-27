using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Google.Apis.Auth.OAuth2;
using Google.Cloud.BigQuery.V2;

namespace Hackathon.N00BS.Dado
{
    public abstract class ADataBase
    {
        protected BigQueryClient client;
        protected BigQueryTable table;

        public ADataBase(string nomeDaTabela)
        {
            this.client = BigQueryClient.Create("hackathon-04", GoogleCredential.FromFile(@"C:\Users\wesley.olivier\Desktop\hackathon\hackathon-04-0c90ce17edf7.json"));
            this.table = client.GetTable("hackathon-04", "dadosBrutos", nomeDaTabela);
        }

        public ADataBase()
        {
            this.client = BigQueryClient.Create("hackathon-04", GoogleCredential.FromFile(@"C:\Users\wesley.olivier\Desktop\hackathon\hackathon-04-0c90ce17edf7.json"));
        }
    }
}
