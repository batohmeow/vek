
# Zeptáme se na věk
vek = int(input("Kolik ti je let? "))

# Pokud je věk 18, pokračujeme
if vek == 18:
    # Zeptáme se na jméno
    jmeno = input("Jaké je tvoje jméno? ")
    
    # Pokud jméno začíná na "A" (nebo "a"), povolíme vstup
    if jmeno.lower().startswith("a"):
        print("Vstup povolen")
    else:
        print("Vstup zamítnut")
else:
    print("Vstup povolen pouze pro 18leté.")
