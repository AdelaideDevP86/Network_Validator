import pytest
from domain.component import Component


def test_component_met_geldige_waarden_heeft_precies_die_waarden():
    laptop = Component("laptop", "laptop van Adelaide", "prive en studie",
                       ip_adres="192.168.2.10", prefix=24,
                       gateway="192.168.2.1", vlan=10)

    assert laptop.component_type == "laptop"
    assert laptop.naam == "laptop van Adelaide"
    assert laptop.beschrijving == "prive en studie"
    assert laptop.ip_adres == "192.168.2.10"
    assert laptop.prefix == 24
    assert laptop.gateway == "192.168.2.1"
    assert laptop.vlan == 10

def test_component_zonder_optionele_velden_krijgt_standaardwaarden():
    component = Component("pc", "pc-01")
    assert component.beschrijving == ""
    assert component.ip_adres is None
    assert component.prefix is None
    assert component.gateway is None
    assert component.vlan is None

@pytest.mark.parametrize("velden", [{"ip_adres": "192.168.2.300"},
                                    {"gateway": "abc"},
                                    {"prefix": 33},
                                    {"vlan": 5000}])

def test_component_met_ongeldige_waarde_wordt_geweigerd(velden):
    with pytest.raises(ValueError):
        Component("pc", "pc-01", **velden)
