vek = int(input("Kolik ti je let? "))

if vek == 18:
    
    jmeno = input("Jaké je tvoje jméno? ")
    
    if jmeno.lower().startswith("a"):
        print("Vstup povolen")
    else:
        print("Vstup zamítnut")
else:
    print("Vstup povolen pouze pro 18leté.")
