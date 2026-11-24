from domain.component import Component
from domain.network_project import NetworkProject
from domain.verbinding import Verbinding
from domain.vlan import Vlan

def pc(naam, ip=None, prefix=None, gateway=None, vlan=None):
    """Maakt snel een component van type pc"""
    return Component("pc", naam, ip_adres=ip, prefix=prefix, gateway=gateway, vlan=vlan)

def project_met(*componenten, verbindingen = (), vlans=()):
    """Bouwt klein project.
    
    verbindingen: tuples (naam_a, naam_b) of (naam_a, naam_b, status)
    vlans: VLAN-nummers; de naam wordt vlan10 enzovoort.
    """
    project = NetworkProject("test")
    for nummer in vlans: 
        project.toevoegen_vlan(Vlan(nummer, f"vlan{nummer}"))
    for component in componenten:
        project.toevoegen_component(component)
    for a, b, *status in verbindingen:
        project.toevoegen_verbinding(Verbinding(project.component_zoeken(a),
                                                project.component_zoeken(b), *status))
    return project