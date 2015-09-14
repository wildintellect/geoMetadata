# geoMetadata
XML stylesheets, XSLTs, and Python scripts, for working with geospatial metadata in ISO 19139 and 19110 formats.

### XSLT

modifyISO.xsl

This XSL can be used for items that already have pre-existing metadata that need to be normalized. It also adds institutional level metadata, such as distributor information and thesauri citations. The example provided in the variables is from the National Atlas of the United States. The top-level variables can be replaced according to specific collection needs.

### Python

addISO.py

This script adds identifiers to ISO 19139 metadata records, including metadata file identifier, citation URL, and distribution URL. A UUID for feature catalogs can also be added, if applicable.

### XML Templates

SUL_Template.xml 
This is an ISO 19139 template for Stanford University. This template can be used for creating new metadata records.


