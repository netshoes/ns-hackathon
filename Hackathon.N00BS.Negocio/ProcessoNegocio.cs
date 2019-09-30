using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Hackathon.N00BS.Comum;
using Hackathon.N00BS.Negocio.EntityManager;

namespace Hackathon.N00BS.Negocio
{
    public class ProcessoNegocio
    {
        public void Processar(List<Comum.ProdutoModel> produtosSeller)
        {
            var corEntityManager = new CorEntityManager();

            foreach (var produtoSeller in produtosSeller)
            {
                Comum.ProdutoModel produtoAjustado;

                var validacaoDaCor = new AjusteCor();
                var validacaoDaMarca = new AjusteMarca();
                var validacaoTamanho = new AjusteTamanho();

                produtoAjustado = validacaoDaCor.Ajustar(produtoSeller);
                produtoAjustado = validacaoDaMarca.Ajustar(produtoAjustado);
                //produtoAjustado = validacaoTamanho.Ajustar(produtoAjustado);

                //if (validacaoDaCor.Bom && validacaoDaMarca.Bom && validacaoTamanho.Bom)
                if (validacaoDaCor.Bom && validacaoDaMarca.Bom)
                    new ProdutoEntityManager().SalvarDadosBom(produtoAjustado);
                else
                    new ProdutoEntityManager().SalvarDadosRuim(produtoAjustado);
            }
        }

        public List<Comum.ProdutoModel> RetornarProdutosBons()
        {
            var produtos = new EntityManager.ProdutoEntityManager().GetAllBons();

            return produtos;
        }

        public List<Comum.ProdutoModel> RetornarProdutosRuins()
        {
            var produtos = new EntityManager.ProdutoEntityManager().GetAllRuins();

            return produtos;
        }

        public List<string> RetornarCores()
        {
            return new EntityManager.CorEntityManager().GetAll();
        }
    }

    public abstract class AAjuste
    {
        public bool Bom { get; set; }

        public abstract Comum.ProdutoModel Ajustar(Comum.ProdutoModel produto);
    }

    class AjusteCor : AAjuste
    {
        public override ProdutoModel Ajustar(ProdutoModel produto)
        {
            var corEntityManager = new CorEntityManager();

            var cores = corEntityManager.GetAll();

            //if (cores.Contains(produto.Cor.ToLower()))
            if (corEntityManager.ExisteEssaCor(produto.Cor.ToLower()))
            {
                //tem a cor exata, bola para frente
                this.Bom = true;
                return produto;
            }
            else
            {
                //nao casou, arrumar essa bagaça

                Dictionary<string, int> corValorCombinacao = new Dictionary<string, int>();

                foreach (var cor in cores)
                {
                    int distancia = StringDistance.GetDamerauLevenshteinDistance(cor, produto.Cor.ToLower());
                    corValorCombinacao.Add(cor, distancia);
                }

                int numeroMaisProximoDeZero = corValorCombinacao.Min(x => x.Value);

                if (numeroMaisProximoDeZero <= 3)
                {
                    produto.Cor = corValorCombinacao.Where(u => u.Value == numeroMaisProximoDeZero).FirstOrDefault().Key;
                    Bom = true;
                }
                else
                    Bom = false;

                return produto;
            }
        }
    }

    class AjusteMarca : AAjuste
    {
        public override ProdutoModel Ajustar(ProdutoModel produto)
        {
            var marcaEntityManager = new MarcaEntityManager();

            var marcas = marcaEntityManager.GetAll();

            if (marcas.Contains(produto.Marca.ToLower()))
            //if (marcaEntityManager.ExisteEssaMarca(produto.Marca.ToLower()))
            {
                //tem a cor exata, bola para frente
                this.Bom = true;
                return produto;
            }
            else
            {
                //nao casou, arrumar essa bagaça

                Dictionary<string, int> marcaValorCombinacao = new Dictionary<string, int>();

                try
                {

                    foreach (var marca in marcas)
                    {
                        int distancia = StringDistance.GetDamerauLevenshteinDistance(marca, produto.Marca.ToLower());
                        marcaValorCombinacao.Add(marca, distancia);
                    }
                }
                catch (Exception e)
                {

                    throw;
                }

                int numeroMaisProximoDeZero = marcaValorCombinacao.Min(x => x.Value);

                if (numeroMaisProximoDeZero <= 3)
                {
                    produto.Marca = marcaValorCombinacao.Where(u => u.Value == numeroMaisProximoDeZero).FirstOrDefault().Key;
                    Bom = true;
                }
                else
                    Bom = false;

                return produto;
            }
        }
    }

    class AjusteTamanho : AAjuste
    {
        public override ProdutoModel Ajustar(ProdutoModel produto)
        {
            List<KeyValuePair<string, string>> tamanhos = new List<KeyValuePair<string, string>>();
            tamanhos.Add(new KeyValuePair<string, string>("PP", "XS"));
            tamanhos.Add(new KeyValuePair<string, string>("PP", "PP"));
            tamanhos.Add(new KeyValuePair<string, string>("P", "S"));
            tamanhos.Add(new KeyValuePair<string, string>("P", "Pequeno"));
            tamanhos.Add(new KeyValuePair<string, string>("P", "P"));
            tamanhos.Add(new KeyValuePair<string, string>("M", "M"));
            tamanhos.Add(new KeyValuePair<string, string>("M", "Medio"));
            tamanhos.Add(new KeyValuePair<string, string>("G", "L"));
            tamanhos.Add(new KeyValuePair<string, string>("G", "Grande"));
            tamanhos.Add(new KeyValuePair<string, string>("G", "G"));
            tamanhos.Add(new KeyValuePair<string, string>("GG", "XL"));
            tamanhos.Add(new KeyValuePair<string, string>("GG", "Extra Grande"));
            tamanhos.Add(new KeyValuePair<string, string>("GG", "EG"));
            tamanhos.Add(new KeyValuePair<string, string>("GG", "GG"));
            tamanhos.Add(new KeyValuePair<string, string>("GGG", "XXL"));
            tamanhos.Add(new KeyValuePair<string, string>("GGG", "XGG"));
            tamanhos.Add(new KeyValuePair<string, string>("GGG", "XXG"));
            tamanhos.Add(new KeyValuePair<string, string>("Unico", "Unico"));

            if (tamanhos.Select(a => a.Value).Contains(produto.Tamanho.ToLower()))
            //if (marcaEntityManager.ExisteEssaMarca(produto.Marca.ToLower()))
            {
                //tem a cor exata, bola para frente
                this.Bom = true;
                return produto;
            }
            else
            {
                //nao casou, arrumar essa bagaça

                Dictionary<string, int> tamanhoValorCombinacao = new Dictionary<string, int>();

                try
                {

                    foreach (var tamanho in tamanhos)
                    {
                        int distancia = StringDistance.GetDamerauLevenshteinDistance(tamanho.Value, produto.Tamanho.ToLower());
                        tamanhoValorCombinacao.Add(tamanho.Key, distancia);
                    }
                }
                catch (Exception e)
                {

                    throw;
                }

                int numeroMaisProximoDeZero = tamanhoValorCombinacao.Min(x => x.Value);

                if (numeroMaisProximoDeZero <= 3)
                {
                    produto.Tamanho = tamanhoValorCombinacao.Where(u => u.Value == numeroMaisProximoDeZero).FirstOrDefault().Key;
                    Bom = true;
                }
                else
                    Bom = false;

                return produto;
            }
        }
    }
}



