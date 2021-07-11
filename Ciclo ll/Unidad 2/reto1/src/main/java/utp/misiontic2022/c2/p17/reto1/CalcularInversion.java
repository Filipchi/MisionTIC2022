package utp.misiontic2022.c2.p17.reto1;

public class CalcularInversion {
    // Atributos
    private Integer tiempo;
    private Double capital;
    private Double interes;
    
    // Constructores
    public CalcularInversion() {
        this.tiempo = 0;
        this.capital = 0.0;
        this.interes = 0.0;
    }

    public CalcularInversion(Integer pTiempo, Double pCapital, Double pInteres) {
        this.tiempo = pTiempo;
        this.capital = pCapital;
        this.interes = pInteres;
    }

    // Métodos
    public Double calcularInteresSimple() {
        Double interesSimple = this.capital * this.interes * this.tiempo / 100.0;
        return Math.round(interesSimple * 1.0) / 1.0;
    }
    
    public Double calcularInteresCompuesto() {
        Double interesCompuesto = this.capital * (Math.pow((1+(this.interes / 100.0)), this.tiempo) -1);
        return Math.round(interesCompuesto * 1.0) / 1.0;
    }
    
    public double compararInversion() {
        Double direfencia = calcularInteresCompuesto() - calcularInteresSimple();
        return Math.round(direfencia * 1.0) / 1.0;
    }
    
    public double compararInversion(int pTiempo, double pCapital, double pInteres) {
        Double direfencia = (pCapital * (Math.pow((1 + (pInteres / 100.0)), pTiempo) - 1)) - (pCapital * pInteres * pTiempo / 100.0);
        return Math.round(direfencia * 1.0) / 1.0;
    }
}