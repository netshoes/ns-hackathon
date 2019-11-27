using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hackathon.N00BS.Negocio.EntityManager
{
    class CorEntityManager
    {
        private Dado.CorDado corDado;

        public CorEntityManager()
        {
            this.corDado = new Dado.CorDado();
        }

        public List<string> GetAll()
        {
            var cores = this.corDado.GetAll();
            cores = cores.ConvertAll(d => d.ToLower());

            return cores;
        }

        public bool ExisteEssaCor(string corDigitada) 
        {
            return this.corDado.ExisteEssaCor(corDigitada);
        }
    }
}
