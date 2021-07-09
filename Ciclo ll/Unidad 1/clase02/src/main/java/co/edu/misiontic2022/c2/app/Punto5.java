package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/*Programa que lea la longitud de los catetos de un triángulo rectángulo y
calcula la longitud de la hipotenusa según el teorema de Pitágoras*/
public class Punto5 {
    public void triangulo5() {
        Scanner input = new Scanner(System.in);

        System.out.println("\n Ingrese el valor de los catetos: ");
        System.out.print("\t\t Cateto 1 [cm]: ");
        double cateto1 = input.nextDouble();
        
        System.out.print("\t\t Cateto 2 [cm]: ");
        double cateto2 = input.nextDouble();
        input.close();

        double hipotenusa = Math.sqrt(Math.pow(cateto1, 2) + Math.pow(cateto2, 2));
        hipotenusa = Math.round(hipotenusa * 100.0) / 100.0;
        System.out.println("\nlos catetos con longitud de "+cateto1+" y "+cateto2+" cm forman un triangulo con hipotenusa "+hipotenusa+" cm \n");
    }
}
