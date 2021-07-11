package misiontic2022.c2.adivina_numero;

import java.util.Scanner;

public class Random {
    public void adivina() {
        Scanner input = new Scanner(System.in);

        int aleatorio = (int) (Math.random() * 100.0);
        int contador = 0;
        int numero;
        System.out.print("\n\t\t Digite un número [1-100]:  ");
        // for (numero = 0; numero < 10; numero++) {
        //     aleatorio = (int) (Math.random() * 100.0);
        //     System.out.println(aleatorio);
        // }

        do {
            numero = input.nextInt();
            contador++;
            if (numero < aleatorio) {
                System.out.print("\n\t\t (" + contador + ")  Digite un número mayor:  ");
            }

            if (numero > aleatorio) {
                System.out.print("\n\t\t (" + contador + ") Digite un número menor:  ");
            }
        } while (numero != aleatorio);
        input.close();
        contador--;
        System.out.println("\n\t\t Felicidades!, adivinaste el número en " + contador + " intentos \n");
    }
}
