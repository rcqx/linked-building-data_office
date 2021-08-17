from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()

g.parse("bot-omg-pro.ttl", format="ttl")

# Discover classes used in model
classes = """SELECT DISTINCT ?class WHERE {
  ?s a ?class .
}
"""
for row in g.query(classes):
    print(row)
    
# how many zones are in the bot model?
zones = g.query(
    """SELECT ?zones WHERE {
    ?zones rdf:type bot:Zone
}""")
for row in zones:
    print(f"{row.zones}")

# How many elements?
ele = g.query(
    """SELECT ?e WHERE {
    ?e rdf:type bot:Element
}""")
for row in ele:
    print(row)

# Select site
Site = g.query(""" SELECT ?site WHERE { ?site a bot:Site}""")
for row in Site:
    print(row)

# Multiple selection, elements class objects within each Space/office room
Off_El = g.query("""SELECT ?s ?e  WHERE {
         ?s a bot:Space . 
         ?s bot:hasElement ?e .
         ?e a bot:Element .
}""")

for row in Off_El:
    print(row)

# Fetch building geometry
geometry = g.query("""
SELECT ?b ?g WHERE {
?b a bot:Building .
?b omg:hasGeometry ?g .
?g a omg:Geometry .
}""")
for row in geometry:
    print(row)
