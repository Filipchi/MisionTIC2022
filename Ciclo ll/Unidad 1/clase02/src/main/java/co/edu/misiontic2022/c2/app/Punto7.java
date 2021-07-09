package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

public class Punto7 {
    public void letra7() {
        Scanner input = new Scanner(System.in);

        System.out.print("\n Ingrese una letra a validar:  ");
        char letra = input.next().charAt(0);
        input.close();
        if (Character.isUpperCase(letra)) {
            System.out.println("\n\t\t\t " + letra + "  es una letra Mayuscula \n");
        } else {
            System.out.println("\n\t\t\t " + letra + "   es una letra Minuscula \n");
        }
    }
}
