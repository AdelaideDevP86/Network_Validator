import pytest
from hulp import pc, project_met

def project_met_laptop():
    """Laptop is verbonden met Switch en met Router (zoals in het oude script)."""
    return project_met(pc("Laptop"), pc("Switch"), pc("Router"),    
                       verbindingen=[("Laptop", "Switch"), ("Laptop", "Router")])

def test_verwijderde_component_is_weg():
    project = project_met_laptop()
    project.component_verwijderen("Laptop")

    assert project.component_zoeken("Laptop") is None
    assert [c.naam for c in project.componenten] == ["Switch", "Router"]


def test_verwijderde_component_verliest_zijn_verbindingen():
    project = project_met_laptop()
    project.component_verwijderen("Laptop")

    assert project.verbindingen == []


def test_verbindingen_tussen_andere_componenten_blijven_bestaan():
    project = project_met(pc("a"), pc("b"), pc("c"),
                          verbindingen=[("a", "b"), ("b", "c")])
    project.component_verwijderen("a")

    assert len(project.verbindingen) == 1
    over = project.verbindingen[0]
    assert {over.component_a.naam, over.component_b.naam} == {"b", "c"}


def test_onbekende_naam_verwijderen_geeft_fout_en_verandert_niets():
    project = project_met_laptop()
    with pytest.raises(ValueError):
        project.component_verwijderen("Bestaat niet")
    
    assert project.project_statistieken() == {"componenten": 3, "verbindingen": 2, "vlans": 0}