from hulp import pc, project_met

def test_zoeken_geeft_hetzelfde_object_terug():
    laptop = pc("laptop")
    project = project_met(laptop )

    gevonden = project.component_zoeken("laptop")

    assert gevonden is laptop

def test_zoeken_naar_onbekende_naam_geeft_none():
    project = project_met()
    gevonden = project.component_zoeken("ipad")

    assert gevonden is None

