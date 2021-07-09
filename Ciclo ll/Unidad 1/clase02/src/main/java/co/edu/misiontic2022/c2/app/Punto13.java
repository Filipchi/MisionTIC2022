package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/*Programa que pase de pesos a dólares y viceversa*/
public class Punto13 {
    public void conversion13() {
        Scanner input = new Scanner(System.in);

        System.out.println("\n Programa de conversión de moneda COP - USD");
        System.out.println("\t\t\t 1) De USD a COP");
        System.out.println("\t\t\t 2) De COP a USD");
        System.out.print("\n ¿Qué conversión desea realizar? (1 o 2):   ");
        int eleccion = input.nextInt();
        
        double cambio = 0;
        if (eleccion == 1) {
            System.out.print("\n Ingrese el monto a convertir(USD ---> COP):   ");
            double monto = input.nextDouble();
            cambio = Math.round((3841 * monto) * 100.00) / 100.00;
            System.out.println("\n\t\t\t " + monto + " USD = " + cambio + " COP \n");
        } else if (eleccion == 2) {
            System.out.print("\n Ingrese el monto a convertir(COP ---> USD):   ");
            double monto = input.nextDouble();
            cambio = Math.round((monto / 3841) * 100.00) /100.00;
            System.out.println("\n\t\t\t " + monto + " COP = " + cambio + " USD \n");
        } else if (eleccion != 1 && eleccion != 2) {
            System.out.print("\n\t Error ! elección inválida \n");
            input.close();
        }
    }
}
