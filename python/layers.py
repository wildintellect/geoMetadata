#runs through xml files and creates a csv ('layers.csv') of filenames and titles
import xml.etree.cElementTree as ET
import os, csv

output_file = open('layers.csv', 'w' )

for dirName, subDirs, fileNames in os.walk(os.getcwd()):
    for f in fileNames:
       if f.endswith('shp.xml') or f.endswith('tif.xml') or f.endswith('metadata.xml'):
          f = os.path.join(dirName, f)
          tree = ET.parse(f)
          root = tree.getroot()
          fileName = root.find('Esri/DataProperties/itemProps/itemName').text
          title = root.find('dataIdInfo/idCitation/resTitle').text
#         title = title.encode('utf-8')
          output_file.write(fileName +  ',' + '"' + title + '"' + ',' + '\n')
          print title         
output_file.close()
