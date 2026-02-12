#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    def dict_to_xml(data, dictionary):
        root = ET.Element(data)

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        return root

    root = dict_to_xml(filename, dictionary)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    def xml_to_dict(element):
        new_dict = {}

        for child in element:
            new_dict[child.tag] = child.text
        return new_dict

    tree = ET.parse(filename)
    root = tree.getroot()
    result = xml_to_dict(root)
    return result
