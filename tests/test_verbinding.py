import pytest
from domain.verbinding import Verbinding
from hulp import pc

def test_nieuwe_verbinding_is_standaard_up():
    a, b = pc("a"), pc("b")
    verbinding = Verbinding(a, b)

    assert verbinding.status == "UP"
    assert verbinding.component_a is a
    assert verbinding.component_b is b


def test_ongeldige_status_bij_aanmaken_geeft_fout():
    with pytest.raises(ValueError):
        Verbinding(pc("a"), pc("b"), "AAN")


def test_tekstweergave_toont_beide_namen_en_status():
    verbinding = Verbinding(pc("test1"), pc("test2"), "DOWN")

    assert str(verbinding) == "test1 <-> test2 [DOWN]"
