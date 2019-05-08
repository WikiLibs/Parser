import unittest
import xml.etree.ElementTree as ET

import Parser.getters as getters


class Test_Getters(unittest.TestCase):
    def test_getCompoundName_error(self):
        '''
        it should return \'obj_name\'
        '''
        obj = ET.ElementTree(ET.fromstring('<root><compounddef><compoundname>obj_name</compoundname></compounddef></root>')).getroot()
        result = getters.getCompoundName(obj)
        self.assertEqual(result, 'obj_name', 'Should return \'obj_name\'')

    def test_getName(self):
        '''
        it should return \'obj_name\'
        '''
        obj = ET.ElementTree(ET.fromstring('<root><name>obj_name</name></root>')).getroot()
        result = getters.getName(obj)
        self.assertEqual(result, 'obj_name', 'Should return \'obj_name\'')

    def test_getType(self):
        '''
        it should return \'obj_type\'
        '''
        obj = ET.ElementTree(ET.fromstring('<root><type>obj_type</type></root>')).getroot()
        result = getters.getType(obj)
        self.assertEqual(result, 'obj_type', 'Should return \'obj_type\'')

    def test_getType_error(self):
        '''
        it should return nothing as object is invalid
        '''
        result = getters.getType(None)
        self.assertEqual(result, '', 'Should be empty')

    def test_getInitializer(self):
        '''
        it should return \'obj_initializer\'
        '''
        obj = ET.ElementTree(ET.fromstring('<root><initializer>obj_initializer</initializer></root>')).getroot()
        result = getters.getInitializer(obj)
        self.assertEqual(result, 'obj_initializer', 'Should return \'obj_initializer\'')

    def test_getInitializer_error(self):
        '''
        it should return nothing as object is invalid
        '''
        result = getters.getInitializer(None)
        self.assertEqual(result, '', 'Should be empty')

    def test_getDetailedDesc(self):
        '''
        it should return \'obj_dd\'
        '''
        obj = ET.ElementTree(ET.fromstring('<root><detaileddescription>obj_dd</detaileddescription></root>')).getroot()
        result = getters.getDetailedDesc(obj)
        self.assertEqual(result, 'obj_dd', 'Should return \'obj_dd\'')

    def test_getDetailedDesc_error(self):
        '''
        it should return nothing as object is invalid
        '''
        result = getters.getDetailedDesc(None)
        self.assertEqual(result, '', 'Should be empty')

    def test_getBriefDesc(self):
        '''
        it should return \'obj_bd\'
        '''
        obj = ET.ElementTree(ET.fromstring('<root><briefdescription>obj_bd</briefdescription></root>')).getroot()
        result = getters.getBriefDesc(obj)
        self.assertEqual(result, 'obj_bd', 'Should return \'obj_bd\'')

    def test_getBriefDesc_error(self):
        '''
        it should return nothing as object is invalid
        '''
        result = getters.getBriefDesc(None)
        self.assertEqual(result, '', 'Should be empty')

    def test_getReturnDesc(self):
        '''
        it should return \'obj_retDesc\'
        '''
        obj = ET.ElementTree(ET.fromstring('<root><detaileddescription><para><simplesect kind=\"return\"><para>obj_retDesc</para></simplesect></para></detaileddescription></root>')).getroot()
        result = getters.getReturnDesc(obj)
        self.assertEqual(result, 'obj_retDesc', 'Should return \'obj_retDesc\'')

    def test_getReturnDesc_error(self):
        '''
        it should return nothing as object is invalid
        '''
        result = getters.getReturnDesc(None)
        self.assertEqual(result, '', 'Should be empty')
