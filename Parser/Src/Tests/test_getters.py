import unittest
import xml.etree.ElementTree as ET

import Parser.Src.getters as getters


class Test_Getters(unittest.TestCase):
    def test_get_compound_name(self):
        '''it should return name'''
        xml_obj = ET.ElementTree(ET.fromstring('<compounddef><compoundname>name</compoundname></compounddef>'))
        result = getters.getCompoundName(xml_obj.getroot())
        print(result)