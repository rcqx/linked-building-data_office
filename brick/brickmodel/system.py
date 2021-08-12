# import classes from rdflib 
from io import StringIO
from rdflib import RDF, RDFS, OWL, Namespace, Graph

# graph object that will contains entities and their relationship
g = Graph()

# define namespaces for building example 
BLDG = Namespace("http://example.com/building#")
g.bind("bldg", BLDG)
BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

# unitary system serving N
# g.add((BLDG.Condenser, RDF.type, BRICK.Condenser))
# g.add((BLDG.FanCoil, RDF.type, BRICK.Fan_Coil_Unit))

#HVAC AHU with VAVs serving 4 of zones
g.add((BLDG.AHU, RDF.type, BRICK.Air_Handling_Unit))
g.add((BLDG.VAV_S, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat))
""" g.add((BLDG.VAV_E, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat))
g.add((BLDG.VAV_W, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat))
g.add((BLDG.VAV_C, RDF.type, BRICK.Variable_Air_Volume_Box_With_Reheat)) """
g.add((BLDG.VAV_S_DPR, RDF.type, BRICK.Damper))
""" g.add((BLDG.VAV_E_DPR, RDF.type, BRICK.Damper))
g.add((BLDG.VAV_W_DPR, RDF.type, BRICK.Damper))
g.add((BLDG.VAV_C_DPR, RDF.type, BRICK.Damper)) """
g.add((BLDG.VAV_S_DPRPOS, RDF.type, BRICK.Damper_Position_Setpoint))
""" g.add((BLDG.VAV_E_DPRPOS, RDF.type, BRICK.Damper_Position_Setpoint))
g.add((BLDG.VAV_W_DPRPOS, RDF.type, BRICK.Damper_Position_Setpoint))
g.add((BLDG.VAV_C_DPRPOS, RDF.type, BRICK.Damper_Position_Setpoint)) """
g.add((BLDG.VAV_S_T, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
""" g.add((BLDG.VAV_E_T, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG.VAV_W_T, RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG.VAV_C_T, RDF.type, BRICK.Supply_Air_Temperature_Sensor)) """
g.add((BLDG.VAV_S_FLOW, RDF.type, BRICK.Supply_Air_Flow_Sensor))
""" g.add((BLDG.VAV_E_FLOW, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.VAV_W_FLOW, RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG.VAV_C_FLOW, RDF.type, BRICK.Supply_Air_Flow_Sensor)) """
g.add((BLDG.VAV_S_FSET, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
""" g.add((BLDG.VAV_E_FSET, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG.VAV_W_FSET, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG.VAV_C_FSET, RDF.type, BRICK.Supply_Air_Flow_Setpoint))
 """
# hvac zones
g.add((BLDG.ZONE_S, RDF.type, BRICK.HVAC_zone))
""" g.add((BLDG.ZONE_E, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_W, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_C, RDF.type, BRICK.HVAC_zone))
g.add((BLDG.ZONE_N, RDF.type, BRICK.HVAC_zone)) """
# rooms
g.add((BLDG.office_S, RDF.type, BRICK.Room))
""" g.add((BLDG.office_E, RDF.type, BRICK.Room))
g.add((BLDG.office_W, RDF.type, BRICK.Room))
g.add((BLDG.office_C, RDF.type, BRICK.Room))
g.add((BLDG.office_N, RDF.type, BRICK.Room)) """
# thermostats
g.add((BLDG.thermostatS, RDF.type, BRICK.Thermostat))
""" g.add((BLDG.thermostatE, RDF.type, BRICK.Thermostat))
g.add((BLDG.thermostatW, RDF.type, BRICK.Thermostat))
g.add((BLDG.thermostatC, RDF.type, BRICK.Thermostat))
g.add((BLDG.thermostatN, RDF.type, BRICK.Thermostat))
"""
# humidity sensor
g.add((BLDG.RHSensor_S, RDF.type, BRICK.Zone_Air_Humidity_Sensor))

# relationships for South Zone
g.add((BLDG.AHU, BRICK.feeds, BLDG.VAV_S))
g.add((BLDG.VAV_S, BRICK.feeds, BLDG.ZONE_S))
g.add((BLDG.VAV_S, BRICK.hasPart, BLDG.VAV_S_DPR))
g.add((BLDG.VAV_S_DPR, BRICK.hasPoint, BLDG.VAV_S_DPRPOS))
g.add((BLDG.VAV_S, BRICK.hasPoint, BLDG.VAV_S_FLOW))
g.add((BLDG.VAV_S, BRICK.hasPoint, BLDG.VAV_S_FSET))
g.add((BLDG.ZONE_S, BRICK.hasPart, BLDG.office_S))
g.add((BLDG.ZONE_S, BRICK.isRegulatedBy, BLDG.thermostatS))

""" # relationships for East Zone
g.add((BLDG.AHU, BRICK.feeds, BLDG.VAV_E))
g.add((BLDG.VAV_E, BRICK.feeds, BLDG.ZONE_E))
g.add((BLDG.VAV_E, BRICK.hasPart, BLDG.VAV_E_DPR))
g.add((BLDG.VAV_E_DPR, BRICK.hasPoint, BLDG.VAV_E_DPRPOS))
g.add((BLDG.VAV_E, BRICK.hasPoint, BLDG.VAV_E_FLOW))
g.add((BLDG.VAV_E, BRICK.hasPoint, BLDG.VAV_E_FSET))
g.add((BLDG.ZONE_E, BRICK.hasPart, BLDG.office_E))
g.add((BLDG.ZONE_E, BRICK.hasPart, BLDG.office_E))
g.add((BLDG.ZONE_E, BRICK.isRegulatedBy, BLDG.thermostatE))
# relationships for West Zone
g.add((BLDG.AHU, BRICK.feeds, BLDG.VAV_W))
g.add((BLDG.VAV_W, BRICK.feeds, BLDG.ZONE_W))
g.add((BLDG.VAV_W, BRICK.hasPart, BLDG.VAV_W_DPR))
g.add((BLDG.VAV_W_DPR, BRICK.hasPoint, BLDG.VAV_W_DPRPOS))
g.add((BLDG.VAV_W, BRICK.hasPoint, BLDG.VAV_W_FLOW))
g.add((BLDG.VAV_W, BRICK.hasPoint, BLDG.VAV_W_FSET))
g.add((BLDG.ZONE_W, BRICK.hasPart, BLDG.office_W))
g.add((BLDG.ZONE_W, BRICK.hasPart, BLDG.office_W))
g.add((BLDG.ZONE_W, BRICK.isRegulatedBy, BLDG.thermostatW))
# relationships for Center Zone
g.add((BLDG.AHU, BRICK.feeds, BLDG.VAV_C))
g.add((BLDG.VAV_C, BRICK.feeds, BLDG.ZONE_C))
g.add((BLDG.VAV_C, BRICK.hasPart, BLDG.VAV_C_DPR))
g.add((BLDG.VAV_C_DPR, BRICK.hasPoint, BLDG.VAV_C_DPRPOS))
g.add((BLDG.VAV_C, BRICK.hasPoint, BLDG.VAV_C_FLOW))
g.add((BLDG.VAV_C, BRICK.hasPoint, BLDG.VAV_C_FSET))
g.add((BLDG.ZONE_C, BRICK.hasPart, BLDG.office_C))
g.add((BLDG.ZONE_C, BRICK.hasPart, BLDG.office_C))
g.add((BLDG.ZONE_C, BRICK.isRegulatedBy, BLDG.thermostatC)) """

""" # unitary system
g.add((BLDG.Condenser, BRICK.isPartOf, BLDG.Fan_Coil_Unit))
 """
with open("example.ttl", "wb") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl", encoding='UTF-8'))


