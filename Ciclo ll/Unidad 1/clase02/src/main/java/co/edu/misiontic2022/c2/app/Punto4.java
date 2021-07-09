package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/*Programa que pase una velocidad en Km/h a m/s. 
La velocidad se lee porteclado.*/
public class Punto4 {
    public void velocidad4() {
        Scanner input = new Scanner(System.in);

        System.out.print(" \nIngrese la velocidad a validar [Km/h]:  ");
        double velocidad = input.nextDouble();
        input.close();

        double conversion = Math.round((velocidad / 3.6) * 100.0) / 100.0;

        System.out.println("\n\t "+velocidad+" Km/h equivalen a "+conversion+" m/s \n");
    }
}
