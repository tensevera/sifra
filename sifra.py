# funkce na sifrovatni
# text je nacteny text, ktery chceme zasifrovat
# posun je o kolik to chceme zasifrovat
# pro hint se podivej do druheho souboru
def zasifruj(text, posun):
    vystup = ""

    # TODO

    return vystup

# nacteme text, ktery chceme zasifrovat
text = input("Zadej text k zasifrovani: ")
# nacteme o kolik to chceme "zasifrovat" aka posunout v ASCII tabulce
posun = int(input("Zadej kolik bude sifra: "))

# zavolame funkci na zasifrovani
sifra = zasifruj(text,posun)

# vypiseme zasifrovany text
print(sifra)