import pytest
from hulp import pc, project_met

def test_twee_keer_dezelfde_naam_geeft_fout():
    project = project_met(pc("laptop van Adelaide"))
    with pytest.raises(ValueError, match="bestaat al"):
        project.toevoegen_component(pc("laptop van Adelaide"))

    assert len(project.componenten) == 1

def test_verschillende_namen_mogen_naast_elkaar_bestaan():
    project = project_met(pc("laptop van Adelaide"))
    project.toevoegen_component(pc("laptop van Adelaide9"))
    
    assert len(project.componenten) == 2

def test_alleen_component_objecten_kunnen_worden_toegevoegd():
    project = project_met()
    with pytest.raises(TypeError):
        project.toevoegen_component("laptop")
