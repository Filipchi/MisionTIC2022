package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/*Programa que lea dos números por teclado y muestre el
resultado de la división del primer número por el segundo. 
Se debe comprobar que el divisor no puede ser cero*/
public class Punto8 {
    public void division8() {
        Scanner input = new Scanner(System.in);
        System.out.println("\n Ingrese dos números para validar la división:");
        System.out.print("\t Dividendo:  ");
        Double dividendo = input.nextDouble();
        System.out.print("\t Divisor:  ");
        Double divisor = input.nextDouble();
        input.close();

        if (divisor == 0) {
            System.out.println("\n Error!, No se puede dividir por cero. \n");
        } else {
            double respuesta = Math.round((dividendo / divisor) * 100.0) / 100.0;
            System.out.println("\n\t El Resultado de la división es "+respuesta+"\n");
        }
    }
}
