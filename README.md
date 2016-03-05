# Taxonomy_Client_Server
A program where a client can insert and retrieve taxonomies to and from a server.

insert(self, path)
Insert the species that is the last element of 'path' into
this object,creating order, family, or genus Taxonomy objects
as needed. 
 
This Taxonomy Level  Expected path length
Order                4
Family               3
Genus                2
Species              1
 
path: front-slash-separated list of categories.

list(self)
Return a string representing the contents of this Taxonomy 
and its sub-Taxonomies, in the format 
top-category-name (subitem1, subitem2,...), 
where subitem1, subitem2... are either strings representing species, 
in the  form <latin-name> [(common-name)], or sublists representing 
Taxonomies.

quit(self) 
Exit the client.
