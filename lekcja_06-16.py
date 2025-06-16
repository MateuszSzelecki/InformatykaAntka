
#include <iostream>
#include <cmath>

using namespace std;

// "42013"

int dowolnyNaDziesietny(string napis, int system) {
    int potega = 0;
    int rezultat = 0;
    for (int i=napis.length()-1; i>=0; i--) {
        int obecnaCyfra = napis[i]-'0';
        rezultat += obecnaCyfra * pow(system, potega);
        potega++;
    }
    return rezultat;
}

string dziesietnyNaDowolny(int dziesietny, int system) {
    string rezultat = "";
    while (dziesietny > 0) {
        int reszta = dziesietny % system;
        dziesietny /= system;
        rezultat = to_string(reszta) + rezultat;
    }
    return rezultat;
}

void zadanie10(string napis, string napis2, int system) {
    int liczba = dowolnyNaDziesietny(napis, system);
    int dzielaca = napis2[0]-'0';
    int rezultat = liczba / dzielaca;
    cout << dziesietnyNaDowolny(rezultat, system) << endl;
}

//napisz program ktory uporzadkuje niemalejaco tablice liczb przez wstawianie. Miejsca na wstawienie powinien znalezc metodą binarna

int funkcja(int tablica[], int szukana) {  //liniowe
    for (int i=0; i<sizeof(tablica); i++) {
        if (tablica[i] == szukana) {
            return i;
        }
    }
}

int znajdzMiejsceBinarnie(int tablica[], int szukana, int koniec) {
    int lewo = 0;
    int prawo = koniec;

    while (lewo < prawo) {
        int srodek = (lewo+prawo)/2;
        if (tablica[srodek] > szukana) {
            prawo = srodek;
        } else {
            lewo = srodek+1;
        }
    }

    return lewo;
}

void przezWstawianie(int tablica[], int n) {
    //polega na znalezieniu odpowiedniego indeksu dla naszego rozwazanego elementu
    for (int i=1; i<n; i++) {
        int klucz = tablica[i];
        int j = i-1;

        int miejsce = znajdzMiejsceBinarnie(tablica, klucz, i);

        while (j >= miejsce) {
            tablica[j+1] = tablica[j];
            j--;
        }

        tablica[miejsce] = klucz;
    }

    for (int i=0; i<n; i++) {
        cout << tablica[i] << endl;
    }
}

int ileJedynekWBinarnym(int dziesietny) {
    int rezultat = 0; //wczesniej było brak inicjalizacji - mogla byc przyjmowana losowa wartosc ;)
    while (dziesietny > 0) {
        int reszta = dziesietny % 2;
        dziesietny /= 2;
        rezultat += reszta;
    }
    return rezultat;
}

void zadanie5(int tablica[], int n) {
    for (int i=0; i<n-1; i++) {
        for (int j=0; j<n-1-i; j++) {
            if (ileJedynekWBinarnym(tablica[j]) < ileJedynekWBinarnym(tablica[j+1])) {
                int temp = tablica[j];
                tablica[j] = tablica[j+1];
                tablica[j+1] = temp;
            }
        }
    }
    for (int i=0; i<n; i++) cout << tablica[i] << endl;
}

int main() {
    int tablica[] = {6, 7, 1, 16};
    zadanie5(tablica, 4);

    return 0;
}
