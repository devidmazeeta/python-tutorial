# XML Processing in Python:
# Python offers several libraries for working with XML data. The most commonly used ones are:
# xml.etree.ElementTree: Built-in library, simple to use for basic XML processing.
# lxml: Third-party library, faster and more powerful than ElementTree.
# xmltodict: Converts XML to Python dictionaries, making it easier to work with the data.

# Parsing XML using ElementTree:
import xml.etree.ElementTree as ET

# Parse XML data from a string
xml_data = """
<bookstore>
  <book category="fiction">
    <title>The Lord of the Rings</title>
    <author>J.R.R. Tolkien</author>
  </book>
</bookstore>
"""

root = ET.fromstring(xml_data)

# Access elements and attributes
print(root.tag)
print(root[0].tag)
print(root[0].attrib)
print(root[0][0].text)

# Converting XML to JSON using xmltodict:
import xmltodict
import json

# Parse XML data
xml_data = """
<bookstore>
  <book category="fiction">
    <title>The Lord of the Rings</title>
    <author>J.R.R. Tolkien</author>
  </book>
</bookstore>
"""

data = xmltodict.parse(xml_data)

# Convert to JSON
json_data = json.dumps(data)

print(json_data)
