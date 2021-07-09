package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/*Programa que lea dos variables enteras N y m y le quite a N sus m últimas
cifras.
Por ejemplo, si N = 123456 y m = 2 el nuevo valor de N será 1234 */
public class Punto3 {
    public void variable3() {
        Scanner input = new Scanner(System.in);

        System.out.print("\n Ingrese un número entero de muchas cifras: ");
        int numero1 = input.nextInt();

        System.out.print("\n Ingrese un número entero de pocas cifras: ");
        int numero2 = input.nextInt();
        
        input.close();

        int respuesta = (int) ((int) numero1 / Math.pow(10, numero2));

        System.out.println("\n El número "+numero1+" sin los últimos "+numero2+" dígitos es "+respuesta);
    }
}
