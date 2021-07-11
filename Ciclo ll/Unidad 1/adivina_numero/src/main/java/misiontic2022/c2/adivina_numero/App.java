package misiontic2022.c2.adivina_numero;

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
        
        Random jugador = new Random();
        jugador.adivina();
    }
}
