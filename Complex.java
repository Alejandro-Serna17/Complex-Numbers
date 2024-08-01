/**
 * Complex Numbers
 * @author Alejandro Serna
 */

public class Complex {

    private double real;
    private double imag;

    public static void main(String[] args) {
        Complex a = new Complex(1.0, 2.0);
        Complex b = new Complex(3.0, 4.0);

        int i = 5;

        System.out.println(a + " + " + b + " = " + a.add(b));
        System.out.println(a + " - " + b + " = " + a.sub(b));
        System.out.println(a + " * " + b + " = " + a.mul(b));
        System.out.println(a + " / " + b + " = " + a.div(b));

        System.out.println(a + " + " + i + " = " + a.add(i));
        System.out.println(a + " - " + i + " = " + a.sub(i));
        System.out.println(a + " * " + i + " = " + a.mul(i));
        System.out.println(a + " / " + i + " = " + a.div(i));
    }

    public Complex() {
        this(0.0, 0.0);
    }

    public Complex(double real) {
        this(real, 0.0);
    }

    public Complex(double real, double imag) {
        this.real = real;
        this.imag = imag;
    }

    public Complex add(Complex o) {
        return new Complex(real + o.real, imag + o.imag);
    }

    public Complex add(double n) {
        return new Complex(real + n, imag);
    }

    public Complex sub(Complex o) {
        return new Complex(real - o.real, imag - o.imag);
    }

    public Complex sub(double n) {
        return new Complex(real - n, imag);
    }

    public Complex mul(Complex o) {
        return new Complex(real * o.real - imag * o.imag, real * o.imag + imag * o.real);
    }

    public Complex mul(double n) {
        return new Complex(real * n, imag * n);
    }

    public Complex div(Complex o) {
        double denom = o.real * o.real + o.imag * o.imag;
        return new Complex((real * o.real + imag * o.imag) / denom, (imag * o.real - real * o.imag) / denom);
    }

    public Complex div(double n) {
        return new Complex(real / n, imag / n);
    }

    @Override
    public String toString() {
        String realStr = real % 1.0 == 0 ? String.format("%.0f", real) : Double.toString(real);
        String imagStr = imag % 1.0 == 0 ? String.format("%.0f", imag) : Double.toString(imag);
        return "(" + realStr + " + " + imagStr + "i)";
    }
}
