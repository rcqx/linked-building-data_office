# AECO-ontologies / vocabularies

With AECO industry migrating from documents to model-based data-rich
approaches, there is an increasing  need to standardise how AECO data is
produced, stored and exchanged among parties during different stages 
of a building development. Furthermore, as each stakeholder utilise
field-related tools suites for outputting custom data structures -suited to their
respective areas-, information heterogeinity increases with every project 
iteration. 

To address this, researchers have envisioned distributed and interdisciplinary 
environments where information is exchanged among stakeholders thru web-apps.
As a result, the adoption of semantic web technologies (SWT) to generate 
linked-data building models over the web is being identified as a promising path
to increase data interoperability in the AECO industry.

The following examples showcase some of the current efforts of the open-source 
community to address the aforementioned problematic. Hence, by implementing 
semantic models, standarisation of the physical, 
logical and virtual assets and the relationships between them can be accomplish 
thru building information models instantiated by semantic-web 
ontologies/vocabularies.

The tested semantic schemas are:
1. [Brick](https://brickschema.org); a semantic schema seeking an efficient deployment of building
analytics apps thru the creation, implementation  and querying of integrated 
semantic models.

2. [BOT](https://w3c-lbd-cg.github.io/bot); a minimal ontology to describe anything in the context of a building 
and to the components (products) that comform them. According to the the BOT 
draft report, _"The Building Topology Ontology (BOT) is a minimal OWL DL
ontology for defining relationships between the sub-components of a building. 
It was suggested as an extensible baseline for use along with more domain 
specific ontologies following general W3C principles of encouraging reuse and 
keeping the schema no more complex than necessary."_ 

3. [DigitalBuildings](https://google.github.io/digitalbuildings); an ontology divised by Google, following the steps of brick 
and haystack, according to google: _"The Digital Buildings project originated 
from the need to manage a very large, heterogeneous building portfolio in a 
scalable way. The project aims to enable management applications/analyses that 
are trivially portable between buildings. This goal is achieved through a 
combination of semantically-expressive abstract modeling, an easy-to-use 
configuration language, and robust validation tooling"_  

![semantic-web](https://smiy.files.wordpress.com/2011/01/sw_layercake.png)

# A single zone building in San Francisco, California

Examples describe an office located in San Francisco, information regarding the 
building components are based on case 640 from ASHRAE 140 std, which describes a 
rectangular low mass single zone, where heating and cooling temperature is 
controlled with a thermostat thru a heating and cooling temperature setback 
schedule.

1. From 2300 to 0700 hours, heat = on if zone temperature < 10°C
2. From 0700 to 2300 hours, heat = on if zone temperature < 20°C
3. All hours, cool = on if zone temperature > 27°C
4. Otherwise, mechanical equipment is off

Finally, the semantic models  describing the base case scenario will be  
linked togueter in an attemp to infer new relationships between models and,
thus, discover new relationships. 

For more information related to the modeled building and it's 
characteristics, please refer to ASHRAE 140 Standard. 

![Base Case 640](https://www.researchgate.net/profile/Daniel-Costola-2/publication/241872818/figure/fig2/AS:726716133691392@1550274036653/BESTEST-case-900-building-The-IEA-ECBCS-Annex-43-Testing-and-Validation-of-Building.ppm)


