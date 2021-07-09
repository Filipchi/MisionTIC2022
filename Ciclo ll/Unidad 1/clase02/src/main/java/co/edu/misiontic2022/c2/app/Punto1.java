package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/* Programa que pida por teclado la fecha de nacimiento de una persona
(día, mes, año) y calcule su número de la suerte.
El número de la suerte se calcula sumando el día, mes y año de la fecha
de nacimiento y a continuación sumando las cifras obtenidas en la suma.

Por ejemplo:
Si la fecha de nacimiento es 12/07/1980
Calculamos el número de la suerte así: 12+7+1980 = 1999 1+9+9+9 =
28
Número de la suerte: 28 */
public class Punto1 {
    public void numero_suerte() {
        Scanner input = new Scanner(System.in);
        System.out.print("\n Ingrese una fecha: "); // 12/07/1980

        String fecha = input.nextLine();
        input.close();

        int indiceSeparador1 = fecha.indexOf('/');
        int dia = Integer.parseInt(fecha.substring(0, indiceSeparador1));
        int indiceSeparador2 = fecha.lastIndexOf('/');
        int mes = Integer.parseInt(fecha.substring(++indiceSeparador1, indiceSeparador2));
        int anio = Integer.parseInt(fecha.substring(indiceSeparador2 + 1, fecha.length()));
        int auxSuerte = dia + mes + anio;

        int digito = 0;
        int numeroSuerte = 0;

        while (auxSuerte != 0) {
            digito = auxSuerte % 10;
            numeroSuerte += digito;
            auxSuerte /= 10;
        }

        System.out.printf("El numero de la suerte para %s es %d", fecha, numeroSuerte,"\n");
    }
}