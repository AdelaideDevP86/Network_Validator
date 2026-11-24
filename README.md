# Network Validator
 
Controleert een netwerkontwerp op fouten **voordat** het netwerk wordt gebouwd.
 
Een netwerkbeheerder beschrijft het ontwerp (componenten, IP-configuratie, VLAN's en verbindingen) en de tool meldt
wat er mis is: dubbele IP-adressen, een gateway buiten het subnet, overlappende subnetten, apparaten zonder actieve
verbinding. Fouten die je op papier vindt, hoef je niet later in een serverruimte op te sporen.
 
> **Status: in ontwikkeling.** Het domeinmodel en de eerste controles werken en zijn getest. Inlezen uit JSON en de
> opdrachtregel-tool volgen. Zie [ROADMAP.md](ROADMAP.md) voor de planning naar versie 1.0.
 
## Wat het nu kan
 
- Een netwerkproject opbouwen met componenten, VLAN's en verbindingen (UP of DOWN).
- Invoer valideren: IPv4-adressen (met de standaardmodule `ipaddress`), prefix (0–32) en VLAN-nummer (1–4094).
  Ongeldige invoer wordt geweigerd met een duidelijke foutmelding.
- Projectregels afdwingen: unieke componentnamen, geen dubbele verbindingen, een VLAN dat in gebruik is kan niet
  worden verwijderd. Bij het verwijderen van een component verdwijnen ook zijn verbindingen.
- Een ontwerp analyseren op dubbele IP-adressen, componenten zonder actieve verbinding en verbindingen die DOWN staan.
## Controles
 
| Regel  | Controle                                   | Status                |
|--------|--------------------------------------------|-----------------------|
| NV-001 | Dubbel IP-adres                            | basisversie aanwezig  |
| NV-002 | Netwerk- of broadcastadres als host-IP     | gepland               |
| NV-003 | Gateway buiten het subnet                  | gepland               |
| NV-004 | Overlappende subnetten                     | gepland               |
| NV-005 | Onvolledige IP-configuratie                | deels (ontbrekend IP) |
| NV-006 | Verwijzing naar onbekend VLAN              | gepland               |
| NV-007 | Component zonder actieve verbinding        | basisversie aanwezig  |
| NV-008 | Verbinding die DOWN staat                  | basisversie aanwezig  |
 
## Voorbeeld
 
Zolang de opdrachtregel-tool er nog niet is, gebruik je het model vanuit Python:
 
```python
from domain.component import Component
from domain.network_project import NetworkProject
from domain.verbinding import Verbinding
from analysis.analysis_service import analyseer
 
project = NetworkProject("kantoor")
router = Component("router", "router-01", ip_adres="192.168.10.1", prefix=24)
pc1 = Component("pc", "pc-01", ip_adres="192.168.10.20", prefix=24, gateway="192.168.10.1")
pc2 = Component("pc", "pc-02", ip_adres="192.168.10.20", prefix=24, gateway="192.168.10.1")
for component in (router, pc1, pc2):
    project.toevoegen_component(component)
project.toevoegen_verbinding(Verbinding(router, pc1))
project.toevoegen_verbinding(Verbinding(router, pc2, "DOWN"))
 
for melding in analyseer(project):
    print(melding)
```
 
Uitvoer:
 
```text
pc-02 heeft geen actieve verbinding.
Verbinding tussen router-01 en pc-02 is DOWN.
pc-01 en pc-02 gebruiken hetzelfde IP-adres.
```
 
## Installeren en testen
 
Vereist Python 3.10 of hoger. De kern gebruikt alleen de standaardbibliotheek; pytest is alleen nodig om te testen.
 
```bash
git clone https://github.com/AdelaideDevP86/Network_Simulator.git
cd Network_Simulator
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
python -m pytest
```
 
De instellingen voor pytest staan in `pyproject.toml`.
 
## Opbouw
 
```text
domain/        Component, Vlan, Verbinding en NetworkProject: het model en zijn regels
validators/    Controle van losse waarden (IPv4, prefix, VLAN, naam)
analysis/      Controles op het ontwerp als geheel
tests/         pytest-tests; hulp.py bevat hulpfuncties om snel een testproject te bouwen
```
 
Afhankelijkheden lopen in één richting: `analysis` gebruikt `domain`, en `domain` gebruikt alleen `validators`. Het
model is bedoeld om alleen waarden terug te geven en het tonen over te laten aan de laag erboven, zodat het los te testen is en later bruikbaar
is vanuit een opdrachtregel-tool of een grafische interface.
 
## Op weg naar versie 1.0
 
1. Domeinmodel repareren en volledig testen
2. Een ontwerp inlezen uit JSON (`voorbeelden/kantoor.json`)
3. Alle acht controles als `Melding` met regel-ID en ernst (FOUT of WAARSCHUWING)
4. Opdrachtregel-tool: `python main.py voorbeelden/kantoor.json`
5. Automatisch testen met GitHub Actions en release v1.0
## Over dit project
 
Persoonlijk portfolioproject naast mijn HBO-ICT-opleiding (software development). Ik combineer hiermee mijn
achtergrond in elektrotechniek met softwareontwikkeling: de regels komen uit de praktijk van netwerkontwerp, de
nadruk ligt op een helder domeinmodel, invoervalidatie en tests.
 
