#include <iostream>
#include <cmath>
#include <bitset>

using namespace std;

int dowolnyNaDziesietny(string liczba, int system) {
    int dziesietny = 0;
    int potega = 0;

    for (int i=liczba.length()-1; i>=0; i--) {
        dziesietny += (liczba[i]-'0')*pow(system, potega);
        //roznica miedzy systemami polega na zmianie podstawy potegi
        potega++;
    }

    return dziesietny;
}

int szesnastkowyNaDziesietny(string szesnastkowy) {
    int dziesietny = 0;
    int potega = 0;

    for (int i=szesnastkowy.length()-1; i>=0; i--) {
        char c = szesnastkowy[i];
        int value;
        if (isdigit(c)) value = c-'0';
        else value = c-'A'+10;
        dziesietny += value*pow(16, potega);
        potega++;
    }

    return dziesietny;
}

string dziesietnyNaDowolny(int dziesietny, int system) {
    if (dziesietny == 0) return "0";

    string rezultat = "";

    while (dziesietny > 0) {
        int reszta = dziesietny % system;
        rezultat = to_string(reszta) + rezultat;
        dziesietny /= system;
    }

    return rezultat;
}

string dziesietnyNaSzesnastkowy(int dziesietny) {
    if (dziesietny == 0) return "0";

    string szesnastkowy = "";

    string pomoc = "0123456789ABCDEF";

    while (dziesietny > 0) {
        int temp = dziesietny % 16;
        dziesietny /= 16;
        szesnastkowy = pomoc[temp] + szesnastkowy;
    }
}

//napisz program dodający dwie liczby binarne zapisane w kodzie uzupelnien do 2 na 16 bitach. Program powinien sygnalizowac przekroczenie zakresu

//na 16 bitach - a wiec uzupelnienie zapisu binarnego do 16 bitow (16 cyfr)
int binarnyNaDziesietnyU2(string binarny) {
    if (binarny[0] == '1') {
        return 0-dowolnyNaDziesietny(binarny.substr(1), 2);
    }
    else return dowolnyNaDziesietny(binarny.substr(1), 2);
}

void zadanie6(string binarny1, string binarny2) {
    int dziesietny1 = binarnyNaDziesietnyU2(binarny1);
    int dziesietny2 = binarnyNaDziesietnyU2(binarny2);
    int result = dziesietny1 + dziesietny2;
    if (result < -32768 || result > 32767) cout << "Przekroczono zakres";
}

//napisz program dzielacy liczbe reprezentowana jako napis w systemie od 2 do 10 przez liczbe jednocyfrowa zapisana w tym samym systemie

void zadanie10(string liczba, string dzielaca, int system) {
    int dziesietnaLiczba = 0;
    int potega = 0;
    for (int i=liczba.length()-1; i>=0; i--) {
        dziesietnaLiczba += (liczba[i]-'0')*pow(system, potega);
        potega++;
    }
    int dziesietnaDzielaca = dzielaca[0]-'0';
    int resultat = dziesietnaLiczba / dziesietnaDzielaca;
    cout << resultat;
}
