using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hackathon.N00BS.Dado
{
    public class ProdutoDado : ADataBase
    {      

        public ProdutoDado()
        {
            
        }

        public void Salvar(Comum.ProdutoModel produto, string tabela) 
        {

            //insert dadosBrutos.DadosRuim(produto.CodigoBarras, produto.Marca, Modelo, Cor, Tamanho, Descricao, Preco) values("1234", "Nike", "42-a", "Azul", "P", "Sapato", 42)
            this.table = client.GetTable("hackathon-04", "dadosBrutos", tabela);

            var results = client.ExecuteQuery(
                @"insert dadosBrutos."+tabela+" values (@CodigoBarras,@Marca, @Modelo,@Cor,@Tamanho,@Descricao,@Preco,@Data)",
                parameters:
                new List<Google.Cloud.BigQuery.V2.BigQueryParameter>
                {
                    new Google.Cloud.BigQuery.V2.BigQueryParameter("CodigoBarras", Google.Cloud.BigQuery.V2.BigQueryDbType.String, produto.CodigoBarras),
                    new Google.Cloud.BigQuery.V2.BigQueryParameter("Marca", Google.Cloud.BigQuery.V2.BigQueryDbType.String, produto.Marca),
                    new Google.Cloud.BigQuery.V2.BigQueryParameter("Modelo", Google.Cloud.BigQuery.V2.BigQueryDbType.String, produto.Modelo),
                    new Google.Cloud.BigQuery.V2.BigQueryParameter("Cor", Google.Cloud.BigQuery.V2.BigQueryDbType.String, produto.Cor),
                    new Google.Cloud.BigQuery.V2.BigQueryParameter("Tamanho", Google.Cloud.BigQuery.V2.BigQueryDbType.String, produto.Tamanho),
                    new Google.Cloud.BigQuery.V2.BigQueryParameter("Descricao", Google.Cloud.BigQuery.V2.BigQueryDbType.String, produto.Descricao),
                    new Google.Cloud.BigQuery.V2.BigQueryParameter("Preco", Google.Cloud.BigQuery.V2.BigQueryDbType.Float64, produto.Preco),
                    new Google.Cloud.BigQuery.V2.BigQueryParameter("Data", Google.Cloud.BigQuery.V2.BigQueryDbType.DateTime, produto.Data),
                });

        }

        public List<Comum.ProdutoModel> GetAll(string tabela) 
        {
            var produtos = new List<Comum.ProdutoModel>();

            var results = client.ExecuteQuery("select * from dadosBrutos."+tabela, parameters: null);

            foreach (var row in results)
            {
                produtos.Add(
                    new Comum.ProdutoModel 
                    { 
                        CodigoBarras = row["CodigoBarras"].ToString(),
                        Marca = row["Marca"].ToString(),
                        Modelo = row["Modelo"].ToString(),
                        Cor = row["Cor"].ToString(),
                        Tamanho = row["Tamanho"].ToString(),
                        Descricao = row["Descricao"].ToString(),
                        Preco = Convert.ToDouble(row["Preco"]),
                        Data = Convert.ToDateTime(row["Data"]),
                    });               
            }

            return produtos;
        }
    }
}
