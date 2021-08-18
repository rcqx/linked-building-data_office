from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()

BLDG = Namespace("http://example.com/building#")
g.bind("bldg", BLDG)

BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

# site
g.add((BLDG.Site, RDF.type, BRICK.Site))
# building
g.add((BLDG.office_building, RDF.type, BRICK.Building))
# story
g.add((BLDG.office, RDF.type, BRICK.Floor))
# rooms
g.add((BLDG.office_N, RDF.type, BRICK.Room))
g.add((BLDG.office_S, RDF.type, BRICK.Room))
g.add((BLDG.office_E, RDF.type, BRICK.Room))
g.add((BLDG.office_W, RDF.type, BRICK.Room))
g.add((BLDG.office_C, RDF.type, BRICK.Room))
# zones
g.add((BLDG.ZONE_N, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_S, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_E, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_W, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_C, RDF.type, BRICK.HVAC_zone))
# temperature sensor
g.add((BLDG.temp_sensor_N, RDF.type, BRICK.Temperature_Sensor))
g.add((BLDG.temp_sensor_S, RDF.type, BRICK.Temperature_Sensor))
g.add((BLDG.temp_sensor_E, RDF.type, BRICK.Temperature_Sensor))
g.add((BLDG.temp_sensor_W, RDF.type, BRICK.Temperature_Sensor))
g.add((BLDG.temp_sensor_C, RDF.type, BRICK.Temperature_Sensor))
# humidity sensor
g.add((BLDG.RHSensor_N, RDF.type, BRICK.Zone_Air_Humidity_Sensor))
g.add((BLDG.RHSensor_S, RDF.type, BRICK.Zone_Air_Humidity_Sensor))
g.add((BLDG.RHSensor_E, RDF.type, BRICK.Zone_Air_Humidity_Sensor))
g.add((BLDG.RHSensor_W, RDF.type, BRICK.Zone_Air_Humidity_Sensor))
g.add((BLDG.RHSensor_C, RDF.type, BRICK.Zone_Air_Humidity_Sensor))

# relationships of Building
g.add((BLDG.office_building, BRICK.hasLocation, BLDG.Site))
g.add((BLDG.office, BRICK.hasLocation, BLDG.office_building))

# relations for North zone
g.add((BLDG.office, BRICK.hasPart, BLDG.office_N))
g.add((BLDG.ZONE_N, BRICK.hasPart, BLDG.office_N))
g.add((BLDG.ZONE_N, BRICK.hasPoint, BLDG.temp_sensor_N))
g.add((BLDG.ZONE_N, BRICK.hasPoint, BLDG.RHSensor_N))
# relations for south zone
g.add((BLDG.office, BRICK.hasPart, BLDG.office_S))
g.add((BLDG.ZONE_S, BRICK.hasPart, BLDG.office_S))
g.add((BLDG.ZONE_S, BRICK.hasPoint, BLDG.temp_sensor_S))
g.add((BLDG.ZONE_S, BRICK.hasPoint, BLDG.RHSensor_S))
# relations for East zone
g.add((BLDG.office, BRICK.hasPart, BLDG.office_E))
g.add((BLDG.ZONE_E, BRICK.hasPart, BLDG.office_E))
g.add((BLDG.ZONE_E, BRICK.hasPoint, BLDG.temp_sensor_E))
g.add((BLDG.ZONE_E, BRICK.hasPoint, BLDG.RHSensor_E))
# relations for West zone
g.add((BLDG.office, BRICK.hasPart, BLDG.office_W))
g.add((BLDG.ZONE_W, BRICK.hasPart, BLDG.office_W))
g.add((BLDG.ZONE_W, BRICK.hasPoint, BLDG.temp_sensor_W))
g.add((BLDG.ZONE_W, BRICK.hasPoint, BLDG.RHSensor_W))
# relations for Core zone
g.add((BLDG.office, BRICK.hasPart, BLDG.office_C))
g.add((BLDG.ZONE_C, BRICK.hasPart, BLDG.office_C))
g.add((BLDG.ZONE_C, BRICK.hasPoint, BLDG.temp_sensor_C))
g.add((BLDG.ZONE_C, BRICK.hasPoint, BLDG.RHSensor_C))

# HVAC entities
# Unitary system with Dx cooling and gas heating serving a north office
g.add((BLDG.Fan_Coil_N, RDF.type, BRICK.Fan_Coil_Unit))
g.add((BLDG.FCU_saf_sensor, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.FCU_set_sensor, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG.FCU_sat_sensor, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG.Condenser, RDF.type, BRICK.Condenser))
g.add((BLDG.office_N_SYS, BRICK.hasPart, BRICK.Fan_Coil_Unit))
g.add((BLDG.office_N_SYS, BRICK.hasPart, BRICK.Condenser))

# System service North Zone
g.add((BLDG.Fan_Coil_N, BRICK.feeds, BLDG.ZONE_N))
g.add((BLDG.Fan_Coil_N, BRICK.hasPoint, BLDG.FCU_saf_sensor))
g.add((BLDG.Fan_Coil_N, BRICK.hasPoint, BLDG.FCU_set_sensor))
g.add((BLDG.Fan_Coil_N, BRICK.hasPoint, BLDG.FCU_sat_sensor))

with open("Brick_Office.ttl", "wb") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl", encoding='UTF-8'))





