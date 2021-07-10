package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/*Programa que pase de pesos a dólares y viceversa*/
public class Punto14 {
    public void fibonacci14() {
        Scanner input = new Scanner(System.in);

        System.out.print("\n Ingrese la cantidad de números de la \n serie Fibonacci que desea mostrar (>2):  ");
        int num = input.nextInt();
        input.close();

        int i = 0, actual = 1, anterior = 0, siguiente = 0;
        System.out.print("\n" + anterior + " - " + actual);
        while (i < (num - 2)) {
            siguiente = actual + anterior;
            anterior = actual;
            actual = siguiente;
            System.out.print(" - " + siguiente);
            i++;
        }
    }
}