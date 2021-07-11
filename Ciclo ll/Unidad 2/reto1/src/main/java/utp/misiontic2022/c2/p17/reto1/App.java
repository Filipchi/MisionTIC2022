package utp.misiontic2022.c2.p17.reto1;

public class App 
{
    public static void main( String[] args )
    {
        System.out.print("\033[H\033[2J");
        System.out.flush();

        //      Introduciendo valores desde la clase:
        // CalcularInversion cInv = new CalcularInversion(12, 2000000.0, 5.0);
        // Double a = cInv.calcularInteresSimple();
        // Double b = cInv.calcularInteresCompuesto();
        // Double c = cInv.compararInversion();
                
        //      Introduciendo valores desde el método
        CalcularInversion cInv = new CalcularInversion();
        Double c = cInv.compararInversion(12, 2000000.0, 5.0);
        Double b = cInv.calcularInteresCompuesto();
        Double a = cInv.calcularInteresSimple();

        System.out.print("\n" + a + "\n" + b + "\n" + c);
    }
}
