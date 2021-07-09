package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/*Programa que lea por teclado tres números enteros H, M, S
correspondientes a hora, minutos y segundos respectivamente,
y comprueba si la hora que indican es una hora válida.*/
public class Punto10 {
    public void reloj10() {
        Scanner input = new Scanner(System.in);

        System.out.println("\n Ingrese una hora a validar:  ");
        System.out.print("\t\t Hora:  ");
        int H = input.nextInt();
        System.out.print("\t\t Minuto:  ");
        int M = input.nextInt();
        System.out.print("\t\t Segundo:  ");
        int S = input.nextInt();
        input.close();
        
        if (H < 0 || H > 24) {
            System.out.println("\n La Hora ingresada es inválida (" + H + ":" + M + ":" + S + ")\n");
        } else if (M < 0 || M > 60) {
            System.out.println("\n El minuto ingresado es inválido (" + H + ":" + M + ":" + S + ")\n");
        } else if (S < 0 || S > 60) {
            System.out.println("\n El segundo ingresado es inválido (" + H + ":" + M + ":" + S + ") \n");
        } else {
            System.out.println("\n La Hora ingresada es válida ! (" + H + ":" + M + ":" + S + ") \n");
        }
    }        
}
