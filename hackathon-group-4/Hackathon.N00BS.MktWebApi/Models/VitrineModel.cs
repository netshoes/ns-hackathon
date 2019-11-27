using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Hackathon.N00BS.MktWebApi.Models
{
    public class VitrineModel
    {
        public string CodigoBarras { get; set; }

        public string Marca { get; set; }

        public string Modelo { get; set; }

        public string Cor { get; set; }

        public string Sabor { get; set; }

        public int Tamanho { get; set; }

        public int Voltagem { get; set; }

        public string Descricao { get; set; }

        public double Preco { get; set; }
    }
}