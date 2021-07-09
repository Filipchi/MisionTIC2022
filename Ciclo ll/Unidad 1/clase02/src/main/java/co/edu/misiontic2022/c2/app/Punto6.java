package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/*Programa que lea un número entero y 
muestre si el número es múltiplo de 10.*/
public class Punto6 {
    public void multiplo10() {
        Scanner input = new Scanner(System.in);

        System.out.print("\n Ingrese el número entero a validar:  ");
        int numero = input.nextInt();
        input.close();

        if (numero % 10 == 0) {
            System.out.println("\n\t El número " + numero + " es múltiplo de 10 \n");
        }
        else {
            System.out.println("\n\t El número " + numero + " No es múltiplo de 10 \n");
        }
    }
}
