# import classes from rdflib 
from rdflib import RDF, RDFS, OWL, Namespace, Graph

# graph object that will contains entities and their relationship
g = Graph()

# define namespaces for building example 
BLDG = Namespace("http://example.com/building#")
g.bind("bldg", BLDG)
BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

# Now we start adding instances. We now that our building has 5 zones and a HVAC system serving those zones.
# Thus, we´ll defined such components with availables brick classes from the brick ontology

# site
g.add(BLDG.site, RDF.type, BRICK.Site)
# building
g.add(BLDG.office, RDF.type, BRICK.Building)
# storey
g.add(BLDG.storey, RDF.type, BRICK.Storey)
# floor
g.add(BLDG.floor, RDF.type, BRICK.Floor)
# spaces
g.add(BLDG.space1, RDF.type, BRICK.Team_Room)
g.add(BLDG.space2, RDF.type, BRICK.Team_Room)
g.add(BLDG.space3, RDF.type, BRICK.Team_Room)
g.add(BLDG.space4, RDF.type, BRICK.Team_Room)
g.add(BLDG.space5, RDF.type, BRICK.Team_Room)
# hvac zones
g.add(BLDG.ZONE1, RDF.type, BRICK.HVAC_zone)
g.add(BLDG.ZONE2, RDF.type, BRICK.HVAC_zone)
g.add(BLDG.ZONE3, RDF.type, BRICK.HVAC_zone)
g.add(BLDG.ZONE4, RDF.type, BRICK.HVAC_zone)
g.add(BLDG.ZONE5, RDF.type, BRICK.HVAC_zone)
# thermostats
g.add(BLDG.thermostat1, RDF.type, BRICK.Thermostat)
g.add(BLDG.thermostat2, RDF.type, BRICK.Thermostat)
g.add(BLDG.thermostat3, RDF.type, BRICK.Thermostat)
g.add(BLDG.thermostat4, RDF.type, BRICK.Thermostat)
g.add(BLDG.thermostat5, RDF.type, BRICK.Thermostat)
# plenum
g.add(BLDG.Plenum, RDF.type, BRICK.HVAC_zone)

# HVAC unitary system serving North Zone
g.add(BLDG.HVAC_condenser, RDF.type, BRICK.Condenser)
g.add(BLDG.HVAC_evaporator, RDF.type, BRICK.FCU)
#HVAC AHU with VAVs serving rest of zones
g.add(BLDG.AHU, RDF.type, BRICK.Air_Handling_Unit)
g.add(BLDG.VAV_South, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat)
g.add(BLDG.VAV_East, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat)
g.add(BLDG.VAV_West, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat)
g.add(BLDG.VAV_Core, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat)

#Chiller, water loops, tower, boiler
g.add(BLDG.Chiller, RDF.type, BRICK.Centrifugal_Chiller)
g.add(BLDG.Tower, RDF.type, BRICK.Cooling_Tower)
g.add(BLDG.Boiler, RDF.type, BRICK.Centrifugal_Chiller)
g.add(BLDG.Chilled_loop, RDF.type, BRICK.Water_Distribution)
g.add(BLDG.Hot_loop, RDF.type, BRICK.Water_Distribution)


# Boiler
g.add(BLDG.boiler, RDF.type, BRICK.Condensing_Natural_Gas_Boiler)

