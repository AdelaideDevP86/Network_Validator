import ipaddress

# -------------------------
# IPv4-validatie
# -------------------------
"""Invoervalidatie: controleert of één losse waarde geldig is."""
def valideer_ipv4(adres):
    if not isinstance(adres, str):
        raise TypeError(f"IP-adres moet tekst zijn, niet {type(adres).__name__}.")
    try:
        ipaddress.IPv4Address(adres)
    except ipaddress.AddressValueError:
        raise ValueError(f'"{adres}" is geen geldig IPv4-adres.') from None
    return True




# -------------------------
# Prefix validatie
# -------------------------
def valideer_prefix(prefix):
    try:
        getal = int(prefix)
    except ValueError:
        raise ValueError("Prefix ongeldig, voer een getal in.")

    if getal < 0 or getal > 32:
        raise ValueError("Prefix ongeldig, voer een getal tussen 0 en 32.")
    else:
        return True


# -------------------------
# VLAN validatie
# -------------------------
def valideer_vlan(vlan):
    try:
        getal = int(vlan)
    except ValueError:
        raise ValueError("Vlan ongeldig, voer een getal in.")

    if getal < 1 or getal > 4094:
        raise ValueError("Vlan ongeldig, voer een getal tussen 1 en 4094.")
    else :
        return True

def valideer_naam(naam):
    if not isinstance(naam, str):
        raise TypeError("Naam moet een string zijn.")

    if not naam.strip():
        raise ValueError("Naam mag niet leeg zijn.")

    if len(naam) > 100:
        raise ValueError("Naam mag maximaal 100 tekens bevatten.")