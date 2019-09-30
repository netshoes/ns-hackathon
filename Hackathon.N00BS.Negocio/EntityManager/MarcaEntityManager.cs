using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hackathon.N00BS.Negocio.EntityManager
{
    class MarcaEntityManager
    {
        private Dado.MarcaDado marcaDado;

        public MarcaEntityManager()
        {
            this.marcaDado = new Dado.MarcaDado();
        }

        public List<string> GetAll()
        {
            var marcas = this.marcaDado.GetAll();
            marcas = marcas.ConvertAll(d => d.ToLower());            

            return marcas.Distinct().ToList();
        }

        public bool ExisteEssaMarca(string marcaDigitada) 
        {
            return this.marcaDado.ExisteEssaMarca(marcaDigitada);
        }
    }
}
