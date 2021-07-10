package co.edu.utp.misiontic2022.c2.app;

public class App 
{
    public static void main( String[] args )
    {
        System.out.print("\033[H\033[2J");
        System.out.flush();
        
        Materia materia = new Materia("Programación",4,40,50,39,76,96);

        materia.mostrarMateria();
        System.out.println();
        materia.mostrarPromedio();
    }
}