from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()

g.parse("Office.ttl", format="ttl")

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

# How many thermostats?
q3 = """SELECT ?sensors WHERE {
    ?sensors a brick:Thermostat .
}"""
for row in g.query(q3):
    print(row)

# Selecting multiple values
multiple = g.query("""
SELECT DISTINCT ?zn ?ts ?hs WHERE {
    ?zn a brick:HVAC_zone .
    ?zn brick:hasPoint ?ts ;
        brick:hasPoint ?hs .
    ?ts a brick:Thermostat .
    ?hs a brick:Zone_Air_Humidity_Sensor .
}""")
for row in multiple:
    print(row)


