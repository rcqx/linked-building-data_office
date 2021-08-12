from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()

BLDG = Namespace("http://example.com/building#")
g.bind("bldg", BLDG)

BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

# classes
# office
g.add((BLDG.Building, RDF.type, BRICK.Building))
# room
g.add((BLDG.office_S, RDF.type, BRICK.Room))
# zone
g.add((BLDG.ZONE_S, RDF.type, BRICK.HVAC_zone))
# thermostats
g.add((BLDG.thermostatS, RDF.type, BRICK.Thermostat))
# humidity sensor
g.add((BLDG.RHSensor_S, RDF.type, BRICK.Zone_Air_Humidity_Sensor))
# database ???

# relationships
g.add((BLDG.Building, BRICK.hasPart, BLDG.office_S))
g.add((BLDG.ZONE_S, BRICK.hasPart, BLDG.office_S))
g.add((BLDG.ZONE_S, BRICK.hasPoint, BLDG.thermostats))
g.add((BLDG.ZONE_S, BRICK.hasPoint, BLDG.RHSensor_S))

with open("HVACZOne.ttl", "wb") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl", encoding='UTF-8'))






