package utp.misiontic2022.c2.p17.reto1;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.print("\033[H\033[2J");
        System.out.flush();

        CalcularInversion cInv = new CalcularInversion(12, 2000000.0, 5.0);
        Double a = cInv.calcularInteresSimple();
        Double b = cInv.calcularInteresCompuesto();
        Double c = cInv.compararInversion();
        
        System.out.print("\n"+ a + "\n"+ b + "\n"+ c );
    }
}
