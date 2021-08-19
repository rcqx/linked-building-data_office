from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()

g.parse("compiled-Brick_Office.ttl", format="ttl")

# Discover classes used in model
classes = """SELECT DISTINCT ?class WHERE {
  ?s a ?class .
}
"""
for row in g.query(classes):
    print(row)
    
# how many hvac zones are in the office model?
zones = g.query(
    """SELECT ?zones WHERE {
    ?zones rdf:type brick:HVAC_zone
}""")
for row in zones:
    print(f"{row.zones}")

# How many temperature sensors?
q3 = """SELECT ?ts WHERE {
    ?ts a brick:Temperature_Sensor .
}"""
for row in g.query(q3):
    print(row)

# Selecting multiple values
multiple = g.query("""
SELECT DISTINCT ?zn ?ts ?hs WHERE {
    ?zn a brick:HVAC_zone .
    ?zn brick:hasPoint ?ts ;
        brick:hasPoint ?hs .
    ?ts a brick:Temperature_Sensor .
    ?hs a brick:Zone_Air_Humidity_Sensor .
}""")
for row in multiple:
    print(row)

# Select vavs, respective sensors and serving zone
for vav, zn, sas, set, sat in g.query(
    """SELECT ?vav ?zn ?sas ?set ?sat WHERE {
    ?vav a brick:Variable_Air_Volume_Box_With_Reheat .
    ?vav brick:feeds ?zn .
    ?zn a brick:HVAC_zone .
    ?sas a brick:Supply_Air_Flow_Sensor .
    ?set a brick:Supply_Air_Flow_Setpoint .
    ?sat a brick:Supply_Air_Temperature_Sensor .
}"""
):
    print(vav, zn, sas, set, sat)

# Select offices associated with floor
for floor, room in g.query("""
SELECT ?floor ?room WHERE {
    ?floor a brick:Floor .
    ?floor brick:hasPart ?room .
    ?room a brick:Room .
}
"""):
    print(floor,room) 

for sensor in g.query("""
SELECT ?s WHERE {
    ?s a brick:Sensor .
}
"""):
    print(sensor)

# HVAC systems 
for hvac, parts in g.query("""
SELECT ?hvac ?p WHERE {
    ?hvac a brick:HVAC_System .
    ?hvac brick:hasPart ?p .
    ?p a brick:HVAC_Equipment .
}
"""):
    print(hvac, parts)

# Zones served by HVAC systems 
for nsys  in g.query("""
SELECT ?nsys ?zn WHERE {
    ?nsys a brick:HVAC_System .
    ?nsys brick:feeds ?zn .
    ?zn a brick:HVAC_zone .
}
"""):
    print(nsys)