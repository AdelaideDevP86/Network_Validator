from domain.component import Component
from domain.network_project import NetworkProject
from domain.verbinding import Verbinding

pc1 = Component("pc", "test1", )
pc2 = Component("pc", "test2", "waarom hebben we een beschrijving")
pc3 = Component("pc", "test3", "waarom hebben we een beschrijving")

systeem = NetworkProject("systeem van Adelaide")

systeem.toevoegen_component(pc1)
systeem.toevoegen_component(pc2)

systeem.toevoegen_component(pc3)

verbinding1 = Verbinding(pc1, pc2, "UP")
verbinding2 = Verbinding(pc2, pc3, "DOWN")
verbinding3 = Verbinding(pc1, pc3, "UP")

#verbinding1.wijzig_status("DOWN")
systeem.toevoegen_verbinding(verbinding1)
systeem.toevoegen_verbinding(verbinding2)
systeem.toevoegen_verbinding(verbinding3)




print(verbinding1)



# for verbinding in systeem.verbindingen:
#     print(verbinding)
