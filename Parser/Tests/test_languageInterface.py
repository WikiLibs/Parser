import unittest
from unittest.mock import patch
import pytest

import Parser.languageInterface as languageInterface


# class Test_LanguageInterface(unittest.TestCase):
#     @patch('Parser.languageInterface.LanguageInterface.getSymbols')
#     @patch('Parser.languageInterface.LanguageInterface.printParsedData')
#     @patch('Parser.languageInterface.LanguageInterface.uploadToApi')
#     def test_parseXMLFileWithoutVerbose(self,
#                                         mock_uploadToApi,
#                                         mock_printParsedData,
#                                         mock_getSymbols):
#         '''
#         it should call getSymbols and uploadToApi but not printParsedData
#         '''
#         interface = languageInterface.LanguageInterface('lang', 'lib')
#         interface.parseXMLFile('filename')
#         mock_getSymbols.assert_called_once()
#         mock_printParsedData.assert_not_called()
#         mock_uploadToApi.assert_called_once()

#     @patch('Parser.languageInterface.useful.verbose', True)
#     @patch('Parser.languageInterface.LanguageInterface.getSymbols')
#     @patch('Parser.languageInterface.LanguageInterface.printParsedData')
#     @patch('Parser.languageInterface.LanguageInterface.uploadToApi')
#     def test_parseXMLFileWithVerbose(self,
#                                      mock_uploadToApi,
#                                      mock_printParsedData,
#                                      mock_getSymbols):
#         '''
#         it should call getSymbols, uploadToApi and printParsedData
#         '''
#         interface = languageInterface.LanguageInterface('lang', 'lib')
#         interface.parseXMLFile('filename')
#         mock_getSymbols.assert_called_once()
#         mock_printParsedData.assert_called_once()
#         mock_uploadToApi.assert_called_once()

#     @patch('Parser.languageInterface.LanguageInterface.printParsedData')
#     @patch('Parser.languageInterface.LanguageInterface.uploadToApi')
#     def test_getSymbolsNotImplemented(self,
#                                       mock_uploadToApi,
#                                       mock_printParsedData):
#         '''
#         it should raise an exception as getSymbols isn't implemented
#         '''
#         interface = languageInterface.LanguageInterface('lang', 'lib')
#         with pytest.raises(Exception) as e:
#             assert interface.parseXMLFile('filename')
#         assert str(e.value) == 'Not implemented'

#     def test_appendToSymbols(self):
#         '''
#         should append the symbol to the list
#         '''
#         interface = languageInterface.LanguageInterface('lang', 'lib')
#         interface.appendToSymbols('variable', 'symbol')
#         self.assertEqual(interface.symbols[0]['symbol_type'], 'variable')
#         self.assertEqual(interface.symbols[0]['symbol_list'][0], 'symbol')
#         interface.appendToSymbols('variable', 'symbol2')
#         self.assertEqual(interface.symbols[0]['symbol_list'][1], 'symbol2')

#     @patch('Parser.languageInterface.printingFunctions.printUnions')
#     def test_printParsedData(self,
#                              mock_printUnions):
#         '''
#         should call the union printing function
#         '''
#         interface = languageInterface.LanguageInterface('lang', 'lib')
#         interface.symbols = [
#             {
#                 'symbol_type': 'union',
#                 'symbol_list': ['symbol']
#             }
#         ]
#         interface.printParsedData()
#         mock_printUnions.assert_called_once()

#     @patch('Parser.languageInterface.useful.upload', False)
#     @patch('Parser.languageInterface.AIClient')
#     @patch('Parser.languageInterface.JSONRequestCrafter')
#     def test_uploadToApiNoUpload(self,
#                                  mock_JSONRequestCrafter,
#                                  mock_AIClient):
#         '''
#         it shouldn't call the JsonRequestCrafter function as upload isn't on
#         '''
#         interface = languageInterface.LanguageInterface('lang', 'lib')
#         interface.symbols = [
#             {
#                 'symbol_type': 'union',
#                 'symbol_list': ['symbol']
#             }
#         ]
#         interface.uploadToApi()
#         mock_JSONRequestCrafter.assert_not_called()

#     @patch('Parser.languageInterface.useful.upload', True)
#     @patch('Parser.languageInterface.AIClient')
#     @patch('Parser.languageInterface.JSONRequestCrafter')
#     def test_uploadToApiUpload(self,
#                                mock_JSONRequestCrafter,
#                                mock_AIClient):
#         '''
#         it should call the JsonRequestCrafter function
#         '''
#         interface = languageInterface.LanguageInterface('lang', 'lib')
#         interface.symbols = [
#             {
#                 'symbol_type': 'union',
#                 'symbol_list': ['symbol']
#             }
#         ]
#         interface.uploadToApi()
#         mock_JSONRequestCrafter.assert_called_once()
