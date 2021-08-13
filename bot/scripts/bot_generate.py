from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()

BLDG = Namespace("http://example.com/building#")
g.bind("bldg", BLDG)

BOT = Namespace("https://w3c-lbd-cg.github.io/bot#")
g.bind("bot", BOT)

# site
g.add((BLDG.Site, RDF.type, BOT.Site))
# building
g.add((BLDG.office_building, RDF.type, BOT.Building))
# story
g.add((BLDG.office, RDF.type, BOT.Storey))
# rooms
g.add((BLDG.office_N, RDF.type, BOT.Space))
g.add((BLDG.office_S, RDF.type, BOT.Space))
g.add((BLDG.office_E, RDF.type, BOT.Space))
g.add((BLDG.office_W, RDF.type, BOT.Space))
g.add((BLDG.office_C, RDF.type, BOT.Space))
# zones
g.add((BLDG.ZONE_N, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_S, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_E, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_W, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_C, RDF.type, BOT.Zone))
# thermostats
g.add((BLDG.thermostatN, RDF.type, BOT.Element))
g.add((BLDG.thermostatS, RDF.type, BOT.Element))
g.add((BLDG.thermostatE, RDF.type, BOT.Element))
g.add((BLDG.thermostatW, RDF.type, BOT.Element))
g.add((BLDG.thermostatC, RDF.type, BOT.Element))
# humidity sensor
g.add((BLDG.RHSensor_N, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_S, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_E, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_W, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_C, RDF.type, BOT.Element))

# Relationships of Building
g.add((BLDG.Site, BOT.hasBuilding, BLDG.office_building))
g.add((BLDG.office_building, BOT.hasStorey, BLDG.office))
# relations for North zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_N))
g.add((BLDG.ZONE_N, BOT.hasSpace, BLDG.office_N))
g.add((BLDG.ZONE_N, BOT.hasElement, BLDG.thermostatN))
g.add((BLDG.ZONE_N, BOT.hasElement, BLDG.RHSensor_N))
# relations for South zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_S))
g.add((BLDG.ZONE_S, BOT.hasSpace, BLDG.office_S))
g.add((BLDG.ZONE_S, BOT.hasElement, BLDG.thermostatS))
g.add((BLDG.ZONE_S, BOT.hasElement, BLDG.RHSensor_S))
# relations for East zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_E))
g.add((BLDG.ZONE_E, BOT.hasSpace, BLDG.office_E))
g.add((BLDG.ZONE_E, BOT.hasElement, BLDG.thermostatE))
g.add((BLDG.ZONE_E, BOT.hasElement, BLDG.RHSensor_E))
# relations for West zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_W))
g.add((BLDG.ZONE_W, BOT.hasSpace, BLDG.office_W))
g.add((BLDG.ZONE_W, BOT.hasElement, BLDG.thermostatW))
g.add((BLDG.ZONE_W, BOT.hasElement, BLDG.RHSensor_W))
# relations for Core zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_C))
g.add((BLDG.ZONE_C, BOT.hasSpace, BLDG.office_C))
g.add((BLDG.ZONE_C, BOT.hasElement, BLDG.thermostatC))
g.add((BLDG.ZONE_C, BOT.hasElement, BLDG.RHSensor_C))

# adjacent zones for N
g.add((BLDG.office_N, BOT.adjacentZone, BLDG.office_E))
g.add((BLDG.office_N, BOT.adjacentZone, BLDG.office_W))
# adjacent zones for S
g.add((BLDG.office_S, BOT.adjacentZone, BLDG.office_E))
g.add((BLDG.office_S, BOT.adjacentZone, BLDG.office_W))
# adjacent zones for W
g.add((BLDG.office_W, BOT.adjacentZone, BLDG.office_N))
g.add((BLDG.office_W, BOT.adjacentZone, BLDG.office_S))
# adjacent zones for E
g.add((BLDG.office_E, BOT.adjacentZone, BLDG.office_N))
g.add((BLDG.office_E, BOT.adjacentZone, BLDG.office_S))
# adjacent zones for C
g.add((BLDG.office_C, BOT.adjacentZone, BLDG.office_N))
g.add((BLDG.office_C, BOT.adjacentZone, BLDG.office_S))
g.add((BLDG.office_C, BOT.adjacentZone, BLDG.office_E))
g.add((BLDG.office_C, BOT.adjacentZone, BLDG.office_W))

with open("bot_Office.ttl", "wb") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl", encoding='UTF-8'))