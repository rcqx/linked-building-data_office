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
g.add((BLDG.office_N_SYS, RDF.type, BRICK.HVAC_System))
g.add((BLDG.Fan_Coil_N, RDF.type, BRICK.Fan_Coil_Unit))
g.add((BLDG.FCU_saf_sensor, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.FCU_set_sensor, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG.FCU_sat_sensor, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG.Condenser, RDF.type, BRICK.Condenser))
g.add((BLDG.office_N_SYS, BRICK.hasPart, BRICK.Fan_Coil_Unit))
g.add((BLDG.office_N_SYS, BRICK.hasPart, BRICK.Condenser))

# System feeding North Zone
g.add((BLDG.office_N_SYS, BRICK.feeds, BLDG.ZONE_N))
g.add((BLDG.Fan_Coil_N, BRICK.feeds, BLDG.ZONE_N))
g.add((BLDG.Fan_Coil_N, BRICK.hasPoint, BLDG.FCU_saf_sensor))
g.add((BLDG.Fan_Coil_N, BRICK.hasPoint, BLDG.FCU_set_sensor))
g.add((BLDG.Fan_Coil_N, BRICK.hasPoint, BLDG.FCU_sat_sensor))

# Plant, AHU, VAVs, DPRs feeding S,E,W and C zones
g.add((BLDG.SEWC_SYS, BRICK.feeds, BLDG.ZONE_S))
g.add((BLDG.SEWC_SYS, BRICK.feeds, BLDG.ZONE_E))
g.add((BLDG.SEWC_SYS, BRICK.feeds, BLDG.ZONE_W))
g.add((BLDG.SEWC_SYS, BRICK.feeds, BLDG.ZONE_C))
g.add((BLDG.SEWC_SYS, RDF.type, BRICK.HVAC_System))
g.add((BLDG["AHU-01"], RDF.type, BRICK.Air_Handling_Unit))
g.add((BLDG["Boiler"], RDF.type, BRICK.Boiler))
g.add((BLDG["Chiller"], RDF.type, BRICK.Chiller))
g.add((BLDG["Tower"], RDF.type, BRICK.Cooling_Tower))

g.add((BLDG["Air-loop"], RDF.type, BRICK.Air_Loop))
g.add((BLDG["Hot-Water-loop"], RDF.type, BRICK.Hot_Water_Loop))
g.add((BLDG["Chilled-Water-loop"], RDF.type, BRICK.Chilled_Water_Loop))

g.add((BLDG.SEWC_SYS, BRICK.hasPart, BLDG["AHU-01"]))
g.add((BLDG.SEWC_SYS, BRICK.hasPart, BLDG["Boiler"]))
g.add((BLDG.SEWC_SYS, BRICK.hasPart, BLDG["Chiller"]))
g.add((BLDG.SEWC_SYS, BRICK.hasPart, BLDG["Tower"]))
g.add((BLDG.SEWC_SYS, BRICK.hasPart, BLDG["Air-loop"]))
g.add((BLDG.SEWC_SYS, BRICK.hasPart, BLDG["Hot-Water-loop"]))
g.add((BLDG.SEWC_SYS, BRICK.hasPart, BLDG["Chilled-Water-loop"]))

g.add((BLDG["VAV-S"], RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat))
g.add((BLDG.VAV_saf_sensor_S, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.VAV_set_sensor_S, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG.VAV_sat_sensor_S, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG["VAV_S_DPR"], RDF.type, BRICK.Damper))
g.add((BLDG["VAV_S_DPRPOS"], RDF.type, BRICK.Damper_Position_Setpoint))

g.add((BLDG["VAV-E"], RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat))
g.add((BLDG.VAV_saf_sensor_E, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.VAV_set_sensor_E, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG.VAV_sat_sensor_E, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG["VAV_E_DPR"], RDF.type, BRICK.Damper))
g.add((BLDG["VAV_E_DPRPOS"], RDF.type, BRICK.Damper_Position_Setpoint))

g.add((BLDG["VAV-W"], RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat))
g.add((BLDG.VAV_saf_sensor_W, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.VAV_set_sensor_W, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG.VAV_sat_sensor_W, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG["VAV_W_DPR"], RDF.type, BRICK.Damper))
g.add((BLDG["VAV_W_DPRPOS"], RDF.type, BRICK.Damper_Position_Setpoint))

g.add((BLDG["VAV-C"], RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat))
g.add((BLDG.VAV_saf_sensor_C, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.VAV_set_sensor_C, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG.VAV_sat_sensor_C, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG["VAV_C_DPR"], RDF.type, BRICK.Damper))
g.add((BLDG["VAV_C_DPRPOS"], RDF.type, BRICK.Damper_Position_Setpoint))

# System feeding South zone
g.add((BLDG["AHU-01"], BRICK.feeds, BLDG["VAV-S"]))
g.add((BLDG["VAV-S"], BRICK.feeds, BLDG.ZONE_S))
g.add((BLDG["VAV-S"], BRICK.hasPart, BLDG["VAV_S_DPR"]))
g.add((BLDG["VAV_S_DPR"], BRICK.hasPoint, BLDG["VAV_S_DPRPOS"]))
g.add((BLDG["VAV-S"], BRICK.hasPoint, BRICK.VAV_saf_sensor_S))
g.add((BLDG["VAV-S"], BRICK.hasPoint, BRICK.VAV_set_sensor_S))
g.add((BLDG["VAV-S"], BRICK.hasPoint, BRICK.VAV_sat_sensor_S))

# System feeding East zone
g.add((BLDG["AHU-01"], BRICK.feeds, BLDG["VAV-E"]))
g.add((BLDG["VAV-E"], BRICK.feeds, BLDG.ZONE_E))
g.add((BLDG["VAV-E"], BRICK.hasPart, BLDG.ZONE_E))
g.add((BLDG["VAV_E_DPR"], BRICK.hasPoint, BLDG["VAV_E_DPRPOS"]))
g.add((BLDG["VAV-E"], BRICK.hasPoint, BRICK.VAV_saf_sensor_E))
g.add((BLDG["VAV-E"], BRICK.hasPoint, BRICK.VAV_set_sensor_E))
g.add((BLDG["VAV-E"], BRICK.hasPoint, BRICK.VAV_sat_sensor_E))

# System feeding West zone
g.add((BLDG["AHU-01"], BRICK.feeds, BLDG["VAV-W"]))
g.add((BLDG["VAV-W"], BRICK.feeds, BLDG.ZONE_W))
g.add((BLDG["VAV-W"], BRICK.hasPart, BLDG.ZONE_W))
g.add((BLDG["VAV_W_DPR"], BRICK.hasPoint, BLDG["VAV_W_DPRPOS"]))
g.add((BLDG["VAV-W"], BRICK.hasPoint, BRICK.VAV_saf_sensor_W))
g.add((BLDG["VAV-W"], BRICK.hasPoint, BRICK.VAV_set_sensor_W))
g.add((BLDG["VAV-W"], BRICK.hasPoint, BRICK.VAV_sat_sensor_W))

# System feeding Core zone
g.add((BLDG["AHU-01"], BRICK.feeds, BLDG["VAV-C"]))
g.add((BLDG["VAV-C"], BRICK.feeds, BLDG.ZONE_C))
g.add((BLDG["VAV-C"], BRICK.hasPart, BLDG.ZONE_C))
g.add((BLDG["VAV_C_DPR"], BRICK.hasPoint, BLDG["VAV_C_DPRPOS"]))
g.add((BLDG["VAV-C"], BRICK.hasPoint, BRICK.VAV_saf_sensor_C))
g.add((BLDG["VAV-C"], BRICK.hasPoint, BRICK.VAV_set_sensor_C))
g.add((BLDG["VAV-C"], BRICK.hasPoint, BRICK.VAV_sat_sensor_C))

with open("Brick_Office.ttl", "wb") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl", encoding='UTF-8'))

