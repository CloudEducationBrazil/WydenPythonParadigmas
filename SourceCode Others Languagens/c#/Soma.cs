using System;

namespace Soma{
    class soma{
        static void Main(string[] arg){
          double n1, n2, avarage;

          Console.Write("Digite Número 1: "); n1 = double.Parse(Console.ReadLine());
          Console.Write("Digite Número 2: "); n2 = double.Parse(Console.ReadLine());
          avarage = ( n1 + n2) / 2.0;

          Console.WriteLine("Resultado = " + avarage);
        }
    }
}
