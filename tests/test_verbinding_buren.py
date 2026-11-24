import pytest
from hulp import pc, project_met

def vier_pcs():
    """test2 is verbonden met test1 (UP), test3 (DOWN) en test4 (UP)."""
    return project_met(pc("test1"), pc("test2"), pc("test3"), pc("test4"),
                       verbindingen=[("test1", "test2"),
                       ("test2", "test3", "DOWN"),
                       ("test1", "test3"),
                       ("test2", "test4")])

def test_actieve_buren_zijn_test1_en_test4():
    project = vier_pcs()
    buren = project.zoek_actieve_buren_component(project.component_zoeken("test2"))
    
    assert {buur.naam for buur in buren} == {"test1", "test4"}

def test_component_zonder_verbindingen_heeft_geen_buren():
    project = project_met(pc("a"), pc("b"))

    assert project.zoek_actieve_buren_component(project.component_zoeken("a")) == []


def test_buren_van_component_buiten_het_project_geeft_fout():
    project = vier_pcs()
    
    with pytest.raises(ValueError):
            project.zoek_actieve_buren_component(pc("vreemde"))


def test_buren_zoeken_met_een_naam_in_plaats_van_component_geeft_typeerror():
    project = vier_pcs()
    
    with pytest.raises(TypeError):
        project.zoek_actieve_buren_component("test2")