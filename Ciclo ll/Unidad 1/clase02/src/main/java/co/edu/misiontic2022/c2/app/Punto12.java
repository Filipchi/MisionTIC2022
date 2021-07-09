package co.edu.misiontic2022.c2.app;

/*Realizar programa que muestre los números del 1 al 100 que no
sean múltiplos de 3, utilizando cada una las instrucciones
repetitivas (while, do while, for)*/
public class Punto12 {
    public void muestra_ciclos() {

        System.out.println("\n\t  Muestra los números del 1 al 100 que no son múltiplos de 3 ");
        
        System.out.println("\n\n\t --------- Ciclo For ---------\n");
        for (int i = 0; i <= 100; i++) {
            if (i % 3 != 0) {
                System.out.print(i + ", ");
            }
        }
        System.out.println("\n\n\t --------- Ciclo while ---------\n");
        int j = 0;
        while (j <= 100) {
            if (j % 3 != 0) {
                System.out.print(j + ", ");
            }
            j++;
        }
        System.out.println("\n\n\t --------- Ciclo Do - while ---------\n");
        int k = 1;
        do {
            if (k % 3 != 0) {
                System.out.print(k + ", ");
            }
            k++;
        } while (k <= 100); 
        
    }
}
