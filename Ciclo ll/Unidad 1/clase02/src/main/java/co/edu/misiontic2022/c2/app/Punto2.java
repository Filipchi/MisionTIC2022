package co.edu.misiontic2022.c2.app;

import java.util.Scanner;

/*Programa que calcule el precio de venta de un producto conociendo el precio
por unidad (sin IVA) del producto, el número de productos vendidos y el
porcentaje de IVA aplicado. Los datos anteriores se leerán por teclado*/

public class Punto2 {
    public void producto_iva() {
        Scanner input = new Scanner(System.in);

        System.out.print( "\n Ingrese el valor del producto: " );
        int precio = input.nextInt();

        System.out.print("Ingrese la cantidad: ");
        int cantidad = input.nextInt();

        System.out.print("Ingrese el porcentaje de iva (sin %): ");
        int iva = input.nextInt();
        input.close();

        int precioIVA = precio + (precio * iva / 100);
        int total = precioIVA * cantidad;

        System.out.printf("El precio del producto es: %d", total, "\n");
    }
}
