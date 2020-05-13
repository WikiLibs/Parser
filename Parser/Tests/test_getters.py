import unittest
import xml.etree.ElementTree as ET
import copy

import Parser.getters as getters
import Parser.classes as classes


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

    def test_getInitializerWithEqual(self):
        '''
        it should return \'obj_initializer\' without the equal sign
        '''
        obj = ET.ElementTree(ET.fromstring('<root><initializer>= obj_initializer</initializer></root>')).getroot()
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

    def test_getLocation(self):
        '''
        it should return \'include\'
        '''
        obj = ET.ElementTree(ET.fromstring('<root><includes>include</includes><location file=""></location></root>')).getroot()
        result = getters.getLocation(obj)
        self.assertEqual(result, 'include', 'Should return \'include\'')

    def test_getFunctionDetailedDesc(self):
        '''
        it should return \'obj_dd I\'m a note\'
        '''
        obj = ET.ElementTree(ET.fromstring('<root><detaileddescription><para>obj_dd<simplesect kind=\'note\'>I\'m a note</simplesect></para></detaileddescription></root>')).getroot()
        result = getters.getFunctionDetailedDesc(obj)
        self.assertEqual(result, 'obj_dd I\'m a note', 'Should return \'obj_dd I\'m a note\'')

    def test_getFunctionDetailedDesc_error(self):
        '''
        it should return nothing as object is invalid
        '''
        result = getters.getFunctionDetailedDesc(None)
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

    def test_getParams_errorEmpty(self):
        '''
        it should return an empty list
        '''
        result = getters.getParams(None)
        self.assertEqual(result, [], 'Should return an empty list')

    def test_getParams(self):
        '''
        it should return the parameters
        '''
        obj = ET.ElementTree(ET.fromstring(
            '<root> \
                <param> \
                    <type>const \
                        <ref refid=\"struct_opus_head\" kindref=\"compound\">OpusHead</ref> * \
                    </type> \
                    <declname>_head</declname> \
                </param> \
                <param> \
                    <type>ogg_int64_t</type> \
                    <declname>_gp</declname> \
                </param> \
            </root>'
        )).getroot()

        firstParam = classes.variableClass()
        firstParam.name = '_head'
        firstParam.type = 'const OpusHead*'
        secondParam = classes.variableClass()
        secondParam.name = '_gp'
        secondParam.type = 'ogg_int64_t'
        expected = [firstParam, secondParam]

        received = getters.getParams(obj)
        self.assertEqual(expected[0].name, received[0].name, 'Should be equal')
        self.assertEqual(expected[0].type, received[0].type, 'Should be equal')
        self.assertEqual(expected[0].desc, received[0].desc, 'Should be equal')
        self.assertEqual(expected[0].value, received[0].value, 'Should be equal')
        self.assertEqual(expected[1].name, received[1].name, 'Should be equal')
        self.assertEqual(expected[1].type, received[1].type, 'Should be equal')
        self.assertEqual(expected[1].desc, received[1].desc, 'Should be equal')
        self.assertEqual(expected[1].value, received[1].value, 'Should be equal')

    def test_removeFromDetailedDescParams(self):
        '''
        it should return the expected
        '''
        expected = 'This is the description '

        param = classes.variableClass()
        param.name = 'awesome_parameter'
        received = getters.removeFromDetailedDescParams('This is the description awesome_parameter', [param])
        self.assertEqual(expected, received, 'Should be equal')

    def test_getParamDesc(self):
        '''
        it should return the list completed
        '''
        obj = ET.ElementTree(ET.fromstring(
            '<root> \
                <detaileddescription> \
                    <para> \
                        <parameterlist kind=\"param\"> \
                            <parameteritem> \
                                <parameternamelist> \
                                    <parametername>_info</parametername> \
                                </parameternamelist> \
                                <parameterdescription> \
                                    <para> \
                                        <ref refid=\"struct_opus_server_info\" kindref=\"compound\">OpusServerInfo</ref> *: Returns information about the server. If there is any error opening the stream, the contents of this structure remain unmodified. On success, fills in the structure with the server information that was available, if any. After a successful return, the contents of this structure should be freed by calling \
                                        <ref refid=\"group__url__options_1ga096536e460277fe890acb265d8fdbd63\" kindref=\"member\">opus_server_info_clear()</ref>. \
                                    </para> \
                                </parameterdescription> \
                            </parameteritem> \
                        </parameterlist> \
                    </para> \
                </detaileddescription> \
            </root>'
        )).getroot()

        firstParam = classes.variableClass()
        firstParam.name = '_info'
        expected = [firstParam]

        received = getters.getParamDesc(obj, copy.deepcopy(expected))
        expected[0].desc = 'OpusServerInfo *: Returns information about the server. If there is any error opening the stream, the contents of this structure remain unmodified. On success, fills in the structure with the server information that was available, if any. After a successful return, the contents of this structure should be freed by calling opus_server_info_clear() .'
        self.assertEqual(expected[0].desc, received[0].desc, 'Should be equal')

    def test_getParamDesc_error(self):
        '''
        it should return the same list
        '''
        firstParam = classes.variableClass()
        firstParam.name = '_head'
        expected = [firstParam]

        obj = None
        received = getters.getParamDesc(obj, expected)
        self.assertEqual(expected, received)

    def test_getRetvals(self):
        '''
        it should return the ret value
        '''
        obj = ET.ElementTree(ET.fromstring(
            '<root> \
                <detaileddescription> \
                    <para> \
                        <parameterlist kind=\"retval\"> \
                            <parameteritem> \
                                <parameternamelist> \
                                    <parametername>0</parametername> \
                                </parameternamelist> \
                                <parameterdescription> \
                                    <para>Success. </para> \
                                </parameterdescription> \
                            </parameteritem> \
                        </parameterlist> \
                    </para> \
                </detaileddescription> \
            </root>'
        )).getroot()

        tmpVar = classes.variableClass()
        tmpVar.value = '0'
        tmpVar.desc = 'Success.'
        expected = [tmpVar]

        received = getters.getRetvals(obj)
        self.assertEqual(expected[0].value, received[0].value, 'Should be equal')
        self.assertEqual(expected[0].desc, received[0].desc, 'Should be equal')

    def test_getRetvals_error(self):
        '''
        it should return an empty list
        '''
        received = getters.getRetvals(None)
        self.assertEqual(received, [], 'Should be equal')
