import pytest
from hulp import project_met
from domain.vlan import Vlan

def test_verwijderen_van_twee_vlans_laat_de_andere_twee_over():
    project = project_met(vlans=[1, 2, 3, 4])
    project.verwijderen_vlan(project.vlans[0]) #verwijdert VLAN 1
    project.verwijderen_vlan(project.vlans[0]) #nu staat VLAN 2 vooraan
    assert [vlan.nummer for vlan in project.vlans] ==[3, 4]

def test_vlan_nummer_mag_maar_een_keer_voorkomen():
    project = project_met(vlans = [10])
    with pytest.raises(ValueError):
        project.toevoegen_vlan(Vlan(10, "dubbel"))