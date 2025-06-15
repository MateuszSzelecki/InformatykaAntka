
#include <iostream>
#include <cmath>

using namespace std;

bool czyPierwsza[1001];

void sitoErastotenesa(int n) { //n to maksymalna liczba dla jakie rozwazamy
    for (int i=2; i*i<=n; i++) {  //rozwazamy sobie i do pierwiastka n (w dol)
        if (czyPierwsza[i]) {
            for (int j=i*i; j<=n; j+=i) {
                czyPierwsza[j] = false;
            }
        }
    }
}

//Program wypisujacy liczby polpierwsze nie wieksze od n, n[2,1000], wypisywane liczby nie musza byc uporzadkowane
//polpierwsze - iloczyn dwoch liczb pierwszych

void zadanie4(int n) {
    for (int i=2; i<=n; i++) {
        for (int j=i; j<=n; j++) {
            if (czyPierwsza[i] && czyPierwsza[j] && i*j <= n) {
                cout << i*j << endl;
            }
        }
    }
}

//Napisz program ktory przyjmuje liczbe i sprawdza czy jest pierwsza

bool zadanieMateusza(int liczba) {
    for (int i=2; i*i<=liczba; i++) {
        if (liczba % i == 0) return false;
    }
    return true;
}

int main() {
    for (int i=0; i<=1000; i++) czyPierwsza[i] = true;
    czyPierwsza[0] = czyPierwsza[1] = false;
    sitoErastotenesa(1000);  //wazna inicjalizacja sita erastotenesa poniewaz pozniej z tego korzystamy
    zadanie4(25);
    return 0;
}
