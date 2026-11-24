import pytest
from hulp import pc, project_met

def test_hernoemen_werkt():
    project = project_met(pc("laptop van Adelaide"))
    project.component_wijzigen("laptop van Adelaide",
    nieuwe_component_naam="laptop van Spiderman")

    assert project.component_zoeken("laptop van Spiderman") is not None
    assert project.component_zoeken("laptop van Adelaide") is None


def test_nieuw_ip_adres_wordt_opgeslagen():
    project = project_met(pc("laptop", ip="192.168.2.10"))
    project.component_wijzigen("laptop", ip_adres="192.168.2.20")
    assert project.component_zoeken("laptop").ip_adres == "192.168.2.20"


def test_hernoemen_naar_bestaande_naam_geeft_fout():
    project = project_met(pc("laptop van Adelaide"), pc("laptop van Spiderman"))
    with pytest.raises(ValueError):
        project.component_wijzigen("laptop van Adelaide",
        nieuwe_component_naam="laptop van Spiderman")

    assert [c.naam for c in project.componenten] == ["laptop van Adelaide",
                                                    "laptop van Spiderman"]

def test_wijzigen_van_onbekende_component_geeft_fout():
    project = project_met(pc("laptop"))
    with pytest.raises(ValueError):
        project.component_wijzigen("Bestaat niet", ip_adres="192.168.2.10")


def test_ongeldige_invoer_laat_component_helemaal_ongewijzigd():
    project = project_met(pc("laptop", ip="192.168.2.10"))
    with pytest.raises(ValueError):
        project.component_wijzigen("laptop", nieuwe_component_naam="nieuwe naam",
                                    ip_adres="192.168.2.300")

    laptop = project.component_zoeken("laptop")
    assert laptop is not None # niet half hernoemd
    assert laptop.ip_adres == "192.168.2.10" # oud adres nog intact