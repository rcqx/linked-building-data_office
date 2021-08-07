# import classes from rdflib 
from rdflib import RDF, RDFS, OWL, Namespace, Graph

# graph object that will contains entities and their relationship
g = Graph()

# define namespaces for building example 
BLDG = Namespace("http://example.com/building#")
g.bind("bldg", BLDG)
BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

# Now we add the instances. we'll start defining VAVs serving 4 of the 5 available zones first. 

#HVAC AHU with VAVs serving rest of zones
g.add((BLDG.AHU, RDF.type, BRICK.Air_Handling_Unit))
g.add((BLDG.VAV_S, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat))
g.add((BLDG.VAV_E, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat))
g.add((BLDG.VAV_W, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat))
g.add((BLDG.VAV_C, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat))
g.add((BLDG.VAV_S_DPR, RDF.type, BRICK.Damper))
g.add((BLDG.VAV_E_DPR, RDF.type, BRICK.Damper))
g.add((BLDG.VAV_W_DPR, RDF.type, BRICK.Damper))
g.add((BLDG.VAV_C_DPR, RDF.type, BRICK.Damper))
g.add((BLDG.VAV_S_DPRPOS, RDF.type, BRICK.Damper_Position_Setpoint))
g.add((BLDG.VAV_E_DPRPOS, RDF.type, BRICK.Damper_Position_Setpoint))
g.add((BLDG.VAV_W_DPRPOS, RDF.type, BRICK.Damper_Position_Setpoint))
g.add((BLDG.VAV_C_DPRPOS, RDF.type, BRICK.Damper_Position_Setpoint))
g.add((BLDG.VAV_S_T, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG.VAV_E_T, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG.VAV_W_T, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG.VAV_C_T, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG.VAV_S_FLOW, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.VAV_E_FLOW, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.VAV_W_FLOW, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.VAV_C_FLOW, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.VAV_S_FSET, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG.VAV_E_FSET, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG.VAV_W_FSET, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG.VAV_C_FSET, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
# hvac zones
g.add((BLDG.ZONE_S, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_E, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_W, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_C, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_N, RDF.type, BRICK.HVAC_zone))
# spaces
g.add((BLDG.office_S, RDF.type, BRICK.Room))
g.add((BLDG.office_E, RDF.type, BRICK.Room))
g.add((BLDG.office_W, RDF.type, BRICK.Room))
g.add((BLDG.office_C, RDF.type, BRICK.Room))
g.add((BLDG.office_N, RDF.type, BRICK.Room))
# thermostats
g.add((BLDG.thermostatS, RDF.type, BRICK.Thermostat))
g.add((BLDG.thermostatE, RDF.type, BRICK.Thermostat))
g.add((BLDG.thermostatW, RDF.type, BRICK.Thermostat))
g.add((BLDG.thermostatC, RDF.type, BRICK.Thermostat))
g.add((BLDG.thermostatN, RDF.type, BRICK.Thermostat))
# relationships for South Zone
g.add((BLDG.AHU, BRICK.feeds, BLDG.VAV_S))
g.add((BLDG.VAV_S, BRICK.feeds, BLDG.ZONE_S))
g.add((BLDG.VAV_S, BRICK.hasPart, BLDG.VAV_S_DPR))
g.add((BLDG.VAV_S_DPR, BRICK.hasPoint, BLDG.VAV_S_DPRPOS))
g.add((BLDG.VAV_S, BRICK.hasPoint, BLDG.VAV_S_FLOW))
g.add((BLDG.VAV_S, BRICK.hasPoint, BLDG.VAV_S_FSET))
g.add((BLDG.ZONE_S, BRICK.hasPart, BLDG.office_S))
g.add((BLDG.ZONE_S, BRICK.hasPart, BLDG.office_S))
g.add((BLDG.ZONE_S, BRICK.isRegulatedBy, BLDG.thermostatS))

with open("building.ttl", "wb") as f:
    f.write(g.serialize(format="ttl"))

# plenum
# g.add(BLDG.Plenum, RDF.type, BRICK.Return_Air_Plenum)

# HVAC unitary system serving North Zone
# g.add(BLDG.HVAC_condenser, RDF.type, BRICK.Condenser)
# g.add(BLDG.HVAC_evaporator, RDF.type, BRICK.FCU)

#Chiller, water loops, tower, boiler
# g.add(BLDG.Chiller, RDF.type, BRICK.Centrifugal_Chiller)
# g.add(BLDG.Tower, RDF.type, BRICK.Cooling_Tower)
# g.add(BLDG.Boiler, RDF.type, BRICK.XXXXXXXX)
# g.add(BLDG.Chilled_loop, RDF.type, BRICK.Water_Distribution)
# g.add(BLDG.Hot_loop, RDF.type, BRICK.Water_Distribution)
 
