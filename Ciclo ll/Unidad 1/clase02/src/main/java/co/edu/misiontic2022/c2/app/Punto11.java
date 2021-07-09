package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/*Programa que lea una variable entera mes y compruebe si el
valor corresponde a un mes de 30 días, de 31 o de 28.
Supondremos que febrero tiene 28 días. Se mostrará además el
nombre del mes. Se debe comprobar que el valor introducido esté
comprendido entre 1 y 12.*/
public class Punto11 {
    public void valida_mes() {
        String meses[] = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};

        Scanner input = new Scanner(System.in);

        System.out.print("\n Ingrese un número entero a validar [1-12]:  ");
        int mes = input.nextInt();
        input.close();
        if (mes < 0 || mes > 12) {
            System.out.println("\n El número ingresado es inválido para un mes \n");
        } else {

            for (int i = 1; i <= 12; i++) {
                if (mes == i) {
                    System.out.println("\n\t El mes ingresado es " + meses[i - 1]);
                    break;
                }
            }

            if (mes == 1 || mes == 3 || mes == 5 || mes == 7 || mes == 8 || mes == 10 || mes == 12) {
                System.out.println("\t El mes ingresado tiene 31 días \n");
            } else if (mes == 4 || mes == 6 || mes == 9 || mes == 11) {
                System.out.println("\t El mes ingresado tiene 30 días \n");
            } else {
                System.out.println("\t El mes ingresado tiene 28 días \n");
            }
        }
    }
}
