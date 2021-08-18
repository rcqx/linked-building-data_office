from rdflib import RDF, RDFS, OWL, Namespace, Graph
from rdflib import Literal
from rdflib.term import BNode

g = Graph()

UNIT = Namespace("http://qudt.org/vocab/unit/")
g.bind("unit", UNIT)
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
BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

# site
g.add((BLDG.Site, RDF.type, BOT.Site))
g.add((BLDG.Site, RDF.type, BRICK.Site))
# building
g.add((BLDG.office_building, RDF.type, BOT.Zone))
g.add((BLDG.office_building, RDF.type, BRICK.Building))
# story
g.add((BLDG.office, RDF.type, BOT.Storey))
g.add((BLDG.office, RDF.type, BRICK.Floor))
# rooms
g.add((BLDG.office_N, RDF.type, BOT.Space))
g.add((BLDG.office_N, RDF.type, BRICK.Room))
g.add((BLDG.office_S, RDF.type, BOT.Space))
g.add((BLDG.office_S, RDF.type, BRICK.Room))
g.add((BLDG.office_E, RDF.type, BOT.Space))
g.add((BLDG.office_E, RDF.type, BRICK.Room))
g.add((BLDG.office_W, RDF.type, BOT.Space))
g.add((BLDG.office_W, RDF.type, BRICK.Room))
g.add((BLDG.office_C, RDF.type, BOT.Space))
g.add((BLDG.office_C, RDF.type, BRICK.Room))
# zones
g.add((BLDG.ZONE_N, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_N, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_S, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_S, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_E, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_E, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_W, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_W, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_C, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_C, RDF.type, BRICK.HVAC_zone))
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

# temperature sensor
g.add((BLDG.temp_sensor_N, RDF.type, BOT.Element))
g.add((BLDG.temp_sensor_N, RDF.type, PRODUCT.Product))
g.add((BLDG.temp_sensor_N, RDF.type, BPO.Product))
g.add((BLDG.temp_sensor_N, RDF.type, BRICK.Temperature_Sensor))
g.add((BLDG.temp_sensor_N, BRICK.hasUnit, UNIT.DEG_C))

g.add((BLDG.temp_sensor_S, RDF.type, BOT.Element))
g.add((BLDG.temp_sensor_S, RDF.type, PRODUCT.Product))
g.add((BLDG.temp_sensor_S, RDF.type, BPO.Product))
g.add((BLDG.temp_sensor_S, RDF.type, BRICK.Temperature_Sensor))
g.add((BLDG.temp_sensor_S, BRICK.hasUnit, UNIT.DEG_C))


g.add((BLDG.temp_sensor_E, RDF.type, BOT.Element))
g.add((BLDG.temp_sensor_E, RDF.type, PRODUCT.Product))
g.add((BLDG.temp_sensor_E, RDF.type, BPO.Product))
g.add((BLDG.temp_sensor_E, RDF.type, BRICK.Temperature_Sensor))
g.add((BLDG.temp_sensor_E, BRICK.hasUnit, UNIT.DEG_C))

g.add((BLDG.temp_sensor_W, RDF.type, BOT.Element))
g.add((BLDG.temp_sensor_W, RDF.type, PRODUCT.Product))
g.add((BLDG.temp_sensor_W, RDF.type, BPO.Product))
g.add((BLDG.temp_sensor_W, RDF.type, BRICK.Temperature_Sensor))
g.add((BLDG.temp_sensor_W, BRICK.hasUnit, UNIT.DEG_C))

g.add((BLDG.temp_sensor_C, RDF.type, BOT.Element))
g.add((BLDG.temp_sensor_C, RDF.type, PRODUCT.Product))
g.add((BLDG.temp_sensor_C, RDF.type, BPO.Product))
g.add((BLDG.temp_sensor_C, RDF.type, BRICK.Temperature_Sensor))
g.add((BLDG.temp_sensor_C, BRICK.hasUnit, UNIT.DEG_C))

# humidity sensors
g.add((BLDG.RHSensor_N, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_N, RDF.type, PRODUCT.Product))
g.add((BLDG.RHSensor_N, RDF.type, BPO.Product))
g.add((BLDG.RHSensor_N, RDF.type, BRICK.Zone_Air_Humidity_Sensor))

g.add((BLDG.RHSensor_S, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_S, RDF.type, PRODUCT.Product))
g.add((BLDG.RHSensor_S, RDF.type, BPO.Product))
g.add((BLDG.RHSensor_S, RDF.type, BRICK.Zone_Air_Humidity_Sensor))

g.add((BLDG.RHSensor_E, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_E, RDF.type, PRODUCT.Product))
g.add((BLDG.RHSensor_E, RDF.type, BPO.Product))
g.add((BLDG.RHSensor_E, RDF.type, BRICK.Zone_Air_Humidity_Sensor))

g.add((BLDG.RHSensor_W, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_W, RDF.type, PRODUCT.Product))
g.add((BLDG.RHSensor_W, RDF.type, BPO.Product))
g.add((BLDG.RHSensor_W, RDF.type, BRICK.Zone_Air_Humidity_Sensor))

g.add((BLDG.RHSensor_C, RDF.type, BOT.Element))
g.add((BLDG.RHSensor_C, RDF.type, PRODUCT.Product))
g.add((BLDG.RHSensor_C, RDF.type, BPO.Product))
g.add((BLDG.RHSensor_C, RDF.type, BRICK.Zone_Air_Humidity_Sensor))

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
g.add((BLDG.ZONE_S, BOT.hasElement, BLDG.temp_sensor_N))
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
g.add((BLDG.ZONE_E, BOT.hasElement, BLDG.temp_sensor_E))
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
g.add((BLDG.ZONE_W, BOT.hasElement, BLDG.temp_sensor_W))
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
g.add((BLDG.ZONE_C, BOT.hasElement, BLDG.temp_sensor_C))
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

# Points
g.add((BLDG.office_N, BRICK.hasPoint, BLDG.RHSensor_N))
g.add((BLDG.office_N, BRICK.hasPoint, BLDG.temp_sensor_N))

g.add((BLDG.office_S, BRICK.hasPoint, BLDG.RHSensor_S))
g.add((BLDG.office_S, BRICK.hasPoint, BLDG.temp_sensor_S))

g.add((BLDG.office_E, BRICK.hasPoint, BLDG.RHSensor_E))
g.add((BLDG.office_E, BRICK.hasPoint, BLDG.temp_sensor_E))

g.add((BLDG.office_W, BRICK.hasPoint, BLDG.RHSensor_W))
g.add((BLDG.office_W, BRICK.hasPoint, BLDG.RHSensor_W)) 

# GEOMETRY
g.add((BLDG.BuildingGeometry, OMG.hasSimpleGeometryDescription, XSD.string))

# timeseries 
N_ts_id = BNode()
g.add((N_ts_id, BRICK.hasTimeseriesId, Literal("987f8342-f917-46c1-a0e7-8402e0fe8ebe")))
g.add((BLDG.temp_sensor_N, BRICK.timeseries, N_ts_id))
S_ts_id = BNode()
g.add((S_ts_id, BRICK.hasTimeseriesId, Literal("00f92284-53d8-44b5-8dc2-ea0cae6c4776")))
g.add((BLDG.temp_sensor_S, BRICK.timeseries, S_ts_id))
E_ts_id = BNode()
g.add((E_ts_id, BRICK.hasTimeseriesId, Literal("cc97ea6b-f879-4be5-a375-ac6bc128a0c0")))
g.add((BLDG.temp_sensor_E, BRICK.timeseries, E_ts_id))
W_ts_id = BNode()
g.add((W_ts_id, BRICK.hasTimeseriesId, Literal("679bb09c-0f15-4392-bf0b-9201c966c5c5")))
g.add((BLDG.temp_sensor_W, BRICK.timeseries, W_ts_id))

g.serialize("brick-bot-omg-pro2.ttl", format="ttl")