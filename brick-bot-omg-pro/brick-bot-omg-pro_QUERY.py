from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()
g.parse("./brick-bot-omg-pro.ttl", format="ttl")

sensors = g.query(
    """SELECT ?sensor WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Air_Temperature_Sensor
}
""")

print(sensors)