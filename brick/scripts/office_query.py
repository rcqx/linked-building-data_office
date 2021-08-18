from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()

g.parse("Brick_Office.ttl", format="ttl")

# # Discover classes used in model
# classes = """SELECT DISTINCT ?class WHERE {
#   ?s a ?class .
# }
# """
# for row in g.query(classes):
#     print(row)
    
# # how many hvac zones are in the office model?
# zones = g.query(
#     """SELECT ?zones WHERE {
#     ?zones rdf:type brick:HVAC_zone
# }""")
# for row in zones:
#     print(f"{row.zones}")

# # How many temperature sensors?
# q3 = """SELECT ?ts WHERE {
#     ?ts a brick:Temperature_Sensor .
# }"""
# for row in g.query(q3):
#     print(row)

# # Selecting multiple values
# multiple = g.query("""
# SELECT DISTINCT ?zn ?ts ?hs WHERE {
#     ?zn a brick:HVAC_zone .
#     ?zn brick:hasPoint ?ts ;
#         brick:hasPoint ?hs .
#     ?ts a brick:Temperature_Sensor .
#     ?hs a brick:Zone_Air_Humidity_Sensor .
# }""")
# for row in multiple:
#     print(row)

# Select system serving each zone
office_N = g.query("""
SELECT ?fcu ?zn ?ts WHERE {
    ?fcu a brick:Fan_Coil_Unit .
    ?fcu brick:feeds ?zn .
    ?fcu brick:hasPoint ?ts .
    ?zn a brick:HVAC_zone .
    ?ts a brick:Supply_Air_Temperature_Sensor .
    }""")

for row in office_N:
    print(row)

