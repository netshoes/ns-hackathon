using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hackathon.N00BS.Comum
{
    public class ProdutoModel
    {
        public string CodigoBarras { get; set; }

        public string Marca { get; set; }

        public string Modelo { get; set; }

        public string Cor { get; set; }       

        public string Tamanho { get; set; }       

        public string Descricao { get; set; }

        public double Preco { get; set; }

        public DateTime Data { get; set; }
    }
}
