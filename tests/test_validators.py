import pytest
from validators.validators import valideer_ipv4

@pytest.mark.parametrize("adres", ["192.168.1.1", "0.0.0.0", "255.255.255.255"])
def test_geldig_ipv4(adres):
    assert valideer_ipv4(adres)

@pytest.mark.parametrize("adres", ["192.168.1.300", "01.2.3.4", "192.88.99.00",
                                   " 1.2.3.4", "1.2.3", "1.2.3.4.5", "abc", ""])


def test_ongeldig_ipv4(adres):
    with pytest.raises(ValueError):
        valideer_ipv4(adres)


def test_ipv4_als_getal_wordt_geweigerd():
    with pytest.raises(TypeError):
        valideer_ipv4(3232235777)