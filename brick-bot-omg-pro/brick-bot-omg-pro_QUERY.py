from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()
g.parse("./brick-bot-omg-pro.ttl", format="ttl")

# semantic model with sensors linked to virtual zones

# # Query 1, retrieve temperature sensors
# sensors = g.query(
#     """SELECT ?sensor WHERE {
#     ?sensor a brick:Thermostat .
# }
# """)
# for row in sensors:
#     print(row)

# # Query 2, retrieve humidity sensors 
# hum_sen = g.query(
#     """SELECT ?hs WHERE {
#     ?hs a brick:Zone_Air_Humidity_Sensor .
# }"""
# )
# for row in hum_sen:
#     print(row)

# # Query 3, retrieve brick zones (physical) and their bot (virtual) representation
# zones = g.query(
#     """SELECT ?brick ?bot WHERE{
#     ?brick a brick:HVAC_zone .
#     ?bot a bot:Zone .
#     }
#     """
# )
# for row in zones:
#     print(row)

# # Query4, lets fetch the associated sensors with each virtual office rooms
# office_sen = g.query("""
# SELECT ?of ?hs ?ts WHERE{
#     ?of a bot:Space .
#     ?of brick:hasPoint ?hs .
#     ?hs a brick:Zone_Air_Humidity_Sensor .
#     ?ts a brick:Temperature_Sensor .
# }"""
# )
# for row in office_sen:
#     print(row)

# Query 5, retrieve universally unique identifier (UUID) associated with temperature sensor: 
ts_unit = g.query("""
SELECT ?ts ?u WHERE {
    ?ts a brick:Temperature_Sensor .
    ?ts brick:hasUnit ?u .
}""")
for row in ts_unit:
    print(row)