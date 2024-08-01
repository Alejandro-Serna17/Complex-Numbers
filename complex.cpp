#include <iostream>

/**
 * Complex Numbers
 * @author Alejandro Serna
 */

using std::ostream;
using std::cout;
using std::endl;

struct Complex {
    double real;
    double imag;

    // Constructor
    Complex(double real = 0.0, double imag = 0.0) : real(real), imag(imag) {}

    // Operator overloads for Complex × Complex
    Complex operator+(const Complex &o) const {
        return Complex(real + o.real, imag + o.imag);
    }

    Complex operator-(const Complex &o) const {
        return Complex(real - o.real, imag - o.imag);
    }

    Complex operator*(const Complex &o) const {
        return Complex(real * o.real - imag * o.imag, real * o.imag + imag * o.real);
    }

    Complex operator/(const Complex &o) const {
        double denom = o.real * o.real + o.imag * o.imag;
        return Complex((real * o.real + imag * o.imag) / denom, (imag * o.real - real * o.imag) / denom);
    }

    // Operator overloads for Complex × double
    Complex operator+(double n) const {
        return Complex(real + n, imag);
    }

    Complex operator-(double n) const {
        return Complex(real - n, imag);
    }

    Complex operator*(double n) const {
        return Complex(real * n, imag * n);
    }

    Complex operator/(double n) const {
        return Complex(real / n, imag / n);
    }

    // Friend functions for double × Complex
    friend Complex operator+(double n, const Complex &o) {
        return Complex(n + o.real, o.imag);
    }

    friend Complex operator-(double n, const Complex &o) {
        return Complex(n - o.real, -o.imag);
    }

    friend Complex operator*(double n, const Complex &o) {
        return Complex(n * o.real, n * o.imag);
    }

    friend Complex operator/(double n, const Complex &o) {
        double denom = o.real * o.real + o.imag * o.imag;
        return Complex((n * o.real) / denom, (-n * o.imag) / denom);
    }

    // Overload the stream insertion operator <<
    friend ostream &operator<<(ostream &out, const Complex &o) {
        out << '(' << o.real << " + " << o.imag << "i)";
        return out;
    }
};

int main() {
    Complex a(1.0, 2.0);
    Complex b(3.0, 4.0);
    double i = 5.0;

    cout << a << " + " << b << " = " << a + b << endl;
    cout << a << " - " << b << " = " << a - b << endl;
    cout << a << " * " << b << " = " << a * b << endl;
    cout << a << " / " << b << " = " << a / b << endl;

    cout << a << " + " << i << " = " << a + i << endl;
    cout << a << " - " << i << " = " << a - i << endl;
    cout << a << " * " << i << " = " << a * i << endl;
    cout << a << " / " << i << " = " << a / i << endl;

    cout << i << " + " << a << " = " << i + a << endl;
    cout << i << " - " << a << " = " << i - a << endl;
    cout << i << " * " << a << " = " << i * a << endl;
    cout << i << " / " << a << " = " << i / a << endl;

    return 0;
}
