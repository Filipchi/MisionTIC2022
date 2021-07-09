package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/*El programa lee por teclado tres números enteros,
   calcula y muestra el mayor de los tres.*/
public class Punto9 {
    public void mayor9() {
        Scanner input = new Scanner(System.in);

        System.out.println("\n Ingrese tres números enteros a validar:  ");
        System.out.print("\t\t Número A:  ");
        int numA = input.nextInt();
        System.out.print("\t\t Número B:  ");
        int numB = input.nextInt();
        System.out.print("\t\t Número C:  ");
        int numC = input.nextInt();
        input.close();

        if (numA > numB & numA > numC) {
            System.out.println("\n El número mayor es " + numA + "\n");
        } else if (numB > numA & numB > numC) {
            System.out.println("\n El número mayor es " + numB + "\n");
        } else if (numC > numA & numC > numB) {
            System.out.println("\n El número mayor es " + numC + "\n");
        }
    } 
}
