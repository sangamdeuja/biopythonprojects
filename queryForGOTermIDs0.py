##Download http://purl.obolibrary.org/obo/go.obo
##and then write a function which will parse this
##file and return a dictionary with GO term IDs
##as keys and NamedTuples (id, name, namespace, definition)
##as values. Check out the materials for UniProt and
##GO to see how named tuples are made and used.


import collections
##import StringIO

def myfunct(myfile):
    readmyfile=myfile.read()
    myDictionary={}
    
    NamedTuples=collections.namedtuple("GOTerm","id, name, namespace, definition")
    for lines in readmyfile.split("\n"):
##      flag variable to identify the required content is in between [Term] and emptyline
        if lines.strip()=="[Term]":
            flag=True
            current_term={}
        elif not lines.strip():
            flag=False

        else:
            if ": " in lines:
                key,value=lines.split(": ",1)
                if key in ["id","name","namespace","def"]:
                    if key=="def":
                        key="definition"
                    if flag:
                        ## only saves the contents from our requirement 
                        current_term[key]=value
                        if len(current_term)==4:
                            term=NamedTuples(**current_term)
                            myDictionary[term.id]=term
                            current_term={}
    return myDictionary
##            NamedTuple=collections.namedtuple("GOTerm","id, name, namespace, definition")
##            
##            
##            
##            return NamedTuple(**current_term)
##

data="""format-version: 1.2
data-version: releases/2016-02-06
date: 05:02:2016 14:56
saved-by: lr
auto-generated-by: TermGenie 1.0
subsetdef: goantislim_grouping "Grouping classes that can be excluded"
subsetdef: gocheck_do_not_annotate "Term not to be used for direct annotation"
subsetdef: gocheck_do_not_manually_annotate "Term not to be used for direct manual annotation"
subsetdef: goslim_aspergillus "Aspergillus GO slim"
subsetdef: goslim_candida "Candida GO slim"
subsetdef: goslim_chembl "ChEMBL protein targets summary"
subsetdef: goslim_generic "Generic GO slim"
subsetdef: goslim_goa "GOA and proteome slim"
subsetdef: goslim_metagenomics "Metagenomics GO slim"
subsetdef: goslim_pir "PIR GO slim"
subsetdef: goslim_plant "Plant GO slim"
subsetdef: goslim_pombe "Fission yeast GO slim"
subsetdef: goslim_synapse "synapse GO slim"
subsetdef: goslim_virus "Viral GO slim"
subsetdef: goslim_yeast "Yeast GO slim"
subsetdef: gosubset_prok "Prokaryotic GO subset"
subsetdef: mf_needs_review "Catalytic activity terms in need of attention"
subsetdef: termgenie_unvetted "Terms created by TermGenie that do not follow a template and require additional vetting by editors"
subsetdef: virus_checked "Viral overhaul terms"
synonymtypedef: systematic_synonym "Systematic synonym" EXACT
default-namespace: gene_ontology
remark: cvs version: $Revision: 31229 $
remark: Includes Ontology(OntologyID(OntologyIRI(<http://purl.obolibrary.org/obo/go/never_in_taxon.owl>))) [Axioms: 18 Logical Axioms: 0]
ontology: go

[Term]
id: GO:0000001
name: mitochondrion inheritance
namespace: biological_process
def: "The distribution of mitochondria, including the mitochondrial genome, into daughter cells after mitosis or meiosis, mediated by interactions between mitochondria and the cytoskeleton." [GOC:mcc, PMID:10873824, PMID:11389764]
synonym: "mitochondrial inheritance" EXACT []
is_a: GO:0048308 ! organelle inheritance
is_a: GO:0048311 ! mitochondrion distribution

[Term]
id: GO:0000002
name: mitochondrial genome maintenance
namespace: biological_process
def: "The maintenance of the structure and integrity of the mitochondrial genome; includes replication and segregation of the mitochondrial chromosome." [GOC:ai, GOC:vw]
is_a: GO:0007005 ! mitochondrion organization

[Term]
id: GO:0000003
name: reproduction
namespace: biological_process
alt_id: GO:0019952
alt_id: GO:0050876
def: "The production of new individuals that contain some portion of genetic material inherited from one or more parent organisms." [GOC:go_curators, GOC:isa_complete, GOC:jl, ISBN:0198506732]
subset: goslim_chembl
subset: goslim_generic
subset: goslim_pir
subset: goslim_plant
subset: gosubset_prok
synonym: "reproductive physiological process" EXACT []
xref: Wikipedia:Reproduction
is_a: GO:0008150 ! biological_process
disjoint_from: GO:0044848 ! biological phase

[Typedef]
id: never_in_taxon
name: never_in_taxon
namespace: external
xref: RO:0002161
expand_assertion_to: "Class: ?X DisjointWith: RO_0002162 some ?Y" []
is_metadata_tag: true
is_class_level: true

[Typedef]
id: occurs_in
name: occurs in
namespace: external
xref: BFO:0000066
holds_over_chain: part_of occurs_in
transitive_over: part_of ! part of


"""

myfile=open("go.obo")
##myfile=StringIO.StringIO(data)
print myfunct(myfile)


