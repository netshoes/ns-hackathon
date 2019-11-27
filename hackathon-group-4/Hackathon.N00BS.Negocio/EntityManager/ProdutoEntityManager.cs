using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hackathon.N00BS.Negocio.EntityManager
{
    class ProdutoEntityManager
    {
        private Dado.ProdutoDado produtoDado;

        public ProdutoEntityManager()
        {
            this.produtoDado = new Dado.ProdutoDado();
        }

        public void SalvarDadosBom(Comum.ProdutoModel produto)
        {
            this.produtoDado.Salvar(produto, "DadosBom");
        }

        public void SalvarDadosRuim(Comum.ProdutoModel produto)
        {
            this.produtoDado.Salvar(produto, "DadosRuim");
        }

        public List<Comum.ProdutoModel> GetAllBons()
        {
            var produtos = this.produtoDado.GetAll("DadosBom");

            return produtos;
        }

        public List<Comum.ProdutoModel> GetAllRuins()
        {
            var produtos = this.produtoDado.GetAll("DadosRuim");

            return produtos;
        }
    }
}
