import java.util.Scanner;

public class Main{
    public static void main(String[] args){
    double n1, n2, avarage;

    Scanner sc = new Scanner(System.in);

    System.out.print("Digite Número 1: "); n1 = sc.nextDouble();
    System.out.print("Digite Número 2: "); n2 = sc.nextDouble();

    avarage = ( n1 + n2 ) / 2.0;

    System.out.println("Resultado = " + avarage);
    sc.close();
    }
}
