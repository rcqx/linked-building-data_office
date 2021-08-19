from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()

XSD = Namespace("http://www.w3.org/2001/XMLSchema")
g.bind("xsd", XSD)
BLDG = Namespace("http://example.com/building#")
g.bind("bldg", BLDG)
BOT = Namespace("https://w3c-lbd-cg.github.io/bot#")
g.bind("bot", BOT)
BPO = Namespace("https://www.projekt-scope.de/ontologies/bpo/")
g.bind("bpo", BPO)
OMG = Namespace("https://www.projekt-scope.de/ontologies/omg/")
g.bind("omg", OMG)
PRODUCT = Namespace("https://w3id.org/product#")
g.bind("product", PRODUCT)
BPO = Namespace("https://w3id.org/bpo")
g.bind("bpo", BPO)

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
# window
g.add((BLDG.window, RDF.type, BOT.Element))
g.add((BLDG.window, RDF.type, PRODUCT.Product))
g.add((BLDG.window, RDF.type, BPO.Product))
# glassdoor
g.add((BLDG.glassdoor, RDF.type, BOT.Element))
g.add((BLDG.glassdoor, RDF.type, PRODUCT.Product))
g.add((BLDG.glassdoor, RDF.type, BPO.Product))
# wall
g.add((BLDG.wall, RDF.type, BOT.Element))
# ceiling
g.add((BLDG.ceiling, RDF.type, BOT.ceiling))
# thermostats
g.add((BLDG.thermostatN, RDF.type, BOT.Element))
g.add((BLDG.thermostatN, RDF.type, PRODUCT.Product))
g.add((BLDG.thermostatN, RDF.type, BPO.Product))

g.add((BLDG.thermostatS, RDF.type, BOT.Element))
g.add((BLDG.thermostatS, RDF.type, PRODUCT.Product))
g.add((BLDG.thermostatS, RDF.type, BPO.Product))

g.add((BLDG.thermostatE, RDF.type, BOT.Element))
g.add((BLDG.thermostatE, RDF.type, PRODUCT.Product))
g.add((BLDG.thermostatE, RDF.type, BPO.Product))

g.add((BLDG.thermostatW, RDF.type, BOT.Element))
g.add((BLDG.thermostatW, RDF.type, PRODUCT.Product))
g.add((BLDG.thermostatW, RDF.type, BPO.Product))

g.add((BLDG.thermostatC, RDF.type, BOT.Element))
g.add((BLDG.thermostatC, RDF.type, PRODUCT.Product))
g.add((BLDG.thermostatC, RDF.type, BPO.Product))

# humidity sensor
g.add((BLDG.RHSensor_N, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_N, RDF.type, PRODUCT.Product))
g.add((BLDG.RHSensor_N, RDF.type, BPO.Product))

g.add((BLDG.RHSensor_S, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_S, RDF.type, PRODUCT.Product))
g.add((BLDG.RHSensor_S, RDF.type, BPO.Product))

g.add((BLDG.RHSensor_E, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_E, RDF.type, PRODUCT.Product))
g.add((BLDG.RHSensor_E, RDF.type, BPO.Product))

g.add((BLDG.RHSensor_W, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_W, RDF.type, PRODUCT.Product))
g.add((BLDG.RHSensor_W, RDF.type, BPO.Product))

g.add((BLDG.RHSensor_C, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_C, RDF.type, PRODUCT.Product))
g.add((BLDG.RHSensor_C, RDF.type, BPO.Product))

# geometry
g.add((BLDG.BuildingGeometry, RDF.type, OMG.Geometry))

# RELATIONSHIPS
# Relationships of Building
g.add((BLDG.Site, BOT.hasBuilding, BLDG.office_building))
g.add((BLDG.office_building, BOT.hasStorey, BLDG.office))
# relations for North zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_N))
g.add((BLDG.ZONE_N, BOT.hasSpace, BLDG.office_N))
g.add((BLDG.ZONE_N, BOT.hasElement, BLDG.thermostatN))
g.add((BLDG.ZONE_N, BOT.hasElement, BLDG.RHSensor_N))
g.add((BLDG.office_N, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_N, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_N, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_N, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_N, BOT.hasElement, BLDG.ceiling))
g.add((BLDG.office_N, BOT.hasElement, BLDG.glassdoor))
g.add((BLDG.office_N, BOT.hasElement, BLDG.window))
# relations for South zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_S))
g.add((BLDG.ZONE_S, BOT.hasSpace, BLDG.office_S))
g.add((BLDG.ZONE_S, BOT.hasElement, BLDG.thermostatS))
g.add((BLDG.ZONE_S, BOT.hasElement, BLDG.RHSensor_S))
g.add((BLDG.office_S, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_S, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_S, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_S, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_S, BOT.hasElement, BLDG.ceiling))
g.add((BLDG.office_S, BOT.hasElement, BLDG.glassdoor))
g.add((BLDG.office_S, BOT.hasElement, BLDG.window))
# relations for East zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_E))
g.add((BLDG.ZONE_E, BOT.hasSpace, BLDG.office_E))
g.add((BLDG.ZONE_E, BOT.hasElement, BLDG.thermostatE))
g.add((BLDG.ZONE_E, BOT.hasElement, BLDG.RHSensor_E))
g.add((BLDG.office_E, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_E, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_E, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_E, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_E, BOT.hasElement, BLDG.ceiling))
g.add((BLDG.office_E, BOT.hasElement, BLDG.window))
# relations for West zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_W))
g.add((BLDG.ZONE_W, BOT.hasSpace, BLDG.office_W))
g.add((BLDG.ZONE_W, BOT.hasElement, BLDG.thermostatW))
g.add((BLDG.ZONE_W, BOT.hasElement, BLDG.RHSensor_W))
g.add((BLDG.office_W, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_W, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_W, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_W, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_W, BOT.hasElement, BLDG.ceiling))
g.add((BLDG.office_W, BOT.hasElement, BLDG.window))
# relations for Core zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_C))
g.add((BLDG.ZONE_C, BOT.hasSpace, BLDG.office_C))
g.add((BLDG.ZONE_C, BOT.hasElement, BLDG.thermostatC))
g.add((BLDG.ZONE_C, BOT.hasElement, BLDG.RHSensor_C))
g.add((BLDG.office_C, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_C, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_C, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_C, BOT.hasElement, BLDG.wall))
g.add((BLDG.office_C, BOT.hasElement, BLDG.ceiling))
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

# GEOMETRY
g.add((BLDG.office_building, OMG.hasGeometry, BLDG.BuildingGeometry))


with open("bot-omg-pro.ttl", "wb") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl", encoding='UTF-8'))