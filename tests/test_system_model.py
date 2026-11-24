from domain.network_project import NetworkProject
from hulp import pc, project_met

def test_statistieken_van_leeg_project_zijn_nul():
    project = NetworkProject("leeg")
    
    assert project.project_statistieken() == {"componenten": 0, "verbindingen": 0, "vlans": 0}

def test_statistieken_tellen_wat_is_toegevoegd():
    project = project_met(pc("a"), pc("b"), verbindingen=[("a", "b")], vlans=[10])

    assert project.project_statistieken() == {"componenten": 2, "verbindingen": 1, "vlans": 1}
