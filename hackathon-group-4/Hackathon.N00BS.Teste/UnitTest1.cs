using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Hackathon.N00BS.Teste
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            string corDigitada = "Azul";

            var cores = new List<string> { "Azul", "Preto", "Amarelo" };

           

            foreach (var cor in cores)
            {
                var x = Regex.Match(corDigitada, cor).Groups;
            }
        }
    }
}
