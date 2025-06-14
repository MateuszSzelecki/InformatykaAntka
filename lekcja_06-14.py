#include <iostream>
#include <cmath>
#include <bitset>

using namespace std;

//napisz program szyfrujaca metoda podstawieniowa tekst zapisany wielkimi literami alfabetu, zastosuj rozne przesuniecia, kluczem

string szyfrowanie(string tekst, int klucz) {  //klucz rozpatrywany calosciowo jako liczba
    string zaszyfrowany = "";
    for (char c : tekst) {
        //zamiana malej na duza:
        //1 sposob: c = toupper(c);
        if (c >= 'a' && c <= 'z') c = char(c-32);
        int kod = c-'A';  //zmiana kodu litery na przedział [0, 25]
        int zaszyfrowanyKod = kod + klucz; //kod litery zwiekszony o klucz
        //rozpatrywanie aby kod litery miescil sie w przedziale [0, 25]
        //1 sposob: zaszyfrowanyKod = zaszyfrowanyKod % 26;
        //2 sposob:
        while (zaszyfrowanyKod > 25) zaszyfrowanyKod -= 26;
        zaszyfrowany += char(zaszyfrowanyKod+'A');
    }
    return zaszyfrowany;
}

string deszyfrowanie(string zaszyfrowany, int klucz) {
    string odszyfrowany = "";
    for (char c : zaszyfrowany) {
        int kod = c-'A';
        int odszyfrowanyKod = kod - klucz;
        while (odszyfrowanyKod < 0) odszyfrowanyKod += 26;
        odszyfrowany += char(odszyfrowanyKod+'A');
    }
    return odszyfrowany;
}

string zadanie5(string tekst, int kluczP) {  //rozdrabniamy ten klucz na cyfry
    string klucz = to_string(kluczP);  //klucz w stringu zeby lepiej sie rozpatrywaly indeksy
    int cyklicznoscKlucza = klucz.length();  //ile tych cyfr w kluczu mamy
    int indexKlucza = 0;  //oznacza jaka cyfre w kluczu teraz rozpatrujemy

    string zaszyfrowany = "";
    for (char c : tekst) {
        int kod = c-'A';
        int zaszyfrowanyKod = kod + (klucz[indexKlucza]-'0'); //roznica taka ze odejmujemy '0' bo beda tu cyfry
        while (zaszyfrowanyKod > 25) zaszyfrowanyKod -= 26;
        zaszyfrowany += char(zaszyfrowanyKod+'A');
        indexKlucza++;  //zeby rozpatrywac sobie kolejne chary ze stringa klucza
        if (indexKlucza == cyklicznoscKlucza) indexKlucza = 0;  //kiedy klucz nam sie skonczy, wracamy na start
    }
    return zaszyfrowany;
}

string szyfrowanieVinegar(string tekst, string klucz) {
    //polega na zakodowaniu tekstu na podstawie klucza w zaleznosci od miejsca w alfabecie kolejnych liter klucza
    int cyklicznoscKlucza = klucz.length();
    int indexKlucza = 0;

    string zaszyfrowany = "";
    for (char c : tekst) {
        int kod = c-'A';
        //(dol) tu bierzemy odpowiednia literke z klucza (po kolei i wyliczamy jej wartosc liczbowa w zakresie [0, 25]
        int zaszyfrowanyKod = kod + (klucz[indexKlucza]-'A');
        while (zaszyfrowanyKod > 25) zaszyfrowanyKod -= 26;
        zaszyfrowany += char(zaszyfrowanyKod+'A');
        indexKlucza++;
        if (indexKlucza == cyklicznoscKlucza) indexKlucza = 0;
    }
}

string deszyfrowanieVinegar(string zaszyfrowany, string klucz) {
    int cyklicznoscKlucza = klucz.length();
    int indexKlucza = 0;

    string odszyfrowany = "";
    for (char c : zaszyfrowany) {
        int kod = c-'A';
        int odszyfrowanyKod = kod - (klucz[indexKlucza]-'A');
        while (odszyfrowanyKod < 0) odszyfrowanyKod += 26;
        odszyfrowany += char(odszyfrowanyKod+'A');
    }
    return odszyfrowany;
}


int main() {
    //przyklady brute force:

    /*
    string tekst;
    getline(cin, tekst);  //getline przyjmuje tylko do stringa
    while (tekst != "0") {
        int klucz = stoi(tekst); //stoi(jakis string) - uzywamy do zamiany stringa na inta
        cout << deszyfrowanie("XTGTYF", klucz) << endl;
        getline(cin, tekst);
    }

    for (int i=1; i<=25; i++) {
        cout << deszyfrowanie("XTGTYF", i) << endl;
    }
    */

    return 0;
}
