import pytest
from hulp import pc, project_met

def drie_pcs():
    """test1-test2 UP, test2-test3 DOWN, test1-test3 UP (zoals in het oude script)."""
    
    return project_met(pc("test1"), pc("test2"), pc("test3"),
                       verbindingen=[("test1", "test2"),
("test2", "test3", "DOWN"),
("test1", "test3")])

def test_scheiden_geeft_twee_actieve_en_een_inactieve_verbinding():
    project = drie_pcs()
    actief, inactief = project.scheid_actieve_en_inactieve_verbindingen()

    assert len(actief) == 2
    assert len(inactief) == 1
    assert str(inactief[0]) == "test2 <-> test3 [DOWN]"


def test_status_wijzigen_naar_down_maakt_verbinding_inactief():
    project = drie_pcs()
    verbinding = project.verbindingen[0] # test1-test2, nu UP
    verbinding.wijzig_status("DOWN")
    actief, inactief = project.scheid_actieve_en_inactieve_verbindingen()


    assert verbinding in inactief
    assert len(actief) == 1


def test_wijzig_status_met_ongeldige_waarde_geeft_fout_en_houdt_oude_status():
    verbinding = drie_pcs().verbindingen[0]
    
    with pytest.raises(ValueError):
        verbinding.wijzig_status("AAN")

    assert verbinding.status == "UP"
