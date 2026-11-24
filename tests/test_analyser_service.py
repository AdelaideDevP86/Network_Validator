from analysis.analysis_service import analyseer
from hulp import pc, project_met

def test_analyseer_meldt_component_zonder_actieve_verbinding_en_down_verbinding():
    # Voorlopige test: in fase 3 herschrijf je dit bestand.
    project = project_met(pc("test1", ip="192.245.245.254"),
                          pc("test2", ip="192.245.245.253"),
                          pc("test3", ip="192.245.245.255"),
                          verbindingen=[("test1", "test2"),
                          ("test2", "test3", "DOWN")])
    meldingen = analyseer(project)
    
    assert meldingen == ["test3 heeft geen actieve verbinding.",
                        "Verbinding tussen test2 en test3 is DOWN."]
