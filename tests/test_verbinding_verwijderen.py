import pytest
from domain.verbinding import Verbinding
from hulp import pc, project_met

def test_toegevoegde_verbinding_verwijderen():
    project = project_met(pc("a"), pc("b"), pc("c"),
                          verbindingen=[("a", "b"), ("b", "c")])
    
    project.verwijderen_verbinding(project.verbindingen[0])

    assert len(project.verbindingen) == 1
    assert str(project.verbindingen[0]) == "b <-> c [UP]"


def test_niet_toegevoegde_verbinding_verwijderen_geeft_fout():
    project = project_met(pc("a"), pc("b"))
    losse = Verbinding(project.component_zoeken("a"), project.component_zoeken("b"))

    with pytest.raises(ValueError):
        project.verwijderen_verbinding(losse)


def test_iets_anders_dan_een_verbinding_verwijderen_geeft_typeerror():
    project = project_met(pc("a"), pc("b"), verbindingen=[("a", "b")])
    
    with pytest.raises(TypeError):
        project.verwijderen_verbinding("a <-> b")
