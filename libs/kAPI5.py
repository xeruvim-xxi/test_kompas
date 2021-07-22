# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)]
# From type library 'kApi5.tlb'
# On Thu Jul 22 12:28:34 2021
''
makepy_version = '0.5.01'
python_version = 0x30905f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{0422828C-F174-495E-AC5D-D31014DBBE87}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class KompasObject(DispatchBaseClass):
	'��������� ���������� ������ 3D.'
	CLSID = IID('{E36BC97C-39D6-4402-9C25-C7008A217E02}')
	coclass_clsid = IID('{FBE002A6-1E06-4703-AEC5-9AD8A10FA1FA}')

	def ActivateControllerAPI(self):
		'�������������� API ��� ������ �����������.'
		return self._oleobj_.InvokeTypes(86, LCID, 1, (11, 0), (),)

	def ActiveDocument2D(self):
		'�������� ��������� ��������� 2D ���������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ActiveDocument2D', None)
		return ret

	def ActiveDocument3D(self):
		'�������� ��������� ��������� 3D ���������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ActiveDocument3D', None)
		return ret

	def ActiveDocumentTxt(self):
		'�������� ��������� ��������� ���������� ���������.'
		ret = self._oleobj_.InvokeTypes(88, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ActiveDocumentTxt', None)
		return ret

	def DataBaseObject(self):
		'�������� � ��.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DataBaseObject', None)
		return ret

	def Document2D(self):
		'�������� ��������� 2D ���������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Document2D', None)
		return ret

	def Document3D(self):
		'�������� ��������� 3D ���������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Document3D', None)
		return ret

	def DocumentTxt(self):
		'�������� ��������� ���������� ���������.'
		ret = self._oleobj_.InvokeTypes(87, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DocumentTxt', None)
		return ret

	def GetAttributeObject(self):
		'�������� ��������� ����������.'
		ret = self._oleobj_.InvokeTypes(43, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAttributeObject', None)
		return ret

	def GetDynamicArray(self, type=defaultNamedNotOptArg):
		'������� ��������� ������������� �������.'
		ret = self._oleobj_.InvokeTypes(39, LCID, 1, (9, 0), ((3, 0),),type
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetDynamicArray', None)
		return ret

	def GetFragmentLibrary(self):
		'������� ��������� ��� ������ � ����������� ����������.'
		ret = self._oleobj_.InvokeTypes(66, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFragmentLibrary', None)
		return ret

	def GetIterator(self):
		'�������� ��������� ���������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetIterator', None)
		return ret

	def GetMathematic2D(self):
		'�������� ��������� �������������� �������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetMathematic2D', None)
		return ret

	def GetModelLibrary(self):
		'������� ��������� ��� ������ � ����������� �������.'
		ret = self._oleobj_.InvokeTypes(65, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetModelLibrary', None)
		return ret

	def GetObjectsFilter3D(self):
		'������� ��������� ���������� �������� 3D.'
		ret = self._oleobj_.InvokeTypes(100, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectsFilter3D', None)
		return ret

	def GetParamStruct(self, structType=defaultNamedNotOptArg):
		'������� ��������� ���������� ������� � �������� ��������� �� ����.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), ((2, 0),),structType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetParamStruct', None)
		return ret

	def LoadDSK(self):
		'��������� dsk.'
		return self._oleobj_.InvokeTypes(98, LCID, 1, (11, 0), (),)

	def Quit(self):
		'������� ����������.'
		return self._oleobj_.InvokeTypes(82, LCID, 1, (24, 0), (),)

	def SpcActiveDocument(self):
		'�������� ��������� �������� ������������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'SpcActiveDocument', None)
		return ret

	def SpcDocument(self):
		'�������� ��������� ������������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'SpcDocument', None)
		return ret

	def TransferInterface(self, obj=defaultNamedNotOptArg, apiNewType=defaultNamedNotOptArg, objNewType=defaultNamedNotOptArg):
		'����� ��� ������� ������ LPUNKNOWN API7Dual, 3D COM, API5Auto.'
		ret = self._oleobj_.InvokeTypes(108, LCID, 1, (13, 0), ((13, 0), (3, 0), (3, 0)),obj
			, apiNewType, objNewType)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'TransferInterface', None)
		return ret

	def TransferReference(self, obj=defaultNamedNotOptArg, docRef=defaultNamedNotOptArg):
		'����� ��� ������� ������ API7Dual �� refererence.'
		ret = self._oleobj_.InvokeTypes(112, LCID, 1, (13, 0), ((3, 0), (3, 0)),obj
			, docRef)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'TransferReference', None)
		return ret

	def ksAttachKompasLibrary(self, libName=defaultNamedNotOptArg):
		'���������� ����������.'
		return self._oleobj_.InvokeTypes(79, LCID, 1, (3, 0), ((8, 0),),libName
			)

	def ksCalculate(self, s=defaultNamedNotOptArg, rez=pythoncom.Missing):
		'��������� ���������.'
		return self._ApplyTypes_(58, 1, (3, 0), ((8, 0), (16389, 2)), 'ksCalculate', None,s
			, rez)

	def ksCalculateReset(self):
		'�������� ������ ���������� ������������.'
		return self._oleobj_.InvokeTypes(59, LCID, 1, (3, 0), (),)

	def ksChoiceFile(self, ext=defaultNamedNotOptArg, filter=defaultNamedNotOptArg, preview=defaultNamedNotOptArg):
		'������ ������ � ������� ��� ����� ��� ������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(25, LCID, 1, (8, 0), ((8, 0), (8, 0), (11, 0)),ext
			, filter, preview)

	def ksChoiceFileAppointedDir(self, ext=defaultNamedNotOptArg, filter=defaultNamedNotOptArg, preview=defaultNamedNotOptArg, typeDir=defaultNamedNotOptArg):
		'������ ������ � ������� ��� ����� ��� ������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(40, LCID, 1, (8, 0), ((8, 0), (8, 0), (11, 0), (3, 0)),ext
			, filter, preview, typeDir)

	def ksChoiceFiles(self, ext=defaultNamedNotOptArg, filter=defaultNamedNotOptArg, p=defaultNamedNotOptArg, preview=defaultNamedNotOptArg):
		'������ ������ � ������� ������ ������ ��� ������.'
		return self._oleobj_.InvokeTypes(41, LCID, 1, (3, 0), ((8, 0), (8, 0), (9, 0), (11, 0)),ext
			, filter, p, preview)

	def ksClearFileCache(self):
		'�������� ��� ������.'
		return self._oleobj_.InvokeTypes(118, LCID, 1, (11, 0), (),)

	def ksConvertLangMenu(self, hMenu=defaultNamedNotOptArg):
		'�������������� ���� � ������������ � ������� ��������.'
		return self._oleobj_.InvokeTypes(76, LCID, 1, (3, 0), ((3, 0),),hMenu
			)

	def ksConvertLangStr(self, src=defaultNamedNotOptArg):
		'�������������� ������ � ������������ � ������� ��������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(74, LCID, 1, (8, 0), ((8, 0),),src
			)

	def ksConvertLangStrEx(self, hInstance=defaultNamedNotOptArg, strID=defaultNamedNotOptArg):
		'�������������� ������ � ������������ � ������� ��������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(96, LCID, 1, (8, 0), ((3, 0), (3, 0)),hInstance
			, strID)

	def ksConvertLangStrEx2(self, hInstance=defaultNamedNotOptArg, strID=defaultNamedNotOptArg):
		'�������������� ������ � ������������ � ������� ��������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(131, LCID, 1, (8, 0), ((12, 0), (3, 0)),hInstance
			, strID)

	def ksConvertLangWindow(self, hWnd=defaultNamedNotOptArg):
		'�������������� ���� � ��������� ��������� ������ � ������������ � ������� ��������.'
		return self._oleobj_.InvokeTypes(75, LCID, 1, (11, 0), ((3, 0),),hWnd
			)

	def ksConvertLangWindowEx(self, hWnd=defaultNamedNotOptArg, hInstance=defaultNamedNotOptArg, dlgID=defaultNamedNotOptArg):
		'�������������� ���� � ��������� ��������� ������ � ������������ � ������� ��������.'
		return self._oleobj_.InvokeTypes(97, LCID, 1, (11, 0), ((3, 0), (3, 0), (8, 0)),hWnd
			, hInstance, dlgID)

	def ksConvertLangWindowEx2(self, hWnd=defaultNamedNotOptArg, hInstance=defaultNamedNotOptArg, dlgID=defaultNamedNotOptArg):
		'�������������� ���� � ��������� ��������� ������ � ������������ � ������� ��������.'
		return self._oleobj_.InvokeTypes(132, LCID, 1, (11, 0), ((3, 0), (12, 0), (8, 0)),hWnd
			, hInstance, dlgID)

	def ksDetachKompasLibrary(self, libId=defaultNamedNotOptArg):
		'��������� ����������.'
		return self._oleobj_.InvokeTypes(80, LCID, 1, (3, 0), ((3, 0),),libId
			)

	def ksDrawBitmap(self, HWindow=defaultNamedNotOptArg, sldID=defaultNamedNotOptArg):
		'���������� BMP � ��������������� bmpID � �������� ����.'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (3, 0), ((3, 0), (3, 0)),HWindow
			, sldID)

	def ksDrawBitmapEx(self, HWindow=defaultNamedNotOptArg, bmpID=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg):
		'���������� BMP � ��������������� bmpID � �������� ����(hWindow).'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (3, 0), ((3, 0), (3, 0), (3, 0)),HWindow
			, bmpID, hInst)

	def ksDrawBitmapEx2(self, HWindow=defaultNamedNotOptArg, bmpID=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg):
		'���������� BMP � ��������������� bmpID � �������� ����(hWindow).'
		return self._oleobj_.InvokeTypes(129, LCID, 1, (3, 0), ((3, 0), (3, 0), (12, 0)),HWindow
			, bmpID, hInst)

	def ksDrawKompasDocument(self, HWindow=defaultNamedNotOptArg, docFileName=defaultNamedNotOptArg):
		'���������� ������-�������� ��� ����� � ���������� ����.'
		return self._oleobj_.InvokeTypes(84, LCID, 1, (3, 0), ((3, 0), (8, 0)),HWindow
			, docFileName)

	def ksDrawKompasDocumentByReference(self, HWindow=defaultNamedNotOptArg, pDoc=defaultNamedNotOptArg):
		'���������� ������-�������� ��� ����� � ���������� ����.'
		return self._oleobj_.InvokeTypes(92, LCID, 1, (3, 0), ((3, 0), (3, 0)),HWindow
			, pDoc)

	def ksDrawKompasText(self, HWindow=defaultNamedNotOptArg, text=defaultNamedNotOptArg):
		'���������� ����� � ������� ������ � ���������� ����.'
		return self._oleobj_.InvokeTypes(113, LCID, 1, (3, 0), ((3, 0), (8, 0)),HWindow
			, text)

	def ksDrawSlide(self, HWindow=defaultNamedNotOptArg, sldID=defaultNamedNotOptArg):
		'���������� ����� � ��������������� slideID � �������� ����(hWindow).'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((3, 0), (3, 0)),HWindow
			, sldID)

	def ksDrawSlideEx(self, HWindow=defaultNamedNotOptArg, sldID=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg):
		'���������� ����� � ��������������� slideID � �������� ����(hWindow).'
		return self._oleobj_.InvokeTypes(72, LCID, 1, (3, 0), ((3, 0), (3, 0), (3, 0)),HWindow
			, sldID, hInst)

	def ksDrawSlideEx2(self, HWindow=defaultNamedNotOptArg, sldID=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg):
		'���������� ����� � ��������������� slideID � �������� ����(hWindow).'
		return self._oleobj_.InvokeTypes(130, LCID, 1, (3, 0), ((3, 0), (3, 0), (12, 0)),HWindow
			, sldID, hInst)

	def ksDrawSlideFromFile(self, HWindow=defaultNamedNotOptArg, fileName=defaultNamedNotOptArg):
		'O��������� ����� �� ���������� �����, ����������� ���� RCDATA.'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (3, 0), ((3, 0), (8, 0)),HWindow
			, fileName)

	def ksEditTextLine(self, HWindow=defaultNamedNotOptArg, res=pythoncom.Missing, str=defaultNamedNotOptArg):
		'������������� ����������������������� �����.'
		return self._ApplyTypes_(77, 1, (8, 0), ((3, 1), (16387, 2), (8, 1)), 'ksEditTextLine', None,HWindow
			, res, str)

	def ksEnableKompasInvisible(self, key=defaultNamedNotOptArg, signature=defaultNamedNotOptArg):
		'���������� ����� ��� ������-Invisible.'
		return self._oleobj_.InvokeTypes(136, LCID, 1, (11, 0), ((8, 0), (8, 0)),key
			, signature)

	def ksEnableTaskAccess(self, enabl=1):
		'��������� ��� ��������� ������ � ������ �� ������� ������������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((3, 48),),enabl
			)

	def ksError(self, s=defaultNamedNotOptArg):
		'������� ��������� �� ������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((8, 0),),s
			)

	def ksExecDialLineStyleSelect(self, HWindow=defaultNamedNotOptArg, caption=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'����� ������� �������� ����� �����'
		return self._oleobj_.InvokeTypes(123, LCID, 1, (3, 0), ((3, 0), (8, 0), (3, 0)),HWindow
			, caption, style)

	def ksExecDialPointStyleSelect(self, HWindow=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'����� ������� �������� ������ ��� �����'
		return self._oleobj_.InvokeTypes(122, LCID, 1, (3, 0), ((3, 0), (3, 0)),HWindow
			, style)

	def ksExecDialPredefinedText(self, HWindow=defaultNamedNotOptArg, res=pythoncom.Missing):
		'����� ���������������� ����� �� ����� *.pdt.'
		return self._ApplyTypes_(71, 1, (8, 0), ((3, 1), (16387, 2)), 'ksExecDialPredefinedText', None,HWindow
			, res)

	def ksExecDialPredefinedTextEx(self, HWindow=defaultNamedNotOptArg):
		'����� ���������������� ����� �� ����� *.pdt.'
		ret = self._oleobj_.InvokeTypes(93, LCID, 1, (9, 0), ((3, 0),),HWindow
			)
		if ret is not None:
			ret = Dispatch(ret, 'ksExecDialPredefinedTextEx', None)
		return ret

	def ksExecDialSpecialSymbol(self, HWindow=defaultNamedNotOptArg):
		'����� ������� ������� ���������'
		return self._oleobj_.InvokeTypes(115, LCID, 1, (3, 0), ((3, 0),),HWindow
			)

	def ksExecDialSymbol(self, HWindow=defaultNamedNotOptArg, symb=pythoncom.Missing, font=defaultNamedNotOptArg):
		'����� ������� ������� �������'
		return self._ApplyTypes_(116, 1, (8, 0), ((3, 1), (16387, 2), (8, 1)), 'ksExecDialSymbol', None,HWindow
			, symb, font)

	def ksExecQualityDialog(self, HWindow=defaultNamedNotOptArg, curQual=defaultNamedNotOptArg, dimValue=defaultNamedNotOptArg, inMM=defaultNamedNotOptArg
			, param=defaultNamedNotOptArg):
		'����� ������� ����� ���������'
		return self._oleobj_.InvokeTypes(124, LCID, 1, (11, 0), ((3, 0), (8, 0), (16389, 0), (3, 0), (9, 0)),HWindow
			, curQual, dimValue, inMM, param)

	def ksExecuteKompasCommand(self, commandID=defaultNamedNotOptArg, post=defaultNamedNotOptArg):
		'��������� ������� �������.'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (11, 0), ((3, 0), (11, 0)),commandID
			, post)

	def ksExecuteKompasLibraryCommand(self, libId=defaultNamedNotOptArg, command=defaultNamedNotOptArg):
		'��������� ������� ����������.'
		return self._oleobj_.InvokeTypes(81, LCID, 1, (3, 0), ((3, 0), (3, 0)),libId
			, command)

	def ksExecuteKompasLibraryCommandEx(self, libId=defaultNamedNotOptArg, command=defaultNamedNotOptArg, external=defaultNamedNotOptArg):
		'��������� ������� ����������.'
		return self._oleobj_.InvokeTypes(101, LCID, 1, (3, 0), ((3, 0), (3, 0), (9, 0)),libId
			, command, external)

	def ksExecuteLibraryCommand(self, fileName=defaultNamedNotOptArg, command=defaultNamedNotOptArg):
		'���������� ������� ������ ����������.'
		return self._oleobj_.InvokeTypes(60, LCID, 1, (3, 0), ((8, 0), (3, 0)),fileName
			, command)

	def ksFullFileName(self, oldName=defaultNamedNotOptArg):
		'��������� ��� ����� �, ���� �� ������ ���, �������� � ���� ������� ����������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(34, LCID, 1, (8, 0), ((8, 0),),oldName
			)

	def ksGet3dDocumentFromRef(self, doc=defaultNamedNotOptArg):
		'�������� ��������� �� 3d ��������, ��������������� ����������� ���������.'
		ret = self._oleobj_.InvokeTypes(64, LCID, 1, (9, 0), ((3, 0),),doc
			)
		if ret is not None:
			ret = Dispatch(ret, 'ksGet3dDocumentFromRef', None)
		return ret

	def ksGetApplication7(self):
		'�������� ��������� ���������� ���������� API ������ 7.'
		ret = self._oleobj_.InvokeTypes(103, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ksGetApplication7', None)
		return ret

	def ksGetDocOptions(self, optionsType=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����� ��������� ���������.'
		return self._oleobj_.InvokeTypes(78, LCID, 1, (3, 0), ((3, 0), (9, 0)),optionsType
			, param)

	def ksGetDocumentByReference(self, docRef=defaultNamedNotOptArg):
		'�������� ��������� ��������� �� ��������� �� ��������.'
		ret = self._oleobj_.InvokeTypes(95, LCID, 1, (9, 0), ((3, 0),),docRef
			)
		if ret is not None:
			ret = Dispatch(ret, 'ksGetDocumentByReference', None)
		return ret

	def ksGetDocumentType(self, doc=0):
		'�������� ��� ���������.'
		return self._oleobj_.InvokeTypes(91, LCID, 1, (3, 0), ((3, 48),),doc
			)

	def ksGetDocumentTypeByName(self, fileName=defaultNamedNotOptArg):
		'�������� ��� ��������� �� ����� �����.'
		return self._oleobj_.InvokeTypes(94, LCID, 1, (3, 0), ((8, 0),),fileName
			)

	def ksGetDocumentTypeByNameEx(self, fileName=defaultNamedNotOptArg, docType=defaultNamedNotOptArg, errorId=defaultNamedNotOptArg):
		'�������� ��� ��������� �� ����� �����.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(138, LCID, 1, (8, 0), ((8, 0), (16387, 0), (16387, 0)),fileName
			, docType, errorId)

	def ksGetExternaldispinterface(self):
		'�������� ��������� �������� ����������.'
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ksGetExternaldispinterface', None)
		return ret

	def ksGetFullPathFromRelativePath(self, mainFilePath=defaultNamedNotOptArg, relativePath=defaultNamedNotOptArg):
		'������������ ������ ���� � ����� �� ��������� ���� � ��������� ����� � �������������� ���� � �����.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(49, LCID, 1, (8, 0), ((8, 0), (8, 0)),mainFilePath
			, relativePath)

	def ksGetFullPathFromSystemPath(self, relativePath=defaultNamedNotOptArg, pathType=defaultNamedNotOptArg):
		'������������ ������ ���� � ����� �� ��������� �������������� ���� � �����.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(47, LCID, 1, (8, 0), ((8, 0), (3, 0)),relativePath
			, pathType)

	def ksGetHWindow(self):
		'������������ ���������� �������� ����.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), (),)

	def ksGetLibraryStylesArray(self, libraryName=defaultNamedNotOptArg, libraryType=defaultNamedNotOptArg):
		'������� ���������� ��������� �� ������������ ������ ������ ��������� ����.'
		ret = self._oleobj_.InvokeTypes(56, LCID, 1, (9, 0), ((8, 0), (2, 0)),libraryName
			, libraryType)
		if ret is not None:
			ret = Dispatch(ret, 'ksGetLibraryStylesArray', None)
		return ret

	def ksGetLibraryTreeStruct(self, libName=defaultNamedNotOptArg, p=defaultNamedNotOptArg):
		'�������� ��������� ������ ���������� ����������.'
		return self._oleobj_.InvokeTypes(89, LCID, 1, (11, 0), ((8, 0), (9, 0)),libName
			, p)

	def ksGetQualityContensParam(self, name=defaultNamedNotOptArg, param=defaultNamedNotOptArg, inMM=defaultNamedNotOptArg):
		'�������� ����������.'
		return self._oleobj_.InvokeTypes(63, LCID, 1, (3, 0), ((8, 0), (9, 0), (2, 0)),name
			, param, inMM)

	def ksGetQualityDefects(self, name=defaultNamedNotOptArg, dimValue=defaultNamedNotOptArg, high=pythoncom.Missing, low=pythoncom.Missing
			, inMM=defaultNamedNotOptArg):
		'�������� ����������.'
		return self._ApplyTypes_(62, 1, (3, 0), ((8, 1), (5, 1), (16389, 2), (16389, 2), (2, 1)), 'ksGetQualityDefects', None,name
			, dimValue, high, low, inMM)

	def ksGetQualityNames(self, names=defaultNamedNotOptArg, dimValue=defaultNamedNotOptArg, high=defaultNamedNotOptArg, low=defaultNamedNotOptArg
			, system=defaultNamedNotOptArg, withLimitation=defaultNamedNotOptArg):
		'�������� ������ ����� ��������.'
		return self._oleobj_.InvokeTypes(61, LCID, 1, (3, 0), ((9, 0), (5, 0), (5, 0), (5, 0), (2, 0), (2, 0)),names
			, dimValue, high, low, system, withLimitation
			)

	def ksGetRelativePathFromFullPath(self, mainFilePath=defaultNamedNotOptArg, sourcePath=defaultNamedNotOptArg):
		'������������ ������������� ���� � ����� �� ������� ���� � ��������� ����� � ������� ���� � �����.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(48, LCID, 1, (8, 0), ((8, 0), (8, 0)),mainFilePath
			, sourcePath)

	def ksGetRelativePathFromSystemPath(self, sourcePath=defaultNamedNotOptArg, pathType=defaultNamedNotOptArg):
		'������������ ������������� ���� � ����� �� ��������� ������� ���� � �����.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(46, LCID, 1, (8, 0), ((8, 0), (3, 0)),sourcePath
			, pathType)

	def ksGetSelectedEmbodimentAdditionalNumber(self):
		'���������� �������������� ����� ���������� ��������� � ������� ������ ����� (ksSelectD3Model).'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(135, LCID, 1, (8, 0), (),)

	def ksGetSelectedEmbodimentMarking(self):
		'���������� ����������� ���������� ��������� � ������� ������ ����� (ksSelectD3Model).'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(134, LCID, 1, (8, 0), (),)

	def ksGetSysOptions(self, optionsType=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'�������� ��������� ���������.'
		return self._oleobj_.InvokeTypes(54, LCID, 1, (3, 0), ((3, 0), (9, 0)),optionsType
			, param)

	def ksGetSystemControlStartResult(self):
		'��������� ������� SystemControlStart ��� ���.'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (3, 0), (),)

	def ksGetSystemProfileString(self, lpSection=defaultNamedNotOptArg, lpKey=defaultNamedNotOptArg):
		'�������� ������ �� INI-����� ������� ��� �� Registry.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(51, LCID, 1, (8, 0), ((8, 0), (8, 0)),lpSection
			, lpKey)

	def ksGetSystemVersion(self, iMajor=pythoncom.Missing, iMinor=pythoncom.Missing, iRelease=pythoncom.Missing, iBuild=pythoncom.Missing):
		'�������� ������ �������.'
		return self._ApplyTypes_(50, 1, (3, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), 'ksGetSystemVersion', None,iMajor
			, iMinor, iRelease, iBuild)

	def ksGetWorkWindowColor(self):
		'�������� ���� ���� �������� ����.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (3, 0), (),)

	def ksIsEnableTaskAccess(self):
		'������� �������� �������� (1) ��� �������� (0) ������ � ������ �� ������� ������������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), (),)

	def ksIsHomeVersion(self):
		'���������, �������� �� ������ ��������.'
		return self._oleobj_.InvokeTypes(120, LCID, 1, (11, 0), (),)

	def ksIsKompasCommandCheck(self, commandID=defaultNamedNotOptArg):
		'��������� ������ �� ������ �������.'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (3, 0), ((3, 0),),commandID
			)

	def ksIsKompasCommandEnable(self, commandID=defaultNamedNotOptArg):
		'��������� �������� �� �������.'
		return self._oleobj_.InvokeTypes(110, LCID, 1, (11, 0), ((3, 0),),commandID
			)

	def ksIsLibraryEnabled(self, libName=defaultNamedNotOptArg):
		'�������� ����������� ����������.'
		return self._oleobj_.InvokeTypes(67, LCID, 1, (3, 0), ((8, 0),),libName
			)

	def ksIsModule2DActive(self):
		'���������, ���� �� �������� �� 2D.'
		return self._oleobj_.InvokeTypes(121, LCID, 1, (11, 0), (),)

	def ksIsModule3DActive(self):
		'��������� ��������� �� ������ � 3D �������.'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (3, 0), (),)

	def ksIsModuleSpecificationActive(self):
		'��������� ��������� �� ������ �� �������������.'
		return self._oleobj_.InvokeTypes(68, LCID, 1, (3, 0), (),)

	def ksIsSpdsVersion(self):
		'���������, ������������ �� ������ ������-���������.'
		return self._oleobj_.InvokeTypes(127, LCID, 1, (11, 0), (),)

	def ksIsStudyVersion(self):
		'���������, �������� �� ������ �������.'
		return self._oleobj_.InvokeTypes(126, LCID, 1, (11, 0), (),)

	def ksKompasVariant(self):
		'����� ������ ������.'
		return self._oleobj_.InvokeTypes(128, LCID, 1, (3, 0), (),)

	def ksLockFileCache(self, lock=defaultNamedNotOptArg):
		'����������������� ����������� ������ ������.'
		return self._oleobj_.InvokeTypes(119, LCID, 1, (11, 0), ((11, 0),),lock
			)

	def ksLockPumpMessages(self, lock=defaultNamedNotOptArg):
		'��������� �������� ���������.'
		return self._oleobj_.InvokeTypes(125, LCID, 1, (11, 0), ((11, 0),),lock
			)

	def ksMaterialDlg(self, HWindow=defaultNamedNotOptArg, res=pythoncom.Missing, plt=pythoncom.Missing, kod_size_1=pythoncom.Missing
			, kod_size_2=pythoncom.Missing, kod_size_3=pythoncom.Missing, kod_size_4=pythoncom.Missing, kod_tip=defaultNamedNotOptArg):
		'������� ���������� ����������.'
		return self._ApplyTypes_(70, 1, (8, 0), ((3, 0), (16387, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (8, 1)), 'ksMaterialDlg', None,HWindow
			, res, plt, kod_size_1, kod_size_2, kod_size_3
			, kod_size_4, kod_tip)

	def ksMessage(self, s=defaultNamedNotOptArg):
		'������� ���� ���������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((8, 0),),s
			)

	def ksMessageBoxResult(self):
		'��������� ���������, ��������������� ���������� ������ ����������.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), (),)

	def ksModule3D(self, attach=defaultNamedNotOptArg):
		'���������� ������������ 3D ������.'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (3, 0), ((11, 0),),attach
			)

	def ksModuleSpecification(self, attach=defaultNamedNotOptArg):
		'���������� ������������ ������ ������������.'
		return self._oleobj_.InvokeTypes(69, LCID, 1, (3, 0), ((11, 0),),attach
			)

	def ksOpenHelpFile(self, file=defaultNamedNotOptArg, command=defaultNamedNotOptArg, iD=defaultNamedNotOptArg):
		'������� ���� ������.'
		return self._oleobj_.InvokeTypes(52, LCID, 1, (11, 0), ((8, 0), (3, 0), (3, 0)),file
			, command, iD)

	def ksPrintKompasDocument(self, fileName=defaultNamedNotOptArg, toFile=defaultNamedNotOptArg, scale=defaultNamedNotOptArg):
		'������ ������-���������.'
		return self._oleobj_.InvokeTypes(83, LCID, 1, (3, 0), ((8, 0), (8, 0), (5, 0)),fileName
			, toFile, scale)

	def ksPrintKompasDocumentEx(self, fileName=defaultNamedNotOptArg, toFile=defaultNamedNotOptArg, scale=defaultNamedNotOptArg, FKompasPrinter=defaultNamedNotOptArg):
		'������ ������-���������.'
		return self._oleobj_.InvokeTypes(114, LCID, 1, (3, 0), ((8, 0), (8, 0), (5, 0), (11, 0)),fileName
			, toFile, scale, FKompasPrinter)

	def ksPrintPreviewWindow(self, docsArr=defaultNamedNotOptArg, inquiry=defaultNamedNotOptArg):
		'��������� ���� ��������� ���������� ����� ������� � ������.'
		return self._oleobj_.InvokeTypes(55, LCID, 1, (3, 0), ((9, 0), (3, 0)),docsArr
			, inquiry)

	def ksPumpWaitingMessages(self):
		'���������� ��� ���������.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (11, 0), (),)

	def ksReadDouble(self, mess=defaultNamedNotOptArg, defValue=defaultNamedNotOptArg, min=defaultNamedNotOptArg, max=defaultNamedNotOptArg
			, value=defaultNamedNotOptArg):
		'��������� ���� ������������� �����.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (3, 0), ((8, 0), (5, 0), (5, 0), (5, 0), (16389, 0)),mess
			, defValue, min, max, value)

	def ksReadInt(self, mess=defaultNamedNotOptArg, defValue=defaultNamedNotOptArg, min=defaultNamedNotOptArg, max=defaultNamedNotOptArg
			, value=defaultNamedNotOptArg):
		'��������� ���� ������ �����.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (3, 0), ((8, 0), (3, 0), (3, 0), (3, 0), (16387, 0)),mess
			, defValue, min, max, value)

	def ksReadString(self, mess=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		'���� ������ �������� �����.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(33, LCID, 1, (8, 0), ((8, 0), (8, 0)),mess
			, value)

	def ksRefreshActiveWindow(self):
		'�������� �������� ���� ���������.'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (3, 0), (),)

	def ksRemoveUniqueFile(self, fileName=defaultNamedNotOptArg):
		'��������� ��������� ����.'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (11, 0), ((8, 0),),fileName
			)

	def ksResultNULL(self):
		'�������� ��������� ������ ����������, ���� ������ �� ���������.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), (),)

	def ksReturnResult(self):
		'������������ ��������� ������ ����������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), (),)

	def ksSaveFile(self, ext=defaultNamedNotOptArg, oldName=defaultNamedNotOptArg, filter=defaultNamedNotOptArg, preview=defaultNamedNotOptArg):
		'������ ������ � ������� ��� ����� ��� ������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(42, LCID, 1, (8, 0), ((8, 0), (8, 0), (8, 0), (11, 0)),ext
			, oldName, filter, preview)

	def ksSelectD3Model(self, onlyDetail=defaultNamedNotOptArg, showAddNum=defaultNamedNotOptArg):
		'������� �� ������ �������� ��� �� ����� ������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(133, LCID, 1, (8, 0), ((11, 0), (11, 0)),onlyDetail
			, showAddNum)

	def ksSetCriticalProcess(self):
		'���������� ����������� �������.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (3, 0), (),)

	def ksSetDebugMessagesMode(self, debugMode=defaultNamedNotOptArg):
		'����������������� ������������ ������ ��������� � ������.'
		return self._oleobj_.InvokeTypes(117, LCID, 1, (11, 0), ((11, 0),),debugMode
			)

	def ksSetDocOptions(self, optionsType=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'�������� ��������� ���������.'
		return self._oleobj_.InvokeTypes(90, LCID, 1, (3, 0), ((3, 0), (9, 0)),optionsType
			, param)

	def ksSetFlagDisableLockApp(self, setDisableLockApp=defaultNamedNotOptArg):
		'���������� ��������� ����, ����������� ���������� ����������.'
		return self._oleobj_.InvokeTypes(85, LCID, 1, (11, 0), ((11, 0),),setDisableLockApp
			)

	def ksSetSysOptions(self, optionsType=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'�������� ��������� ���������.'
		return self._oleobj_.InvokeTypes(53, LCID, 1, (3, 0), ((3, 0), (9, 0)),optionsType
			, param)

	def ksSlideBackground(self, color=defaultNamedNotOptArg):
		'��������� ���� ���� �� ��������� ��� ��������� ������.'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (11, 0), ((3, 0),),color
			)

	def ksStrResult(self):
		'������������ ������ ���������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(20, LCID, 1, (8, 0), (),)

	def ksSystemControlStart(self, menuCommand=defaultNamedNotOptArg):
		'����� ��� ���������� �������.'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (3, 0), ((8, 0),),menuCommand
			)

	def ksSystemControlStop(self):
		'������� ���������� � ����������.'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (11, 0), (),)

	def ksSystemPath(self, pathType=defaultNamedNotOptArg):
		'������ ��������� ���� �������������� ����.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(45, LCID, 1, (8, 0), ((3, 0),),pathType
			)

	def ksUniqueFileName(self):
		'����������� � �������������� � ������� ���������� ��� ���������� �����.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(35, LCID, 1, (8, 0), (),)

	def ksViewGetDensity(self, HWindow=defaultNamedNotOptArg):
		'������� �� ������� ���������. ��������� ���������� �� ���������� ����� ���������� graphic.dsn.'
		return self._oleobj_.InvokeTypes(57, LCID, 1, (5, 0), ((3, 0),),HWindow
			)

	def ksViewGetDensityAndMaterial(self, density=pythoncom.Missing, HWindow=defaultNamedNotOptArg):
		'������� �� ������� ��������� � ������������ ���������.'
		return self._ApplyTypes_(73, 1, (8, 0), ((16389, 2), (3, 1)), 'ksViewGetDensityAndMaterial', None,density
			, HWindow)

	def ksWriteSlide(self, fileName=defaultNamedNotOptArg, iD=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg):
		'�������� ������ �������������� � ������� ������ � ��������� ����.'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (3, 0), ((8, 0), (3, 0), (5, 0), (5, 0)),fileName
			, iD, x, y)

	def ksYesNo(self, s=defaultNamedNotOptArg):
		'������ ������ ��� ������� �������������.'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (3, 0), ((8, 0),),s
			)

	_prop_map_get_ = {
		"Visible": (1, 2, (11, 0), (), "Visible", None),
		"currentDirectory": (137, 2, (8, 0), (), "currentDirectory", None),
		"lookStyle": (99, 2, (3, 0), (), "lookStyle", None),
	}
	_prop_map_put_ = {
		"Visible" : ((1, LCID, 4, 0),()),
		"currentDirectory" : ((137, LCID, 4, 0),()),
		"lookStyle" : ((99, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksABreakDimParam(DispatchBaseClass):
	'��������� �������� ������� � �������.'
	CLSID = IID('{7F7D6FC0-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FC2-97DA-11D6-8732-00C0262CDD2C}')

	def GetDPar(self):
		'���������� ��������� ����������� �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDPar', None)
		return ret

	def GetSPar(self):
		'���������� ��������� �������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSPar', None)
		return ret

	def GetTPar(self):
		'���������� ��������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTPar', None)
		return ret

	def SetDPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ����������� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetSPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� �������� ��������� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetTPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksADimParam(DispatchBaseClass):
	'��������� �������� �������.'
	CLSID = IID('{7F7D6FDE-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FE0-97DA-11D6-8732-00C0262CDD2C}')

	def GetDPar(self):
		'���������� ��������� ����������� �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDPar', None)
		return ret

	def GetSPar(self):
		'���������� ��������� �������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSPar', None)
		return ret

	def GetTPar(self):
		'���������� ��������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTPar', None)
		return ret

	def SetDPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ����������� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetSPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� �������� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetTPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksADimSourceParam(DispatchBaseClass):
	'��������� �������� �������� �������.'
	CLSID = IID('{7F7D6FD8-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FDA-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ang1": (7, 2, (5, 0), (), "ang1", None),
		"ang2": (8, 2, (5, 0), (), "ang2", None),
		"dir": (9, 2, (3, 0), (), "dir", None),
		"rad": (10, 2, (5, 0), (), "rad", None),
		"x1": (3, 2, (5, 0), (), "x1", None),
		"x2": (5, 2, (5, 0), (), "x2", None),
		"xc": (1, 2, (5, 0), (), "xc", None),
		"y1": (4, 2, (5, 0), (), "y1", None),
		"y2": (6, 2, (5, 0), (), "y2", None),
		"yc": (2, 2, (5, 0), (), "yc", None),
	}
	_prop_map_put_ = {
		"ang1" : ((7, LCID, 4, 0),()),
		"ang2" : ((8, LCID, 4, 0),()),
		"dir" : ((9, LCID, 4, 0),()),
		"rad" : ((10, LCID, 4, 0),()),
		"x1" : ((3, LCID, 4, 0),()),
		"x2" : ((5, LCID, 4, 0),()),
		"xc" : ((1, LCID, 4, 0),()),
		"y1" : ((4, LCID, 4, 0),()),
		"y2" : ((6, LCID, 4, 0),()),
		"yc" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAdditionFormatParam(DispatchBaseClass):
	'��������� ��� ����������� � �������������� ������� jgs, sat,xt,x_b, step, stl, VRML.'
	CLSID = IID('{0FD25FF9-AB0A-48F3-BAD4-F193116C0887}')
	coclass_clsid = IID('{13DF9CCA-122C-4CEC-87FA-CF16818E013A}')

	def GetObjectsOptions(self, option=defaultNamedNotOptArg):
		'�������� �������, ������������ �������� ������. option - ksD3ConverterOptionsEnum'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), ((3, 0),),option
			)

	def GetPlacement(self):
		'���, ������������ ������� ��������������� ������.'
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	def SetObjectsOptions(self, option=defaultNamedNotOptArg, set=defaultNamedNotOptArg):
		'�������� �������, ������������ �������� ������. option - ksD3ConverterOptionsEnum'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((3, 0), (3, 0)),option
			, set)

	def SetPlacement(self, p=defaultNamedNotOptArg):
		'���, ������������ ������� ��������������� ������.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), ((9, 0),),p
			)

	_prop_map_get_ = {
		"angle": (9, 2, (5, 0), (), "angle", None),
		"author": (15, 2, (8, 0), (), "author", None),
		"comment": (17, 2, (8, 0), (), "comment", None),
		"createLocalComponents": (6, 2, (11, 0), (), "createLocalComponents", None),
		"format": (1, 2, (2, 0), (), "format", None),
		"formatBinary": (2, 2, (11, 0), (), "formatBinary", None),
		"length": (10, 2, (5, 0), (), "length", None),
		"lengthUnits": (12, 2, (3, 0), (), "lengthUnits", None),
		"maxTeselationCellCount": (11, 2, (3, 0), (), "maxTeselationCellCount", None),
		"needCreateComponentsFiles": (23, 2, (11, 0), (), "needCreateComponentsFiles", None),
		"organization": (16, 2, (8, 0), (), "organization", None),
		"password": (22, 2, (8, 0), (), "password", None),
		"saveResultDocument": (24, 2, (11, 0), (), "saveResultDocument", None),
		"step": (8, 2, (5, 0), (), "step", None),
		"stepType": (7, 2, (3, 0), (), "stepType", None),
		"stitchPrecision": (14, 2, (5, 0), (), "stitchPrecision", None),
		"stitchSurfaces": (13, 2, (11, 0), (), "stitchSurfaces", None),
		"textExportForm": (5, 2, (3, 0), (), "textExportForm", None),
		"topolgyIncluded": (3, 2, (11, 0), (), "topolgyIncluded", None),
	}
	_prop_map_put_ = {
		"angle" : ((9, LCID, 4, 0),()),
		"author" : ((15, LCID, 4, 0),()),
		"comment" : ((17, LCID, 4, 0),()),
		"createLocalComponents" : ((6, LCID, 4, 0),()),
		"format" : ((1, LCID, 4, 0),()),
		"formatBinary" : ((2, LCID, 4, 0),()),
		"length" : ((10, LCID, 4, 0),()),
		"lengthUnits" : ((12, LCID, 4, 0),()),
		"maxTeselationCellCount" : ((11, LCID, 4, 0),()),
		"needCreateComponentsFiles" : ((23, LCID, 4, 0),()),
		"organization" : ((16, LCID, 4, 0),()),
		"password" : ((22, LCID, 4, 0),()),
		"saveResultDocument" : ((24, LCID, 4, 0),()),
		"step" : ((8, LCID, 4, 0),()),
		"stepType" : ((7, LCID, 4, 0),()),
		"stitchPrecision" : ((14, LCID, 4, 0),()),
		"stitchSurfaces" : ((13, LCID, 4, 0),()),
		"textExportForm" : ((5, LCID, 4, 0),()),
		"topolgyIncluded" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAggregateDefinition(DispatchBaseClass):
	'��������� ������� ��������'
	CLSID = IID('{44277B89-EEB4-456C-8EF9-2DC48D61EC91}')
	coclass_clsid = IID('{8E8A474C-5ED5-4C72-AED6-EB04C317C7DE}')

	def BodyCollection(self):
		'�������� ������ ���.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'BodyCollection', None)
		return ret

	_prop_map_get_ = {
		"BooleanType": (1, 2, (3, 0), (), "BooleanType", None),
	}
	_prop_map_put_ = {
		"BooleanType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksArc3dParam(DispatchBaseClass):
	'��������� ���������� 3d Arc.'
	CLSID = IID('{7DCBCC76-5041-4C1E-9B33-12B1352D6D57}')
	coclass_clsid = IID('{4CA2655E-EC4E-433C-9706-8E3864D5DBD2}')

	def GetPlacement(self):
		'�������� �� ����.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	_prop_map_get_ = {
		"angle": (3, 2, (5, 0), (), "angle", None),
		"radius": (2, 2, (5, 0), (), "radius", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksArcByAngleParam(DispatchBaseClass):
	'��������� ���� �� ������ � ���� �����.'
	CLSID = IID('{7F7D6F8A-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6F8C-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ang1": (4, 2, (5, 0), (), "ang1", None),
		"ang2": (5, 2, (5, 0), (), "ang2", None),
		"dir": (6, 2, (2, 0), (), "dir", None),
		"rad": (3, 2, (5, 0), (), "rad", None),
		"style": (7, 2, (3, 0), (), "style", None),
		"xc": (1, 2, (5, 0), (), "xc", None),
		"yc": (2, 2, (5, 0), (), "yc", None),
	}
	_prop_map_put_ = {
		"ang1" : ((4, LCID, 4, 0),()),
		"ang2" : ((5, LCID, 4, 0),()),
		"dir" : ((6, LCID, 4, 0),()),
		"rad" : ((3, LCID, 4, 0),()),
		"style" : ((7, LCID, 4, 0),()),
		"xc" : ((1, LCID, 4, 0),()),
		"yc" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksArcByPointParam(DispatchBaseClass):
	'��������� ���� �� ������ � ���� ������.'
	CLSID = IID('{7F7D6F8D-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6F8F-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"dir": (8, 2, (2, 0), (), "dir", None),
		"rad": (3, 2, (5, 0), (), "rad", None),
		"style": (9, 2, (3, 0), (), "style", None),
		"x1": (4, 2, (5, 0), (), "x1", None),
		"x2": (6, 2, (5, 0), (), "x2", None),
		"xc": (1, 2, (5, 0), (), "xc", None),
		"y1": (5, 2, (5, 0), (), "y1", None),
		"y2": (7, 2, (5, 0), (), "y2", None),
		"yc": (2, 2, (5, 0), (), "yc", None),
	}
	_prop_map_put_ = {
		"dir" : ((8, LCID, 4, 0),()),
		"rad" : ((3, LCID, 4, 0),()),
		"style" : ((9, LCID, 4, 0),()),
		"x1" : ((4, LCID, 4, 0),()),
		"x2" : ((6, LCID, 4, 0),()),
		"xc" : ((1, LCID, 4, 0),()),
		"y1" : ((5, LCID, 4, 0),()),
		"y2" : ((7, LCID, 4, 0),()),
		"yc" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAssociationViewParam(DispatchBaseClass):
	'��������� ���������� �������������� ����.'
	CLSID = IID('{C81EB1DA-BCB0-491A-8D22-923BF817D572}')
	coclass_clsid = IID('{7A86E2BA-6DE3-4DB3-AEB6-9738DAA69CFC}')

	def GetHatchParam(self):
		'�������� ��������� ���������, ������������ ������ � ���� ��������������.'
		ret = self._oleobj_.InvokeTypes(16, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetHatchParam', None)
		return ret

	def GetViewParam(self):
		'�������� ��������� �������� ����.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetViewParam', None)
		return ret

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	def SetDimensionLayoutScaling(self, scaling=defaultNamedNotOptArg):
		'������� ��������������� ������������� �������� ����.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((11, 0),),scaling
			)

	_prop_map_get_ = {
		"disassembly": (7, 2, (11, 0), (), "disassembly", None),
		"fileName": (3, 2, (8, 0), (), "fileName", None),
		"hiddenLinesShow": (11, 2, (11, 0), (), "hiddenLinesShow", None),
		"hiddenLinesStyle": (9, 2, (3, 0), (), "hiddenLinesStyle", None),
		"projBodies": (13, 2, (11, 0), (), "projBodies", None),
		"projSurfaces": (14, 2, (11, 0), (), "projSurfaces", None),
		"projThreads": (15, 2, (11, 0), (), "projThreads", None),
		"projectionLink": (6, 2, (11, 0), (), "projectionLink", None),
		"projectionName": (4, 2, (8, 0), (), "projectionName", None),
		"sameHatch": (19, 2, (11, 0), (), "sameHatch", None),
		"section": (17, 2, (11, 0), (), "section", None),
		"tangentEdgesShow": (12, 2, (11, 0), (), "tangentEdgesShow", None),
		"tangentEdgesStyle": (10, 2, (3, 0), (), "tangentEdgesStyle", None),
		"visibleLinesStyle": (8, 2, (3, 0), (), "visibleLinesStyle", None),
		"viewType": (5, 2, (2, 0), (), "viewType", None),
	}
	_prop_map_put_ = {
		"disassembly" : ((7, LCID, 4, 0),()),
		"fileName" : ((3, LCID, 4, 0),()),
		"hiddenLinesShow" : ((11, LCID, 4, 0),()),
		"hiddenLinesStyle" : ((9, LCID, 4, 0),()),
		"projBodies" : ((13, LCID, 4, 0),()),
		"projSurfaces" : ((14, LCID, 4, 0),()),
		"projThreads" : ((15, LCID, 4, 0),()),
		"projectionLink" : ((6, LCID, 4, 0),()),
		"projectionName" : ((4, LCID, 4, 0),()),
		"sameHatch" : ((19, LCID, 4, 0),()),
		"section" : ((17, LCID, 4, 0),()),
		"tangentEdgesShow" : ((12, LCID, 4, 0),()),
		"tangentEdgesStyle" : ((10, LCID, 4, 0),()),
		"visibleLinesStyle" : ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAttribute3D(DispatchBaseClass):
	'��������� ��������.'
	CLSID = IID('{3EEB2B43-56FF-49C0-AFCF-69E990A7D84C}')
	coclass_clsid = IID('{620BFE17-2F66-4102-A8EA-4DD33C081061}')

	# Result is of type ksFeatureCollection
	def FeatureCollection(self, objType=defaultNamedNotOptArg):
		'�������� ������ ��������, ������� ������ ������� (objType==o3d_unknown - �������� ��� �������).'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((3, 0),),objType
			)
		if ret is not None:
			ret = Dispatch(ret, 'FeatureCollection', '{CE6A46FF-02B4-4C7E-AF50-3F3707C8B122}')
		return ret

	_prop_map_get_ = {
		"nameType": (3, 2, (8, 0), (), "nameType", None),
		"reference": (1, 2, (3, 0), (), "reference", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAttribute3DCollection(DispatchBaseClass):
	'��������� ������� ���������.'
	CLSID = IID('{EB61A981-F63E-47E1-BEE8-2D1612C78E78}')
	coclass_clsid = IID('{17CAB61A-770A-4FCE-8FC5-F291CDADF80A}')

	def FindIt(self, obj=defaultNamedNotOptArg):
		'�������� ������ �������� �������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((9, 0),),obj
			)

	# Result is of type ksAttribute3D
	def First(self):
		'�������� ��������� �� ��������� ������� ����������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', '{3EEB2B43-56FF-49C0-AFCF-69E990A7D84C}')
		return ret

	# Result is of type ksAttribute3D
	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ��������� �� ��������� ���������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', '{3EEB2B43-56FF-49C0-AFCF-69E990A7D84C}')
		return ret

	def GetCount(self):
		'�������� ���������� ��������� ������� ����������� ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	# Result is of type ksAttribute3D
	def Last(self):
		'�������� ��������� �� ��������� ���������� ����������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', '{3EEB2B43-56FF-49C0-AFCF-69E990A7D84C}')
		return ret

	# Result is of type ksAttribute3D
	def Next(self):
		'�������� ��������� �� ��������� ���������� ����������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', '{3EEB2B43-56FF-49C0-AFCF-69E990A7D84C}')
		return ret

	# Result is of type ksAttribute3D
	def Prev(self):
		'�������� ��������� �� ��������� ����������� ����������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', '{3EEB2B43-56FF-49C0-AFCF-69E990A7D84C}')
		return ret

	def Select(self, key1=defaultNamedNotOptArg, key2=defaultNamedNotOptArg, key3=defaultNamedNotOptArg, key4=defaultNamedNotOptArg
			, numb=defaultNamedNotOptArg, objType=defaultNamedNotOptArg):
		'������������� ��������, ������� ���� ��� � ������� �������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((3, 0), (3, 0), (3, 0), (3, 0), (5, 0), (3, 0)),key1
			, key2, key3, key4, numb, objType
			)

	def refresh(self):
		'������� �������� ��� �������� �� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAttributeObject(DispatchBaseClass):
	'��������� ��������.'
	CLSID = IID('{FA93AA24-9B3D-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{FA93AA26-9B3D-11D6-95CE-00C0262D30E3}')

	def ksAddAttrRow(self, pAttr=defaultNamedNotOptArg, rowNumb=defaultNamedNotOptArg, flagVisible=defaultNamedNotOptArg, value=defaultNamedNotOptArg
			, password=defaultNamedNotOptArg):
		'�������� ������ � ���������� �������� �������������� �����.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((3, 0), (3, 0), (9, 0), (9, 0), (8, 0)),pAttr
			, rowNumb, flagVisible, value, password)

	def ksChoiceAttr(self, pObj=defaultNamedNotOptArg):
		'��������� ������ ��� ��������� ��������� ������� � ������ ������� ��������.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), ((3, 0),),pObj
			)

	# Result is of type ksAttribute3D
	def ksChoiceAttr3D(self, pObj=defaultNamedNotOptArg):
		'��������� ������ ��� ��������� ��������� ������� � ������ ������� ��������.'
		ret = self._oleobj_.InvokeTypes(25, LCID, 1, (9, 0), ((9, 0),),pObj
			)
		if ret is not None:
			ret = Dispatch(ret, 'ksChoiceAttr3D', '{3EEB2B43-56FF-49C0-AFCF-69E990A7D84C}')
		return ret

	def ksChoiceAttrTypes(self, libName=defaultNamedNotOptArg):
		'��������� ������ ��� ��������� � ���������� ��������� ������ ����� ��������� � ������ ������� ����.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (5, 0), ((8, 0),),libName
			)

	def ksCreateAttr(self, pObj=defaultNamedNotOptArg, attr=defaultNamedNotOptArg, attrID=defaultNamedNotOptArg, libName=defaultNamedNotOptArg):
		'������� ������� �� ������ ���� �������� �� ���������� libname.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((3, 0), (9, 0), (5, 0), (8, 0)),pObj
			, attr, attrID, libName)

	# Result is of type ksAttribute3D
	def ksCreateAttr3D(self, pObj=defaultNamedNotOptArg, attr=defaultNamedNotOptArg, attrID=defaultNamedNotOptArg, libName=defaultNamedNotOptArg):
		'������� ������� �� ������ ���� �������� �� ���������� libname.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((9, 0), (9, 0), (5, 0), (8, 0)),pObj
			, attr, attrID, libName)
		if ret is not None:
			ret = Dispatch(ret, 'ksCreateAttr3D', '{3EEB2B43-56FF-49C0-AFCF-69E990A7D84C}')
		return ret

	# Result is of type ksAttribute3D
	def ksCreateAttr3DEx(self, pObj=defaultNamedNotOptArg, pSourcePart=defaultNamedNotOptArg, attr=defaultNamedNotOptArg, attrID=defaultNamedNotOptArg
			, libName=defaultNamedNotOptArg):
		'������� ������� � ��������� �� ������ ���� �������� �� ���������� libname.'
		ret = self._oleobj_.InvokeTypes(26, LCID, 1, (9, 0), ((9, 0), (9, 0), (9, 0), (5, 0), (8, 0)),pObj
			, pSourcePart, attr, attrID, libName)
		if ret is not None:
			ret = Dispatch(ret, 'ksCreateAttr3DEx', '{3EEB2B43-56FF-49C0-AFCF-69E990A7D84C}')
		return ret

	def ksCreateAttrType(self, attrType=defaultNamedNotOptArg, libName=defaultNamedNotOptArg):
		'������� ��� �������� � ���������� libname.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (5, 0), ((9, 0), (8, 0)),attrType
			, libName)

	def ksDeleteAttr(self, pObj=defaultNamedNotOptArg, pAttr=defaultNamedNotOptArg, password=defaultNamedNotOptArg):
		'������� �������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((3, 0), (3, 0), (8, 0)),pObj
			, pAttr, password)

	def ksDeleteAttr3D(self, pObj=defaultNamedNotOptArg, pAttr=defaultNamedNotOptArg, password=defaultNamedNotOptArg):
		'������� �������.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (3, 0), ((9, 1), (9, 1), (8, 1)),pObj
			, pAttr, password)

	def ksDeleteAttrRow(self, pAttr=defaultNamedNotOptArg, rowNumb=defaultNamedNotOptArg, password=defaultNamedNotOptArg):
		'������� ������ ���������� �������� �������������� �����.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((3, 0), (3, 0), (8, 0)),pAttr
			, rowNumb, password)

	def ksDeleteAttrType(self, attrID=defaultNamedNotOptArg, libName=defaultNamedNotOptArg, password=defaultNamedNotOptArg):
		'������� ��� �������� � ���������� libname.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), ((5, 0), (8, 0), (8, 0)),attrID
			, libName, password)

	def ksGetAttrColumnInfo(self, pAttr=defaultNamedNotOptArg, columnNumb=defaultNamedNotOptArg, columnInfo=defaultNamedNotOptArg):
		'�������� ���������� � ������� ��������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((3, 0), (3, 0), (9, 0)),pAttr
			, columnNumb, columnInfo)

	def ksGetAttrKeysInfo(self, pAttr=defaultNamedNotOptArg, key1=pythoncom.Missing, key2=pythoncom.Missing, key3=pythoncom.Missing
			, key4=pythoncom.Missing, numb=pythoncom.Missing):
		'������ ���������� � ������ ��������.'
		return self._ApplyTypes_(16, 1, (3, 0), ((3, 1), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16389, 2)), 'ksGetAttrKeysInfo', None,pAttr
			, key1, key2, key3, key4, numb
			)

	def ksGetAttrRow(self, pAttr=defaultNamedNotOptArg, rowNumb=defaultNamedNotOptArg, flagVisible=defaultNamedNotOptArg, columnKeys=defaultNamedNotOptArg
			, value=defaultNamedNotOptArg):
		'�������� ������ ������ �� ������� ��������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), ((3, 0), (3, 0), (9, 0), (9, 0), (9, 0)),pAttr
			, rowNumb, flagVisible, columnKeys, value)

	def ksGetAttrTabInfo(self, pAttr=defaultNamedNotOptArg, rowsCount=pythoncom.Missing, columnsCount=pythoncom.Missing):
		'�������� ���������� � ���������� ����� � �������� ��������.'
		return self._ApplyTypes_(18, 1, (3, 0), ((3, 1), (16387, 2), (16387, 2)), 'ksGetAttrTabInfo', None,pAttr
			, rowsCount, columnsCount)

	def ksGetAttrType(self, attrID=defaultNamedNotOptArg, libName=defaultNamedNotOptArg, attrType=defaultNamedNotOptArg):
		'�������� ��� �������� �� ���������� libname.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((5, 0), (8, 0), (9, 0)),attrID
			, libName, attrType)

	def ksGetAttrValue(self, pAttr=defaultNamedNotOptArg, rowNumb=defaultNamedNotOptArg, columnNumb=defaultNamedNotOptArg, flagVisible=defaultNamedNotOptArg
			, columnKeys=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		'�������� �������� ������ �� ������� ��������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((3, 0), (3, 0), (3, 0), (9, 0), (9, 0), (9, 0)),pAttr
			, rowNumb, columnNumb, flagVisible, columnKeys, value
			)

	def ksGetLibraryAttrTypesArray(self, libName=defaultNamedNotOptArg):
		'���������� ������ ����� ���������, ����������� � �������� ���������� �����.'
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), ((8, 0),),libName
			)
		if ret is not None:
			ret = Dispatch(ret, 'ksGetLibraryAttrTypesArray', None)
		return ret

	def ksGetSizeAttrRow(self, pAttr=defaultNamedNotOptArg, count=pythoncom.Missing):
		'�������� ������ ������ ������ ���������.'
		return self._ApplyTypes_(15, 1, (3, 0), ((3, 1), (16387, 2)), 'ksGetSizeAttrRow', None,pAttr
			, count)

	def ksGetSizeAttrRowW(self, pAttr=defaultNamedNotOptArg, count=pythoncom.Missing):
		'�������� ������ ������ ������ ���������. ������ ������ ��� Unicode.'
		return self._ApplyTypes_(28, 1, (3, 0), ((3, 1), (16387, 2)), 'ksGetSizeAttrRowW', None,pAttr
			, count)

	def ksGetSizeAttrValue(self, pAttr=defaultNamedNotOptArg, columnNumb=defaultNamedNotOptArg, count=pythoncom.Missing):
		'�������� ������ ������ ������.'
		return self._ApplyTypes_(14, 1, (3, 0), ((3, 1), (3, 1), (16387, 2)), 'ksGetSizeAttrValue', None,pAttr
			, columnNumb, count)

	def ksGetSizeAttrValueW(self, pAttr=defaultNamedNotOptArg, columnNumb=defaultNamedNotOptArg, count=pythoncom.Missing):
		'�������� ������ ������ ������. ������ ������ ��� Unicode.'
		return self._ApplyTypes_(27, 1, (3, 0), ((3, 1), (3, 1), (16387, 2)), 'ksGetSizeAttrValueW', None,pAttr
			, columnNumb, count)

	def ksSetAttrRow(self, pAttr=defaultNamedNotOptArg, rowNumb=defaultNamedNotOptArg, flagVisible=defaultNamedNotOptArg, columnKeys=defaultNamedNotOptArg
			, value=defaultNamedNotOptArg, password=defaultNamedNotOptArg):
		'�������� ������ ������ � ������� ��������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((3, 0), (3, 0), (9, 0), (9, 0), (9, 0), (8, 0)),pAttr
			, rowNumb, flagVisible, columnKeys, value, password
			)

	def ksSetAttrType(self, attrID=defaultNamedNotOptArg, libName=defaultNamedNotOptArg, attrType=defaultNamedNotOptArg, password=defaultNamedNotOptArg):
		'�������� ��� �������� � ���������� libname.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (5, 0), ((5, 0), (8, 0), (9, 0), (8, 0)),attrID
			, libName, attrType, password)

	def ksSetAttrValue(self, pAttr=defaultNamedNotOptArg, rowNumb=defaultNamedNotOptArg, columnNumb=defaultNamedNotOptArg, flagVisible=defaultNamedNotOptArg
			, columnKeys=defaultNamedNotOptArg, value=defaultNamedNotOptArg, password=defaultNamedNotOptArg):
		'�������� �������� ������ � ������� ��������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((3, 0), (3, 0), (3, 0), (9, 0), (9, 0), (9, 0), (8, 0)),pAttr
			, rowNumb, columnNumb, flagVisible, columnKeys, value
			, password)

	def ksViewEditAttr(self, pAttr=defaultNamedNotOptArg, type=defaultNamedNotOptArg, password=defaultNamedNotOptArg):
		'��������� ������ ��� ��������� � �������������� ��������.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((3, 0), (3, 0), (8, 0)),pAttr
			, type, password)

	def ksViewEditAttrType(self, libName=defaultNamedNotOptArg, type=defaultNamedNotOptArg, attrID=defaultNamedNotOptArg, password=defaultNamedNotOptArg):
		'��������� ������ ��� ��������� � �������������� ���� ��������.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), ((8, 0), (3, 0), (5, 0), (8, 0)),libName
			, type, attrID, password)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAttributeParam(DispatchBaseClass):
	'��������� ��������.'
	CLSID = IID('{CE0D05E4-9B2A-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{CE0D05E6-9B2A-11D6-95CE-00C0262D30E3}')

	def GetColumnKeys(self):
		'������ ������ ������ �������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetColumnKeys', None)
		return ret

	def GetFlagVisible(self):
		'������ ������, ������������ ��� ������ ������� �������� ���������-�����������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFlagVisible', None)
		return ret

	def GetValues(self):
		'������ ������ �������� ����� ������� ���������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetValues', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

	def SetColumnKeys(self, columnKeys=defaultNamedNotOptArg):
		'�������� ������ ������ �������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 0),),columnKeys
			)

	def SetFlagVisible(self, flagVisible=defaultNamedNotOptArg):
		'�������� ������, ������������ ��� ������ ������� �������� ���������-�����������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),flagVisible
			)

	def SetValues(self, values=defaultNamedNotOptArg):
		'�������� ������ �������� ����� ������� ���������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((9, 0),),values
			)

	_prop_map_get_ = {
		"key1": (1, 2, (3, 0), (), "key1", None),
		"key2": (2, 2, (3, 0), (), "key2", None),
		"key3": (3, 2, (3, 0), (), "key3", None),
		"key4": (4, 2, (3, 0), (), "key4", None),
		"password": (5, 2, (8, 0), (), "password", None),
	}
	_prop_map_put_ = {
		"key1" : ((1, LCID, 4, 0),()),
		"key2" : ((2, LCID, 4, 0),()),
		"key3" : ((3, LCID, 4, 0),()),
		"key4" : ((4, LCID, 4, 0),()),
		"password" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAttributeTypeParam(DispatchBaseClass):
	'��������� ���� ��������.'
	CLSID = IID('{CC26DA61-9B22-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{CC26DA63-9B22-11D6-95CE-00C0262D30E3}')

	def GetColumns(self):
		'������ ������ ���������� � ��������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetColumns', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

	def SetColumns(self, val=defaultNamedNotOptArg):
		'�������� ������ ���������� � ��������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"flagVisible": (7, 2, (11, 0), (), "flagVisible", None),
		"header": (6, 2, (8, 0), (), "header", None),
		"key1": (1, 2, (3, 0), (), "key1", None),
		"key2": (2, 2, (3, 0), (), "key2", None),
		"key3": (3, 2, (3, 0), (), "key3", None),
		"key4": (4, 2, (3, 0), (), "key4", None),
		"password": (8, 2, (8, 0), (), "password", None),
		"rowsCount": (5, 2, (3, 0), (), "rowsCount", None),
	}
	_prop_map_put_ = {
		"flagVisible" : ((7, LCID, 4, 0),()),
		"header" : ((6, LCID, 4, 0),()),
		"key1" : ((1, LCID, 4, 0),()),
		"key2" : ((2, LCID, 4, 0),()),
		"key3" : ((3, LCID, 4, 0),()),
		"key4" : ((4, LCID, 4, 0),()),
		"password" : ((8, LCID, 4, 0),()),
		"rowsCount" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAxis2PlanesDefinition(DispatchBaseClass):
	'��� �� ���� ����������.'
	CLSID = IID('{0307BB81-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BB83-C193-11D6-8734-00C0262CDD2C}')

	def GetCurve3D(self):
		'�������� ��������� �������������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurve3D', None)
		return ret

	def GetPlane(self, number=defaultNamedNotOptArg):
		'�������� ��������� ���������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((3, 0),),number
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def SetPlane(self, number=defaultNamedNotOptArg, plane=defaultNamedNotOptArg):
		'���������� ��������� ���������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((3, 0), (9, 0)),number
			, plane)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAxis2PointsDefinition(DispatchBaseClass):
	'��� �� ���� ������.'
	CLSID = IID('{0307BB87-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BB89-C193-11D6-8734-00C0262CDD2C}')

	def GetCurve3D(self):
		'�������� ��������� �������������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurve3D', None)
		return ret

	def GetPoint(self, number=defaultNamedNotOptArg):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((3, 0),),number
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPoint', None)
		return ret

	def SetPoint(self, number=defaultNamedNotOptArg, point=defaultNamedNotOptArg):
		'���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((3, 0), (9, 0)),number
			, point)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAxisConefaceDefinition(DispatchBaseClass):
	'��� ���������� �����.'
	CLSID = IID('{97337DAF-B7CD-4FB8-8E18-23F0230E5CBE}')
	coclass_clsid = IID('{C6BD0D90-C8BE-4378-9A71-835597A7D1E9}')

	def GetCurve3D(self):
		'�������� ��������� �������������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurve3D', None)
		return ret

	def GetFace(self):
		'���������� ��������� �� ������� ���������� �����������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFace', None)
		return ret

	def SetFace(self, face=defaultNamedNotOptArg):
		'�������� ��������� �� ������� ���������� �����������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((9, 0),),face
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAxisEdgeDefinition(DispatchBaseClass):
	'��� �� �����.'
	CLSID = IID('{0307BB8A-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BB8C-C193-11D6-8734-00C0262CDD2C}')

	def GetCurve3D(self):
		'�������� ��������� �������������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurve3D', None)
		return ret

	def GetEdge(self):
		'�������� ��������� �����.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEdge', None)
		return ret

	def SetEdge(self, edge=defaultNamedNotOptArg):
		'�������� ��������� �����.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((9, 0),),edge
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAxisLineParam(DispatchBaseClass):
	'��������� ���������� ������ �����.'
	CLSID = IID('{AFE694D7-C1E5-468F-99B0-FE4C60C49899}')
	coclass_clsid = IID('{705962E9-5E9B-4379-8504-FA754D11FC66}')

	def GetBegPoint(self):
		'�������� ���������� ��������� ����� ������ �����.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetBegPoint', None)
		return ret

	def GetEndPoint(self):
		'�������� ���������� �������� ����� ������ �����.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEndPoint', None)
		return ret

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksAxisOperationsDefinition(DispatchBaseClass):
	'��� ��������.'
	CLSID = IID('{0307BB84-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BB86-C193-11D6-8734-00C0262CDD2C}')

	def GetCurve3D(self):
		'�������� ��������� �������������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurve3D', None)
		return ret

	def GetOperation(self):
		'�������� ��������� ��������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetOperation', None)
		return ret

	def SetOperation(self, plane=defaultNamedNotOptArg):
		'���������� ��������� ��������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((9, 0),),plane
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBaseEvolutionDefinition(DispatchBaseClass):
	'��������� ������� �������������� ��������.'
	CLSID = IID('{DEEFEFF9-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFEFFB-C3E2-11D6-8734-00C0262CDD2C}')

	def GetPathLength(self, bitVector=defaultNamedNotOptArg):
		'�������� ����� ������ ����������(ST_MIX_MM..ST_MIX_M ������� ���������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (5, 0), ((19, 0),),bitVector
			)

	def GetSketch(self):
		'�������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def GetThinParam(self, thin=pythoncom.Missing, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(5, 1, (11, 0), ((16395, 2), (16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thin
			, thinType, normalThickness, reverseTthickness)

	def PathPartArray(self):
		'�������� ��������� ������� ������ ����������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PathPartArray', None)
		return ret

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'�������� ��������� ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"sketchShiftType": (1, 2, (2, 0), (), "sketchShiftType", None),
	}
	_prop_map_put_ = {
		"sketchShiftType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBaseExtrusionDefinition(DispatchBaseClass):
	'��������� ������� �������� ������������.'
	CLSID = IID('{DEEFEFE1-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFEFE3-C3E2-11D6-8734-00C0262CDD2C}')

	def ExtrusionParam(self):
		'��������� ���������� ������������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ExtrusionParam', None)
		return ret

	def GetDepthObject(self, normal=defaultNamedNotOptArg):
		'�������� ������ �������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((11, 0),),normal
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetDepthObject', None)
		return ret

	def GetSideParam(self, side1=defaultNamedNotOptArg, type=pythoncom.Missing, depth=pythoncom.Missing, draftValue=pythoncom.Missing
			, draftOutward=pythoncom.Missing):
		'�������� ��������� ������������ � ���� �������.'
		return self._ApplyTypes_(4, 1, (11, 0), ((11, 1), (16386, 2), (16389, 2), (16389, 2), (16395, 2)), 'GetSideParam', None,side1
			, type, depth, draftValue, draftOutward)

	def GetSketch(self):
		'�������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def GetThinParam(self, thin=pythoncom.Missing, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16395, 2), (16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thin
			, thinType, normalThickness, reverseTthickness)

	def ResetDepthObject(self, normal=defaultNamedNotOptArg):
		'����� ������� �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((11, 0),),normal
			)

	def SetDepthObject(self, normal=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'���������� ������ �������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((11, 0), (9, 0)),normal
			, obj)

	def SetSideParam(self, side1=defaultNamedNotOptArg, type=0, depth=1.0, draftValue=0.0
			, draftOutward=False):
		'���������� ��������� ������������ � ���� �������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48), (11, 48)),side1
			, type, depth, draftValue, draftOutward)

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'�������� ��������� ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"directionType": (1, 2, (2, 0), (), "directionType", None),
	}
	_prop_map_put_ = {
		"directionType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBaseLoftDefinition(DispatchBaseClass):
	'������� �������� �� ��������.'
	CLSID = IID('{DEEFEFEA-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFEFEC-C3E2-11D6-8734-00C0262CDD2C}')

	def GetLoftParam(self, closed=pythoncom.Missing, flipVertex=pythoncom.Missing, autoPath=pythoncom.Missing):
		'�������� ��������� ��������.'
		return self._ApplyTypes_(1, 1, (11, 0), ((16395, 2), (16395, 2), (16395, 2)), 'GetLoftParam', None,closed
			, flipVertex, autoPath)

	def GetThinParam(self, thin=pythoncom.Missing, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(3, 1, (11, 0), ((16395, 2), (16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thin
			, thinType, normalThickness, reverseTthickness)

	def SetLoftParam(self, closed=defaultNamedNotOptArg, flipVertex=defaultNamedNotOptArg, autoPath=defaultNamedNotOptArg):
		'���������� ��������� ��������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((11, 0), (11, 0), (11, 0)),closed
			, flipVertex, autoPath)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def Sketchs(self):
		'������ �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Sketchs', None)
		return ret

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBaseParam(DispatchBaseClass):
	'��������� ����������� ����.'
	CLSID = IID('{E79C2513-9584-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{E79C2515-9584-11D6-8732-00C0262CDD2C}')

	def GetPTextItem(self):
		'���������� ������������ ������ ��������� ����� TEXT_ITEM_ARR.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPTextItem', None)
		return ret

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	def SetPTextItem(self, val=defaultNamedNotOptArg):
		'�������� ������������ ������ ��������� ����� TEXT_ITEM_ARR.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"str": (7, 2, (8, 0), (), "str", None),
		"style": (1, 2, (3, 0), (), "style", None),
		"type": (6, 2, (11, 0), (), "type", None),
		"x1": (2, 2, (5, 0), (), "x1", None),
		"x2": (4, 2, (5, 0), (), "x2", None),
		"y1": (3, 2, (5, 0), (), "y1", None),
		"y2": (5, 2, (5, 0), (), "y2", None),
	}
	_prop_map_put_ = {
		"str" : ((7, LCID, 4, 0),()),
		"style" : ((1, LCID, 4, 0),()),
		"type" : ((6, LCID, 4, 0),()),
		"x1" : ((2, LCID, 4, 0),()),
		"x2" : ((4, LCID, 4, 0),()),
		"y1" : ((3, LCID, 4, 0),()),
		"y2" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBaseRotatedDefinition(DispatchBaseClass):
	'������� �������� ��������.'
	CLSID = IID('{2DFACC67-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{2DFACC69-C4A4-11D6-8734-00C0262CDD2C}')

	def GetSideParam(self, side1=defaultNamedNotOptArg, angle=pythoncom.Missing):
		'�������� ��������� �������� � ���� �������.'
		return self._ApplyTypes_(5, 1, (11, 0), ((11, 1), (16389, 2)), 'GetSideParam', None,side1
			, angle)

	def GetSketch(self):
		'�������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def GetThinParam(self, thin=pythoncom.Missing, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(7, 1, (11, 0), ((16395, 2), (16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thin
			, thinType, normalThickness, reverseTthickness)

	def RotatedParam(self):
		'��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RotatedParam', None)
		return ret

	def SetSideParam(self, side1=False, angle=180.0):
		'���������� ��������� �������� � ���� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((11, 48), (5, 48)),side1
			, angle)

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'���������� ��������� ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"directionType": (1, 2, (2, 0), (), "directionType", None),
		"toroidShapeType": (2, 2, (11, 0), (), "toroidShapeType", None),
	}
	_prop_map_put_ = {
		"directionType" : ((1, LCID, 4, 0),()),
		"toroidShapeType" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBezierParam(DispatchBaseClass):
	'��������� bezier �������.'
	CLSID = IID('{7F7D6FC6-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FC8-97DA-11D6-8732-00C0262CDD2C}')

	def GetMathPointArr(self):
		'���������� ������������ ������ �������������� ����� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetMathPointArr', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetMathPointArr(self, val=defaultNamedNotOptArg):
		'�������� ������������ ������ �������������� ����� �������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"closed": (2, 2, (2, 0), (), "closed", None),
		"style": (1, 2, (3, 0), (), "style", None),
	}
	_prop_map_put_ = {
		"closed" : ((2, LCID, 4, 0),()),
		"style" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBezierPointParam(DispatchBaseClass):
	'��������� ���� ��� Bezier - ������.'
	CLSID = IID('{7F7D6FC9-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FCB-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ang": (3, 2, (5, 0), (), "ang", None),
		"left": (4, 2, (5, 0), (), "left", None),
		"right": (5, 2, (5, 0), (), "right", None),
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"ang" : ((3, LCID, 4, 0),()),
		"left" : ((4, LCID, 4, 0),()),
		"right" : ((5, LCID, 4, 0),()),
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBody(DispatchBaseClass):
	'���� 3D.'
	CLSID = IID('{03EFC9DD-E05A-4277-BC7C-4FD499A252DE}')
	coclass_clsid = IID('{A99FFD41-AA46-4BFC-B6F2-32E1A956E0B1}')

	def CalcMassInertiaProperties(self, bitVector=defaultNamedNotOptArg):
		'���������� �����-������������ �������������� (bitVector - ���������� ����������� �����, ����������� �����, ����� ��������� � ��������� [ST_MIX_MM..ST_MIX_KG] ) ������: �����|��| ST_MIX_M|ST_MIX_KG.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((19, 0),),bitVector
			)
		if ret is not None:
			ret = Dispatch(ret, 'CalcMassInertiaProperties', None)
		return ret

	def CheckIntersectionWithBody(self, otherBody=defaultNamedNotOptArg, checkTangent=defaultNamedNotOptArg):
		'�������� ������� ����������� � �����.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((9, 0), (11, 0)),otherBody
			, checkTangent)
		if ret is not None:
			ret = Dispatch(ret, 'CheckIntersectionWithBody', None)
		return ret

	def CurveIntersection(self, curve=defaultNamedNotOptArg, fases=defaultNamedNotOptArg, points=defaultNamedNotOptArg):
		'������� ����������� � ������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0), (9, 0), (9, 0)),curve
			, fases, points)

	def FaceCollection(self):
		'�������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'FaceCollection', None)
		return ret

	def GetFeature(self):
		'�������� ������ ������, ��������� � ������ ��������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFeature', None)
		return ret

	def GetGabarit(self, x1=pythoncom.Missing, y1=pythoncom.Missing, z1=pythoncom.Missing, x2=pythoncom.Missing
			, y2=pythoncom.Missing, z2=pythoncom.Missing):
		'�������� �������.'
		return self._ApplyTypes_(1, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetGabarit', None,x1
			, y1, z1, x2, y2, z2
			)

	def GetIntersectionFacesWithBody(self, otherBody=defaultNamedNotOptArg, intersectionFaces1=pythoncom.Missing, intersectionFaces2=pythoncom.Missing, connectedFaces1=pythoncom.Missing
			, connectedFaces2=pythoncom.Missing):
		'���������� ����������������� ����� ��� ����������� ������� ���� � ������.'
		return self._ApplyTypes_(9, 1, (3, 0), ((9, 1), (16396, 2), (16396, 2), (16396, 2), (16396, 2)), 'GetIntersectionFacesWithBody', None,otherBody
			, intersectionFaces1, intersectionFaces2, connectedFaces1, connectedFaces2)

	def IsSolid(self):
		'�������� �� ���� ������� ��� ��������� (TRUE - ������� ����, FALSE - ��������).'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"MultiBodyParts": (7, 2, (11, 0), (), "MultiBodyParts", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBodyCollection(DispatchBaseClass):
	'��������� ������� ��� 3D.'
	CLSID = IID('{CFC49C01-7653-4845-93FD-13428F5D58EC}')
	coclass_clsid = IID('{EEEAB203-43D8-4F04-A7CE-010D9BA419C2}')

	def Add(self, body=defaultNamedNotOptArg):
		'�������� ������� � ����� �������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),body
			)

	def AddAt(self, body=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� ������� ����� �������� � ��������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 0), (3, 0)),body
			, index)

	def AddBefore(self, body=defaultNamedNotOptArg, base=defaultNamedNotOptArg):
		'�������� ������� ����� ���������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((9, 0), (9, 0)),body
			, base)

	def Clear(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	def DetachByBody(self, body=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((9, 0),),body
			)

	def DetachByIndex(self, index=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((3, 0),),index
			)

	def FindIt(self, entity=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((9, 0),),entity
			)

	def First(self):
		'�������� ������ �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetCount(self):
		'�������� ���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'�������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def SetByIndex(self, body=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), ((9, 0), (3, 0)),body
			, index)

	def refresh(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBodyParts(DispatchBaseClass):
	'��������� ������ ����.'
	CLSID = IID('{1E3E9348-DB9B-4967-A62A-B412DF95146A}')
	coclass_clsid = None

	def GetPartSelected(self, index=defaultNamedNotOptArg):
		'�������� ��� ����� ���� � �������� ������� ���������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((3, 0),),index
			)

	def SetGreatPartsSelected(self):
		'�������� ����� ���� �� ���������(������������).'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	def SetPartSelected(self, index=defaultNamedNotOptArg, Select=defaultNamedNotOptArg):
		'���������� ��� ����� ���� � �������� ������� ���������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((3, 0), (11, 0)),index
			, Select)

	def UserBodyPartsChoice(self):
		'��������� ���������� ������� ������ ������ ����.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"AllSelected": (3, 2, (11, 0), (), "AllSelected", None),
		"count": (2, 2, (3, 0), (), "count", None),
	}
	_prop_map_put_ = {
		"AllSelected" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ksBossEvolutionDefinition(DispatchBaseClass):
	'��������� �������� ��������� ��������������.'
	CLSID = IID('{DEEFEFFC-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFEFFE-C3E2-11D6-8734-00C0262CDD2C}')

	def ChooseBodies(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� ���.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseBodies', None)
		return ret

	def ChooseParts(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseParts', None)
		return ret

	def GetPathLength(self, bitVector=defaultNamedNotOptArg):
		'�������� ����� ������ ����������(ST_MIX_MM..ST_MIX_M ������� ���������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (5, 0), ((19, 0),),bitVector
			)

	def GetSketch(self):
		'�������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def GetThinParam(self, thin=pythoncom.Missing, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(5, 1, (11, 0), ((16395, 2), (16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thin
			, thinType, normalThickness, reverseTthickness)

	def PathPartArray(self):
		'�������� ��������� ������� ������ ����������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PathPartArray', None)
		return ret

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'�������� ��������� ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"chooseType": (10, 2, (3, 0), (), "chooseType", None),
		"sketchShiftType": (1, 2, (2, 0), (), "sketchShiftType", None),
	}
	_prop_map_put_ = {
		"chooseType" : ((10, LCID, 4, 0),()),
		"sketchShiftType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBossExtrusionDefinition(DispatchBaseClass):
	'��������� �������� ������������.'
	CLSID = IID('{DEEFEFE4-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFEFE6-C3E2-11D6-8734-00C0262CDD2C}')

	def ChooseBodies(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� ���.'
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseBodies', None)
		return ret

	def ChooseParts(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseParts', None)
		return ret

	def ExtrusionParam(self):
		'��������� ���������� ������������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ExtrusionParam', None)
		return ret

	def GetDepthObject(self, normal=defaultNamedNotOptArg):
		'�������� ������ �������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((11, 0),),normal
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetDepthObject', None)
		return ret

	def GetSideParam(self, side1=defaultNamedNotOptArg, type=pythoncom.Missing, depth=pythoncom.Missing, draftValue=pythoncom.Missing
			, draftOutward=pythoncom.Missing):
		'�������� ��������� ������������ � ���� �������.'
		return self._ApplyTypes_(4, 1, (11, 0), ((11, 1), (16386, 2), (16389, 2), (16389, 2), (16395, 2)), 'GetSideParam', None,side1
			, type, depth, draftValue, draftOutward)

	def GetSketch(self):
		'�������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def GetThinParam(self, thin=defaultNamedNotOptArg, thinType=defaultNamedNotOptArg, normalThickness=defaultNamedNotOptArg, reverseTthickness=defaultNamedNotOptArg):
		'�������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((16395, 0), (16386, 0), (16389, 0), (16389, 0)),thin
			, thinType, normalThickness, reverseTthickness)

	def ResetDepthObject(self, normal=defaultNamedNotOptArg):
		'����� ������� �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((11, 0),),normal
			)

	def SetDepthObject(self, normal=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'���������� ������ �������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((11, 0), (9, 0)),normal
			, obj)

	def SetSideParam(self, side1=defaultNamedNotOptArg, type=0, depth=1.0, draftValue=0.0
			, draftOutward=False):
		'���������� ��������� ������������ � ���� �������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48), (11, 48)),side1
			, type, depth, draftValue, draftOutward)

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'�������� ��������� ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"chooseType": (14, 2, (3, 0), (), "chooseType", None),
		"directionType": (1, 2, (2, 0), (), "directionType", None),
	}
	_prop_map_put_ = {
		"chooseType" : ((14, LCID, 4, 0),()),
		"directionType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBossLoftDefinition(DispatchBaseClass):
	'�������� ������������ �� ��������.'
	CLSID = IID('{DEEFEFED-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFEFEF-C3E2-11D6-8734-00C0262CDD2C}')

	def ChooseBodies(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� ���.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseBodies', None)
		return ret

	def ChooseParts(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseParts', None)
		return ret

	def GetDirectionalLine(self):
		'�������� ������������ �����. ����� � ������� ����� ������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDirectionalLine', None)
		return ret

	def GetLoftParam(self, closed=pythoncom.Missing, flipVertex=pythoncom.Missing, autoPath=pythoncom.Missing):
		'�������� ��������� ��������.'
		return self._ApplyTypes_(1, 1, (11, 0), ((16395, 2), (16395, 2), (16395, 2)), 'GetLoftParam', None,closed
			, flipVertex, autoPath)

	def GetThinParam(self, thin=pythoncom.Missing, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(3, 1, (11, 0), ((16395, 2), (16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thin
			, thinType, normalThickness, reverseTthickness)

	def SetDirectionalLine(self, sketch=defaultNamedNotOptArg):
		'���������� ������������ �����. ����� � ������� ����� ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetLoftParam(self, closed=defaultNamedNotOptArg, flipVertex=defaultNamedNotOptArg, autoPath=defaultNamedNotOptArg):
		'���������� ��������� ��������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((11, 0), (11, 0), (11, 0)),closed
			, flipVertex, autoPath)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def Sketchs(self):
		'������ �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Sketchs', None)
		return ret

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"chooseType": (10, 2, (3, 0), (), "chooseType", None),
	}
	_prop_map_put_ = {
		"chooseType" : ((10, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBossRotatedDefinition(DispatchBaseClass):
	'�������� ������������.'
	CLSID = IID('{2DFACC6A-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{2DFACC6C-C4A4-11D6-8734-00C0262CDD2C}')

	def ChooseBodies(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� ���.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseBodies', None)
		return ret

	def ChooseParts(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseParts', None)
		return ret

	def GetSideParam(self, side1=defaultNamedNotOptArg, angle=defaultNamedNotOptArg):
		'�������� ��������� �������� � ���� �������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((11, 0), (16389, 0)),side1
			, angle)

	def GetSketch(self):
		'�������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def GetThinParam(self, thin=pythoncom.Missing, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(7, 1, (11, 0), ((16395, 2), (16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thin
			, thinType, normalThickness, reverseTthickness)

	def RotatedParam(self):
		'��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RotatedParam', None)
		return ret

	def SetSideParam(self, side1=False, angle=180.0):
		'���������� ��������� �������� � ���� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((11, 48), (5, 48)),side1
			, angle)

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'���������� ��������� ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"chooseType": (12, 2, (3, 0), (), "chooseType", None),
		"directionType": (1, 2, (2, 0), (), "directionType", None),
		"toroidShapeType": (2, 2, (11, 0), (), "toroidShapeType", None),
	}
	_prop_map_put_ = {
		"chooseType" : ((12, LCID, 4, 0),()),
		"directionType" : ((1, LCID, 4, 0),()),
		"toroidShapeType" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBrandLeaderParam(DispatchBaseClass):
	'����� ������� ��� ����������� ���������.'
	CLSID = IID('{3F715E46-97D9-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3F715E48-97D9-11D6-95CE-00C0262D30E3}')

	def GetpPolyline(self):
		'������������ ������ ����������� �����-�������.'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpPolyline', None)
		return ret

	def GetpTextline(self):
		'������������ ������ ����� ������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpTextline', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), (),)

	def SetpPolyline(self, pPolyline=defaultNamedNotOptArg):
		'������������ ������ ����������� �����-�������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((9, 0),),pPolyline
			)

	def SetpTextline(self, pTextLine=defaultNamedNotOptArg):
		'������������ ������ ����� ������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 0),),pTextLine
			)

	_prop_map_get_ = {
		"arrowType": (4, 2, (2, 0), (), "arrowType", None),
		"cText0": (7, 2, (2, 0), (), "cText0", None),
		"cText1": (8, 2, (2, 0), (), "cText1", None),
		"cText2": (9, 2, (3, 0), (), "cText2", None),
		"dirX": (1, 2, (3, 0), (), "dirX", None),
		"style1": (5, 2, (3, 0), (), "style1", None),
		"style2": (6, 2, (3, 0), (), "style2", None),
		"x": (2, 2, (5, 0), (), "x", None),
		"y": (3, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"arrowType" : ((4, LCID, 4, 0),()),
		"cText0" : ((7, LCID, 4, 0),()),
		"cText1" : ((8, LCID, 4, 0),()),
		"cText2" : ((9, LCID, 4, 0),()),
		"dirX" : ((1, LCID, 4, 0),()),
		"style1" : ((5, LCID, 4, 0),()),
		"style2" : ((6, LCID, 4, 0),()),
		"x" : ((2, LCID, 4, 0),()),
		"y" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksBreakDimDrawing(DispatchBaseClass):
	'��������� ��������� ��������� � �������� ������� � �������.'
	CLSID = IID('{7F7D6FBA-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FBC-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"angle": (5, 2, (5, 0), (), "angle", None),
		"length": (6, 2, (3, 0), (), "length", None),
		"pl": (1, 2, (11, 0), (), "pl", None),
		"pt": (2, 2, (2, 0), (), "pt", None),
		"shelfDir": (4, 2, (3, 0), (), "shelfDir", None),
		"textPos": (3, 2, (3, 0), (), "textPos", None),
	}
	_prop_map_put_ = {
		"angle" : ((5, LCID, 4, 0),()),
		"length" : ((6, LCID, 4, 0),()),
		"pl" : ((1, LCID, 4, 0),()),
		"pt" : ((2, LCID, 4, 0),()),
		"shelfDir" : ((4, LCID, 4, 0),()),
		"textPos" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCON(DispatchBaseClass):
	'������ ��������� ����� ����������.'
	CLSID = IID('{C175BFB8-D7D6-4325-BFDA-2A282B9D1119}')
	coclass_clsid = IID('{9CC1A2E2-29A8-49BB-ABF6-792FA2D38014}')

	def GetCount(self):
		'���������� ���������� ��������� ����������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetX1(self, index=defaultNamedNotOptArg):
		'���������� ���������� �1 ����� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (5, 0), ((3, 0),),index
			)

	def GetX2(self, index=defaultNamedNotOptArg):
		'���������� ���������� �2 ����� ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (5, 0), ((3, 0),),index
			)

	def GetXc(self, index=defaultNamedNotOptArg):
		'���������� ���������� � ������ ����������� ����������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (5, 0), ((3, 0),),index
			)

	def GetY1(self, index=defaultNamedNotOptArg):
		'���������� ���������� y1 ����� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (5, 0), ((3, 0),),index
			)

	def GetY2(self, index=defaultNamedNotOptArg):
		'���������� ���������� y2 ����� ����������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (5, 0), ((3, 0),),index
			)

	def GetYc(self, index=defaultNamedNotOptArg):
		'���������� ���������� y ������ ����������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (5, 0), ((3, 0),),index
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCentreParam(DispatchBaseClass):
	'��������� ������� ����������� ������.'
	CLSID = IID('{7F7D6FA5-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FA7-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"angle": (4, 2, (5, 0), (), "angle", None),
		"baseCurve": (1, 2, (3, 0), (), "baseCurve", None),
		"lenXmTail": (11, 2, (5, 0), (), "lenXmTail", None),
		"lenXpTail": (10, 2, (5, 0), (), "lenXpTail", None),
		"lenYmTail": (13, 2, (5, 0), (), "lenYmTail", None),
		"lenYpTail": (12, 2, (5, 0), (), "lenYpTail", None),
		"standXmTail": (7, 2, (11, 0), (), "standXmTail", None),
		"standXpTail": (6, 2, (11, 0), (), "standXpTail", None),
		"standYmTail": (9, 2, (11, 0), (), "standYmTail", None),
		"standYpTail": (8, 2, (11, 0), (), "standYpTail", None),
		"type": (5, 2, (2, 0), (), "type", None),
		"x": (2, 2, (5, 0), (), "x", None),
		"y": (3, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"angle" : ((4, LCID, 4, 0),()),
		"baseCurve" : ((1, LCID, 4, 0),()),
		"lenXmTail" : ((11, LCID, 4, 0),()),
		"lenXpTail" : ((10, LCID, 4, 0),()),
		"lenYmTail" : ((13, LCID, 4, 0),()),
		"lenYpTail" : ((12, LCID, 4, 0),()),
		"standXmTail" : ((7, LCID, 4, 0),()),
		"standXpTail" : ((6, LCID, 4, 0),()),
		"standYmTail" : ((9, LCID, 4, 0),()),
		"standYpTail" : ((8, LCID, 4, 0),()),
		"type" : ((5, LCID, 4, 0),()),
		"x" : ((2, LCID, 4, 0),()),
		"y" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksChamferDefinition(DispatchBaseClass):
	'��������� �������� �����.'
	CLSID = IID('{0307BBAE-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BBB0-C193-11D6-8734-00C0262CDD2C}')

	def GetChamferParam(self, transfer=pythoncom.Missing, distance1=pythoncom.Missing, distance2=pythoncom.Missing):
		'�������� ��������� �����.'
		return self._ApplyTypes_(2, 1, (11, 0), ((16395, 2), (16389, 2), (16389, 2)), 'GetChamferParam', None,transfer
			, distance1, distance2)

	def SetChamferParam(self, transfer=defaultNamedNotOptArg, distance1=defaultNamedNotOptArg, distance2=defaultNamedNotOptArg):
		'�������� ��������� �����.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((11, 0), (5, 0), (5, 0)),transfer
			, distance1, distance2)

	def array(self):
		'������ ��������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'array', None)
		return ret

	_prop_map_get_ = {
		"tangent": (1, 2, (11, 0), (), "tangent", None),
	}
	_prop_map_put_ = {
		"tangent" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksChangeLeaderParam(DispatchBaseClass):
	'���� ���������.'
	CLSID = IID('{391938AE-79B6-4E3B-9815-AC1A31D9EA9D}')
	coclass_clsid = IID('{BC662523-43E2-41FF-A04B-3D92F8097DF9}')

	def GetpPolyline(self):
		'������������ ������ ����������� �����-�������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpPolyline', None)
		return ret

	def GetpTextline(self):
		'������������ ������ ����� ������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpTextline', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

	def SetpPolyline(self, pPolyline=defaultNamedNotOptArg):
		'������������ ������ ����������� �����-�������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),pPolyline
			)

	def SetpTextline(self, pTextLine=defaultNamedNotOptArg):
		'������������ ������ ����� ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((9, 0),),pTextLine
			)

	_prop_map_get_ = {
		"leaderLength": (5, 2, (5, 0), (), "leaderLength", None),
		"signHeight": (4, 2, (5, 0), (), "signHeight", None),
		"signType": (3, 2, (2, 0), (), "signType", None),
		"style": (6, 2, (3, 0), (), "style", None),
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"leaderLength" : ((5, LCID, 4, 0),()),
		"signHeight" : ((4, LCID, 4, 0),()),
		"signType" : ((3, LCID, 4, 0),()),
		"style" : ((6, LCID, 4, 0),()),
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksChar255(DispatchBaseClass):
	'������ ������ ������� 255 ��������.'
	CLSID = IID('{3F715E39-97D9-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3F715E3B-97D9-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"str": (1, 2, (8, 0), (), "str", None),
	}
	_prop_map_put_ = {
		"str" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksChooseBodies(DispatchBaseClass):
	'��������� ������� ����������\t��� ��� ��������� � ��������.'
	CLSID = IID('{E06B18BF-D2AF-4201-99BE-B7FA9EECF7A8}')
	coclass_clsid = IID('{9B59D68B-3502-4FE9-9E09-AC691443BF3E}')

	def BodyCollection(self):
		'�������� ������ ���.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'BodyCollection', None)
		return ret

	_prop_map_get_ = {
		"ChooseBodiesType": (1, 2, (3, 0), (), "ChooseBodiesType", None),
	}
	_prop_map_put_ = {
		"ChooseBodiesType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksChooseMng(DispatchBaseClass):
	'��������� ��������� ������ (���������) ��������.'
	CLSID = IID('{8F2AA755-D9D1-42A0-97BF-C92548CE7232}')
	coclass_clsid = IID('{2280DF87-5688-4082-8FAE-6E4C84249352}')

	def Choose(self, obj=defaultNamedNotOptArg):
		'������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def First(self):
		'������ ������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetCount(self):
		'�������� ����������� ��������� ��������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), (),)

	def GetManagerIndex(self, obj=defaultNamedNotOptArg):
		'�������� ������ ��������� �� ��������� �� ��������� ������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((9, 0),),obj
			)

	def GetObjectByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������ �� �������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectByIndex', None)
		return ret

	def GetObjectType(self, index=defaultNamedNotOptArg):
		'�������� ��� ������� �� �������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((3, 0),),index
			)

	def IsChoosen(self, obj=defaultNamedNotOptArg):
		'������ �� ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def Last(self):
		'��������� ������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'��������� ������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'���������� ������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def UnChoose(self, obj=defaultNamedNotOptArg):
		'����� ����� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def UnChooseAll(self):
		'����� ����� �� ���� ��������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"currentManagerType": (12, 2, (3, 0), (), "currentManagerType", None),
	}
	_prop_map_put_ = {
		"currentManagerType" : ((12, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksChooseParts(DispatchBaseClass):
	'��������� ������� ���������� ��� ����������� ������ � ��������� ��������.'
	CLSID = IID('{08B7A093-D829-44A9-A238-2BFF31770112}')
	coclass_clsid = IID('{9FD4E52C-5B9B-4D07-B788-8D188EF940FD}')

	def PartCollection(self):
		'�������� ������ �����������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PartCollection', None)
		return ret

	_prop_map_get_ = {
		"ChoosePartsType": (1, 2, (3, 0), (), "ChoosePartsType", None),
	}
	_prop_map_put_ = {
		"ChoosePartsType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCircle3dParam(DispatchBaseClass):
	'��������� ���������� 3d Circle.'
	CLSID = IID('{82758442-C9EB-48F7-B304-083C5E64D4E0}')
	coclass_clsid = IID('{4E96B6C2-BF75-4B32-A4E7-7267F60A2593}')

	def GetPlacement(self):
		'��������  �� ����������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	_prop_map_get_ = {
		"radius": (1, 2, (5, 0), (), "radius", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCircleParam(DispatchBaseClass):
	'��������� ����������.'
	CLSID = IID('{7F7D6F87-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6F89-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"rad": (3, 2, (5, 0), (), "rad", None),
		"style": (4, 2, (3, 0), (), "style", None),
		"xc": (1, 2, (5, 0), (), "xc", None),
		"yc": (2, 2, (5, 0), (), "yc", None),
	}
	_prop_map_put_ = {
		"rad" : ((3, LCID, 4, 0),()),
		"style" : ((4, LCID, 4, 0),()),
		"xc" : ((1, LCID, 4, 0),()),
		"yc" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCircularCopyDefinition(DispatchBaseClass):
	'��������� �������� ����������� �� ��������������� �����.'
	CLSID = IID('{0307BB90-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BB92-C193-11D6-8734-00C0262CDD2C}')

	def DeletedCollection(self):
		'�������� ������ �������� ��������� �����.'
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DeletedCollection', None)
		return ret

	def GetAxis(self):
		'��� �������� �����������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAxis', None)
		return ret

	def GetCopyParamAlongDir(self, count=pythoncom.Missing, step=pythoncom.Missing, factor=pythoncom.Missing, dir=defaultNamedNotOptArg):
		'�������� ��������� �����������.'
		return self._ApplyTypes_(11, 1, (11, 0), ((16387, 2), (16389, 2), (16395, 2), (11, 1)), 'GetCopyParamAlongDir', None,count
			, step, factor, dir)

	def GetOperationArray(self):
		'�������� ��������� ������� �������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetOperationArray', None)
		return ret

	def SetAxis(self, axis=defaultNamedNotOptArg):
		'��� �������� �����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),axis
			)

	def SetCopyParamAlongDir(self, count=defaultNamedNotOptArg, step=defaultNamedNotOptArg, factor=defaultNamedNotOptArg, dir=defaultNamedNotOptArg):
		'���������� ��������� �����������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((3, 0), (5, 0), (11, 0), (11, 0)),count
			, step, factor, dir)

	_prop_map_get_ = {
		"count1": (1, 2, (3, 0), (), "count1", None),
		"count2": (4, 2, (3, 0), (), "count2", None),
		"factor1": (3, 2, (11, 0), (), "factor1", None),
		"factor2": (6, 2, (11, 0), (), "factor2", None),
		"geomArray": (14, 2, (11, 0), (), "geomArray", None),
		"inverce": (7, 2, (11, 0), (), "inverce", None),
		"step1": (2, 2, (5, 0), (), "step1", None),
		"step2": (5, 2, (5, 0), (), "step2", None),
	}
	_prop_map_put_ = {
		"count1" : ((1, LCID, 4, 0),()),
		"count2" : ((4, LCID, 4, 0),()),
		"factor1" : ((3, LCID, 4, 0),()),
		"factor2" : ((6, LCID, 4, 0),()),
		"geomArray" : ((14, LCID, 4, 0),()),
		"inverce" : ((7, LCID, 4, 0),()),
		"step1" : ((2, LCID, 4, 0),()),
		"step2" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCircularPartArrayDefinition(DispatchBaseClass):
	'��������� �������� ������ ����������� �� ��������������� �����.'
	CLSID = IID('{DDD05143-C180-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DDD05145-C180-11D6-8734-00C0262CDD2C}')

	def DeletedCollection(self):
		'�������� ������ �������� ��������� �����.'
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DeletedCollection', None)
		return ret

	def GetAxis(self):
		'�������� ��� �������� �����������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAxis', None)
		return ret

	def GetCopyParamAlongDir(self, count=pythoncom.Missing, step=pythoncom.Missing, factor=pythoncom.Missing, dir=defaultNamedNotOptArg):
		'�������� ��������� �����������.'
		return self._ApplyTypes_(11, 1, (11, 0), ((16387, 2), (16389, 2), (16395, 2), (11, 1)), 'GetCopyParamAlongDir', None,count
			, step, factor, dir)

	def PartArray(self):
		'�������� ��������� ������� �������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PartArray', None)
		return ret

	def SetAxis(self, axis=defaultNamedNotOptArg):
		'������ ��� �������� �����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),axis
			)

	def SetCopyParamAlongDir(self, count=defaultNamedNotOptArg, step=defaultNamedNotOptArg, factor=defaultNamedNotOptArg, dir=defaultNamedNotOptArg):
		'���������� ��������� �����������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((3, 0), (5, 0), (11, 0), (11, 0)),count
			, step, factor, dir)

	_prop_map_get_ = {
		"count1": (1, 2, (3, 0), (), "count1", None),
		"count2": (4, 2, (3, 0), (), "count2", None),
		"factor1": (3, 2, (11, 0), (), "factor1", None),
		"factor2": (6, 2, (11, 0), (), "factor2", None),
		"inverce": (7, 2, (11, 0), (), "inverce", None),
		"keepAngle": (14, 2, (11, 0), (), "keepAngle", None),
		"step1": (2, 2, (5, 0), (), "step1", None),
		"step2": (5, 2, (5, 0), (), "step2", None),
	}
	_prop_map_put_ = {
		"count1" : ((1, LCID, 4, 0),()),
		"count2" : ((4, LCID, 4, 0),()),
		"factor1" : ((3, LCID, 4, 0),()),
		"factor2" : ((6, LCID, 4, 0),()),
		"inverce" : ((7, LCID, 4, 0),()),
		"keepAngle" : ((14, LCID, 4, 0),()),
		"step1" : ((2, LCID, 4, 0),()),
		"step2" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksColorParam(DispatchBaseClass):
	'�������� ����� �������.'
	CLSID = IID('{2DFACC61-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{2DFACC63-C4A4-11D6-8734-00C0262CDD2C}')

	def Clear(self):
		'�������� �������� ����� �������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ambient": (2, 2, (5, 0), (), "ambient", None),
		"color": (1, 2, (3, 0), (), "color", None),
		"diffuse": (3, 2, (5, 0), (), "diffuse", None),
		"emission": (7, 2, (5, 0), (), "emission", None),
		"shininess": (5, 2, (5, 0), (), "shininess", None),
		"specularity": (4, 2, (5, 0), (), "specularity", None),
		"transparency": (6, 2, (5, 0), (), "transparency", None),
		"useColor": (9, 2, (3, 0), (), "useColor", None),
	}
	_prop_map_put_ = {
		"ambient" : ((2, LCID, 4, 0),()),
		"color" : ((1, LCID, 4, 0),()),
		"diffuse" : ((3, LCID, 4, 0),()),
		"emission" : ((7, LCID, 4, 0),()),
		"shininess" : ((5, LCID, 4, 0),()),
		"specularity" : ((4, LCID, 4, 0),()),
		"transparency" : ((6, LCID, 4, 0),()),
		"useColor" : ((9, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksColumnInfoParam(DispatchBaseClass):
	'�������������� ��������� ��� ������ ������� ���������� ��������.'
	CLSID = IID('{CE0D05E1-9B2A-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{CE0D05E3-9B2A-11D6-95CE-00C0262D30E3}')

	def GetColumns(self):
		'������ ������ ���������� � ��������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetColumns', None)
		return ret

	def GetFieldEnum(self):
		'������ ������ ������������ (������).'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFieldEnum', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	def SetColumns(self, fieldEnum=defaultNamedNotOptArg):
		'�������� ������ ���������� � ��������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),fieldEnum
			)

	def SetFieldEnum(self, fieldEnum=defaultNamedNotOptArg):
		'�������� ������ ������������ (������).'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((9, 0),),fieldEnum
			)

	_prop_map_get_ = {
		"Def": (4, 2, (8, 0), (), "def", None),
		"flagEnum": (5, 2, (11, 0), (), "flagEnum", None),
		"header": (2, 2, (8, 0), (), "header", None),
		"key": (3, 2, (2, 0), (), "key", None),
		"type": (1, 2, (2, 0), (), "type", None),
	}
	_prop_map_put_ = {
		"Def" : ((4, LCID, 4, 0),()),
		"flagEnum" : ((5, LCID, 4, 0),()),
		"header" : ((2, LCID, 4, 0),()),
		"key" : ((3, LCID, 4, 0),()),
		"type" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksComponentPositioner(DispatchBaseClass):
	'��������� ���������� ���������� ����������� � ������.'
	CLSID = IID('{508B5962-DF59-4CEE-8611-AD10FDF0C811}')
	coclass_clsid = IID('{7DAB018D-9EF9-4D0F-84BB-54B3DC0558D3}')

	def Finish(self):
		'��������� �����������'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	def MoveComponent(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg):
		'����������� ����������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0)),x
			, y, z)

	def Prepare(self, part=defaultNamedNotOptArg, positionerType=defaultNamedNotOptArg):
		'������������� � ����������� ����������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((9, 0), (3, 0)),part
			, positionerType)

	def RotateComponent(self, angl=defaultNamedNotOptArg):
		'������������� � �������� ����������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((5, 0),),angl
			)

	def SetAxis(self, axis=defaultNamedNotOptArg):
		'���������� ���.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0),),axis
			)

	def SetAxisByPoints(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, z1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg
			, y2=defaultNamedNotOptArg, z2=defaultNamedNotOptArg):
		'���������� ��� �� ������ .'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0)),x1
			, y1, z1, x2, y2, z2
			)

	def SetDragPoint(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg):
		'���������� ����� ������� ( �����).'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0)),x
			, y, z)

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'���������� ���������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),plane
			)

	def SetPlaneByPlacement(self, plane=defaultNamedNotOptArg):
		'���������� ��������� �� ��.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((9, 0),),plane
			)

	def SetPlaneByPoints(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, z1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg
			, y2=defaultNamedNotOptArg, z2=defaultNamedNotOptArg, x3=defaultNamedNotOptArg, y3=defaultNamedNotOptArg, z3=defaultNamedNotOptArg):
		'���������� ��������� �� ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0)),x1
			, y1, z1, x2, y2, z2
			, x3, y3, z3)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksConeParam(DispatchBaseClass):
	'��������� ���������� ���������� �����������.'
	CLSID = IID('{CCFA0D95-0834-4F92-988B-6E477AD67589}')
	coclass_clsid = IID('{3940C963-446D-4701-883C-A93BBDAC5469}')

	def GetPlacement(self):
		'�������� �� ���������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	_prop_map_get_ = {
		"angle": (3, 2, (5, 0), (), "angle", None),
		"height": (2, 2, (5, 0), (), "height", None),
		"radius": (1, 2, (5, 0), (), "radius", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksConicArcParam(DispatchBaseClass):
	'��������� ��� ���������� ����������� �������.'
	CLSID = IID('{7F7D6FA2-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FA4-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"A": (1, 2, (5, 0), (), "A", None),
		"B": (2, 2, (5, 0), (), "B", None),
		"C": (3, 2, (5, 0), (), "C", None),
		"D": (4, 2, (5, 0), (), "D", None),
		"E": (5, 2, (5, 0), (), "E", None),
		"F": (6, 2, (5, 0), (), "F", None),
		"style": (11, 2, (3, 0), (), "style", None),
		"x1": (7, 2, (5, 0), (), "x1", None),
		"x2": (9, 2, (5, 0), (), "x2", None),
		"y1": (8, 2, (5, 0), (), "y1", None),
		"y2": (10, 2, (5, 0), (), "y2", None),
	}
	_prop_map_put_ = {
		"A" : ((1, LCID, 4, 0),()),
		"B" : ((2, LCID, 4, 0),()),
		"C" : ((3, LCID, 4, 0),()),
		"D" : ((4, LCID, 4, 0),()),
		"E" : ((5, LCID, 4, 0),()),
		"F" : ((6, LCID, 4, 0),()),
		"style" : ((11, LCID, 4, 0),()),
		"x1" : ((7, LCID, 4, 0),()),
		"x2" : ((9, LCID, 4, 0),()),
		"y1" : ((8, LCID, 4, 0),()),
		"y2" : ((10, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksConicSpiralDefinition(DispatchBaseClass):
	'������� ����������.'
	CLSID = IID('{0307BB9C-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BB9E-C193-11D6-8734-00C0262CDD2C}')

	def GetCurve3D(self):
		'�������� ��������� �� ��������� �������������� ������.'
		ret = self._oleobj_.InvokeTypes(28, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurve3D', None)
		return ret

	def GetHeightObject(self):
		'�������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetHeightObject', None)
		return ret

	def GetInitialDiamObject(self):
		'�������� ������ ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetInitialDiamObject', None)
		return ret

	def GetLocation(self, x=pythoncom.Missing, y=pythoncom.Missing):
		'�������� ����� �������� �������.'
		return self._ApplyTypes_(19, 1, (11, 0), ((16389, 2), (16389, 2)), 'GetLocation', None,x
			, y)

	def GetPlane(self):
		'�������� ������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def GetSketch(self):
		'�������� ��������� �� ��������� ������ ��������.'
		ret = self._oleobj_.InvokeTypes(27, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def GetTerminalDiamObject(self):
		'�������� ������ ��������� ��������.'
		ret = self._oleobj_.InvokeTypes(25, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTerminalDiamObject', None)
		return ret

	def SetHeightObject(self, heightObject=defaultNamedNotOptArg):
		'�������� ������ ������.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (11, 0), ((9, 0),),heightObject
			)

	def SetInitialDiamObject(self, initialDiamObject=defaultNamedNotOptArg):
		'�������� ������ ���������� ��������.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), ((9, 0),),initialDiamObject
			)

	def SetLocation(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg):
		'�������� ����� �������� �������.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((5, 0), (5, 0)),x
			, y)

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'�������� ������� ��������� �������.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((9, 0),),plane
			)

	def SetTerminalDiamObject(self, terminalDiamObject=defaultNamedNotOptArg):
		'�������� ������ ��������� ��������.'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (11, 0), ((9, 0),),terminalDiamObject
			)

	_prop_map_get_ = {
		"buildDir": (5, 2, (11, 0), (), "buildDir", None),
		"buildMode": (4, 2, (2, 0), (), "buildMode", None),
		"firstAngle": (15, 2, (5, 0), (), "firstAngle", None),
		"height": (6, 2, (5, 0), (), "height", None),
		"heightAdd": (8, 2, (5, 0), (), "heightAdd", None),
		"heightAddHow": (9, 2, (11, 0), (), "heightAddHow", None),
		"heightType": (7, 2, (2, 0), (), "heightType", None),
		"initialDiam": (10, 2, (5, 0), (), "initialDiam", None),
		"initialDiamType": (11, 2, (2, 0), (), "initialDiamType", None),
		"step": (2, 2, (5, 0), (), "step", None),
		"terminalDiam": (12, 2, (5, 0), (), "terminalDiam", None),
		"terminalDiamType": (13, 2, (2, 0), (), "terminalDiamType", None),
		"tiltAngle": (16, 2, (5, 0), (), "tiltAngle", None),
		"tiltAngleHow": (14, 2, (11, 0), (), "tiltAngleHow", None),
		"turn": (1, 2, (5, 0), (), "turn", None),
		"turnDir": (3, 2, (11, 0), (), "turnDir", None),
	}
	_prop_map_put_ = {
		"buildDir" : ((5, LCID, 4, 0),()),
		"buildMode" : ((4, LCID, 4, 0),()),
		"firstAngle" : ((15, LCID, 4, 0),()),
		"height" : ((6, LCID, 4, 0),()),
		"heightAdd" : ((8, LCID, 4, 0),()),
		"heightAddHow" : ((9, LCID, 4, 0),()),
		"heightType" : ((7, LCID, 4, 0),()),
		"initialDiam" : ((10, LCID, 4, 0),()),
		"initialDiamType" : ((11, LCID, 4, 0),()),
		"step" : ((2, LCID, 4, 0),()),
		"terminalDiam" : ((12, LCID, 4, 0),()),
		"terminalDiamType" : ((13, LCID, 4, 0),()),
		"tiltAngle" : ((16, LCID, 4, 0),()),
		"tiltAngleHow" : ((14, LCID, 4, 0),()),
		"turn" : ((1, LCID, 4, 0),()),
		"turnDir" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksConjunctivePointDefinition(DispatchBaseClass):
	"��������� ������� '����������������� �����'."
	CLSID = IID('{177CBAF3-87E6-4376-B6A9-669C0E661BFF}')
	coclass_clsid = IID('{88BD7F23-21A6-4C90-B784-0B38FB7FD0F3}')

	def GetEdge(self):
		'�������� ��������� �� ��������� �������� ������� ��� ����������� ������� �����������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEdge', None)
		return ret

	def GetPoint(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� �����.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetPoint', None,x
			, y, z)

	def GetVertex(self):
		'�������� ��������� �� ��������� ������� �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetVertex', None)
		return ret

	def SetEdge(self, val=defaultNamedNotOptArg):
		'���������� ��������� �� ��������� �������� ������� ��� ����������� ������� �����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetVertex(self, val=defaultNamedNotOptArg):
		'���������� ��������� �� ��������� ������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"direction": (1, 2, (11, 0), (), "direction", None),
	}
	_prop_map_put_ = {
		"direction" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksConstraintParam(DispatchBaseClass):
	'��������� ��� ��������������� �����������.'
	CLSID = IID('{862E250D-9DB1-47E8-8EE2-9BE2D2453D5A}')
	coclass_clsid = IID('{77C095F7-3ABC-4292-B9E1-C112620AFC56}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"constrType": (1, 2, (2, 0), (), "constrType", None),
		"index": (2, 2, (3, 0), (), "index", None),
		"partner": (3, 2, (3, 0), (), "partner", None),
		"partnerIndex": (4, 2, (3, 0), (), "partnerIndex", None),
	}
	_prop_map_put_ = {
		"constrType" : ((1, LCID, 4, 0),()),
		"index" : ((2, LCID, 4, 0),()),
		"partner" : ((3, LCID, 4, 0),()),
		"partnerIndex" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksContourParam(DispatchBaseClass):
	'��������� �������.'
	CLSID = IID('{E79C2504-9584-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{E79C2506-9584-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"style": (1, 2, (3, 0), (), "style", None),
	}
	_prop_map_put_ = {
		"style" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksControlPointDefinition(DispatchBaseClass):
	"��������� ������� '����������� �����'."
	CLSID = IID('{BC4C15A4-16E9-4CFA-A33E-CC86BA2FB546}')
	coclass_clsid = IID('{3DA1922B-1FAB-4990-8D9A-8F03AFDB18D9}')

	def GetPoint(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� �����.'
		return self._ApplyTypes_(3, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetPoint', None,x
			, y, z)

	def GetVertex(self):
		'�������� ��������� �� ��������� ������� �������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetVertex', None)
		return ret

	def SetVertex(self, val=defaultNamedNotOptArg):
		'���������� ��������� �� ��������� ������� �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCoordinate3dCollection(DispatchBaseClass):
	'��������� ��������� ��������� ����� � 3D.'
	CLSID = IID('{E4091969-1C4E-4959-8D93-C2421564418B}')
	coclass_clsid = IID('{17150452-8320-4721-9765-13353F08AE7E}')

	def GetByIndex(self, index=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ���������� ����� �� �������.'
		return self._ApplyTypes_(2, 1, (11, 0), ((3, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetByIndex', None,index
			, x, y, z)

	def GetCount(self):
		'�������� ���������� �����.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetSafeArray(self, array=pythoncom.Missing):
		'������������ SAFEARRAY ��������� �����.'
		return self._ApplyTypes_(3, 1, (11, 0), ((16396, 2),), 'GetSafeArray', None,array
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCopyObjectParam(DispatchBaseClass):
	'��������� ���������� ��� ����������� ������� 2d ���������.'
	CLSID = IID('{AACAD820-7790-46EB-B17F-06AE42215ED7}')
	coclass_clsid = IID('{8867DEAC-C699-41B6-BD3D-C470A52B1B9C}')

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"angle": (8, 2, (5, 0), (), "angle", None),
		"attrCopy": (9, 2, (11, 0), (), "attrCopy", None),
		"dimLineScale": (10, 2, (11, 0), (), "dimLineScale", None),
		"hyperLinksCopy": (13, 2, (11, 0), (), "hyperLinksCopy", None),
		"objRef": (2, 2, (3, 0), (), "objRef", None),
		"scale": (7, 2, (5, 0), (), "scale", None),
		"spcObjCopy": (11, 2, (11, 0), (), "spcObjCopy", None),
		"storagesCopy": (12, 2, (11, 0), (), "storagesCopy", None),
		"xNew": (5, 2, (5, 0), (), "xNew", None),
		"xOld": (3, 2, (5, 0), (), "xOld", None),
		"yNew": (6, 2, (5, 0), (), "yNew", None),
		"yOld": (4, 2, (5, 0), (), "yOld", None),
	}
	_prop_map_put_ = {
		"angle" : ((8, LCID, 4, 0),()),
		"attrCopy" : ((9, LCID, 4, 0),()),
		"dimLineScale" : ((10, LCID, 4, 0),()),
		"hyperLinksCopy" : ((13, LCID, 4, 0),()),
		"objRef" : ((2, LCID, 4, 0),()),
		"scale" : ((7, LCID, 4, 0),()),
		"spcObjCopy" : ((11, LCID, 4, 0),()),
		"storagesCopy" : ((12, LCID, 4, 0),()),
		"xNew" : ((5, LCID, 4, 0),()),
		"xOld" : ((3, LCID, 4, 0),()),
		"yNew" : ((6, LCID, 4, 0),()),
		"yOld" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCornerParam(DispatchBaseClass):
	'��������� ����� ��� ��������������� � ���������������.'
	CLSID = IID('{E79C2501-9584-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{E79C2503-9584-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"fillet": (2, 2, (11, 0), (), "fillet", None),
		"index": (1, 2, (3, 0), (), "index", None),
		"l1": (3, 2, (5, 0), (), "l1", None),
		"l2": (4, 2, (5, 0), (), "l2", None),
	}
	_prop_map_put_ = {
		"fillet" : ((2, LCID, 4, 0),()),
		"index" : ((1, LCID, 4, 0),()),
		"l1" : ((3, LCID, 4, 0),()),
		"l2" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCurve3D(DispatchBaseClass):
	'��������� �������������� ������ � ���������� ������������.'
	CLSID = IID('{7572648A-D4EE-41FE-8D74-EC7D1F91BDE2}')
	coclass_clsid = IID('{54152184-0B08-4DFB-8249-4579A7368BF4}')

	def CalculatePolygon(self, step=defaultNamedNotOptArg):
		'��������� �������.'
		return self._ApplyTypes_(24, 1, (12, 0), ((5, 0),), 'CalculatePolygon', None,step
			)

	def GetCurveParam(self):
		'��������� �����, ����������, �������, nurbs ��� NULL.'
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurveParam', None)
		return ret

	def GetDerivativeT(self, paramT=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'������ ����������� �� T.'
		return self._ApplyTypes_(4, 1, (11, 0), ((5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeT', None,paramT
			, x, y, z)

	def GetDerivativeTT(self, paramT=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'������ ����������� �� T.'
		return self._ApplyTypes_(5, 1, (11, 0), ((5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeTT', None,paramT
			, x, y, z)

	def GetDerivativeTTT(self, paramT=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'������ ����������� �� T.'
		return self._ApplyTypes_(6, 1, (11, 0), ((5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeTTT', None,paramT
			, x, y, z)

	def GetGabarit(self, x1=pythoncom.Missing, y1=pythoncom.Missing, z1=pythoncom.Missing, x2=pythoncom.Missing
			, y2=pythoncom.Missing, z2=pythoncom.Missing):
		'������ ������� ������.'
		return self._ApplyTypes_(12, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetGabarit', None,x1
			, y1, z1, x2, y2, z2
			)

	def GetLength(self, bitVector=defaultNamedNotOptArg):
		'�������� ����� ������ (ST_MIX_MM..ST_MIX_M ������� ���������.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (5, 0), ((19, 0),),bitVector
			)

	def GetMetricLength(self, startParam=defaultNamedNotOptArg, endParam=defaultNamedNotOptArg):
		'����������� ����� ������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (5, 0), ((5, 0), (5, 0)),startParam
			, endParam)

	def GetNormal(self, paramT=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������.'
		return self._ApplyTypes_(3, 1, (11, 0), ((5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetNormal', None,paramT
			, x, y, z)

	def GetNurbs3dParam(self):
		'�������� ��������� ������ � Nurbs-�������������.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNurbs3dParam', None)
		return ret

	def GetParamMax(self):
		'�������� �������� ��������� ��������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (5, 0), (),)

	def GetParamMin(self):
		'�������� �������� ��������� ���������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (5, 0), (),)

	def GetPoint(self, paramT=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'����� �� ������.'
		return self._ApplyTypes_(1, 1, (11, 0), ((5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetPoint', None,paramT
			, x, y, z)

	def GetTangentVector(self, paramT=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������������� ������ (���������������).'
		return self._ApplyTypes_(2, 1, (11, 0), ((5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetTangentVector', None,paramT
			, x, y, z)

	def IsArc(self):
		'�������� �� ������ �����.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), (),)

	def IsCircle(self):
		'�������� �� ������ �����������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), (),)

	def IsClosed(self):
		'����������� ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	def IsDegenerate(self):
		'�������� ������������� ������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), (),)

	def IsEllipse(self):
		'�������� �� ������ ��������.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), (),)

	def IsLineSeg(self):
		'�������� �� ������ ������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), (),)

	def IsNurbs(self):
		'�������� �� ������ �������.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), (),)

	def IsPeriodic(self):
		'������������� ��������� ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	def IsPlanar(self):
		'�������� �� ������ �������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), (),)

	def NearPointProjection(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg, t=pythoncom.Missing
			, ext=defaultNamedNotOptArg):
		'�������� ��������� �������� ����� �� ������.'
		return self._ApplyTypes_(22, 1, (11, 0), ((5, 1), (5, 1), (5, 1), (16389, 2), (11, 1)), 'NearPointProjection', None,x
			, y, z, t, ext)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCurveCopyDefinition(DispatchBaseClass):
	'��������� �������� ����������� �� ������.'
	CLSID = IID('{0307BB93-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BB95-C193-11D6-8734-00C0262CDD2C}')

	def CurveArray(self):
		'�������� ��������� ������� ������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CurveArray', None)
		return ret

	def DeletedCollection(self):
		'�������� ������ �������� ��������� �����.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DeletedCollection', None)
		return ret

	def OperationArray(self):
		'�������� ��������� ������� �������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'OperationArray', None)
		return ret

	_prop_map_get_ = {
		"count": (1, 2, (3, 0), (), "count", None),
		"factor": (3, 2, (11, 0), (), "factor", None),
		"fullCurve": (5, 2, (11, 0), (), "fullCurve", None),
		"geomArray": (10, 2, (11, 0), (), "geomArray", None),
		"keepAngle": (4, 2, (11, 0), (), "keepAngle", None),
		"sence": (6, 2, (11, 0), (), "sence", None),
		"step": (2, 2, (5, 0), (), "step", None),
	}
	_prop_map_put_ = {
		"count" : ((1, LCID, 4, 0),()),
		"factor" : ((3, LCID, 4, 0),()),
		"fullCurve" : ((5, LCID, 4, 0),()),
		"geomArray" : ((10, LCID, 4, 0),()),
		"keepAngle" : ((4, LCID, 4, 0),()),
		"sence" : ((6, LCID, 4, 0),()),
		"step" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ksCurvePartArrayDefinition(DispatchBaseClass):
	'��������� �������� ������ ����������� ����� ������.'
	CLSID = IID('{DDD05146-C180-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DDD05148-C180-11D6-8734-00C0262CDD2C}')

	def CurveArray(self):
		'�������� ��������� ������� ������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CurveArray', None)
		return ret

	def DeletedCollection(self):
		'�������� ������ �������� ��������� �����.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DeletedCollection', None)
		return ret

	def PartArray(self):
		'�������� ��������� ������� �������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PartArray', None)
		return ret

	_prop_map_get_ = {
		"count": (1, 2, (3, 0), (), "count", None),
		"factor": (3, 2, (11, 0), (), "factor", None),
		"fullCurve": (5, 2, (11, 0), (), "fullCurve", None),
		"keepAngle": (4, 2, (11, 0), (), "keepAngle", None),
		"sence": (6, 2, (11, 0), (), "sence", None),
		"step": (2, 2, (5, 0), (), "step", None),
	}
	_prop_map_put_ = {
		"count" : ((1, LCID, 4, 0),()),
		"factor" : ((3, LCID, 4, 0),()),
		"fullCurve" : ((5, LCID, 4, 0),()),
		"keepAngle" : ((4, LCID, 4, 0),()),
		"sence" : ((6, LCID, 4, 0),()),
		"step" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ksCurvePattern(DispatchBaseClass):
	'������� ��������� ������.'
	CLSID = IID('{910EC544-958D-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{910EC546-958D-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"invisibleSeg": (2, 2, (5, 0), (), "invisibleSeg", None),
		"visibleSeg": (1, 2, (5, 0), (), "visibleSeg", None),
	}
	_prop_map_put_ = {
		"invisibleSeg" : ((2, LCID, 4, 0),()),
		"visibleSeg" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCurvePatternEx(DispatchBaseClass):
	'��������� ������� ��������� ������ �����������.'
	CLSID = IID('{910EC549-958D-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{910EC54B-958D-11D6-95CE-00C0262D30E3}')

	def GetCurvePicture(self):
		'������ �������� � ���� �������� ���������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurvePicture', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), (),)

	def SetCurvePicture(self, picture=defaultNamedNotOptArg):
		'�������� �������� � ���� �������� ���������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),picture
			)

	_prop_map_get_ = {
		"dx": (3, 2, (5, 0), (), "dx", None),
		"dy": (4, 2, (5, 0), (), "dy", None),
		"frwName": (6, 2, (8, 0), (), "frwName", None),
		"invisibleSeg": (2, 2, (5, 0), (), "invisibleSeg", None),
		"pictureType": (5, 2, (2, 0), (), "pictureType", None),
		"visibleSeg": (1, 2, (5, 0), (), "visibleSeg", None),
	}
	_prop_map_put_ = {
		"dx" : ((3, LCID, 4, 0),()),
		"dy" : ((4, LCID, 4, 0),()),
		"frwName" : ((6, LCID, 4, 0),()),
		"invisibleSeg" : ((2, LCID, 4, 0),()),
		"pictureType" : ((5, LCID, 4, 0),()),
		"visibleSeg" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCurvePicture(DispatchBaseClass):
	'��������� ���������� ��� �������� �����.'
	CLSID = IID('{910EC541-958D-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{910EC543-958D-11D6-95CE-00C0262D30E3}')

	def GetFill(self):
		'������ ������������ ������ �����, ����������� ������� �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFill', None)
		return ret

	def GetPolygon(self):
		'������ ������������ ������ ���������, ����������� ��������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPolygon', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	def SetFill(self, fill=defaultNamedNotOptArg):
		'�������� ������������ ������ �����, ����������� ������� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),fill
			)

	def SetPolygon(self, polygon=defaultNamedNotOptArg):
		'�������� ������������ ������ ���������, ����������� ��������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),polygon
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCurveStyleParam(DispatchBaseClass):
	'����� ������.'
	CLSID = IID('{910EC54C-958D-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{910EC54E-958D-11D6-95CE-00C0262D30E3}')

	def GetPPattern(self, type=defaultNamedNotOptArg):
		'������ ������ ���������� �������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),type
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPPattern', None)
		return ret

	def GetPropertyCurve(self, val=defaultNamedNotOptArg):
		'�������� �������� �������� �����.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((3, 0),),val
			)

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

	def SetPPattern(self, pattern=defaultNamedNotOptArg):
		'�������� ������ ���������� �������� ��������� ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((9, 0),),pattern
			)

	def SetPropertyCurve(self, val=defaultNamedNotOptArg, state=defaultNamedNotOptArg):
		'���������� �������� �������� �����.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((3, 0), (11, 0)),val
			, state)

	_prop_map_get_ = {
		"color": (2, 2, (3, 0), (), "color", None),
		"curveType": (5, 2, (2, 0), (), "curveType", None),
		"even": (6, 2, (2, 0), (), "even", None),
		"name": (1, 2, (8, 0), (), "name", None),
		"paperWidth": (3, 2, (5, 0), (), "paperWidth", None),
		"screenWidth": (4, 2, (2, 0), (), "screenWidth", None),
		"widthPen": (12, 2, (2, 0), (), "widthPen", None),
	}
	_prop_map_put_ = {
		"color" : ((2, LCID, 4, 0),()),
		"curveType" : ((5, LCID, 4, 0),()),
		"even" : ((6, LCID, 4, 0),()),
		"name" : ((1, LCID, 4, 0),()),
		"paperWidth" : ((3, LCID, 4, 0),()),
		"screenWidth" : ((4, LCID, 4, 0),()),
		"widthPen" : ((12, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCutByPlaneDefinition(DispatchBaseClass):
	'��������� �������� ������� ����������.'
	CLSID = IID('{DEEFF005-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF007-C3E2-11D6-8734-00C0262CDD2C}')

	def ChooseBodies(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� ���.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseBodies', None)
		return ret

	def ChooseParts(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseParts', None)
		return ret

	def GetPlane(self):
		'�������� ���������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'������ ���������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),plane
			)

	_prop_map_get_ = {
		"chooseType": (5, 2, (3, 0), (), "chooseType", None),
		"direction": (1, 2, (11, 0), (), "direction", None),
	}
	_prop_map_put_ = {
		"chooseType" : ((5, LCID, 4, 0),()),
		"direction" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCutBySketchDefinition(DispatchBaseClass):
	'��������� �������� ������� �������.'
	CLSID = IID('{DEEFF008-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF00A-C3E2-11D6-8734-00C0262CDD2C}')

	def ChooseBodies(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� ���.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseBodies', None)
		return ret

	def ChooseParts(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseParts', None)
		return ret

	def GetSketch(self):
		'�������� �����.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'������ �����.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	_prop_map_get_ = {
		"chooseType": (5, 2, (3, 0), (), "chooseType", None),
		"direction": (1, 2, (11, 0), (), "direction", None),
	}
	_prop_map_put_ = {
		"chooseType" : ((5, LCID, 4, 0),()),
		"direction" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCutEvolutionDefinition(DispatchBaseClass):
	'��������� �������� �������� �������������.'
	CLSID = IID('{DEEFEFFF-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF001-C3E2-11D6-8734-00C0262CDD2C}')

	def ChooseBodies(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� ���.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseBodies', None)
		return ret

	def ChooseParts(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseParts', None)
		return ret

	def GetPathLength(self, bitVector=defaultNamedNotOptArg):
		'�������� ����� ������ ����������(ST_MIX_MM..ST_MIX_M ������� ���������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (5, 0), ((19, 0),),bitVector
			)

	def GetSketch(self):
		'�������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def GetThinParam(self, thin=pythoncom.Missing, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16395, 2), (16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thin
			, thinType, normalThickness, reverseTthickness)

	def PathPartArray(self):
		'�������� ��������� ������� ������ ����������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PathPartArray', None)
		return ret

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'�������� ��������� ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"chooseType": (10, 2, (3, 0), (), "chooseType", None),
		"cut": (2, 2, (11, 0), (), "cut", None),
		"sketchShiftType": (1, 2, (2, 0), (), "sketchShiftType", None),
	}
	_prop_map_put_ = {
		"chooseType" : ((10, LCID, 4, 0),()),
		"cut" : ((2, LCID, 4, 0),()),
		"sketchShiftType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCutExtrusionDefinition(DispatchBaseClass):
	'��������� �������� ���������.'
	CLSID = IID('{DEEFEFE7-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFEFE9-C3E2-11D6-8734-00C0262CDD2C}')

	def ChooseBodies(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� ���.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseBodies', None)
		return ret

	def ChooseParts(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(16, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseParts', None)
		return ret

	def ExtrusionParam(self):
		'��������� ���������� ������������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ExtrusionParam', None)
		return ret

	def GetDepthObject(self, normal=defaultNamedNotOptArg):
		'�������� ������ �������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), ((11, 0),),normal
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetDepthObject', None)
		return ret

	def GetSideParam(self, side1=defaultNamedNotOptArg, type=pythoncom.Missing, depth=pythoncom.Missing, draftValue=pythoncom.Missing
			, draftOutward=pythoncom.Missing):
		'�������� ��������� ������������ � ���� �������.'
		return self._ApplyTypes_(5, 1, (11, 0), ((11, 1), (16386, 2), (16389, 2), (16389, 2), (16395, 2)), 'GetSideParam', None,side1
			, type, depth, draftValue, draftOutward)

	def GetSketch(self):
		'�������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def GetThinParam(self, thin=pythoncom.Missing, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(7, 1, (11, 0), ((16395, 2), (16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thin
			, thinType, normalThickness, reverseTthickness)

	def ResetDepthObject(self, normal=defaultNamedNotOptArg):
		'����� ������� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((11, 0),),normal
			)

	def SetDepthObject(self, normal=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'���������� ������ �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((11, 0), (9, 0)),normal
			, obj)

	def SetSideParam(self, side1=defaultNamedNotOptArg, type=0, depth=1.0, draftValue=0.0
			, draftOutward=False):
		'���������� ��������� ������������ � ���� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48), (11, 48)),side1
			, type, depth, draftValue, draftOutward)

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'�������� ��������� ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"chooseType": (15, 2, (3, 0), (), "chooseType", None),
		"cut": (2, 2, (11, 0), (), "cut", None),
		"directionType": (1, 2, (2, 0), (), "directionType", None),
	}
	_prop_map_put_ = {
		"chooseType" : ((15, LCID, 4, 0),()),
		"cut" : ((2, LCID, 4, 0),()),
		"directionType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCutLineParam(DispatchBaseClass):
	'��������� ���������� ����� �������/�������.'
	CLSID = IID('{4FD7CE81-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CE83-9968-11D6-95CE-00C0262D30E3}')

	def GetpMathPoint(self):
		'������������ ������ ����� ������� �����.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpMathPoint', None)
		return ret

	def GetpTextline(self):
		'������������ ������ ����� ������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpTextline', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), (),)

	def SetpMathPoint(self, pMathPoint=defaultNamedNotOptArg):
		'������������ ������ ����� ������� �����.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((9, 0),),pMathPoint
			)

	def SetpTextline(self, pTextLine=defaultNamedNotOptArg):
		'������������ ������ ����� ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),pTextLine
			)

	_prop_map_get_ = {
		"right": (2, 2, (2, 0), (), "right", None),
		"str": (8, 2, (8, 0), (), "str", None),
		"style": (1, 2, (3, 0), (), "style", None),
		"type": (7, 2, (2, 0), (), "type", None),
		"x1": (3, 2, (5, 0), (), "x1", None),
		"x2": (5, 2, (5, 0), (), "x2", None),
		"y1": (4, 2, (5, 0), (), "y1", None),
		"y2": (6, 2, (5, 0), (), "y2", None),
	}
	_prop_map_put_ = {
		"right" : ((2, LCID, 4, 0),()),
		"str" : ((8, LCID, 4, 0),()),
		"style" : ((1, LCID, 4, 0),()),
		"type" : ((7, LCID, 4, 0),()),
		"x1" : ((3, LCID, 4, 0),()),
		"x2" : ((5, LCID, 4, 0),()),
		"y1" : ((4, LCID, 4, 0),()),
		"y2" : ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCutLoftDefinition(DispatchBaseClass):
	'�������� ��������� �� ��������.'
	CLSID = IID('{DEEFEFF0-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFEFF2-C3E2-11D6-8734-00C0262CDD2C}')

	def ChooseBodies(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� ���.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseBodies', None)
		return ret

	def ChooseParts(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseParts', None)
		return ret

	def GetDirectionalLine(self):
		'�������� ������������ �����. ����� � ������� ����� ������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDirectionalLine', None)
		return ret

	def GetLoftParam(self, closed=pythoncom.Missing, flipVertex=pythoncom.Missing, autoPath=pythoncom.Missing):
		'�������� ��������� ��������.'
		return self._ApplyTypes_(2, 1, (11, 0), ((16395, 2), (16395, 2), (16395, 2)), 'GetLoftParam', None,closed
			, flipVertex, autoPath)

	def GetThinParam(self, thin=pythoncom.Missing, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(4, 1, (11, 0), ((16395, 2), (16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thin
			, thinType, normalThickness, reverseTthickness)

	def SetDirectionalLine(self, sketch=defaultNamedNotOptArg):
		'���������� ������������ �����. ����� � ������� ����� ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetLoftParam(self, closed=defaultNamedNotOptArg, flipVertex=defaultNamedNotOptArg, autoPath=defaultNamedNotOptArg):
		'���������� ��������� ��������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((11, 0), (11, 0), (11, 0)),closed
			, flipVertex, autoPath)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def Sketchs(self):
		'������ �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Sketchs', None)
		return ret

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"chooseType": (11, 2, (3, 0), (), "chooseType", None),
		"cut": (1, 2, (11, 0), (), "cut", None),
	}
	_prop_map_put_ = {
		"chooseType" : ((11, LCID, 4, 0),()),
		"cut" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCutRotatedDefinition(DispatchBaseClass):
	'�������� ���������.'
	CLSID = IID('{2DFACC6D-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{2DFACC6F-C4A4-11D6-8734-00C0262CDD2C}')

	def ChooseBodies(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� ���.'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseBodies', None)
		return ret

	def ChooseParts(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseParts', None)
		return ret

	def GetSideParam(self, side1=defaultNamedNotOptArg, angle=defaultNamedNotOptArg):
		'�������� ��������� �������� � ���� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((11, 0), (16389, 0)),side1
			, angle)

	def GetSketch(self):
		'.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def GetThinParam(self, thin=pythoncom.Missing, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(8, 1, (11, 0), ((16395, 2), (16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thin
			, thinType, normalThickness, reverseTthickness)

	def RotatedParam(self):
		'��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RotatedParam', None)
		return ret

	def SetSideParam(self, side1=False, angle=180.0):
		'���������� ��������� �������� � ���� �������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((11, 48), (5, 48)),side1
			, angle)

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetThinParam(self, thin=defaultNamedNotOptArg, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((11, 0), (2, 48), (5, 48), (5, 48)),thin
			, thinType, normalThickness, reverseThickness)

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"chooseType": (13, 2, (3, 0), (), "chooseType", None),
		"cut": (3, 2, (11, 0), (), "cut", None),
		"directionType": (1, 2, (2, 0), (), "directionType", None),
		"toroidShapeType": (2, 2, (11, 0), (), "toroidShapeType", None),
	}
	_prop_map_put_ = {
		"chooseType" : ((13, LCID, 4, 0),()),
		"cut" : ((3, LCID, 4, 0),()),
		"directionType" : ((1, LCID, 4, 0),()),
		"toroidShapeType" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCylinderParam(DispatchBaseClass):
	'��������� ���������� �������������� �����������.'
	CLSID = IID('{5D462836-CF69-4995-AB78-8C7A83D09BD7}')
	coclass_clsid = IID('{379D658E-47BB-414F-A952-FB41037F17AC}')

	def GetPlacement(self):
		'�������� �� ���������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	_prop_map_get_ = {
		"height": (2, 2, (5, 0), (), "height", None),
		"radius": (1, 2, (5, 0), (), "radius", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksCylindricSpiralDefinition(DispatchBaseClass):
	'������� ��������������.'
	CLSID = IID('{0307BB9F-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BBA1-C193-11D6-8734-00C0262CDD2C}')

	def GetCurve3D(self):
		'�������� ��������� �� ��������� �������������� ������.'
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurve3D', None)
		return ret

	def GetDiamObject(self):
		'�������� ������ ��������.'
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDiamObject', None)
		return ret

	def GetHeightObject(self):
		'�������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetHeightObject', None)
		return ret

	def GetLocation(self, x=pythoncom.Missing, y=pythoncom.Missing):
		'�������� ����� �������� �������.'
		return self._ApplyTypes_(15, 1, (11, 0), ((16389, 2), (16389, 2)), 'GetLocation', None,x
			, y)

	def GetPlane(self):
		'�������� ������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def GetSketch(self):
		'�������� ��������� �� ��������� ������ ��������.'
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def SetDiamObject(self, diamObject=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((9, 0),),diamObject
			)

	def SetHeightObject(self, heightObject=defaultNamedNotOptArg):
		'�������� ������ ������.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((9, 0),),heightObject
			)

	def SetLocation(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg):
		'�������� ����� �������� �������.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((5, 0), (5, 0)),x
			, y)

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'�������� ������� ��������� �������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((9, 0),),plane
			)

	_prop_map_get_ = {
		"buildDir": (5, 2, (11, 0), (), "buildDir", None),
		"buildMode": (4, 2, (2, 0), (), "buildMode", None),
		"diam": (10, 2, (5, 0), (), "diam", None),
		"diamType": (11, 2, (2, 0), (), "diamType", None),
		"firstAngle": (12, 2, (5, 0), (), "firstAngle", None),
		"height": (6, 2, (5, 0), (), "height", None),
		"heightAdd": (8, 2, (5, 0), (), "heightAdd", None),
		"heightAddHow": (9, 2, (11, 0), (), "heightAddHow", None),
		"heightType": (7, 2, (2, 0), (), "heightType", None),
		"step": (2, 2, (5, 0), (), "step", None),
		"turn": (1, 2, (5, 0), (), "turn", None),
		"turnDir": (3, 2, (11, 0), (), "turnDir", None),
	}
	_prop_map_put_ = {
		"buildDir" : ((5, LCID, 4, 0),()),
		"buildMode" : ((4, LCID, 4, 0),()),
		"diam" : ((10, LCID, 4, 0),()),
		"diamType" : ((11, LCID, 4, 0),()),
		"firstAngle" : ((12, LCID, 4, 0),()),
		"height" : ((6, LCID, 4, 0),()),
		"heightAdd" : ((8, LCID, 4, 0),()),
		"heightAddHow" : ((9, LCID, 4, 0),()),
		"heightType" : ((7, LCID, 4, 0),()),
		"step" : ((2, LCID, 4, 0),()),
		"turn" : ((1, LCID, 4, 0),()),
		"turnDir" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDataBaseObject(DispatchBaseClass):
	'�������� � ��.'
	CLSID = IID('{0981CD01-9A49-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{0981CD03-9A49-11D6-8732-00C0262CDD2C}')

	def ksCloseTextFile(self, F=defaultNamedNotOptArg):
		'������� ��������� ����.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), ((3, 0),),F
			)

	def ksCondition(self, db=defaultNamedNotOptArg, r=defaultNamedNotOptArg, stSQL=defaultNamedNotOptArg):
		'�������� ������� ��� ��������� �������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), ((3, 0), (3, 0), (8, 0)),db
			, r, stSQL)

	def ksConnectDB(self, db=defaultNamedNotOptArg, DBName=defaultNamedNotOptArg):
		'������� ������ �� � ���������� ����� ������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), ((3, 0), (8, 0)),db
			, DBName)

	def ksCreateDB(self, typeBD=defaultNamedNotOptArg):
		'�������� ������� ���� ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((8, 0),),typeBD
			)

	def ksDeleteDB(self, db=defaultNamedNotOptArg):
		'������� ������ ���� ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), ((3, 0),),db
			)

	def ksDisconnectDB(self, db=defaultNamedNotOptArg):
		'�������  �������� ������������� � ���������� ����� ������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((3, 0),),db
			)

	def ksDoStatement(self, db=defaultNamedNotOptArg, r=defaultNamedNotOptArg, stSQL=defaultNamedNotOptArg):
		'���������� ������ ��� ������� ��.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((3, 0), (3, 0), (8, 0)),db
			, r, stSQL)

	def ksEndRelation(self):
		'������� ��������� ��������� ��������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	def ksFreeStatement(self, db=defaultNamedNotOptArg, r=defaultNamedNotOptArg, fOption=defaultNamedNotOptArg):
		'���������� ������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((3, 0), (3, 0), (3, 0)),db
			, r, fOption)

	def ksGetColumnName(self, db=defaultNamedNotOptArg, tableName=defaultNamedNotOptArg, res=pythoncom.Missing, firstOrNext=defaultNamedNotOptArg):
		'������� ��� ������� �������.'
		return self._ApplyTypes_(20, 1, (8, 0), ((3, 1), (8, 1), (16387, 2), (8, 1)), 'ksGetColumnName', None,db
			, tableName, res, firstOrNext)

	def ksGetTableName(self, db=defaultNamedNotOptArg, res=pythoncom.Missing, firstOrNext=defaultNamedNotOptArg):
		'������� ��� �������.'
		return self._ApplyTypes_(19, 1, (8, 0), ((3, 1), (16387, 2), (8, 1)), 'ksGetTableName', None,db
			, res, firstOrNext)

	def ksIsODBCOkey(self):
		'�������� ���������� � ODBC.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), (),)

	def ksOpenTextFile(self, fileName=defaultNamedNotOptArg):
		'������� ��������� ����.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((8, 0),),fileName
			)

	def ksOpenTextFileEx(self, fileName=defaultNamedNotOptArg, textFileType=defaultNamedNotOptArg):
		'������� ��������� ����.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (3, 0), ((8, 0), (3, 0)),fileName
			, textFileType)

	def ksRChar(self, name=defaultNamedNotOptArg, size=defaultNamedNotOptArg, type=defaultNamedNotOptArg):
		'�������� ���� char[size] � ��������� ��.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((8, 0), (3, 0), (3, 0)),name
			, size, type)

	def ksRCharW(self, name=defaultNamedNotOptArg, size=defaultNamedNotOptArg, type=defaultNamedNotOptArg):
		'�������� ���� wchar[size] � ��������� ��.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (3, 0), ((8, 0), (3, 0), (3, 0)),name
			, size, type)

	def ksRDouble(self, name=defaultNamedNotOptArg):
		'�������� ���� double � ��������� ��.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((8, 0),),name
			)

	def ksRFloat(self, name=defaultNamedNotOptArg):
		'�������� ���� float � ��������� ��.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((8, 0),),name
			)

	def ksRInt(self, name=defaultNamedNotOptArg):
		'�������� ���� short int � ��������� ��.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((8, 0),),name
			)

	def ksRLong(self, name=defaultNamedNotOptArg):
		'�������� ���� int ��� long int � ��������� ��.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((8, 0),),name
			)

	def ksReadRecord(self, db=defaultNamedNotOptArg, r=defaultNamedNotOptArg, userPars=defaultNamedNotOptArg):
		'������� ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((3, 0), (3, 0), (9, 0)),db
			, r, userPars)

	def ksReadStrFrFile(self, F=defaultNamedNotOptArg, res=pythoncom.Missing, numb=defaultNamedNotOptArg):
		'C������ ������ �� txt-����� � �������� �������.'
		return self._ApplyTypes_(18, 1, (8, 0), ((3, 1), (16387, 2), (3, 1)), 'ksReadStrFrFile', None,F
			, res, numb)

	def ksRelation(self, db=defaultNamedNotOptArg):
		'��������� �������� - ��������� ��������� ��� ���� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), ((3, 0),),db
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDefaultObject(DispatchBaseClass):
	'������������� ������.'
	CLSID = IID('{508A0CC7-9D74-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{508A0CC9-9D74-11D6-95CE-00C0262D30E3}')

	def GetCurve3D(self):
		'�������� ��������� �������������� ������ ��� ������� ����.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurve3D', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� ����������� ��� ������� ����������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDeletedCopyCollection(DispatchBaseClass):
	'��������� ������� ��������� �������� ��� ������� ����������� � �������� ���������.'
	CLSID = IID('{82F60797-D69C-4EB4-9F1A-24D625D5EAFA}')
	coclass_clsid = IID('{9807E658-53C5-4445-A389-3F800FB3BB8A}')

	def Add(self, index1=defaultNamedNotOptArg, index2=defaultNamedNotOptArg):
		'�������� ������� � ����� �������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((3, 0), (3, 0)),index1
			, index2)

	def AddAt(self, index1=defaultNamedNotOptArg, index2=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� ������� ����� �������� � ��������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((3, 0), (3, 0), (3, 0)),index1
			, index2, index)

	def Clear(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	def DetachByBody(self, index1=defaultNamedNotOptArg, index2=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((3, 0), (3, 0)),index1
			, index2)

	def DetachByIndex(self, index=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((3, 0),),index
			)

	def FindIt(self, index1=defaultNamedNotOptArg, index2=defaultNamedNotOptArg):
		'�������� ������ �������� �������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((3, 0), (3, 0)),index1
			, index2)

	def First(self, index1=pythoncom.Missing, index2=pythoncom.Missing):
		'�������� ������� ������ ��������� �����.'
		return self._ApplyTypes_(3, 1, (11, 0), ((16387, 2), (16387, 2)), 'First', None,index1
			, index2)

	def GetByIndex(self, index=defaultNamedNotOptArg, index1=pythoncom.Missing, index2=pythoncom.Missing):
		'�������� ������� ��������� ����� �� �������.'
		return self._ApplyTypes_(7, 1, (11, 0), ((3, 1), (16387, 2), (16387, 2)), 'GetByIndex', None,index
			, index1, index2)

	def GetCount(self):
		'���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self, index1=pythoncom.Missing, index2=pythoncom.Missing):
		'�������� ������� ��������� ��������� �����.'
		return self._ApplyTypes_(4, 1, (11, 0), ((16387, 2), (16387, 2)), 'Last', None,index1
			, index2)

	def Next(self, index1=pythoncom.Missing, index2=pythoncom.Missing):
		'�������� ������� ��������� ��������� �����.'
		return self._ApplyTypes_(5, 1, (11, 0), ((16387, 2), (16387, 2)), 'Next', None,index1
			, index2)

	def Prev(self, index1=pythoncom.Missing, index2=pythoncom.Missing):
		'�������� ������� ���������� ��������� �����.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16387, 2), (16387, 2)), 'Prev', None,index1
			, index2)

	def SetByIndex(self, index1=defaultNamedNotOptArg, index2=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((3, 0), (3, 0), (3, 0)),index1
			, index2, index)

	def refresh(self):
		'�������� ������ .'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDerivativePartArrayDefinition(DispatchBaseClass):
	'��������� �������� ������ ����������� �� �������.'
	CLSID = IID('{DDD05149-C180-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DDD0514B-C180-11D6-8734-00C0262CDD2C}')

	def DeletedCollection(self):
		'�������� ������ �������� ��������� �����.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DeletedCollection', None)
		return ret

	def GetDeriv(self):
		'�������� ������� �����������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDeriv', None)
		return ret

	def PartArray(self):
		'�������� ��������� ������� �������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PartArray', None)
		return ret

	def SetDeriv(self, deriv=defaultNamedNotOptArg):
		'������ ������� �����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),deriv
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDimDrawingParam(DispatchBaseClass):
	'��������� ��������� ��������� � �������� ��������.'
	CLSID = IID('{7F7D6FD2-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FD4-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ang": (8, 2, (5, 0), (), "ang", None),
		"lenght": (9, 2, (3, 0), (), "lenght", None),
		"pl1": (1, 2, (11, 0), (), "pl1", None),
		"pl2": (2, 2, (11, 0), (), "pl2", None),
		"pt1": (3, 2, (2, 0), (), "pt1", None),
		"pt2": (4, 2, (2, 0), (), "pt2", None),
		"shelfDir": (7, 2, (3, 0), (), "shelfDir", None),
		"textBase": (6, 2, (2, 0), (), "textBase", None),
		"textPos": (5, 2, (3, 0), (), "textPos", None),
	}
	_prop_map_put_ = {
		"ang" : ((8, LCID, 4, 0),()),
		"lenght" : ((9, LCID, 4, 0),()),
		"pl1" : ((1, LCID, 4, 0),()),
		"pl2" : ((2, LCID, 4, 0),()),
		"pt1" : ((3, LCID, 4, 0),()),
		"pt2" : ((4, LCID, 4, 0),()),
		"shelfDir" : ((7, LCID, 4, 0),()),
		"textBase" : ((6, LCID, 4, 0),()),
		"textPos" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDimTextParam(DispatchBaseClass):
	'��������� ��������� �������.'
	CLSID = IID('{7F7D6FCC-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FCE-97DA-11D6-8732-00C0262CDD2C}')

	def GetBitFlagValue(self, bitFlag=defaultNamedNotOptArg):
		'���������� �������� �������� ����.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((3, 0),),bitFlag
			)

	def GetTextArr(self):
		'���������� ������������ ������ �����.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTextArr', None)
		return ret

	def Init(self, stringFlag=defaultNamedNotOptArg):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((11, 0),),stringFlag
			)

	def SetBitFlagValue(self, val=defaultNamedNotOptArg, state=defaultNamedNotOptArg):
		'�������� �������� �������� ����.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((3, 0), (11, 0)),val
			, state)

	def SetTextArr(self, val=defaultNamedNotOptArg):
		'�������� ������������ ������ �����.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"bitFlag": (4, 2, (3, 0), (), "bitFlag", None),
		"sign": (2, 2, (3, 0), (), "sign", None),
		"stringFlag": (3, 2, (11, 0), (), "stringFlag", None),
		"style": (1, 2, (3, 0), (), "style", None),
	}
	_prop_map_put_ = {
		"bitFlag" : ((4, LCID, 4, 0),()),
		"sign" : ((2, LCID, 4, 0),()),
		"stringFlag" : ((3, LCID, 4, 0),()),
		"style" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDimensionPartsParam(DispatchBaseClass):
	'��������� ������������ �������� �������.'
	CLSID = IID('{7F7D6FDB-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FDD-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"curveExt": (8, 2, (3, 0), (), "curveExt", None),
		"dimLine": (3, 2, (3, 0), (), "dimLine", None),
		"dimLine1": (4, 2, (3, 0), (), "dimLine1", None),
		"gr": (7, 2, (3, 0), (), "gr", None),
		"leg": (5, 2, (3, 0), (), "leg", None),
		"line1": (1, 2, (3, 0), (), "line1", None),
		"line2": (2, 2, (3, 0), (), "line2", None),
		"shelf": (6, 2, (3, 0), (), "shelf", None),
	}
	_prop_map_put_ = {
		"curveExt" : ((8, LCID, 4, 0),()),
		"dimLine" : ((3, LCID, 4, 0),()),
		"dimLine1" : ((4, LCID, 4, 0),()),
		"gr" : ((7, LCID, 4, 0),()),
		"leg" : ((5, LCID, 4, 0),()),
		"line1" : ((1, LCID, 4, 0),()),
		"line2" : ((2, LCID, 4, 0),()),
		"shelf" : ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDimensionsOptions(DispatchBaseClass):
	'��������� ��� ����������� �������� ��������.'
	CLSID = IID('{FBCC5B99-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5B9B-996C-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"anglePrecisionLevel": (8, 2, (3, 0), (), "anglePrecisionLevel", None),
		"arrowLength": (5, 2, (5, 0), (), "arrowLength", None),
		"decimalsCount": (7, 2, (2, 0), (), "decimalsCount", None),
		"dimLineExtension": (4, 2, (5, 0), (), "dimLineExtension", None),
		"hiddenToleranceNumber": (9, 2, (3, 0), (), "hiddenToleranceNumber", None),
		"proLineExtension": (1, 2, (5, 0), (), "proLineExtension", None),
		"style": (6, 2, (3, 0), (), "style", None),
		"textDistanceFromDimLine": (2, 2, (5, 0), (), "textDistanceFromDimLine", None),
		"textDistanceFromProLine": (3, 2, (5, 0), (), "textDistanceFromProLine", None),
	}
	_prop_map_put_ = {
		"anglePrecisionLevel" : ((8, LCID, 4, 0),()),
		"arrowLength" : ((5, LCID, 4, 0),()),
		"decimalsCount" : ((7, LCID, 4, 0),()),
		"dimLineExtension" : ((4, LCID, 4, 0),()),
		"hiddenToleranceNumber" : ((9, LCID, 4, 0),()),
		"proLineExtension" : ((1, LCID, 4, 0),()),
		"style" : ((6, LCID, 4, 0),()),
		"textDistanceFromDimLine" : ((2, LCID, 4, 0),()),
		"textDistanceFromProLine" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDocAttachedSpcParam(DispatchBaseClass):
	'��������� �������������� ��������� � ������� ������������.'
	CLSID = IID('{4FD7CEA8-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CEAA-9968-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"comment": (2, 2, (8, 0), (), "comment", None),
		"fileName": (1, 2, (8, 0), (), "fileName", None),
		"transmit": (3, 2, (2, 0), (), "transmit", None),
	}
	_prop_map_put_ = {
		"comment" : ((2, LCID, 4, 0),()),
		"fileName" : ((1, LCID, 4, 0),()),
		"transmit" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDocument2D(DispatchBaseClass):
	'2D ��������.'
	CLSID = IID('{AF4E160D-5C89-4F21-B0F2-D53397BDAF78}')
	coclass_clsid = IID('{14FD27F5-B7FD-4276-AC2C-2804EDC3944F}')

	# Result is of type Document2DNotify
	def GetDocument2DNotify(self):
		'�������� �������� ������� ��� 2d ���������.'
		ret = self._oleobj_.InvokeTypes(208, LCID, 1, (13, 0), (),)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetDocument2DNotify', '{1B9B9B4E-DCD7-496E-A583-547EC1E91E47}')
		return ret

	def GetFragment(self):
		'���������� LPDISPATCH ���������.'
		ret = self._oleobj_.InvokeTypes(122, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFragment', None)
		return ret

	# Result is of type Object2DNotify
	def GetObject2DNotify(self, objType=defaultNamedNotOptArg):
		'�������� ������ �������� ������� ������� 2D ���������.'
		ret = self._oleobj_.InvokeTypes(205, LCID, 1, (13, 0), ((3, 0),),objType
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetObject2DNotify', '{C7EBA9A1-9E76-436E-B362-A80C5763944C}')
		return ret

	# Result is of type ksObject2DNotifyResult
	def GetObject2DNotifyResult(self):
		'��������� ����������� �������������� ������� ��� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(207, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObject2DNotifyResult', '{1FE1EB28-CD28-4700-8E46-25CCFE9C0EC8}')
		return ret

	# Result is of type SelectionMngNotify
	def GetSelectionMngNotify(self):
		'�������� ������ �������� ������� ��������� �������������� ���������.'
		ret = self._oleobj_.InvokeTypes(206, LCID, 1, (13, 0), (),)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetSelectionMngNotify', '{DC2E4057-7F8E-4652-860D-6B9E1F6F43AA}')
		return ret

	def GetSpecification(self):
		'������� ��������� ��� ������ � ��������� ������������.'
		ret = self._oleobj_.InvokeTypes(177, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSpecification', None)
		return ret

	def GetStamp(self):
		'������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(169, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetStamp', None)
		return ret

	def GetStampEx(self, SheetNumb=defaultNamedNotOptArg):
		'������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(225, LCID, 1, (9, 0), ((3, 0),),SheetNumb
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetStampEx', None)
		return ret

	def RasterFormatParam(self):
		'�������� ��������� �� ��������� ���������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(191, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RasterFormatParam', None)
		return ret

	def SaveAsToRasterFormat(self, fileName=defaultNamedNotOptArg, rasterPar=defaultNamedNotOptArg):
		'��������� �������� � ��������� ������.'
		return self._oleobj_.InvokeTypes(190, LCID, 1, (11, 0), ((8, 0), (9, 0)),fileName
			, rasterPar)

	def SaveAsToUncompressedRasterFormat(self, fileName=defaultNamedNotOptArg, rasterPar=defaultNamedNotOptArg):
		'��������� �������� ��� ������ � ��������� ������.'
		return self._oleobj_.InvokeTypes(195, LCID, 1, (11, 0), ((8, 0), (9, 0)),fileName
			, rasterPar)

	def ksAddObjGroup(self, g=defaultNamedNotOptArg, p=defaultNamedNotOptArg):
		'�������� ������ � ������.'
		return self._oleobj_.InvokeTypes(65, LCID, 1, (3, 0), ((3, 0), (3, 0)),g
			, p)

	def ksAddObjectToMacro(self, macro=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'�������� ������, ����, ��� ��� ������ �������� � �����������.'
		return self._oleobj_.InvokeTypes(55, LCID, 1, (3, 0), ((3, 0), (3, 0)),macro
			, obj)

	def ksAddPowerForm(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg):
		'���� ��������� ��� ���������� Nurbs ������� �������-��������� ��������.'
		return self._oleobj_.InvokeTypes(185, LCID, 1, (3, 0), ((5, 0), (5, 0)),x
			, y)

	def ksAddStyle(self, type=defaultNamedNotOptArg, param=defaultNamedNotOptArg, copy=defaultNamedNotOptArg):
		'�������� ��������� �����.'
		return self._oleobj_.InvokeTypes(84, LCID, 1, (3, 0), ((2, 0), (9, 0), (2, 0)),type
			, param, copy)

	def ksAngBreakDimension(self, angPar=defaultNamedNotOptArg):
		'������� ������-������� ������ � �������.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (3, 0), ((9, 0),),angPar
			)

	def ksAngDimension(self, angPar=defaultNamedNotOptArg):
		'������� ������ ������� ������.'
		return self._oleobj_.InvokeTypes(79, LCID, 1, (3, 0), ((9, 0),),angPar
			)

	def ksAnnArcByPoint(self, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, x1=defaultNamedNotOptArg
			, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg, direction=defaultNamedNotOptArg, term1=defaultNamedNotOptArg
			, term2=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'���� � ������ ���� �� ������ �� ���������.'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (2, 0), (2, 0), (2, 0), (3, 0)),xc
			, yc, rad, x1, y1, x2
			, y2, direction, term1, term2, style
			)

	def ksAnnCircle(self, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		"������� ������ '������������� ����������'."
		return self._oleobj_.InvokeTypes(235, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (3, 0)),xc
			, yc, rad, style)

	def ksAnnEllipse(self, par=defaultNamedNotOptArg):
		"������� ������ '������������� ������'."
		return self._oleobj_.InvokeTypes(236, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksAnnEllipseArc(self, par=defaultNamedNotOptArg, term1=defaultNamedNotOptArg, term2=defaultNamedNotOptArg):
		"������� ������ '������������� ���� �������'"
		return self._oleobj_.InvokeTypes(233, LCID, 1, (3, 0), ((9, 0), (2, 0), (2, 0)),par
			, term1, term2)

	def ksAnnLineSeg(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg
			, term1=defaultNamedNotOptArg, term2=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'���� � ������ �������������� �������.'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (2, 0), (2, 0), (3, 0)),x1
			, y1, x2, y2, term1, term2
			, style)

	def ksAnnParEllipseArc(self, par=defaultNamedNotOptArg, term1=defaultNamedNotOptArg, term2=defaultNamedNotOptArg):
		"������� ������ '������������� ���� �������' �� ����������."
		return self._oleobj_.InvokeTypes(234, LCID, 1, (3, 0), ((9, 0), (2, 0), (2, 0)),par
			, term1, term2)

	def ksAnnPoint(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'������� ������������� �����.'
		return self._oleobj_.InvokeTypes(239, LCID, 1, (3, 0), ((5, 0), (5, 0), (3, 0)),x
			, y, style)

	def ksAnnPolyline(self, style=defaultNamedNotOptArg, term1=defaultNamedNotOptArg, term2=defaultNamedNotOptArg):
		'������� ������������� ���������.'
		return self._oleobj_.InvokeTypes(237, LCID, 1, (3, 0), ((3, 0), (2, 0), (2, 0)),style
			, term1, term2)

	def ksAnnPolylineEx(self, par=defaultNamedNotOptArg, term1=defaultNamedNotOptArg, term2=defaultNamedNotOptArg):
		"������� ������ '������������� ���������' �� ��������� ����������"
		return self._oleobj_.InvokeTypes(232, LCID, 1, (3, 0), ((9, 0), (2, 0), (2, 0)),par
			, term1, term2)

	def ksAnnTextEx(self, txtParam=defaultNamedNotOptArg, align=defaultNamedNotOptArg):
		'������� ������������� ����� c ������������� ������ �������� �� ��������� ���������� ksTextParam.'
		return self._oleobj_.InvokeTypes(238, LCID, 1, (3, 0), ((9, 0), (3, 0)),txtParam
			, align)

	def ksApproximationCurve(self, p=defaultNamedNotOptArg, eps=defaultNamedNotOptArg, curentLayer=defaultNamedNotOptArg, maxRad=defaultNamedNotOptArg
			, smooth=defaultNamedNotOptArg):
		'���������������� ������ ������ � ��������� � ������������ ���������.'
		return self._oleobj_.InvokeTypes(143, LCID, 1, (3, 0), ((3, 0), (5, 0), (11, 0), (5, 0), (11, 0)),p
			, eps, curentLayer, maxRad, smooth)

	def ksArcBy3Points(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg
			, x3=defaultNamedNotOptArg, y3=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'��������� ���� �� 3 ������ � 2D ���������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (3, 0)),x1
			, y1, x2, y2, x3, y3
			, style)

	def ksArcByAngle(self, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, f1=defaultNamedNotOptArg
			, f2=defaultNamedNotOptArg, direction=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'��������� ���� �� ������ � ����� � 2D ���������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (2, 0), (3, 0)),xc
			, yc, rad, f1, f2, direction
			, style)

	def ksArcByPoint(self, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, x1=defaultNamedNotOptArg
			, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg, direction=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'��������� ���� �� ������ � ���� ������ � 2D ���������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (2, 0), (3, 0)),xc
			, yc, rad, x1, y1, x2
			, y2, direction, style)

	def ksAssociationViewMatrix3D(self, ViewRef=defaultNamedNotOptArg):
		'������� �������������� ����.'
		return self._ApplyTypes_(222, 1, (12, 0), ((3, 0),), 'ksAssociationViewMatrix3D', None,ViewRef
			)

	def ksAxisLine(self, param=defaultNamedNotOptArg):
		'������� ������ - ������ �����.'
		return self._oleobj_.InvokeTypes(194, LCID, 1, (3, 0), ((9, 0),),param
			)

	def ksBase(self, par=defaultNamedNotOptArg):
		'������� ������ - ����������� ����.'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksBezier(self, closed=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'��������� ������ Bezier-������.'
		return self._oleobj_.InvokeTypes(74, LCID, 1, (3, 0), ((2, 0), (3, 0)),closed
			, style)

	def ksBezierPoint(self, par=defaultNamedNotOptArg):
		'���� ����� ��� ���������� Bezier-�������.'
		return self._oleobj_.InvokeTypes(75, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksBrandLeader(self, brandLeaderParam=defaultNamedNotOptArg):
		'����� ������� ��� ����������� ���������.'
		return self._oleobj_.InvokeTypes(115, LCID, 1, (3, 0), ((9, 0),),brandLeaderParam
			)

	def ksCalcRasterScale(self, fileName=defaultNamedNotOptArg, w=defaultNamedNotOptArg, h=defaultNamedNotOptArg):
		'���������� ������� ��� ������� ������ � ������������� �������� ���������.'
		return self._oleobj_.InvokeTypes(218, LCID, 1, (5, 0), ((8, 0), (5, 0), (5, 0)),fileName
			, w, h)

	def ksCentreMarker(self, par=defaultNamedNotOptArg):
		'������� ������ - ����������� ������.'
		return self._oleobj_.InvokeTypes(73, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksChangeLeader(self, leaderParam=defaultNamedNotOptArg):
		'����� ������� ��� ����������� ���������.'
		return self._oleobj_.InvokeTypes(229, LCID, 1, (3, 0), ((9, 0),),leaderParam
			)

	def ksChangeObjectInLibRequest(self, info=defaultNamedNotOptArg, phantom=defaultNamedNotOptArg):
		'�������� ������ � ���������� ������ �� ����� ������ Cursor � Placement.'
		return self._oleobj_.InvokeTypes(120, LCID, 1, (3, 0), ((9, 0), (9, 0)),info
			, phantom)

	def ksChangeObjectLayer(self, obj=defaultNamedNotOptArg, number=defaultNamedNotOptArg):
		'�������� ���� ������ �������.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (3, 0), ((3, 0), (3, 0)),obj
			, number)

	def ksChangeObjectsOrder(self, group=defaultNamedNotOptArg, obj=defaultNamedNotOptArg, type=defaultNamedNotOptArg):
		'�������� ������� ��������� �������� �������.'
		return self._oleobj_.InvokeTypes(210, LCID, 1, (3, 0), ((3, 0), (3, 0), (3, 0)),group
			, obj, type)

	def ksCircle(self, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'��������� ���������� � 2D ���������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (3, 0)),xc
			, yc, rad, style)

	def ksClearGroup(self, g=defaultNamedNotOptArg, deleteTmp=defaultNamedNotOptArg):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(63, LCID, 1, (3, 0), ((3, 0), (11, 0)),g
			, deleteTmp)

	def ksClearRegion(self, grClear=defaultNamedNotOptArg, grRegion=defaultNamedNotOptArg, inside=defaultNamedNotOptArg):
		'������� ������� ��������� ������� (������������ ������� ��� ������� ���) � ������������ � ��������� ������ grRegion.'
		return self._oleobj_.InvokeTypes(167, LCID, 1, (3, 0), ((3, 0), (3, 0), (11, 0)),grClear
			, grRegion, inside)

	def ksClearTableColumnText(self, numb=defaultNamedNotOptArg):
		'�������� ������ ������� ��� ������� �����.'
		return self._oleobj_.InvokeTypes(129, LCID, 1, (3, 0), ((3, 0),),numb
			)

	def ksCloseDocument(self):
		'������� ��������.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (11, 0), (),)

	def ksCloseTechnicalDemand(self):
		'������� ��������� ������ - ����������� ����������.'
		return self._oleobj_.InvokeTypes(139, LCID, 1, (3, 0), (),)

	def ksColouring(self, color=defaultNamedNotOptArg):
		'��������� ������� ������� ������. ��������� ������.'
		return self._oleobj_.InvokeTypes(57, LCID, 1, (3, 0), ((3, 0),),color
			)

	def ksColouringEx(self, color=defaultNamedNotOptArg, group=defaultNamedNotOptArg):
		'������� ������� ������� ������. ������� �� ������ group �������� ������� �������.'
		return self._oleobj_.InvokeTypes(220, LCID, 1, (3, 0), ((3, 0), (3, 0)),color
			, group)

	def ksColumnNumber(self, numb=defaultNamedNotOptArg):
		'���������� ����� ������.'
		return self._oleobj_.InvokeTypes(135, LCID, 1, (3, 0), ((3, 0),),numb
			)

	def ksCombineTwoTableItems(self, index1=defaultNamedNotOptArg, index2=defaultNamedNotOptArg):
		'���������� ��� ������ �������, ���� ��� ����� ����� �����.'
		return self._oleobj_.InvokeTypes(130, LCID, 1, (3, 0), ((3, 0), (3, 0)),index1
			, index2)

	def ksCommandWindow(self, info=defaultNamedNotOptArg):
		'������ � ������� �� �������� ���� � ������� ������.'
		return self._oleobj_.InvokeTypes(119, LCID, 1, (3, 0), ((9, 0),),info
			)

	def ksConicArc(self, par=defaultNamedNotOptArg):
		'���� � ������ ����������� �������.'
		return self._oleobj_.InvokeTypes(72, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksContour(self, style=defaultNamedNotOptArg):
		'��������� ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), ((3, 0),),style
			)

	def ksConvertTextToCurve(self, text=defaultNamedNotOptArg):
		'������������� ����� � ������.'
		return self._oleobj_.InvokeTypes(52, LCID, 1, (3, 0), ((3, 0),),text
			)

	def ksCopyGroupToDocument(self, gr=defaultNamedNotOptArg, From=defaultNamedNotOptArg):
		'C���������� ������ � ��������.'
		return self._oleobj_.InvokeTypes(247, LCID, 1, (3, 0), ((3, 0), (3, 0)),gr
			, From)

	def ksCopyObj(self, ref=defaultNamedNotOptArg, xOld=defaultNamedNotOptArg, yOld=defaultNamedNotOptArg, xNew=defaultNamedNotOptArg
			, yNew=defaultNamedNotOptArg, scale=defaultNamedNotOptArg, angle=defaultNamedNotOptArg):
		'���������� ������ � ���������� ref (������ ����, ���, ������, ����) � �����.'
		return self._oleobj_.InvokeTypes(41, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0)),ref
			, xOld, yOld, xNew, yNew, scale
			, angle)

	def ksCopyObjEx(self, param=defaultNamedNotOptArg):
		'���������� ������.'
		return self._oleobj_.InvokeTypes(204, LCID, 1, (3, 0), ((9, 0),),param
			)

	def ksCreateDocument(self, par=defaultNamedNotOptArg):
		'������� ��������.'
		return self._oleobj_.InvokeTypes(152, LCID, 1, (11, 0), ((9, 0),),par
			)

	def ksCreatePowerArc(self):
		'�������� ����� Nurbs ������� �������-��������� ��������.'
		return self._oleobj_.InvokeTypes(186, LCID, 1, (3, 0), (),)

	def ksCreateSheetArbitraryView(self, par=defaultNamedNotOptArg, number=defaultNamedNotOptArg):
		'������� ������������ ������������� ���.'
		return self._oleobj_.InvokeTypes(196, LCID, 1, (3, 0), ((9, 1), (16387, 1)),par
			, number)

	def ksCreateSheetArrowView(self, par=defaultNamedNotOptArg, number=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'������� ������������� ��� �� �������.'
		return self._oleobj_.InvokeTypes(199, LCID, 1, (3, 0), ((9, 1), (16387, 1), (3, 1)),par
			, number, obj)

	def ksCreateSheetProjectionView(self, par=defaultNamedNotOptArg, number=defaultNamedNotOptArg, view=defaultNamedNotOptArg):
		'������� ������������ ������������� ���.'
		return self._oleobj_.InvokeTypes(198, LCID, 1, (3, 0), ((9, 1), (16387, 1), (3, 1)),par
			, number, view)

	def ksCreateSheetRemoteView(self, par=defaultNamedNotOptArg, number=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'������� ������������� �������� ���.'
		return self._oleobj_.InvokeTypes(201, LCID, 1, (3, 0), ((9, 1), (16387, 1), (3, 1)),par
			, number, obj)

	def ksCreateSheetSectionView(self, par=defaultNamedNotOptArg, number=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'������� ������������� ��� ��������������.'
		return self._oleobj_.InvokeTypes(200, LCID, 1, (3, 0), ((9, 1), (16387, 1), (3, 1)),par
			, number, obj)

	def ksCreateSheetStandartViews(self, par=defaultNamedNotOptArg, bitVector=defaultNamedNotOptArg, dx=defaultNamedNotOptArg, dy=defaultNamedNotOptArg):
		'������� ����������� ������������� ����.'
		return self._oleobj_.InvokeTypes(197, LCID, 1, (11, 0), ((9, 0), (3, 0), (5, 0), (5, 0)),par
			, bitVector, dx, dy)

	def ksCreateSheetView(self, par=defaultNamedNotOptArg, number=defaultNamedNotOptArg):
		'������� ���. ��� ���������� �������.'
		return self._ApplyTypes_(98, 1, (3, 0), ((9, 1), (16387, 3)), 'ksCreateSheetView', None,par
			, number)

	def ksCreateViewObject(self, type=defaultNamedNotOptArg):
		'������� ������ ��������� ����, ��������� ���������� ������� �������� �������.'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (3, 0), ((3, 0),),type
			)

	def ksCursor(self, info=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, phantom=defaultNamedNotOptArg):
		'������ � ������� �� ��������� �����.'
		return self._ApplyTypes_(117, 1, (3, 0), ((9, 1), (16389, 3), (16389, 3), (9, 1)), 'ksCursor', None,info
			, x, y, phantom)

	def ksCursorEx(self, info=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, phantom=defaultNamedNotOptArg
			, processParam=defaultNamedNotOptArg):
		'������ � ������� �� ��������� �����.'
		return self._ApplyTypes_(216, 1, (3, 0), ((9, 1), (16389, 3), (16389, 3), (9, 1), (9, 1)), 'ksCursorEx', None,info
			, x, y, phantom, processParam)

	def ksCutLine(self, par=defaultNamedNotOptArg):
		'������� ������ ����� ������� ��� �������.'
		return self._oleobj_.InvokeTypes(142, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksDecomposeObj(self, p=defaultNamedNotOptArg, level=defaultNamedNotOptArg, arrow=defaultNamedNotOptArg, type=defaultNamedNotOptArg):
		'������� ������ �� ������������ ����� - �������, ����, ������.'
		return self._oleobj_.InvokeTypes(99, LCID, 1, (3, 0), ((3, 0), (2, 0), (5, 0), (2, 0)),p
			, level, arrow, type)

	def ksDeleteMtr(self):
		'���������� ������� �������������.'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (3, 0), (),)

	def ksDeleteObj(self, ref=defaultNamedNotOptArg):
		'������� �� ������ ������ � ���������� ref.'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (3, 0), ((3, 0),),ref
			)

	def ksDeleteStyleFromDocument(self, type=defaultNamedNotOptArg, param=defaultNamedNotOptArg, copy=defaultNamedNotOptArg):
		'������� ����� � ������� ���������.'
		return self._oleobj_.InvokeTypes(86, LCID, 1, (3, 0), ((2, 0), (9, 0), (2, 0)),type
			, param, copy)

	def ksDestroyObjConstraint(self, obj=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'������� ��������������� �����������.'
		return self._oleobj_.InvokeTypes(165, LCID, 1, (3, 0), ((3, 0), (9, 0)),obj
			, par)

	def ksDestroyObjects(self, gr=defaultNamedNotOptArg):
		'��������� ��������� ������.'
		return self._oleobj_.InvokeTypes(183, LCID, 1, (3, 0), ((3, 0),),gr
			)

	def ksDiamDimension(self, par=defaultNamedNotOptArg):
		'������� ������ ������������� ������.'
		return self._oleobj_.InvokeTypes(80, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksDivideTableItem(self, index=defaultNamedNotOptArg, vertical=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'��������� ������ �������.'
		return self._oleobj_.InvokeTypes(131, LCID, 1, (3, 0), ((3, 0), (11, 0), (3, 0)),index
			, vertical, style)

	def ksDrawKompasDocument(self, HWindow=defaultNamedNotOptArg, docFileName=defaultNamedNotOptArg):
		'���������� ������-�������� ��� ����� � ���������� ����.'
		return self._oleobj_.InvokeTypes(155, LCID, 1, (3, 0), ((3, 0), (8, 0)),HWindow
			, docFileName)

	def ksDrawKompasGroup(self, HWindow=defaultNamedNotOptArg, gr=defaultNamedNotOptArg):
		'���������� ������ ��� ����� � ���������� ����.'
		return self._oleobj_.InvokeTypes(159, LCID, 1, (3, 0), ((3, 0), (3, 0)),HWindow
			, gr)

	def ksDuplicateBoundaries(self, p=defaultNamedNotOptArg):
		'������� ���������� ����� ������� ��������� ��� ������� �� ��������� ������.'
		return self._oleobj_.InvokeTypes(58, LCID, 1, (3, 0), ((3, 0),),p
			)

	def ksEditMacroMode(self):
		'�������������� �������������.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (3, 0), (),)

	def ksEditViewObject(self, ref=defaultNamedNotOptArg):
		'��������� ���������� ������� �������������� �������.'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (3, 0), ((3, 0),),ref
			)

	def ksEllipse(self, par=defaultNamedNotOptArg):
		'������� ������ - ������.'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksEllipseArc(self, par=defaultNamedNotOptArg):
		'������� ������ - ���� ������� �� �����.'
		return self._oleobj_.InvokeTypes(48, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksEnableUndo(self, enabl=defaultNamedNotOptArg):
		'��������/��������� ������ ���������� ��������.'
		return self._oleobj_.InvokeTypes(184, LCID, 1, (11, 0), ((11, 0),),enabl
			)

	def ksEndGroup(self):
		'����� ������.'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (3, 0), (),)

	def ksEndObj(self):
		'������� ��������� ������. ���������� ��������� �� ��������� ������.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), (),)

	def ksEquidistant(self, par=defaultNamedNotOptArg):
		'������� ������ - ������������.'
		return self._oleobj_.InvokeTypes(50, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksExcludeObjGroup(self, g=defaultNamedNotOptArg, p=defaultNamedNotOptArg):
		'��������� ������ �� ������.'
		return self._oleobj_.InvokeTypes(64, LCID, 1, (3, 0), ((3, 0), (3, 0)),g
			, p)

	def ksExistGroupObj(self, g=defaultNamedNotOptArg):
		'���������� ���� �� � ������ �������.'
		return self._oleobj_.InvokeTypes(68, LCID, 1, (3, 0), ((3, 0),),g
			)

	def ksExistObj(self, ref=defaultNamedNotOptArg):
		'���������, ���������� �� ������ � ���������� ref.'
		return self._oleobj_.InvokeTypes(87, LCID, 1, (3, 0), ((3, 0),),ref
			)

	def ksFindObj(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, limit=defaultNamedNotOptArg):
		'����� ������, ��������� � �������� �����.'
		return self._oleobj_.InvokeTypes(39, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0)),x
			, y, limit)

	def ksGetAnnObjTerminators(self, annObj=defaultNamedNotOptArg, term1=pythoncom.Missing, term2=pythoncom.Missing):
		'�������� �������������� ������������ �������� ��� �������������� �������.'
		return self._ApplyTypes_(240, 1, (11, 0), ((3, 1), (16386, 2), (16386, 2)), 'ksGetAnnObjTerminators', None,annObj
			, term1, term2)

	def ksGetCursorLimit(self):
		'���������� ������ ���������� ��������� � ������� �������.'
		return self._oleobj_.InvokeTypes(179, LCID, 1, (5, 0), (),)

	def ksGetCursorPosition(self, x=pythoncom.Missing, y=pythoncom.Missing, type=defaultNamedNotOptArg):
		'������� ���������� �������.'
		return self._ApplyTypes_(30, 1, (3, 0), ((16389, 2), (16389, 2), (3, 1)), 'ksGetCursorPosition', None,x
			, y, type)

	def ksGetDimensionVariableName(self, dimObj=defaultNamedNotOptArg):
		'������ ��� ��������������� ���������� �������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(188, LCID, 1, (8, 0), ((3, 0),),dimObj
			)

	def ksGetDocOptions(self, optionsType=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����� ��������� ���������.'
		return self._oleobj_.InvokeTypes(162, LCID, 1, (3, 0), ((3, 0), (9, 0)),optionsType
			, param)

	def ksGetDocVariableArray(self, p=defaultNamedNotOptArg):
		'������� ���������� ������ ��������������� ���������� ������������ ��������� ��� ������� ���������.'
		ret = self._oleobj_.InvokeTypes(160, LCID, 1, (9, 0), ((3, 0),),p
			)
		if ret is not None:
			ret = Dispatch(ret, 'ksGetDocVariableArray', None)
		return ret

	def ksGetDocumentPagesCount(self):
		'�������� ���������� ������ ���������.'
		return self._oleobj_.InvokeTypes(226, LCID, 1, (3, 0), (),)

	def ksGetEditMacroVisibleRegime(self, p=defaultNamedNotOptArg):
		'��������� �� �������� � ������ �������������� �����'
		return self._oleobj_.InvokeTypes(246, LCID, 1, (11, 0), ((3, 0),),p
			)

	def ksGetGroup(self, name=defaultNamedNotOptArg):
		'����� ������ �� �����.'
		return self._oleobj_.InvokeTypes(70, LCID, 1, (3, 0), ((8, 0),),name
			)

	def ksGetGroupName(self, gr=defaultNamedNotOptArg, group=pythoncom.Missing, size=defaultNamedNotOptArg):
		'�������� ��� ������ �� ��������� �� ������.'
		return self._ApplyTypes_(106, 1, (8, 0), ((3, 1), (16387, 2), (3, 1)), 'ksGetGroupName', None,gr
			, group, size)

	def ksGetLayerNumber(self, p=defaultNamedNotOptArg):
		'���������� ����� ���� �� ��������� �� ����.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), ((3, 0),),p
			)

	def ksGetLayerReference(self, number=defaultNamedNotOptArg):
		'���������� ��������� �� ���� �� ������ ���� ��� �������� ����.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (3, 0), ((3, 0),),number
			)

	def ksGetLeaderShelfLength(self, leader=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing):
		'�������� ����� � ���������� �������� ����� ����� ����� ������� '
		return self._ApplyTypes_(192, 1, (5, 0), ((3, 1), (16389, 2), (16389, 2)), 'ksGetLeaderShelfLength', None,leader
			, x, y)

	def ksGetMacroParam(self, ref=defaultNamedNotOptArg, userPars=defaultNamedNotOptArg):
		'������ ��� ������������� � ���������� ref ��������� ��������������.'
		return self._oleobj_.InvokeTypes(137, LCID, 1, (3, 0), ((3, 0), (9, 0)),ref
			, userPars)

	def ksGetMacroParamSize(self, ref=defaultNamedNotOptArg):
		'�������� ������ ������ ���������� �������������.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (3, 0), ((3, 0),),ref
			)

	def ksGetMacroPlacement(self, macro=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, angl=defaultNamedNotOptArg):
		'�������� ����� �������� � ���� �������� - �� ������������.'
		return self._ApplyTypes_(157, 1, (3, 0), ((3, 1), (16389, 2), (16389, 2), (16389, 3)), 'ksGetMacroPlacement', None,macro
			, x, y, angl)

	def ksGetMacroPlacementEx(self, macro=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, angl=pythoncom.Missing
			, sheetParam=defaultNamedNotOptArg, mirrorSymmetry=pythoncom.Missing):
		'�������� ����� �������� � ���� �������� - �� ������������.'
		return self._ApplyTypes_(243, 1, (3, 0), ((3, 1), (16389, 2), (16389, 2), (16389, 2), (3, 1), (16387, 2)), 'ksGetMacroPlacementEx', None,macro
			, x, y, angl, sheetParam, mirrorSymmetry
			)

	def ksGetMacroWaitDblClickEdit(self, ref=defaultNamedNotOptArg):
		'�������� ����� �������� DblClick ��� �������������� ������������.'
		return self._oleobj_.InvokeTypes(213, LCID, 1, (3, 0), ((3, 0),),ref
			)

	def ksGetObjConstraints(self, obj=defaultNamedNotOptArg):
		'�������� ��������������� �����������, ���������� �� ������.'
		ret = self._oleobj_.InvokeTypes(164, LCID, 1, (9, 0), ((3, 0),),obj
			)
		if ret is not None:
			ret = Dispatch(ret, 'ksGetObjConstraints', None)
		return ret

	def ksGetObjGabaritRect(self, p=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'���������� ������� �������.'
		return self._oleobj_.InvokeTypes(88, LCID, 1, (3, 0), ((3, 0), (9, 0)),p
			, par)

	def ksGetObjParam(self, ref=defaultNamedNotOptArg, param=defaultNamedNotOptArg, parType=-1):
		'�������� ��������� �������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((3, 0), (9, 0), (3, 48)),ref
			, param, parType)

	def ksGetObjectNameByType(self, type=defaultNamedNotOptArg):
		'������� ��� ������� �� ��� ����.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(252, LCID, 1, (8, 0), ((3, 0),),type
			)

	def ksGetObjectStyle(self, obj=defaultNamedNotOptArg):
		'�������� ����� ��� ������� 2D ���������.'
		return self._oleobj_.InvokeTypes(241, LCID, 1, (3, 0), ((3, 0),),obj
			)

	def ksGetObjectsNameByType(self, type=defaultNamedNotOptArg):
		'������� ��� ������� �� ��� ����. ������������� �����.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(253, LCID, 1, (8, 0), ((3, 0),),type
			)

	def ksGetPointOnToleranceTable(self, tolerance=defaultNamedNotOptArg, entry=defaultNamedNotOptArg, point=defaultNamedNotOptArg):
		'��� ������� ������ ����� �������� ���������� ����� �� �������.'
		return self._oleobj_.InvokeTypes(148, LCID, 1, (3, 0), ((3, 0), (2, 0), (9, 0)),tolerance
			, entry, point)

	def ksGetReferenceDocumentPart(self, t=defaultNamedNotOptArg):
		'�������� ������� �����(�����, ������� ����, � �.�.).'
		return self._oleobj_.InvokeTypes(93, LCID, 1, (3, 0), ((2, 0),),t
			)

	def ksGetReferenceDocumentPartEx(self, t=defaultNamedNotOptArg, SheetNumb=defaultNamedNotOptArg):
		'�������� ������� �����(�����, ������� ����, � �.�.).'
		return self._oleobj_.InvokeTypes(224, LCID, 1, (3, 0), ((2, 0), (3, 0)),t
			, SheetNumb)

	def ksGetShelfPoint(self, p=defaultNamedNotOptArg, index=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, paramType=defaultNamedNotOptArg):
		'�������� ���������� �������� ����� �������.'
		return self._ApplyTypes_(230, 1, (11, 0), ((3, 1), (3, 1), (16389, 2), (16389, 2), (3, 1)), 'ksGetShelfPoint', None,p
			, index, x, y, paramType)

	def ksGetSnapInfo(self):
		'�������� ��������� ���������� � ������ ���������.'
		ret = self._oleobj_.InvokeTypes(248, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ksGetSnapInfo', None)
		return ret

	def ksGetStyleParam(self, type=defaultNamedNotOptArg, styleId=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'�������� ��������� �����.'
		return self._oleobj_.InvokeTypes(76, LCID, 1, (3, 0), ((2, 0), (2, 0), (9, 0)),type
			, styleId, param)

	def ksGetTableBorderStyle(self, index=defaultNamedNotOptArg, typeBorder=defaultNamedNotOptArg):
		'������ ����� ����� �������.'
		return self._oleobj_.InvokeTypes(133, LCID, 1, (3, 0), ((3, 0), (2, 0)),index
			, typeBorder)

	def ksGetTableColumnText(self, numb=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'������ ����� ������, � ��������� �� ��������� ������.'
		return self._ApplyTypes_(127, 1, (3, 0), ((16387, 3), (9, 1)), 'ksGetTableColumnText', None,numb
			, par)

	def ksGetTableItemsCount(self, type=defaultNamedNotOptArg):
		'������ ���������� ����� � �������.'
		return self._oleobj_.InvokeTypes(126, LCID, 1, (3, 0), ((3, 0),),type
			)

	def ksGetTextAlign(self, pText=defaultNamedNotOptArg):
		'�������� ����� �������� ������.'
		return self._oleobj_.InvokeTypes(180, LCID, 1, (3, 0), ((3, 0),),pText
			)

	def ksGetTextLength(self, text=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'���������� ����� ������ � �����������.'
		return self._oleobj_.InvokeTypes(170, LCID, 1, (5, 0), ((8, 0), (3, 0)),text
			, style)

	def ksGetTextLengthFromReference(self, pText=defaultNamedNotOptArg):
		'���������� ����� ������ � �����������.'
		return self._oleobj_.InvokeTypes(171, LCID, 1, (5, 0), ((3, 0),),pText
			)

	def ksGetToleranceColumnText(self, numb=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'������� ������ ����� ������, � ��������� �� ��������� ������.'
		return self._ApplyTypes_(146, 1, (3, 0), ((16387, 3), (9, 1)), 'ksGetToleranceColumnText', None,numb
			, par)

	def ksGetViewNumber(self, p=defaultNamedNotOptArg):
		'������������ ����� ���� �� ��������� �� ���.'
		return self._oleobj_.InvokeTypes(95, LCID, 1, (3, 0), ((3, 0),),p
			)

	def ksGetViewObjCount(self, p=defaultNamedNotOptArg):
		'���������� ����� �������� � ����.'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (3, 0), ((3, 0),),p
			)

	def ksGetViewReference(self, number=defaultNamedNotOptArg):
		'������������ ��������� �� ��� �� ������ ����.'
		return self._oleobj_.InvokeTypes(94, LCID, 1, (3, 0), ((3, 0),),number
			)

	def ksGetZona(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, result_=pythoncom.Missing):
		'�������� ���� �������� ��������� (������������) �� �������� �����.'
		return self._ApplyTypes_(166, 1, (8, 0), ((5, 1), (5, 1), (16387, 2)), 'ksGetZona', None,x
			, y, result_)

	def ksGetZoomScale(self, x=pythoncom.Missing, y=pythoncom.Missing, scale=pythoncom.Missing):
		'������� ������� � ���� ��������� ���� ������������ ���������.'
		return self._ApplyTypes_(175, 1, (3, 0), ((16389, 2), (16389, 2), (16389, 2)), 'ksGetZoomScale', None,x
			, y, scale)

	def ksHatch(self, style=defaultNamedNotOptArg, angle=defaultNamedNotOptArg, step=defaultNamedNotOptArg, width=defaultNamedNotOptArg
			, x0=defaultNamedNotOptArg, y0=defaultNamedNotOptArg):
		'��������� ���������. ��������� ������.'
		return self._oleobj_.InvokeTypes(56, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0)),style
			, angle, step, width, x0, y0
			)

	def ksHatchByParam(self, param=defaultNamedNotOptArg):
		'������� ������ - ��������� �� ����������.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), ((9, 0),),param
			)

	def ksInitFilePreviewFunc(self, funcName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'��������������� ����� ���������������� ������� ��������� ����������������� �����.'
		return self._oleobj_.InvokeTypes(123, LCID, 1, (3, 0), ((8, 0), (3, 0), (9, 0)),funcName
			, hInst, dispatchOCX)

	def ksInitFilePreviewFuncW(self, funcName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'��������������� ����� ���������������� ������� ��������� ����������������� �����.'
		return self._oleobj_.InvokeTypes(228, LCID, 1, (3, 0), ((8, 0), (3, 0), (9, 0)),funcName
			, hInst, dispatchOCX)

	def ksInsertRaster(self, par=defaultNamedNotOptArg):
		'�������� ��������� ������.'
		return self._oleobj_.InvokeTypes(77, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksIsActiveProcessRunnig(self):
		'��������� ������� �� � ������� ����������� ��������� �������������� �������.'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (3, 0), (),)

	def ksIsCursorOrPlacementDocument(self):
		'�������: �������� �� ������� �������� ���, � ������� ��������� �������.'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (3, 0), (),)

	def ksIsCurveClosed(self, p=defaultNamedNotOptArg):
		'��������� �������� ������ ��� ���.'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (3, 0), ((3, 0),),p
			)

	def ksIsPointInsideContour(self, p=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, precision=defaultNamedNotOptArg):
		'��������� ���������� ����� �� ��������� � �������.'
		return self._oleobj_.InvokeTypes(51, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0), (5, 0)),p
			, x, y, precision)

	def ksIsSlaveSpcOpened(self):
		'������ �� slave ����� ��.'
		return self._oleobj_.InvokeTypes(211, LCID, 1, (3, 0), (),)

	def ksIsStyleInDocument(self, type=defaultNamedNotOptArg, param=defaultNamedNotOptArg, copy=defaultNamedNotOptArg):
		'���������, ���� �� ����� � ������� ���������.'
		return self._oleobj_.InvokeTypes(85, LCID, 1, (3, 0), ((2, 0), (9, 0), (2, 0)),type
			, param, copy)

	def ksKeepReference(self, r=defaultNamedNotOptArg):
		'��������� ��������� �� ������ ��� ������������� ��� ��������� ���������� ����������.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (3, 0), ((3, 0),),r
			)

	def ksLayer(self, n=defaultNamedNotOptArg):
		'��������������� �������� ����.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), ((3, 0),),n
			)

	def ksLeader(self, leaderPar=defaultNamedNotOptArg):
		'������� ������ ����� �������.'
		return self._oleobj_.InvokeTypes(113, LCID, 1, (3, 0), ((9, 0),),leaderPar
			)

	def ksLengthFromMtr(self, len=defaultNamedNotOptArg):
		'��������� �����  �� ��������� ��.'
		return self._ApplyTypes_(112, 1, (3, 0), ((16389, 3),), 'ksLengthFromMtr', None,len
			)

	def ksLengthIntoMtr(self, len=defaultNamedNotOptArg):
		'��������� ����� � ��������� ��.'
		return self._ApplyTypes_(111, 1, (3, 0), ((16389, 3),), 'ksLengthIntoMtr', None,len
			)

	def ksLightObj(self, ref=defaultNamedNotOptArg, light=defaultNamedNotOptArg):
		'�������� ��� ��������� ��������� ��� �������.'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (3, 0), ((3, 0), (2, 0)),ref
			, light)

	def ksLinBreakDimension(self, linPar=defaultNamedNotOptArg):
		'������� ������-�������� ������ � �������.'
		return self._oleobj_.InvokeTypes(101, LCID, 1, (3, 0), ((9, 0),),linPar
			)

	def ksLinDimension(self, linPar=defaultNamedNotOptArg):
		'������� ������ �������� ������.'
		return self._oleobj_.InvokeTypes(78, LCID, 1, (3, 0), ((9, 0),),linPar
			)

	def ksLine(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, angle=defaultNamedNotOptArg):
		'������� ������ - ��������������� �����.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0)),x
			, y, angle)

	def ksLineSeg(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg
			, style=defaultNamedNotOptArg):
		'��������� ������� � 2D ���������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (3, 0)),x1
			, y1, x2, y2, style)

	def ksMacro(self, type=defaultNamedNotOptArg):
		'C������ ����� ������������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((2, 0),),type
			)

	def ksMakeEncloseContours(self, gr=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg):
		'������������ ������ ��������.'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0)),gr
			, x, y)

	def ksMakeEncloseContoursEx(self, gr=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, forHatch=defaultNamedNotOptArg):
		'������������ ������ ��������.'
		return self._oleobj_.InvokeTypes(231, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0), (11, 0)),gr
			, x, y, forHatch)

	def ksMarkerLeader(self, markerLeaderParam=defaultNamedNotOptArg):
		'����� ������� ��� ����������� ������������.'
		return self._oleobj_.InvokeTypes(116, LCID, 1, (3, 0), ((9, 0),),markerLeaderParam
			)

	def ksMoveObj(self, ref=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg):
		'�������� ������ � ���������� ref.'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0)),ref
			, x, y)

	def ksMovePoint(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, ang=defaultNamedNotOptArg, len=defaultNamedNotOptArg):
		'�������� ����� �� ���������� � �����.'
		return self._ApplyTypes_(153, 1, (11, 0), ((16389, 3), (16389, 3), (5, 1), (5, 1)), 'ksMovePoint', None,x
			, y, ang, len)

	def ksMtr(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, angle=defaultNamedNotOptArg, scaleX=defaultNamedNotOptArg
			, scaleY=defaultNamedNotOptArg):
		'���� ������� �������������.'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0)),x
			, y, angle, scaleX, scaleY)

	def ksNewGroup(self, type=defaultNamedNotOptArg):
		'�������� ����� ������.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (3, 0), ((2, 0),),type
			)

	def ksNewViewNumber(self):
		'������������ ����� ���������� ���� ��� 0 ��� �������.'
		return self._oleobj_.InvokeTypes(97, LCID, 1, (3, 0), (),)

	def ksNurbs(self, degree=defaultNamedNotOptArg, close=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'��������� ������ Nurbs-������. ��������� ������.'
		return self._oleobj_.InvokeTypes(61, LCID, 1, (3, 0), ((2, 0), (11, 0), (3, 0)),degree
			, close, style)

	def ksNurbsForConicCurve(self, xArr=defaultNamedNotOptArg, yArr=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'Nurbs �� ������������������ ������ ����������� �������.'
		return self._oleobj_.InvokeTypes(168, LCID, 1, (3, 0), ((9, 0), (9, 0), (2, 0)),xArr
			, yArr, style)

	def ksNurbsKnot(self, knot=defaultNamedNotOptArg):
		'���� ���� ��� ���������� Nurbs-�������.'
		return self._oleobj_.InvokeTypes(60, LCID, 1, (3, 0), ((5, 0),),knot
			)

	def ksNurbsPoint(self, par=defaultNamedNotOptArg):
		'���� ����� ��� ���������� Nurbs-�������.'
		return self._oleobj_.InvokeTypes(59, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksOpenDocument(self, nameDoc=defaultNamedNotOptArg, regim=defaultNamedNotOptArg):
		'������� ��������.'
		return self._oleobj_.InvokeTypes(149, LCID, 1, (11, 0), ((8, 0), (11, 0)),nameDoc
			, regim)

	def ksOpenMacro(self, macro=defaultNamedNotOptArg):
		'������� ����������� ��� ��������������.'
		return self._oleobj_.InvokeTypes(54, LCID, 1, (3, 0), ((3, 0),),macro
			)

	def ksOpenTable(self, table=defaultNamedNotOptArg):
		'������� ��������� ������ - ������� ��� ��������������.'
		return self._oleobj_.InvokeTypes(134, LCID, 1, (3, 0), ((3, 0),),table
			)

	def ksOpenTechnicalDemand(self, pGab=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'������� ��������� ������ - ����������� ����������.'
		return self._oleobj_.InvokeTypes(138, LCID, 1, (3, 0), ((9, 0), (3, 0)),pGab
			, style)

	def ksOpenTolerance(self, tolerance=defaultNamedNotOptArg):
		'O������ ���������  ������ - ������ ����� ��� ��������������.'
		return self._oleobj_.InvokeTypes(145, LCID, 1, (3, 0), ((3, 0),),tolerance
			)

	def ksOpenView(self, number=defaultNamedNotOptArg):
		'������� ��� �� ������, � ���������� ���������� �������.'
		return self._oleobj_.InvokeTypes(96, LCID, 1, (3, 0), ((3, 0),),number
			)

	def ksOrdinatedDimension(self, ordPar=defaultNamedNotOptArg):
		'������� ������ ������ ������.'
		return self._oleobj_.InvokeTypes(83, LCID, 1, (3, 0), ((9, 0),),ordPar
			)

	def ksParEllipseArc(self, par=defaultNamedNotOptArg):
		'������� ������ - ���� ������� �� ����������.'
		return self._oleobj_.InvokeTypes(49, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksParagraph(self, par=defaultNamedNotOptArg):
		'��������� ����� ��������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksParametrizeObjects(self, obj=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'���������� ��������������� ����������� �� ������ ��������.'
		return self._oleobj_.InvokeTypes(215, LCID, 1, (3, 0), ((3, 0), (9, 0)),obj
			, par)

	def ksPhantomShowHide(self, show=defaultNamedNotOptArg):
		'��������(show=0) ��� ��������(show=1) ������.'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (3, 0), ((8, 0),),show
			)

	def ksPlacement(self, info=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, angle=defaultNamedNotOptArg
			, phantom=defaultNamedNotOptArg):
		'������ � ������� �� ��������� ����� � ����.'
		return self._ApplyTypes_(118, 1, (3, 0), ((9, 1), (16389, 3), (16389, 3), (16389, 3), (9, 1)), 'ksPlacement', None,info
			, x, y, angle, phantom)

	def ksPlacementEx(self, info=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, angle=defaultNamedNotOptArg
			, phantom=defaultNamedNotOptArg, processParam=defaultNamedNotOptArg):
		'������ � ������� �� ��������� ����� � ����.'
		return self._ApplyTypes_(217, 1, (3, 0), ((9, 1), (16389, 3), (16389, 3), (16389, 3), (9, 1), (9, 1)), 'ksPlacementEx', None,info
			, x, y, angle, phantom, processParam
			)

	def ksPoint(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'������� �����.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((5, 0), (5, 0), (3, 0)),x
			, y, style)

	def ksPoint3DToAssociationView(self, view=defaultNamedNotOptArg, x3D=defaultNamedNotOptArg, y3D=defaultNamedNotOptArg, z3D=defaultNamedNotOptArg
			, x2D=pythoncom.Missing, y2D=pythoncom.Missing):
		'������������� ���������� 3D ����� � ���������� �������������� ����.'
		return self._ApplyTypes_(223, 1, (11, 0), ((3, 1), (5, 1), (5, 1), (5, 1), (16389, 2), (16389, 2)), 'ksPoint3DToAssociationView', None,view
			, x3D, y3D, z3D, x2D, y2D
			)

	def ksPointArraw(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, ang=defaultNamedNotOptArg, term=defaultNamedNotOptArg):
		'���� � ������ ������ ������������� ����.'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (2, 0)),x
			, y, ang, term)

	def ksPointFromMtr(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, xn=pythoncom.Missing, yn=pythoncom.Missing):
		'��������� ����� �� ��������� �� � �� ����.'
		return self._ApplyTypes_(110, 1, (3, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2)), 'ksPointFromMtr', None,x
			, y, xn, yn)

	def ksPointIntoMtr(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, xn=pythoncom.Missing, yn=pythoncom.Missing):
		'��������� ����� �� �� ���� � ��������� ��.'
		return self._ApplyTypes_(109, 1, (3, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2)), 'ksPointIntoMtr', None,x
			, y, xn, yn)

	def ksPolyline(self, style=defaultNamedNotOptArg):
		'��������� ���������. ��������� ������.'
		return self._oleobj_.InvokeTypes(91, LCID, 1, (3, 0), ((3, 0),),style
			)

	def ksPolylineByParam(self, par=defaultNamedNotOptArg):
		'������� ��������� �� ��������� ���������.'
		return self._oleobj_.InvokeTypes(92, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksPositionLeader(self, posLeaderParam=defaultNamedNotOptArg):
		'����������� ����� �������.'
		return self._oleobj_.InvokeTypes(114, LCID, 1, (3, 0), ((9, 0),),posLeaderParam
			)

	def ksRadBreakDimension(self, par=defaultNamedNotOptArg):
		'������� ������ ���������� ������ � �������.'
		return self._oleobj_.InvokeTypes(82, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksRadDimension(self, par=defaultNamedNotOptArg):
		'������� ������ ���������� ������.'
		return self._oleobj_.InvokeTypes(81, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksReDrawDocPart(self, rect=defaultNamedNotOptArg, view=defaultNamedNotOptArg):
		'�������������� ����� 2D ���������.'
		return self._oleobj_.InvokeTypes(178, LCID, 1, (3, 0), ((9, 0), (3, 0)),rect
			, view)

	def ksReDrawDocPartEx(self, rect=defaultNamedNotOptArg, view=defaultNamedNotOptArg, paramType=defaultNamedNotOptArg):
		'�������������� ����� 2D ���������.'
		return self._oleobj_.InvokeTypes(249, LCID, 1, (3, 0), ((9, 0), (3, 0), (3, 0)),rect
			, view, paramType)

	def ksReadGroupFromClip(self):
		'��������� ��������� �� clip � �������� �� �� ��������� ������.'
		return self._oleobj_.InvokeTypes(71, LCID, 1, (3, 0), (),)

	def ksReadTableFromFile(self, tblFileName=defaultNamedNotOptArg):
		'������� �������, ��������� ����������, ���������� � ����� *.tbl.'
		return self._oleobj_.InvokeTypes(154, LCID, 1, (3, 0), ((8, 0),),tblFileName
			)

	def ksRebuildDocument(self):
		'����������� 2D ������.'
		return self._oleobj_.InvokeTypes(202, LCID, 1, (11, 0), (),)

	def ksRebuildTableVirtualGrid(self):
		'����������� ����������� ����� �������.'
		return self._oleobj_.InvokeTypes(125, LCID, 1, (3, 0), (),)

	def ksRectangle(self, par=defaultNamedNotOptArg, centre=0):
		'��������� �������������� � 2D ���������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((9, 0), (2, 48)),par
			, centre)

	def ksRegularPolygon(self, par=defaultNamedNotOptArg, centre=0):
		'������� ������ - ���������� �������������.'
		return self._oleobj_.InvokeTypes(62, LCID, 1, (3, 0), ((9, 0), (2, 48)),par
			, centre)

	def ksReleaseReference(self, p=defaultNamedNotOptArg):
		'���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(121, LCID, 1, (3, 0), ((3, 0),),p
			)

	def ksRemoteElement(self, par=defaultNamedNotOptArg):
		"������� ������  '�������� �������'."
		return self._oleobj_.InvokeTypes(203, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksRotateObj(self, ref=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, angle=defaultNamedNotOptArg):
		'��������� ������ � ���������� ref.'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0), (5, 0)),ref
			, x, y, angle)

	def ksRough(self, roughPar=defaultNamedNotOptArg):
		'������� ������ ������������� �����������.'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (3, 0), ((9, 0),),roughPar
			)

	def ksSaveDocument(self, fileName=defaultNamedNotOptArg):
		'��������� ��������.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (11, 0), ((8, 0),),fileName
			)

	def ksSaveDocumentEx(self, fileName=defaultNamedNotOptArg, SaveMode=defaultNamedNotOptArg):
		'��������� ��������.'
		return self._oleobj_.InvokeTypes(221, LCID, 1, (11, 0), ((8, 0), (3, 0)),fileName
			, SaveMode)

	def ksSaveGroup(self, g=defaultNamedNotOptArg, name=defaultNamedNotOptArg):
		'��������� ������ � ������.'
		return self._oleobj_.InvokeTypes(66, LCID, 1, (3, 0), ((3, 0), (8, 0)),g
			, name)

	def ksSaveToDXF(self, DXFFileName=defaultNamedNotOptArg):
		'��������� �������� � ������� DXF.'
		return self._oleobj_.InvokeTypes(227, LCID, 1, (11, 0), ((8, 0),),DXFFileName
			)

	def ksSelectGroup(self, g=defaultNamedNotOptArg, selectMode=defaultNamedNotOptArg, xmin=defaultNamedNotOptArg, ymin=defaultNamedNotOptArg
			, xmax=defaultNamedNotOptArg, ymax=defaultNamedNotOptArg):
		'����� ������ �� �����.'
		return self._oleobj_.InvokeTypes(67, LCID, 1, (3, 0), ((3, 0), (2, 0), (5, 0), (5, 0), (5, 0), (5, 0)),g
			, selectMode, xmin, ymin, xmax, ymax
			)

	def ksSetDocOptions(self, optionsType=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'�������� ��������� ���������.'
		return self._oleobj_.InvokeTypes(193, LCID, 1, (3, 0), ((3, 0), (9, 0)),optionsType
			, param)

	def ksSetDocVariableArray(self, obj=defaultNamedNotOptArg, arr=defaultNamedNotOptArg, setNote=defaultNamedNotOptArg):
		'������� �������� �������� � ���� ����� ����������� � ��������������� ���������� ������������ ��������� ��� ������� ���������.'
		return self._oleobj_.InvokeTypes(161, LCID, 1, (3, 0), ((3, 0), (9, 0), (11, 0)),obj
			, arr, setNote)

	def ksSetLightObjType(self, ref=defaultNamedNotOptArg, light=defaultNamedNotOptArg):
		'���������� ��� ��������� ������� (light=1 - �������) ��� (light=0 - �������).'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (3, 0), ((3, 0), (3, 0)),ref
			, light)

	def ksSetMacroParam(self, ref=defaultNamedNotOptArg, userPars=defaultNamedNotOptArg, dblClickOff=defaultNamedNotOptArg, hotpoints=defaultNamedNotOptArg
			, externEdit=defaultNamedNotOptArg):
		'��������� � ������������ � ���������� ref ��������� ��������������.'
		return self._oleobj_.InvokeTypes(136, LCID, 1, (3, 0), ((3, 0), (9, 0), (11, 0), (11, 0), (11, 0)),ref
			, userPars, dblClickOff, hotpoints, externEdit)

	def ksSetMacroPlacement(self, macro=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, angl=defaultNamedNotOptArg
			, relativ=defaultNamedNotOptArg):
		'���������� ����� �������� � ���� �������� - ������� ��������� ������������.'
		return self._oleobj_.InvokeTypes(158, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0), (5, 0), (3, 0)),macro
			, x, y, angl, relativ)

	def ksSetMacroPlacementEx(self, macro=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, angl=defaultNamedNotOptArg
			, relativ=defaultNamedNotOptArg, mirrorSymmetry=defaultNamedNotOptArg):
		'���������� ����� �������� � ���� �������� - ������� ��������� ������������.'
		return self._oleobj_.InvokeTypes(244, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0), (5, 0), (3, 0), (3, 0)),macro
			, x, y, angl, relativ, mirrorSymmetry
			)

	def ksSetMacroWaitDblClickEdit(self, ref=defaultNamedNotOptArg, waitDblClick=defaultNamedNotOptArg):
		'���������� ����� �������� DblClick ��� �������������� ������������.'
		return self._oleobj_.InvokeTypes(214, LCID, 1, (3, 0), ((3, 0), (3, 0)),ref
			, waitDblClick)

	def ksSetMaterialParam(self, material=defaultNamedNotOptArg, density=defaultNamedNotOptArg):
		'���������� ��������� ��������� � �������.'
		return self._oleobj_.InvokeTypes(209, LCID, 1, (3, 0), ((9, 0), (5, 0)),material
			, density)

	def ksSetMixDlgMaterialParam(self, material=defaultNamedNotOptArg, density=defaultNamedNotOptArg):
		'���������� ��������� ��������� � �������.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (3, 0), ((8, 0), (5, 0)),material
			, density)

	def ksSetObjConstraint(self, obj=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'���������� ��������������� �����������.'
		return self._oleobj_.InvokeTypes(163, LCID, 1, (3, 0), ((3, 0), (9, 0)),obj
			, par)

	def ksSetObjParam(self, referObj=defaultNamedNotOptArg, param=defaultNamedNotOptArg, parType=-1):
		'������������� ����� ��������� �������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((3, 0), (9, 0), (3, 48)),referObj
			, param, parType)

	def ksSetObjectStyle(self, obj=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'���������� ����� ��� ������� 2D ���������.'
		return self._oleobj_.InvokeTypes(242, LCID, 1, (11, 0), ((3, 0), (3, 0)),obj
			, style)

	def ksSetTableBorderStyle(self, index=defaultNamedNotOptArg, typeBorder=defaultNamedNotOptArg, style=defaultNamedNotOptArg):
		'�������� ����� ����� �������.'
		return self._oleobj_.InvokeTypes(132, LCID, 1, (3, 0), ((3, 0), (2, 0), (3, 0)),index
			, typeBorder, style)

	def ksSetTableColumnText(self, numb=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'������� �������� ����� ������ �������.'
		return self._oleobj_.InvokeTypes(128, LCID, 1, (3, 0), ((3, 0), (9, 0)),numb
			, par)

	def ksSetTextAlign(self, pText=defaultNamedNotOptArg, align=defaultNamedNotOptArg):
		'���������� ����� �������� ������.'
		return self._oleobj_.InvokeTypes(181, LCID, 1, (3, 0), ((3, 0), (3, 0)),pText
			, align)

	def ksSetTextLineAlign(self, align=defaultNamedNotOptArg):
		'���������� ������������ ������.'
		return self._oleobj_.InvokeTypes(182, LCID, 1, (3, 0), ((2, 0),),align
			)

	def ksSetToleranceColumnText(self, numb=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'������� �������� ����� ������ ������� �����.'
		return self._oleobj_.InvokeTypes(147, LCID, 1, (3, 0), ((3, 0), (9, 0)),numb
			, par)

	def ksSheetToView(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, outX=pythoncom.Missing, outY=pythoncom.Missing):
		'����������� ����� �� CK ����� � CK �������� ����.'
		return self._ApplyTypes_(89, 1, (3, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2)), 'ksSheetToView', None,x
			, y, outX, outY)

	def ksShowHideTmpObj(self, ref=defaultNamedNotOptArg, show=defaultNamedNotOptArg):
		'�������� ��� ��������� ����������� ���������� ������� � ���������.'
		return self._oleobj_.InvokeTypes(250, LCID, 1, (3, 0), ((3, 0), (3, 0)),ref
			, show)

	def ksSpecRough(self, par=defaultNamedNotOptArg):
		'������� ������ - ����������� �������������.'
		return self._oleobj_.InvokeTypes(140, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksSpecificationOnSheet(self, onSheet=defaultNamedNotOptArg):
		'�������� ��� ��������� C����������� �� �����.'
		return self._oleobj_.InvokeTypes(176, LCID, 1, (3, 0), ((2, 0),),onSheet
			)

	def ksStoreTmpGroup(self, g=defaultNamedNotOptArg):
		'��������� ��������� ������ � ������.'
		return self._oleobj_.InvokeTypes(53, LCID, 1, (3, 0), ((3, 0),),g
			)

	def ksSymmetryObj(self, ref=defaultNamedNotOptArg, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg
			, y2=defaultNamedNotOptArg, copy=defaultNamedNotOptArg):
		'����������� ���������� (copy=0) ������ � ���������� ref.'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0), (5, 0), (5, 0), (8, 0)),ref
			, x1, y1, x2, y2, copy
			)

	def ksTable(self):
		'��������� �������.'
		return self._oleobj_.InvokeTypes(124, LCID, 1, (3, 0), (),)

	def ksText(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, ang=defaultNamedNotOptArg, hStr=defaultNamedNotOptArg
			, ksuStr=defaultNamedNotOptArg, bitVector=defaultNamedNotOptArg, s=defaultNamedNotOptArg):
		'������� ������ - �����.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (3, 0), (8, 0)),x
			, y, ang, hStr, ksuStr, bitVector
			, s)

	def ksTextEx(self, txtParam=defaultNamedNotOptArg, align=defaultNamedNotOptArg):
		'������� ������������� ����� �� ��������� ���������� ksTextParam.'
		return self._oleobj_.InvokeTypes(219, LCID, 1, (3, 0), ((9, 0), (3, 0)),txtParam
			, align)

	def ksTextLine(self, textItem=defaultNamedNotOptArg):
		'������� ���������� ������ ������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((9, 0),),textItem
			)

	def ksTolerance(self, par=defaultNamedNotOptArg):
		'������� ������ ������ �����.'
		return self._oleobj_.InvokeTypes(144, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksTransformObj(self, ref=defaultNamedNotOptArg):
		'������������� ������ � ���������� ref.'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (3, 0), ((3, 0),),ref
			)

	def ksTrimNurbs(self, pObj=defaultNamedNotOptArg, tMin=defaultNamedNotOptArg, tMax=defaultNamedNotOptArg):
		'.'
		return self._oleobj_.InvokeTypes(187, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0)),pObj
			, tMin, tMax)

	def ksTrimmCurve(self, curve=defaultNamedNotOptArg, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg
			, y2=defaultNamedNotOptArg, x3=defaultNamedNotOptArg, y3=defaultNamedNotOptArg, deleteOldCurve=defaultNamedNotOptArg):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(189, LCID, 1, (3, 0), ((3, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (2, 0)),curve
			, x1, y1, x2, y2, x3
			, y3, deleteOldCurve)

	def ksUndoContainer(self, Add=defaultNamedNotOptArg):
		'��������/��������� ����������� �������� ��� Undo.'
		return self._oleobj_.InvokeTypes(245, LCID, 1, (11, 0), ((11, 0),),Add
			)

	def ksUpdateMacro(self, macro=defaultNamedNotOptArg, gr=defaultNamedNotOptArg):
		'�������� ����������� � �������� � ���� ������ gr.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((3, 0), (3, 0)),macro
			, gr)

	def ksViewGetObjectArea(self):
		'�������� ������ ����������� ��������, ������������ ������� ���������, ��������� ���������� �������.'
		return self._oleobj_.InvokeTypes(156, LCID, 1, (3, 0), (),)

	def ksViewPointer(self, par=defaultNamedNotOptArg):
		'������� ������ ������� ����.'
		return self._oleobj_.InvokeTypes(141, LCID, 1, (3, 0), ((9, 0),),par
			)

	def ksViewToSheet(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, outX=pythoncom.Missing, outY=pythoncom.Missing):
		'����������� ����� �� CK �������� ���� � CK �����.'
		return self._ApplyTypes_(90, 1, (3, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2)), 'ksViewToSheet', None,x
			, y, outX, outY)

	def ksWriteGroupToClip(self, g=defaultNamedNotOptArg, copy=defaultNamedNotOptArg):
		'�������� ������ � clip � ��������� ��� ������������ ��������� �� ��������� ���������.'
		return self._oleobj_.InvokeTypes(69, LCID, 1, (3, 0), ((3, 0), (11, 0)),g
			, copy)

	def ksZoom(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg):
		'��������� ����������� ��������� ����.'
		return self._oleobj_.InvokeTypes(172, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (5, 0)),x1
			, y1, x2, y2)

	def ksZoomPrevNextOrAll(self, type=defaultNamedNotOptArg):
		'���������� ����������/��������� "����" ��� ��������� ��������� ��� �������� ���� ��������.'
		return self._oleobj_.InvokeTypes(174, LCID, 1, (3, 0), ((2, 0),),type
			)

	def ksZoomScale(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, scale=defaultNamedNotOptArg):
		'��������� ����������� ��������� ����.'
		return self._oleobj_.InvokeTypes(173, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0)),x
			, y, scale)

	_prop_map_get_ = {
		"orthoMode": (212, 2, (11, 0), (), "orthoMode", None),
		"reference": (1, 2, (3, 0), (), "reference", None),
	}
	_prop_map_put_ = {
		"orthoMode" : ((212, LCID, 4, 0),()),
		"reference" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDocument2DNotify:
	'������� 2D ���������.'
	CLSID = CLSID_Sink = IID('{13F0BE95-3361-4AD9-90AF-D935EA64A127}')
	coclass_clsid = IID('{1B9B9B4E-DCD7-496E-A583-547EC1E91E47}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnBeginRebuild",
		        2 : "OnRebuild",
		        3 : "OnBeginChoiceMaterial",
		        4 : "OnChoiceMaterial",
		        5 : "OnBeginInsertFragment",
		        6 : "OnLocalFragmentEdit",
		        7 : "OnBeginChoiceProperty",
		        8 : "OnChoiceProperty",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnBeginRebuild(self):
#		'������ ������������ �������������� �������.'
#	def OnRebuild(self):
#		'������������� ������ ����������.'
#	def OnBeginChoiceMaterial(self):
#		'������ ������ ���������.'
#	def OnChoiceMaterial(self, material=defaultNamedNotOptArg, density=defaultNamedNotOptArg):
#		'�������� ����� ���������.'
#	def OnBeginInsertFragment(self):
#		'������ ������� ���������  (�� ������� ������ �����).'
#	def OnLocalFragmentEdit(self, newDoc=defaultNamedNotOptArg, newFrw=defaultNamedNotOptArg):
#		'�������������� ���������� ���������.'
#	def OnBeginChoiceProperty(self, objRef=defaultNamedNotOptArg, propID=defaultNamedNotOptArg):
#		'������ ������ ��������.'
#	def OnChoiceProperty(self, objRef=defaultNamedNotOptArg, propID=defaultNamedNotOptArg):
#		'�������� ����� ��������.'


class ksDocument3D(DispatchBaseClass):
	'3D ��������.'
	CLSID = IID('{111CEFE1-A0A7-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{111CEFE3-A0A7-11D6-95CE-00C0262D30E3}')

	def AddImportedSurfaces(self, fileName=defaultNamedNotOptArg, together=defaultNamedNotOptArg):
		'�������� ��������������� �����������.'
		ret = self._oleobj_.InvokeTypes(56, LCID, 1, (9, 0), ((8, 0), (11, 0)),fileName
			, together)
		if ret is not None:
			ret = Dispatch(ret, 'AddImportedSurfaces', None)
		return ret

	def AddMateConstraint(self, constraintType=defaultNamedNotOptArg, obj1=defaultNamedNotOptArg, obj2=defaultNamedNotOptArg, direction=0
			, fixed=0, val=0.0):
		'�������� ����������.'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (11, 0), ((3, 0), (9, 0), (9, 0), (2, 48), (2, 48), (5, 48)),constraintType
			, obj1, obj2, direction, fixed, val
			)

	def AdditionFormatParam(self):
		'�������� ��������� �� ��������� ���������� �������������� ��������.'
		ret = self._oleobj_.InvokeTypes(38, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AdditionFormatParam', None)
		return ret

	# Result is of type ksAttribute3DCollection
	def AttributeCollection(self, key1=defaultNamedNotOptArg, key2=defaultNamedNotOptArg, key3=defaultNamedNotOptArg, key4=defaultNamedNotOptArg
			, numb=defaultNamedNotOptArg, pObj=defaultNamedNotOptArg):
		'�������� ������ ���������.'
		ret = self._oleobj_.InvokeTypes(58, LCID, 1, (9, 0), ((3, 0), (3, 0), (3, 0), (3, 0), (5, 0), (9, 0)),key1
			, key2, key3, key4, numb, pObj
			)
		if ret is not None:
			ret = Dispatch(ret, 'AttributeCollection', '{EB61A981-F63E-47E1-BEE8-2D1612C78E78}')
		return ret

	def ChangeObjectInLibRequest(self):
		'������������� �������� ��������� ��������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

	# Result is of type ksComponentPositioner
	def ComponentPositioner(self):
		'��������� ���������� ���������� ����������� � ������.'
		ret = self._oleobj_.InvokeTypes(61, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ComponentPositioner', '{508B5962-DF59-4CEE-8611-AD10FDF0C811}')
		return ret

	def CopyPart(self, sourcePart=defaultNamedNotOptArg, newPlacement=defaultNamedNotOptArg):
		'������� ����� ���������� � ���������.'
		ret = self._oleobj_.InvokeTypes(69, LCID, 1, (9, 0), ((9, 0), (9, 0)),sourcePart
			, newPlacement)
		if ret is not None:
			ret = Dispatch(ret, 'CopyPart', None)
		return ret

	def Create(self, invisible=False, typeDoc=True):
		'������� ����� 3D ��������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((11, 48), (11, 48)),invisible
			, typeDoc)

	def CreatePartFromFile(self, fileName=defaultNamedNotOptArg, part=defaultNamedNotOptArg, plane=defaultNamedNotOptArg):
		'������� ��������� �� �����.'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (11, 0), ((8, 0), (9, 0), (9, 0)),fileName
			, part, plane)

	def CreatePartInAssembly(self, fileName=defaultNamedNotOptArg, plane=defaultNamedNotOptArg):
		'���������� ��������� ����������, ��������� �� �����.'
		ret = self._oleobj_.InvokeTypes(31, LCID, 1, (9, 0), ((8, 0), (9, 0)),fileName
			, plane)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePartInAssembly', None)
		return ret

	# Result is of type ksPlacement
	def DefaultPlacement(self):
		'��������� ������������� C�.'
		ret = self._oleobj_.InvokeTypes(62, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DefaultPlacement', '{2DFACC64-C4A4-11D6-8734-00C0262CDD2C}')
		return ret

	def DeleteObject(self, obj=defaultNamedNotOptArg):
		'������� ������ ������, ��������, ����������.'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def EntityCollection(self, objType=0, checkEntity=True):
		'������ ������ ��������.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((2, 48), (11, 48)),objType
			, checkEntity)
		if ret is not None:
			ret = Dispatch(ret, 'EntityCollection', None)
		return ret

	def ExcludeFeaturesAfter(self, obj=defaultNamedNotOptArg, exclude=defaultNamedNotOptArg):
		'����������������� �� ������� ������� � ������ ����� ���������.'
		return self._oleobj_.InvokeTypes(76, LCID, 1, (11, 0), ((9, 0), (11, 0)),obj
			, exclude)

	# Result is of type ksFeatureCollection
	def FeatureCollection(self, key1=defaultNamedNotOptArg, key2=defaultNamedNotOptArg, key3=defaultNamedNotOptArg, key4=defaultNamedNotOptArg
			, numb=defaultNamedNotOptArg, objType=defaultNamedNotOptArg):
		'�������� ������ ��������, ������� ������ ������� (objType==o3d_unknown - �������� ��� �������).'
		ret = self._oleobj_.InvokeTypes(59, LCID, 1, (9, 0), ((3, 0), (3, 0), (3, 0), (3, 0), (5, 0), (3, 0)),key1
			, key2, key3, key4, numb, objType
			)
		if ret is not None:
			ret = Dispatch(ret, 'FeatureCollection', '{CE6A46FF-02B4-4C7E-AF50-3F3707C8B122}')
		return ret

	def GetChooseMng(self):
		'�������� �������� ������ (���������) ��������.'
		ret = self._oleobj_.InvokeTypes(45, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetChooseMng', None)
		return ret

	# Result is of type Document3DNotify
	def GetDocument3DNotify(self):
		'�������� �������� ������� ��� 3d ���������.'
		ret = self._oleobj_.InvokeTypes(57, LCID, 1, (13, 0), (),)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetDocument3DNotify', '{22B81342-42D6-4907-A91E-F75A959F2270}')
		return ret

	def GetDocument3DNotifyResult(self):
		'�������������� ��������� ��� ������� ��������� 3D.'
		ret = self._oleobj_.InvokeTypes(83, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDocument3DNotifyResult', None)
		return ret

	def GetEditMacroObject(self):
		'�������� ������������� ����������� 3D.'
		ret = self._oleobj_.InvokeTypes(65, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEditMacroObject', None)
		return ret

	def GetInterface(self, o3dType=defaultNamedNotOptArg):
		'�������� ��������� �� ���� o3d_type.'
		ret = self._oleobj_.InvokeTypes(67, LCID, 1, (9, 0), ((3, 0),),o3dType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetInterface', None)
		return ret

	def GetLastFeature(self):
		'�������� ��������� ������ � ������.'
		ret = self._oleobj_.InvokeTypes(89, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetLastFeature', None)
		return ret

	def GetMateConstraint(self):
		'�������� ��������� �� ��������� ������ �������-����������.'
		ret = self._oleobj_.InvokeTypes(34, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetMateConstraint', None)
		return ret

	def GetObjectType(self, obj=defaultNamedNotOptArg):
		'�������� ��� �������.'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (3, 0), ((9, 0),),obj
			)

	def GetPart(self, type=defaultNamedNotOptArg):
		'���������� ��������� ����������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),type
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPart', None)
		return ret

	def GetRequestInfo(self, part=defaultNamedNotOptArg):
		'���������� ��������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), ((9, 0),),part
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetRequestInfo', None)
		return ret

	def GetRollBackFeature(self):
		'�������� ��������� ��������� � ������.'
		ret = self._oleobj_.InvokeTypes(74, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetRollBackFeature', None)
		return ret

	def GetSelectionMng(self):
		'�������� �������� ��������������� ��������.'
		ret = self._oleobj_.InvokeTypes(44, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSelectionMng', None)
		return ret

	def GetSpecification(self):
		'�������� ��������� ������������ ��� 3D ���������.'
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSpecification', None)
		return ret

	def GetViewProjectionCollection(self):
		'��� ��������� ���� 3d ��������� �������� ��������� ������� �������� ����������� ������ � ����.'
		ret = self._oleobj_.InvokeTypes(42, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetViewProjectionCollection', None)
		return ret

	def IsActive(self):
		'True - �������� �������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), (),)

	def IsDetail(self):
		'��� ���������: true - ������, false - ������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	def IsEditMode(self):
		'True - ����� �������������� ����� ����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	def LoadFromAdditionFormat(self, fileName=defaultNamedNotOptArg, additionPar=defaultNamedNotOptArg):
		'��������� �������� �� �������������� �������� jgs, sat, xt, x_b, step, stl.'
		return self._oleobj_.InvokeTypes(88, LCID, 1, (11, 0), ((8, 0), (9, 0)),fileName
			, additionPar)

	def MateConstraintCollection(self):
		'������ ������ ����������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MateConstraintCollection', None)
		return ret

	def Open(self, fileName=defaultNamedNotOptArg, invisible=False):
		'��������� ������������ 3D ��������.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((8, 0), (11, 48)),fileName
			, invisible)

	def PartCollection(self, refresh=defaultNamedNotOptArg):
		'�������� ������ ����������� ������.'
		ret = self._oleobj_.InvokeTypes(29, LCID, 1, (9, 0), ((11, 0),),refresh
			)
		if ret is not None:
			ret = Dispatch(ret, 'PartCollection', None)
		return ret

	def PlaceFeatureAfter(self, obj=defaultNamedNotOptArg, afterObj=defaultNamedNotOptArg):
		'��������� ������ ������ ����� ������� ������� ������.'
		return self._oleobj_.InvokeTypes(72, LCID, 1, (11, 0), ((9, 0), (9, 0)),obj
			, afterObj)

	def RasterFormatParam(self):
		'�������� ��������� �� ��������� ���������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(36, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RasterFormatParam', None)
		return ret

	def RebuildDocument(self):
		'����������� ��������.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (11, 0), (),)

	def RemoveMateConstraint(self, constraintType=defaultNamedNotOptArg, obj1=defaultNamedNotOptArg, obj2=defaultNamedNotOptArg):
		'������� ����������.'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (11, 0), ((3, 0), (9, 0), (9, 0)),constraintType
			, obj1, obj2)

	def RunTakeCreateObjectProc(self, processType=defaultNamedNotOptArg, takeObject=defaultNamedNotOptArg, needCreateTakeObj=defaultNamedNotOptArg, lostTakeObj=defaultNamedNotOptArg):
		'��������� ����������� ����� �������� ��������.'
		return self._oleobj_.InvokeTypes(87, LCID, 1, (11, 0), ((3, 0), (9, 0), (11, 0), (11, 0)),processType
			, takeObject, needCreateTakeObj, lostTakeObj)

	def Save(self):
		'��������� ��������.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), (),)

	def SaveAs(self, fileName=defaultNamedNotOptArg):
		'��������� �������� � ����� ������ �����.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((8, 0),),fileName
			)

	def SaveAsEx(self, fileName=defaultNamedNotOptArg, SaveMode=defaultNamedNotOptArg):
		'��������� �������� � ����� ������ �����.'
		return self._oleobj_.InvokeTypes(66, LCID, 1, (11, 0), ((8, 0), (3, 0)),fileName
			, SaveMode)

	def SaveAsToAdditionFormat(self, fileName=defaultNamedNotOptArg, additionPar=defaultNamedNotOptArg):
		'���������  �������� � �������������� ������� jgs, sat, xt, x_b, step, stl, VRML.'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (11, 0), ((8, 0), (9, 0)),fileName
			, additionPar)

	def SaveAsToRasterFormat(self, fileName=defaultNamedNotOptArg, rasterPar=defaultNamedNotOptArg):
		'��������� �������� � ��������� ������.'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (11, 0), ((8, 0), (9, 0)),fileName
			, rasterPar)

	def SaveAsToUncompressedRasterFormat(self, fileName=defaultNamedNotOptArg, rasterPar=defaultNamedNotOptArg):
		'��������� �������� ��� ������ � ��������� ������.'
		return self._oleobj_.InvokeTypes(49, LCID, 1, (11, 0), ((8, 0), (9, 0)),fileName
			, rasterPar)

	def SetActive(self):
		'������ �������� �������.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), (),)

	def SetPartFromFile(self, fileName=defaultNamedNotOptArg, part=defaultNamedNotOptArg, externalFile=True):
		'������ ��������� �� �����.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (11, 0), ((8, 0), (9, 0), (11, 48)),fileName
			, part, externalFile)

	def SetPartFromFileEx(self, fileName=defaultNamedNotOptArg, part=defaultNamedNotOptArg, externalFile=True, redraw=False):
		'�������� � ������ ��������� �� ����� ��� �� ���������� �������.'
		return self._oleobj_.InvokeTypes(60, LCID, 1, (11, 0), ((8, 0), (9, 0), (11, 48), (11, 48)),fileName
			, part, externalFile, redraw)

	def SetRollBackFeature(self, obj=defaultNamedNotOptArg):
		'���������� ��������� ��������� � ������.'
		return self._oleobj_.InvokeTypes(73, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def StopLibRequest(self):
		'���������� ������� �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

	def UpdateDocumentParam(self):
		'�������� ��������� ���������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	def UserGetCursor(self, prompt=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ���������� �������.'
		return self._ApplyTypes_(22, 1, (11, 0), ((8, 1), (16389, 2), (16389, 2), (16389, 2)), 'UserGetCursor', None,prompt
			, x, y, z)

	def UserGetPlacementAndEntity(self, entityCount=defaultNamedNotOptArg):
		'������� �������� �������� �������������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), ((3, 0),),entityCount
			)

	def UserSelectEntity(self, filterObject=defaultNamedNotOptArg, methodName=defaultNamedNotOptArg, prompt=defaultNamedNotOptArg, hInst=0
			, val=None):
		'������� �������� �������.'
		ret = self._oleobj_.InvokeTypes(25, LCID, 1, (9, 0), ((9, 0), (8, 0), (8, 0), (3, 48), (9, 48)),filterObject
			, methodName, prompt, hInst, val)
		if ret is not None:
			ret = Dispatch(ret, 'UserSelectEntity', None)
		return ret

	def UserSelectEntityEx(self, filterObject=defaultNamedNotOptArg, methodName=defaultNamedNotOptArg, prompt=defaultNamedNotOptArg, hInst=0
			, val=None, processParam=None):
		'������� �������� �������.'
		ret = self._oleobj_.InvokeTypes(71, LCID, 1, (9, 0), ((9, 0), (8, 0), (8, 0), (3, 48), (9, 48), (13, 48)),filterObject
			, methodName, prompt, hInst, val, processParam
			)
		if ret is not None:
			ret = Dispatch(ret, 'UserSelectEntityEx', None)
		return ret

	def UserSelectEntityEx2(self, filterObject=defaultNamedNotOptArg, methodName=defaultNamedNotOptArg, prompt=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg
			, val=None, processParam=None):
		'������� �������� �������.'
		ret = self._oleobj_.InvokeTypes(86, LCID, 1, (9, 0), ((9, 0), (8, 0), (8, 0), (12, 0), (9, 48), (13, 48)),filterObject
			, methodName, prompt, hInst, val, processParam
			)
		if ret is not None:
			ret = Dispatch(ret, 'UserSelectEntityEx2', None)
		return ret

	def ZoomPrevNextOrAll(self, type=defaultNamedNotOptArg):
		'��������� ����������� ��������� ����.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (11, 0), ((2, 0),),type
			)

	def close(self):
		'������� 3D ��������.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), (),)

	def ksDeleteObj(self, ref=defaultNamedNotOptArg):
		'������� �� ������ ������ � ���������� ref.'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (3, 0), ((3, 0),),ref
			)

	def ksGetObjParam(self, ref=defaultNamedNotOptArg, param=defaultNamedNotOptArg, parType=-1):
		'�������� ��������� �������.'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (3, 0), ((3, 0), (9, 0), (3, 48)),ref
			, param, parType)

	def ksIsSlaveSpcOpened(self):
		'������ �� slave ����� ��.'
		return self._oleobj_.InvokeTypes(64, LCID, 1, (3, 0), (),)

	def ksSetObjParam(self, referObj=defaultNamedNotOptArg, param=defaultNamedNotOptArg, parType=-1):
		'������������� ����� ��������� �������.'
		return self._oleobj_.InvokeTypes(48, LCID, 1, (3, 0), ((3, 0), (9, 0), (3, 48)),referObj
			, param, parType)

	_prop_map_get_ = {
		"author": (3, 2, (8, 0), (), "author", None),
		"comment": (2, 2, (8, 0), (), "comment", None),
		"dismantleMode": (68, 2, (11, 0), (), "dismantleMode", None),
		"drawMode": (41, 2, (3, 0), (), "drawMode", None),
		"enableRollBackFeaturesInCollections": (75, 2, (11, 0), (), "enableRollBackFeaturesInCollections", None),
		"fileName": (1, 2, (8, 0), (), "fileName", None),
		"hideAllAuxiliaryGeom": (81, 2, (11, 0), (), "hideAllAuxiliaryGeom", None),
		"hideAllAxis": (51, 2, (11, 0), (), "hideAllAxis", None),
		"hideAllControlPoints": (78, 2, (11, 0), (), "hideAllControlPoints", None),
		"hideAllCurves": (77, 2, (11, 0), (), "hideAllCurves", None),
		"hideAllDesignations": (80, 2, (11, 0), (), "hideAllDesignations", None),
		"hideAllDimensions": (79, 2, (11, 0), (), "hideAllDimensions", None),
		"hideAllPlaces": (53, 2, (11, 0), (), "hideAllPlaces", None),
		"hideAllPlanes": (50, 2, (11, 0), (), "hideAllPlanes", None),
		"hideAllSketches": (52, 2, (11, 0), (), "hideAllSketches", None),
		"hideAllSurfaces": (54, 2, (11, 0), (), "hideAllSurfaces", None),
		"hideAllThreads": (55, 2, (11, 0), (), "hideAllThreads", None),
		"hideInComponentsMode": (82, 2, (11, 0), (), "hideInComponentsMode", None),
		"hideLayoutGeometry": (85, 2, (11, 0), (), "hideLayoutGeometry", None),
		"perspective": (40, 2, (11, 0), (), "perspective", None),
		"reference": (39, 2, (3, 0), (), "reference", None),
		"shadedWireframe": (63, 2, (11, 0), (), "shadedWireframe", None),
		"treeNeedRebuild": (70, 2, (11, 0), (), "treeNeedRebuild", None),
		"windowNeedRebuild": (84, 2, (11, 0), (), "windowNeedRebuild", None),
		"invisibleMode": (4, 2, (11, 0), (), "invisibleMode", None),
	}
	_prop_map_put_ = {
		"author" : ((3, LCID, 4, 0),()),
		"comment" : ((2, LCID, 4, 0),()),
		"dismantleMode" : ((68, LCID, 4, 0),()),
		"drawMode" : ((41, LCID, 4, 0),()),
		"enableRollBackFeaturesInCollections" : ((75, LCID, 4, 0),()),
		"fileName" : ((1, LCID, 4, 0),()),
		"hideAllAuxiliaryGeom" : ((81, LCID, 4, 0),()),
		"hideAllAxis" : ((51, LCID, 4, 0),()),
		"hideAllControlPoints" : ((78, LCID, 4, 0),()),
		"hideAllCurves" : ((77, LCID, 4, 0),()),
		"hideAllDesignations" : ((80, LCID, 4, 0),()),
		"hideAllDimensions" : ((79, LCID, 4, 0),()),
		"hideAllPlaces" : ((53, LCID, 4, 0),()),
		"hideAllPlanes" : ((50, LCID, 4, 0),()),
		"hideAllSketches" : ((52, LCID, 4, 0),()),
		"hideAllSurfaces" : ((54, LCID, 4, 0),()),
		"hideAllThreads" : ((55, LCID, 4, 0),()),
		"hideInComponentsMode" : ((82, LCID, 4, 0),()),
		"hideLayoutGeometry" : ((85, LCID, 4, 0),()),
		"perspective" : ((40, LCID, 4, 0),()),
		"reference" : ((39, LCID, 4, 0),()),
		"shadedWireframe" : ((63, LCID, 4, 0),()),
		"treeNeedRebuild" : ((70, LCID, 4, 0),()),
		"windowNeedRebuild" : ((84, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDocument3DNotify:
	'������� ��� 3D ���������.'
	CLSID = CLSID_Sink = IID('{B6C1BCFD-68DA-4A0A-A95C-296084C6A01A}')
	coclass_clsid = IID('{22B81342-42D6-4907-A91E-F75A959F2270}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnBeginRebuild",
		        2 : "OnRebuild",
		        3 : "OnBeginChoiceMaterial",
		        4 : "OnChoiceMaterial",
		        5 : "OnBeginChoiceMarking",
		        6 : "OnChoiceMarking",
		        7 : "OnBeginSetPartFromFile",
		        8 : "OnBeginCreatePartFromFile",
		        9 : "OnCreateEmbodiment",
		       10 : "OnDeleteEmbodiment",
		       11 : "OnChangeCurrentEmbodiment",
		       12 : "OnBeginChoiceProperty",
		       13 : "OnChoiceProperty",
		       14 : "OnBeginRollbackFeatures",
		       15 : "OnRollbackFeatures",
		       16 : "OnBedinLoadCombinationChange",
		       17 : "OnLoadCombinationChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnBeginRebuild(self):
#		'������ ������������ ������.'
#	def OnRebuild(self):
#		'������ �����������.'
#	def OnBeginChoiceMaterial(self):
#		'������ ������ ���������.'
#	def OnChoiceMaterial(self, material=defaultNamedNotOptArg, density=defaultNamedNotOptArg):
#		'�������� ����� ���������.'
#	def OnBeginChoiceMarking(self):
#		'������ ������ �����������.'
#	def OnChoiceMarking(self, marking=defaultNamedNotOptArg):
#		'�������� ����� �����������.'
#	def OnBeginSetPartFromFile(self):
#		'������ ��������� ���������� � ������ (�� ������� ������ �����).'
#	def OnBeginCreatePartFromFile(self, typeDoc=defaultNamedNotOptArg, plane=defaultNamedNotOptArg):
#		'������ �������� ���������� � ������  (�� ������� ������ �����).'
#	def OnCreateEmbodiment(self, marking=defaultNamedNotOptArg):
#		'��������� ����� ����������.'
#	def OnDeleteEmbodiment(self, marking=defaultNamedNotOptArg):
#		'������� ����������.'
#	def OnChangeCurrentEmbodiment(self, marking=defaultNamedNotOptArg):
#		'��������� ����������� �������.'
#	def OnBeginChoiceProperty(self, obj=defaultNamedNotOptArg, propID=defaultNamedNotOptArg):
#		'������ ������ ��������.'
#	def OnChoiceProperty(self, obj=defaultNamedNotOptArg, propID=defaultNamedNotOptArg):
#		'�������� ����� ��������.'
#	def OnBeginRollbackFeatures(self):
#		'������ ������ ������ ������.'
#	def OnRollbackFeatures(self):
#		'���������� ������ ������ ������.'
#	def OnBedinLoadCombinationChange(self, index=defaultNamedNotOptArg):
#		'������ ������������ ���� ��������.'
#	def OnLoadCombinationChange(self, index=defaultNamedNotOptArg):
#		'���������� ������������ ���� ��������.'


class ksDocument3DNotifyResult(DispatchBaseClass):
	'�������������� ��������� ��� ������� ���������� 3D.'
	CLSID = IID('{9F88CAAA-A50F-46F4-904A-846C792FA649}')
	coclass_clsid = IID('{129E9083-E4D2-4991-B69F-70B696AD1A55}')

	def GetNotifyObject(self):
		'������ ��� �������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNotifyObject', None)
		return ret

	def GetNotifyObjectType(self):
		'��� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def GetNotifyType(self):
		'��� �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetRequestFilesType(self):
		'��� ��������, �������������� ����.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDocumentFileNotify:
	'C������ ��������� - ������ � ������.'
	CLSID = CLSID_Sink = IID('{324C1A45-67AD-41FB-BE57-624F930646F1}')
	coclass_clsid = IID('{111CEFE3-A0A7-11D6-95CE-00C0262D30E3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnBeginCloseDocument",
		        2 : "OnCloseDocument",
		        3 : "OnBeginSaveDocument",
		        4 : "OnSaveDocument",
		        5 : "OnActivate",
		        6 : "OnDeactivate",
		        7 : "OnBeginSaveAsDocument",
		        8 : "OnDocumentFrameOpen",
		        9 : "OnProcessActivate",
		       10 : "OnProcessDeactivate",
		       11 : "OnBeginProcess",
		       12 : "OnEndProcess",
		       13 : "OnBeginAutoSaveDocument",
		       14 : "OnAutoSaveDocument",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnBeginCloseDocument(self):
#		'������ �������� ���������.'
#	def OnCloseDocument(self):
#		'�������� ������.'
#	def OnBeginSaveDocument(self, fileName=defaultNamedNotOptArg):
#		'������ ���������� ���������.'
#	def OnSaveDocument(self):
#		'�������� ��������.'
#	def OnActivate(self):
#		'�������� �������������.'
#	def OnDeactivate(self):
#		'�������� ���������������.'
#	def OnBeginSaveAsDocument(self):
#		'������ ���������� ��������� c ������ ������ (�� ������� ������ �����).'
#	def OnDocumentFrameOpen(self, v=defaultNamedNotOptArg):
#		'���� ��������� ���������.'
#	def OnProcessActivate(self, iD=defaultNamedNotOptArg):
#		'����������� ��������.'
#	def OnProcessDeactivate(self, iD=defaultNamedNotOptArg):
#		'������������� ��������.'
#	def OnBeginProcess(self, iD=defaultNamedNotOptArg):
#		'������ ��������.'
#	def OnEndProcess(self, iD=defaultNamedNotOptArg, Success=defaultNamedNotOptArg):
#		'���������� ��������.'
#	def OnBeginAutoSaveDocument(self, fileName=defaultNamedNotOptArg):
#		'������ �������������� ���������.'
#	def OnAutoSaveDocument(self):
#		'�������� ������������.'


class ksDocumentParam(DispatchBaseClass):
	'��������� ���������� ���������.'
	CLSID = IID('{FBCC5B96-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5B98-996C-11D6-8732-00C0262CDD2C}')

	def GetLayoutParam(self):
		'���������� ��������� ���������� ���������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetLayoutParam', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"author": (3, 2, (8, 0), (), "author", None),
		"comment": (2, 2, (8, 0), (), "comment", None),
		"fileName": (1, 2, (8, 0), (), "fileName", None),
		"regime": (5, 2, (2, 0), (), "regime", None),
		"type": (4, 2, (2, 0), (), "type", None),
	}
	_prop_map_put_ = {
		"author" : ((3, LCID, 4, 0),()),
		"comment" : ((2, LCID, 4, 0),()),
		"fileName" : ((1, LCID, 4, 0),()),
		"regime" : ((5, LCID, 4, 0),()),
		"type" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDocumentTxt(DispatchBaseClass):
	'��������� ��������.'
	CLSID = IID('{74D745F1-9A3A-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{74D745F3-9A3A-11D6-95CE-00C0262D30E3}')

	def GetStamp(self):
		'������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetStamp', None)
		return ret

	def GetStampEx(self, SheetNumb=defaultNamedNotOptArg):
		'������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), ((3, 0),),SheetNumb
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetStampEx', None)
		return ret

	def RasterFormatParam(self):
		'�������� ��������� �� ��������� ���������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RasterFormatParam', None)
		return ret

	def SaveAsToRasterFormat(self, fileName=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'��������� �������� � ��������� ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((8, 0), (9, 0)),fileName
			, par)

	def SaveAsToUncompressedRasterFormat(self, fileName=defaultNamedNotOptArg, rasterPar=defaultNamedNotOptArg):
		'��������� �������� ��� ������ � ��������� ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((8, 0), (9, 0)),fileName
			, rasterPar)

	def ksCloseDocument(self):
		'������� ��������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def ksCreateDocument(self, par=defaultNamedNotOptArg):
		'������� ��������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((9, 0),),par
			)

	def ksGetDocumentPagesCount(self):
		'�������� ���������� ������ ���������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), (),)

	def ksGetObjParam(self, ref=defaultNamedNotOptArg, param=defaultNamedNotOptArg, parType=-1):
		'�������� ��������� �������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((3, 0), (9, 0), (3, 48)),ref
			, param, parType)

	def ksGetTxtDocumentPagesCount(self):
		'��� ���������� ��������� �������� ���������� ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	def ksOpenDocument(self, nameDoc=defaultNamedNotOptArg, regim=defaultNamedNotOptArg):
		'������� ��������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((8, 0), (2, 0)),nameDoc
			, regim)

	def ksSaveDocument(self, fileName=defaultNamedNotOptArg):
		'��������� ��������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((8, 0),),fileName
			)

	def ksSaveDocumentEx(self, fileName=defaultNamedNotOptArg, SaveMode=defaultNamedNotOptArg):
		'��������� ��������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((8, 0), (3, 0)),fileName
			, SaveMode)

	def ksSetObjParam(self, ref=defaultNamedNotOptArg, param=defaultNamedNotOptArg, parType=-1):
		'������������� ����� ��������� �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((3, 0), (9, 0), (3, 48)),ref
			, param, parType)

	_prop_map_get_ = {
		"reference": (1, 2, (3, 0), (), "reference", None),
	}
	_prop_map_put_ = {
		"reference" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDoubleValue(DispatchBaseClass):
	'��������� ����.'
	CLSID = IID('{7F7D6F9C-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6F9E-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"value": (1, 2, (5, 0), (), "value", None),
	}
	_prop_map_put_ = {
		"value" : ((1, LCID, 4, 0),()),
	}
	# Default property for this class is 'value'
	def __call__(self):
		return self._ApplyTypes_(*(1, 2, (5, 0), (), "value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksDynamicArray(DispatchBaseClass):
	'��������� ������������� �������.'
	CLSID = IID('{4D91CD9A-6E02-409D-9360-CF7FEF60D31C}')
	coclass_clsid = IID('{FD30B325-9E27-42CA-ADCF-C30EEBE0BBB8}')

	def ksAddArrayItem(self, index=defaultNamedNotOptArg, item=defaultNamedNotOptArg):
		'�������� ������� � ������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((3, 0), (9, 0)),index
			, item)

	def ksClearArray(self):
		'������� ������������ ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	def ksDeleteArray(self):
		'������� ������������ ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def ksExcludeArrayItem(self, index=defaultNamedNotOptArg):
		'��������� ������� �� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((3, 0),),index
			)

	def ksGetArrayCount(self):
		'������ ���������� ��������� � ������������ �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	def ksGetArrayItem(self, index=defaultNamedNotOptArg, item=defaultNamedNotOptArg):
		'�������� ��������� �������� � �������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((3, 0), (9, 0)),index
			, item)

	def ksGetArrayType(self):
		'������ ��� ������������� �������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), (),)

	def ksSetArrayItem(self, index=defaultNamedNotOptArg, item=defaultNamedNotOptArg):
		'�������� ��������� �������� � �������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((3, 0), (9, 0)),index
			, item)

	_prop_map_get_ = {
		"reference": (1, 2, (3, 0), (), "reference", None),
	}
	_prop_map_put_ = {
		"reference" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksEdgeCollection(DispatchBaseClass):
	'��������� ������� �����.'
	CLSID = IID('{6096A4FD-970B-468C-815E-37CA1970A203}')
	coclass_clsid = IID('{7519BF63-27B3-415F-AC25-904910CB27B5}')

	def FindIt(self, entity=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((9, 0),),entity
			)

	def First(self):
		'�������� ������ �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetCount(self):
		'�������� ���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'�������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def refresh(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksEdgeDefinition(DispatchBaseClass):
	'��������� �����.'
	CLSID = IID('{0307BBAB-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BBAD-C193-11D6-8734-00C0262CDD2C}')

	def EdgeCollection(self, begin=defaultNamedNotOptArg):
		'�������� ������ �����, ����������� � �������� ������ � ��� ������ - begin==TRUE, ����� - begin==FALSE.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((11, 0),),begin
			)
		if ret is not None:
			ret = Dispatch(ret, 'EdgeCollection', None)
		return ret

	def GetAdjacentFace(self, facePlus=defaultNamedNotOptArg):
		'�������� �����, � ������� ����� ������ � loop (TRUE - ���������� ����).'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((11, 0),),facePlus
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetAdjacentFace', None)
		return ret

	def GetCurve3D(self):
		'�������� ��������� �������������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurve3D', None)
		return ret

	def GetEntity(self):
		'�������� ��������� �� ������ - �����.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEntity', None)
		return ret

	def GetLength(self, bitVector=defaultNamedNotOptArg):
		'�������� ����� ����� (ST_MIX_MM..ST_MIX_M ������� ���������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (5, 0), ((19, 0),),bitVector
			)

	def GetOwnerEntity(self):
		'�������� ������ ���������� ��� �����.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetOwnerEntity', None)
		return ret

	def GetVertex(self, start=defaultNamedNotOptArg):
		'�������� ������� ��������� � ��������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((11, 0),),start
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetVertex', None)
		return ret

	def IsArc(self):
		'�������� �� ������ �����.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	def IsCircle(self):
		'�������� �� ������ �����������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	def IsEllipse(self):
		'�������� �� ������ ��������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	def IsNurbs(self):
		'�������� �� ������ �������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

	def IsPeriodic(self):
		'�������� ������������� ��������� ������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

	def IsStraight(self):
		'TRUE - ����� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'�������� ��������� ����������� �������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), (),)

	def OrientedEdgeCollection(self):
		'�������� ������ ��������������� �����, ������� ��������� �� ������ �����.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'OrientedEdgeCollection', None)
		return ret

	_prop_map_get_ = {
		"sketchEdge": (16, 2, (11, 0), (), "sketchEdge", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksEllipse3dParam(DispatchBaseClass):
	'��������� ���������� 3d Ellipse.'
	CLSID = IID('{5B8082B8-6AD3-4509-826D-D23B7F613213}')
	coclass_clsid = IID('{33583282-14FB-4975-B040-9267A639E340}')

	def GetPlacement(self):
		'�������� �� ������� - ����� � ���������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	_prop_map_get_ = {
		"majorRadius": (1, 2, (5, 0), (), "majorRadius", None),
		"minorRadius": (2, 2, (5, 0), (), "minorRadius", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksEllipseArcParam(DispatchBaseClass):
	'��������� ���� ������� �� �����.'
	CLSID = IID('{364521A9-94B5-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{364521AB-94B5-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"A": (3, 2, (5, 0), (), "A", None),
		"B": (4, 2, (5, 0), (), "B", None),
		"angle": (5, 2, (5, 0), (), "angle", None),
		"angleFirst": (6, 2, (5, 0), (), "angleFirst", None),
		"angleSecond": (7, 2, (5, 0), (), "angleSecond", None),
		"direction": (8, 2, (5, 0), (), "direction", None),
		"style": (9, 2, (3, 0), (), "style", None),
		"xc": (1, 2, (5, 0), (), "xc", None),
		"yc": (2, 2, (5, 0), (), "yc", None),
	}
	_prop_map_put_ = {
		"A" : ((3, LCID, 4, 0),()),
		"B" : ((4, LCID, 4, 0),()),
		"angle" : ((5, LCID, 4, 0),()),
		"angleFirst" : ((6, LCID, 4, 0),()),
		"angleSecond" : ((7, LCID, 4, 0),()),
		"direction" : ((8, LCID, 4, 0),()),
		"style" : ((9, LCID, 4, 0),()),
		"xc" : ((1, LCID, 4, 0),()),
		"yc" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksEllipseArcParam1(DispatchBaseClass):
	'��������� ���� ������� �� ����������.'
	CLSID = IID('{364521AC-94B5-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{364521AE-94B5-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"A": (3, 2, (5, 0), (), "A", None),
		"B": (4, 2, (5, 0), (), "B", None),
		"angle": (5, 2, (5, 0), (), "angle", None),
		"direction": (8, 2, (5, 0), (), "direction", None),
		"parFirst": (6, 2, (5, 0), (), "parFirst", None),
		"parSecond": (7, 2, (5, 0), (), "parSecond", None),
		"style": (9, 2, (3, 0), (), "style", None),
		"xc": (1, 2, (5, 0), (), "xc", None),
		"yc": (2, 2, (5, 0), (), "yc", None),
	}
	_prop_map_put_ = {
		"A" : ((3, LCID, 4, 0),()),
		"B" : ((4, LCID, 4, 0),()),
		"angle" : ((5, LCID, 4, 0),()),
		"direction" : ((8, LCID, 4, 0),()),
		"parFirst" : ((6, LCID, 4, 0),()),
		"parSecond" : ((7, LCID, 4, 0),()),
		"style" : ((9, LCID, 4, 0),()),
		"xc" : ((1, LCID, 4, 0),()),
		"yc" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksEllipseParam(DispatchBaseClass):
	'��������� �������.'
	CLSID = IID('{364521A6-94B5-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{364521A8-94B5-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"A": (3, 2, (5, 0), (), "A", None),
		"B": (4, 2, (5, 0), (), "B", None),
		"angle": (5, 2, (5, 0), (), "angle", None),
		"style": (6, 2, (3, 0), (), "style", None),
		"xc": (1, 2, (5, 0), (), "xc", None),
		"yc": (2, 2, (5, 0), (), "yc", None),
	}
	_prop_map_put_ = {
		"A" : ((3, LCID, 4, 0),()),
		"B" : ((4, LCID, 4, 0),()),
		"angle" : ((5, LCID, 4, 0),()),
		"style" : ((6, LCID, 4, 0),()),
		"xc" : ((1, LCID, 4, 0),()),
		"yc" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksEmbodiment3D(DispatchBaseClass):
	'����������'
	CLSID = IID('{4F6A3404-8F06-4363-AF66-4CDCC4E09462}')
	coclass_clsid = None

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksEntity(DispatchBaseClass):
	'3D ������.'
	CLSID = IID('{508A0CCA-9D74-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{508A0CCC-9D74-11D6-95CE-00C0262D30E3}')

	def BodyCollection(self):
		'�������� ������ ���������� ���.'
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'BodyCollection', None)
		return ret

	def ColorParam(self):
		'��������� ����� �������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ColorParam', None)
		return ret

	def Create(self):
		'������� ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	def GetAdvancedColor(self, color=pythoncom.Missing, ambient=pythoncom.Missing, diffuse=pythoncom.Missing, specularity=pythoncom.Missing
			, shininess=pythoncom.Missing, transparency=pythoncom.Missing, emission=pythoncom.Missing):
		'�������� ��������� ����� �������.'
		return self._ApplyTypes_(12, 1, (11, 0), ((16387, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetAdvancedColor', None,color
			, ambient, diffuse, specularity, shininess, transparency
			, emission)

	def GetBodyParts(self):
		'�������� ��������� ������ ����.'
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetBodyParts', None)
		return ret

	def GetDefinition(self):
		'�������� ��������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDefinition', None)
		return ret

	def GetFeature(self):
		'�������� ������ ������, ��������� � ������ ��������.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFeature', None)
		return ret

	def GetParent(self):
		'�������� ����������, ������� ����������� ������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetParent', None)
		return ret

	def IsCreated(self):
		'True - ��������� ������ ��������� � ������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), (),)

	def IsIt(self, objType=defaultNamedNotOptArg):
		'��������� ������ �� ������������ ����.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((3, 0),),objType
			)

	def SetAdvancedColor(self, color=defaultNamedNotOptArg, ambient=-47.0, diffuse=-47.0, specularity=-47.0
			, shininess=-47.0, transparency=1.0, emission=-47.0):
		'���������� ��������� ����� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((3, 1), (5, 49), (5, 49), (5, 49), (5, 49), (5, 49), (5, 49)),color
			, ambient, diffuse, specularity, shininess, transparency
			, emission)

	def Update(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"excluded": (4, 2, (11, 0), (), "excluded", None),
		"hidden": (1, 2, (11, 0), (), "hidden", None),
		"name": (2, 2, (8, 0), (), "name", None),
		"useColor": (18, 2, (3, 0), (), "useColor", None),
		"MultiBodyParts": (16, 2, (11, 0), (), "MultiBodyParts", None),
		"type": (3, 2, (2, 0), (), "type", None),
	}
	_prop_map_put_ = {
		"excluded" : ((4, LCID, 4, 0),()),
		"hidden" : ((1, LCID, 4, 0),()),
		"name" : ((2, LCID, 4, 0),()),
		"useColor" : ((18, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksEntityCollection(DispatchBaseClass):
	'������ ��������.'
	CLSID = IID('{B0170141-C02C-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{B0170143-C02C-11D6-8734-00C0262CDD2C}')

	def Add(self, entity=defaultNamedNotOptArg):
		'�������� ������ � ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),entity
			)

	def AddAt(self, entity=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� ������ � ������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 0), (3, 0)),entity
			, index)

	def AddBefore(self, entity=defaultNamedNotOptArg, base=defaultNamedNotOptArg):
		'�������� ������ � ������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((9, 0), (9, 0)),entity
			, base)

	def Clear(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), (),)

	def DetachByBody(self, entity=defaultNamedNotOptArg):
		'������� ������ �� �������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((9, 0),),entity
			)

	def DetachByIndex(self, index=defaultNamedNotOptArg):
		'������� ������ �� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((3, 0),),index
			)

	def FindIt(self, entity=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((9, 0),),entity
			)

	def First(self):
		'�������� ��������� �� ��������� ������� ��������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ��������� �� ��������� �������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetByName(self, name=defaultNamedNotOptArg, testFullName=False, testIgnoreCase=True):
		'�������� ��������� �� ��������� �������� �� �����.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), ((8, 0), (11, 48), (11, 48)),name
			, testFullName, testIgnoreCase)
		if ret is not None:
			ret = Dispatch(ret, 'GetByName', None)
		return ret

	def GetCount(self):
		'�������� ���������� ��������� � �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'�������� ��������� �� ��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'�������� ��������� �� ��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'�������� ��������� �� ��������� ����������� ��������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def SelectByPoint(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg):
		'������� �� ������� �������� �� ���������� �����.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0)),x
			, y, z)

	def SetByIndex(self, entity=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� ������ �� �������.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((9, 0), (3, 0)),entity
			, index)

	def refresh(self):
		'�������� ������ ����������� �������� ���������� ������ (����, ���������� � �.�.).'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksEquidistantParam(DispatchBaseClass):
	'��������� ������������.'
	CLSID = IID('{364521AF-94B5-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{364521B1-94B5-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"cutMode": (3, 2, (11, 0), (), "cutMode", None),
		"degState": (4, 2, (11, 0), (), "degState", None),
		"geoObj": (1, 2, (3, 0), (), "geoObj", None),
		"radLeft": (6, 2, (5, 0), (), "radLeft", None),
		"radRight": (5, 2, (5, 0), (), "radRight", None),
		"side": (2, 2, (2, 0), (), "side", None),
		"style": (7, 2, (3, 0), (), "style", None),
	}
	_prop_map_put_ = {
		"cutMode" : ((3, LCID, 4, 0),()),
		"degState" : ((4, LCID, 4, 0),()),
		"geoObj" : ((1, LCID, 4, 0),()),
		"radLeft" : ((6, LCID, 4, 0),()),
		"radRight" : ((5, LCID, 4, 0),()),
		"side" : ((2, LCID, 4, 0),()),
		"style" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksEvolutionSurfaceDefinition(DispatchBaseClass):
	'��������� �������������� �����������.'
	CLSID = IID('{2BD4C79E-E2C3-42E8-8FCC-B51FFBDE9F69}')
	coclass_clsid = IID('{DB947005-AA19-4ED2-9775-E7BD80BE872E}')

	def GetPathLength(self, bitVector=defaultNamedNotOptArg):
		'�������� ����� ������ ����������(ST_MIX_MM..ST_MIX_M ������� ���������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (5, 0), ((19, 0),),bitVector
			)

	def GetSketch(self):
		'�������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def PathPartArray(self):
		'�������� ��������� ������� ������ ����������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PathPartArray', None)
		return ret

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'�������� ��������� ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	_prop_map_get_ = {
		"closedShell": (2, 2, (11, 0), (), "closedShell", None),
		"sketchShiftType": (1, 2, (2, 0), (), "sketchShiftType", None),
	}
	_prop_map_put_ = {
		"closedShell" : ((2, LCID, 4, 0),()),
		"sketchShiftType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksExtrusionParam(DispatchBaseClass):
	'��������� ������������.'
	CLSID = IID('{DEEFF02C-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF02E-C3E2-11D6-8734-00C0262CDD2C}')

	_prop_map_get_ = {
		"depthNormal": (2, 2, (5, 0), (), "depthNormal", None),
		"depthReverse": (6, 2, (5, 0), (), "depthReverse", None),
		"direction": (9, 2, (3, 0), (), "direction", None),
		"draftOutwardNormal": (4, 2, (11, 0), (), "draftOutwardNormal", None),
		"draftOutwardReverse": (8, 2, (11, 0), (), "draftOutwardReverse", None),
		"draftValueNormal": (3, 2, (5, 0), (), "draftValueNormal", None),
		"draftValueReverse": (7, 2, (5, 0), (), "draftValueReverse", None),
		"typeNormal": (1, 2, (2, 0), (), "typeNormal", None),
		"typeReverse": (5, 2, (2, 0), (), "typeReverse", None),
	}
	_prop_map_put_ = {
		"depthNormal" : ((2, LCID, 4, 0),()),
		"depthReverse" : ((6, LCID, 4, 0),()),
		"direction" : ((9, LCID, 4, 0),()),
		"draftOutwardNormal" : ((4, LCID, 4, 0),()),
		"draftOutwardReverse" : ((8, LCID, 4, 0),()),
		"draftValueNormal" : ((3, LCID, 4, 0),()),
		"draftValueReverse" : ((7, LCID, 4, 0),()),
		"typeNormal" : ((1, LCID, 4, 0),()),
		"typeReverse" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksExtrusionSurfaceDefinition(DispatchBaseClass):
	'��������� ����������� ������������.'
	CLSID = IID('{B20E24C3-5E4A-4CDA-A1ED-6BB8EBC81A29}')
	coclass_clsid = IID('{31E66F64-B93D-4196-B3FE-B6CCB679610F}')

	def ExtrusionParam(self):
		'��������� ���������� ������������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ExtrusionParam', None)
		return ret

	def GetDepthObject(self, normal=defaultNamedNotOptArg):
		'�������� ������ �������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), ((11, 0),),normal
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetDepthObject', None)
		return ret

	def GetSideParam(self, side1=defaultNamedNotOptArg, type=pythoncom.Missing, depth=pythoncom.Missing, draftValue=pythoncom.Missing
			, draftOutward=pythoncom.Missing):
		'�������� ��������� ������������ � ���� �������.'
		return self._ApplyTypes_(5, 1, (11, 0), ((11, 1), (16386, 2), (16389, 2), (16389, 2), (16395, 2)), 'GetSideParam', None,side1
			, type, depth, draftValue, draftOutward)

	def GetSketch(self):
		'�������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def ResetDepthObject(self, normal=defaultNamedNotOptArg):
		'����� ������� �������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((11, 0),),normal
			)

	def SetDepthObject(self, normal=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'���������� ������ �������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((11, 0), (9, 0)),normal
			, obj)

	def SetSideParam(self, side1=defaultNamedNotOptArg, type=0, depth=1.0, draftValue=0.0
			, draftOutward=False):
		'���������� ��������� ������������ � ���� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((11, 1), (2, 48), (5, 48), (5, 48), (11, 48)),side1
			, type, depth, draftValue, draftOutward)

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'�������� ��������� ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	_prop_map_get_ = {
		"closedShell": (2, 2, (2, 0), (), "closedShell", None),
		"directionType": (1, 2, (2, 0), (), "directionType", None),
	}
	_prop_map_put_ = {
		"closedShell" : ((2, LCID, 4, 0),()),
		"directionType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksFaceCollection(DispatchBaseClass):
	'��������� ������� ������.'
	CLSID = IID('{0E95ACE0-0E73-406F-AE94-E8A0592E298D}')
	coclass_clsid = IID('{CB7B9677-9F62-473E-9663-AD516B5F37B5}')

	def FindIt(self, entity=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((9, 0),),entity
			)

	def First(self):
		'�������� ������ �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetByName(self, name=defaultNamedNotOptArg, testFullName=False, testIgnoreCase=True):
		'�������� ��������� �� ��������� �������� �� �����.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), ((8, 0), (11, 48), (11, 48)),name
			, testFullName, testIgnoreCase)
		if ret is not None:
			ret = Dispatch(ret, 'GetByName', None)
		return ret

	def GetCount(self):
		'�������� ���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'�������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def refresh(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksFaceDefinition(DispatchBaseClass):
	'��������� �����.'
	CLSID = IID('{0307BBA8-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BBAA-C193-11D6-8734-00C0262CDD2C}')

	def ConnectedFaceCollection(self):
		'�������� ������ ������, ����������� � ������ ������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ConnectedFaceCollection', None)
		return ret

	def EdgeCollection(self):
		'�������� ������ �����, �������������� �����.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'EdgeCollection', None)
		return ret

	def GetArea(self, bitVector=defaultNamedNotOptArg):
		'�������� ������� ����� (ST_MIX_MM..ST_MIX_M ������� ���������.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (5, 0), ((19, 0),),bitVector
			)

	def GetCylinderParam(self, h=pythoncom.Missing, r=pythoncom.Missing):
		'�������� ��������� �������������� �����������.'
		return self._ApplyTypes_(4, 1, (11, 0), ((16389, 2), (16389, 2)), 'GetCylinderParam', None,h
			, r)

	def GetEntity(self):
		'�������� ��������� �� ������ - �����.'
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEntity', None)
		return ret

	def GetNextFace(self):
		'�������� ��������� ����� � ���� ����.'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextFace', None)
		return ret

	def GetOwnerEntity(self):
		'�������� ������ ���������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetOwnerEntity', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def GetTessellation(self):
		'�������� ��������� ������������.'
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTessellation', None)
		return ret

	def IsCone(self):
		'TRUE - ����� ����������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	def IsConnectedWith(self, faceDefinition=defaultNamedNotOptArg):
		'������� �� �����.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),faceDefinition
			)

	def IsCylinder(self):
		'TRUE - ����� ��������������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def IsNurbsSurface(self):
		'�������� �� ����� nurbs ������������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), (),)

	def IsPlanar(self):
		'TRUE - ����� �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	def IsRevolved(self):
		'������������ �� ����� ������������ ��������.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), (),)

	def IsSphere(self):
		'�������� �� ����� �����������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), (),)

	def IsSwept(self):
		'������������ �� ����� ������������ �� ����������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), (),)

	def IsTorus(self):
		'�������� �� ����� �����.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'�������� ��������� ����������� �������.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), (),)

	def LoopCollection(self):
		'�������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'LoopCollection', None)
		return ret

	_prop_map_get_ = {
		"normalOrientation": (8, 2, (11, 0), (), "normalOrientation", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksFacet(DispatchBaseClass):
	'��������� ���������������� ��������.'
	CLSID = IID('{EB6AFBC0-C387-4E07-B24E-DDF2B7926A26}')
	coclass_clsid = IID('{F7F45063-0B37-40B1-B3AD-BB0A545EC2C8}')

	def GetNormal(self, index=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ���������� �������, index - ������ ����� � ��������.'
		return self._ApplyTypes_(3, 1, (11, 0), ((3, 1), (16388, 2), (16388, 2), (16388, 2)), 'GetNormal', None,index
			, x, y, z)

	def GetPoint(self, index=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ���������� �������, index - ������ ����� � ��������.'
		return self._ApplyTypes_(2, 1, (11, 0), ((3, 1), (16388, 2), (16388, 2), (16388, 2)), 'GetPoint', None,index
			, x, y, z)

	def GetPointsCount(self):
		'�������� ����� ������ ��������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetTessellationIndex(self, index=defaultNamedNotOptArg):
		'�������� ������ ������� � ������� ������ ����������������� �����, index - ������ ������� � ��������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), ((3, 0),),index
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksFeature(DispatchBaseClass):
	'��������� ������� ������.'
	CLSID = IID('{088BF9A8-37D3-4B15-A7CA-8C52FF1DBC41}')
	coclass_clsid = IID('{1978BA1C-EE2F-48ED-86D7-B15065B36E4A}')

	# Result is of type ksAttribute3DCollection
	def AttributeCollection(self, key1=defaultNamedNotOptArg, key2=defaultNamedNotOptArg, key3=defaultNamedNotOptArg, key4=defaultNamedNotOptArg
			, numb=defaultNamedNotOptArg):
		'�������� ������ ���������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((3, 0), (3, 0), (3, 0), (3, 0), (5, 0)),key1
			, key2, key3, key4, numb)
		if ret is not None:
			ret = Dispatch(ret, 'AttributeCollection', '{EB61A981-F63E-47E1-BEE8-2D1612C78E78}')
		return ret

	def BodyCollection(self):
		'�������� ������ ���������� ���.'
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'BodyCollection', None)
		return ret

	# Result is of type ksEntityCollection
	def EntityCollection(self, objType=defaultNamedNotOptArg):
		'�������� ������ ��������( �����. �����. �������).'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), ((2, 0),),objType
			)
		if ret is not None:
			ret = Dispatch(ret, 'EntityCollection', '{B0170141-C02C-11D6-8734-00C0262CDD2C}')
		return ret

	# Result is of type ksAttribute3DCollection
	def GetAttributeCollectionInSource(self, key1=defaultNamedNotOptArg, key2=defaultNamedNotOptArg, key3=defaultNamedNotOptArg, key4=defaultNamedNotOptArg
			, numb=defaultNamedNotOptArg, sourcePart=defaultNamedNotOptArg):
		'�������� ������ ��������� �� ���������.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), ((3, 0), (3, 0), (3, 0), (3, 0), (5, 0), (9, 0)),key1
			, key2, key3, key4, numb, sourcePart
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetAttributeCollectionInSource', '{EB61A981-F63E-47E1-BEE8-2D1612C78E78}')
		return ret

	def GetObject(self):
		'�������� ������ ������, ��������� � �������� ������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObject', None)
		return ret

	def GetOwnerFeature(self):
		'�������� ��������� �������-���������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetOwnerFeature', None)
		return ret

	def IsModified(self, recursive=defaultNamedNotOptArg):
		'�������������� �� ������ � ������� ���������� ������������ (recursive==TRUE �������� ���������� �� ��������� ��������).'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((11, 0),),recursive
			)

	def IsRollBacked(self):
		'����� �� ������ ���� ����� ���������� ������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'�������� ��������� ����������� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	def SubFeatureCollection(self, through=defaultNamedNotOptArg, libObject=defaultNamedNotOptArg):
		'�������� ������ ��������, �������� ������ ����� ������� (through==TRUE - �������� ��� �������, ���� �������, libObject==TRUE - �������� ����������� ��� ������������� ��������).'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((11, 0), (11, 0)),through
			, libObject)
		if ret is not None:
			ret = Dispatch(ret, 'SubFeatureCollection', None)
		return ret

	def VariableCollectionEx(self, sourse=defaultNamedNotOptArg):
		'�������� ������ ����������.'
		ret = self._oleobj_.InvokeTypes(16, LCID, 1, (9, 0), ((11, 0),),sourse
			)
		if ret is not None:
			ret = Dispatch(ret, 'VariableCollectionEx', None)
		return ret

	_prop_map_get_ = {
		"excluded": (9, 2, (11, 0), (), "excluded", None),
		"VariableCollection": (12, 2, (9, 0), (), "VariableCollection", None),
		"name": (1, 2, (8, 0), (), "name", None),
		"objectError": (17, 2, (3, 0), (), "objectError", None),
		"type": (7, 2, (2, 0), (), "type", None),
		"updateStamp": (2, 2, (19, 0), (), "updateStamp", None),
	}
	_prop_map_put_ = {
		"excluded" : ((9, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksFeatureCollection(DispatchBaseClass):
	'��������� ������� �������� ������.'
	CLSID = IID('{CE6A46FF-02B4-4C7E-AF50-3F3707C8B122}')
	coclass_clsid = IID('{87CD4F95-083C-4514-B8B4-025C8907D8F1}')

	def Add(self, obj=defaultNamedNotOptArg):
		'�������� ������ � ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def AddAt(self, obj=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� ������ � ������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 0), (3, 0)),obj
			, index)

	def AddBefore(self, obj=defaultNamedNotOptArg, base=defaultNamedNotOptArg):
		'�������� ������ � ������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((9, 0), (9, 0)),obj
			, base)

	# Result is of type ksAttribute3DCollection
	def AttributeCollection(self, key1=defaultNamedNotOptArg, key2=defaultNamedNotOptArg, key3=defaultNamedNotOptArg, key4=defaultNamedNotOptArg
			, numb=defaultNamedNotOptArg):
		'�������� ������ ���������.'
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((3, 0), (3, 0), (3, 0), (3, 0), (5, 0)),key1
			, key2, key3, key4, numb)
		if ret is not None:
			ret = Dispatch(ret, 'AttributeCollection', '{EB61A981-F63E-47E1-BEE8-2D1612C78E78}')
		return ret

	def Clear(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), (),)

	def DetachByBody(self, obj=defaultNamedNotOptArg):
		'������� ������ �� �������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def DetachByIndex(self, index=defaultNamedNotOptArg):
		'������� ������ �� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((3, 0),),index
			)

	def FindIt(self, entity=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((9, 0),),entity
			)

	# Result is of type ksFeature
	def First(self):
		'�������� ������ �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', '{088BF9A8-37D3-4B15-A7CA-8C52FF1DBC41}')
		return ret

	# Result is of type ksFeature
	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', '{088BF9A8-37D3-4B15-A7CA-8C52FF1DBC41}')
		return ret

	# Result is of type ksFeature
	def GetByName(self, name=defaultNamedNotOptArg, testFullName=False, testIgnoreCase=True):
		'�������� ��������� �� ��������� �������� �� �����.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), ((8, 0), (11, 48), (11, 48)),name
			, testFullName, testIgnoreCase)
		if ret is not None:
			ret = Dispatch(ret, 'GetByName', '{088BF9A8-37D3-4B15-A7CA-8C52FF1DBC41}')
		return ret

	def GetCount(self):
		'�������� ���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	# Result is of type ksFeature
	def Last(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', '{088BF9A8-37D3-4B15-A7CA-8C52FF1DBC41}')
		return ret

	# Result is of type ksFeature
	def Next(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', '{088BF9A8-37D3-4B15-A7CA-8C52FF1DBC41}')
		return ret

	# Result is of type ksFeature
	def Prev(self):
		'�������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', '{088BF9A8-37D3-4B15-A7CA-8C52FF1DBC41}')
		return ret

	def SetByIndex(self, obj=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� ������ �� �������.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((9, 0), (3, 0)),obj
			, index)

	def refresh(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksFilletDefinition(DispatchBaseClass):
	'��������� �������� ����������.'
	CLSID = IID('{0307BBB1-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BBB3-C193-11D6-8734-00C0262CDD2C}')

	def array(self):
		'������ ����������� ��������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'array', None)
		return ret

	_prop_map_get_ = {
		"radius": (1, 2, (5, 0), (), "radius", None),
		"tangent": (2, 2, (11, 0), (), "tangent", None),
	}
	_prop_map_put_ = {
		"radius" : ((1, LCID, 4, 0),()),
		"tangent" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksFragment(DispatchBaseClass):
	'��������.'
	CLSID = IID('{D06C9104-98CA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{D06C9106-98CA-11D6-8732-00C0262CDD2C}')

	def ksCloseLocalFragmentDefinition(self):
		'��������� ����������� ���������� ���������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), (),)

	def ksFragmentDefinition(self, fileName=defaultNamedNotOptArg, comment=defaultNamedNotOptArg, insertType=defaultNamedNotOptArg):
		'����������� ��������� �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), ((8, 0), (8, 0), (2, 0)),fileName
			, comment, insertType)

	def ksInsertFragment(self, p=defaultNamedNotOptArg, curentLayer=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), ((3, 0), (11, 0), (9, 0)),p
			, curentLayer, par)

	def ksInsertFragmentEx(self, p=defaultNamedNotOptArg, curentLayer=defaultNamedNotOptArg, par=defaultNamedNotOptArg, scaleProjLinesSize=defaultNamedNotOptArg):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((3, 0), (11, 0), (9, 0), (11, 0)),p
			, curentLayer, par, scaleProjLinesSize)

	def ksLocalFragmentDefinition(self, comment=defaultNamedNotOptArg):
		'��������� ������ ����������� ���������� ���������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((8, 0),),comment
			)

	def ksReadFragment(self, fileName=defaultNamedNotOptArg, curentLayer=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'������� ��������� �������� ����� � ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((8, 0), (11, 0), (9, 0)),fileName
			, curentLayer, par)

	def ksReadFragmentToGroup(self, fileName=defaultNamedNotOptArg, curentLayer=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'������� ��������� �������� �� ��������� ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), ((8, 0), (11, 0), (9, 0)),fileName
			, curentLayer, par)

	def ksReadFragmentToGroupEx(self, fileName=defaultNamedNotOptArg, curentLayer=defaultNamedNotOptArg, par=defaultNamedNotOptArg, scaleProjLinesSize=defaultNamedNotOptArg):
		'������� ��������� �������� �� ��������� ������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), ((8, 0), (11, 0), (9, 0), (11, 0)),fileName
			, curentLayer, par, scaleProjLinesSize)

	def ksWriteFragment(self, gr=defaultNamedNotOptArg, fileName=defaultNamedNotOptArg, comment=defaultNamedNotOptArg, xb=defaultNamedNotOptArg
			, yb=defaultNamedNotOptArg):
		'�������� ������ �� ��������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((3, 0), (8, 0), (8, 0), (5, 0), (5, 0)),gr
			, fileName, comment, xb, yb)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksFragmentLibrary(DispatchBaseClass):
	'��������� ���������� ����������.'
	CLSID = IID('{D06C910A-98CA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{D06C910C-98CA-11D6-8732-00C0262CDD2C}')

	def ksAddFragmentToLibrary(self, libName=defaultNamedNotOptArg, frwName=defaultNamedNotOptArg):
		'�������� �������� � ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((8, 0), (8, 0)),libName
			, frwName)

	def ksCheckFragmentLibrary(self, libName=defaultNamedNotOptArg, possibleMessage=defaultNamedNotOptArg):
		'�������� ������� �� ���������� ���������� � ������ ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), ((8, 0), (11, 0)),libName
			, possibleMessage)

	def ksChoiceFragmentFromLib(self, frwLibFile=defaultNamedNotOptArg, type=pythoncom.Missing):
		'����� ����� ��������� ��� ����� � ���������� ����������.'
		return self._ApplyTypes_(1, 1, (8, 0), ((8, 1), (16387, 2)), 'ksChoiceFragmentFromLib', None,frwLibFile
			, type)

	def ksExistFragmentInLibrary(self, frwName=defaultNamedNotOptArg):
		'������� ��������� ���������� �� �������� � ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), ((8, 0),),frwName
			)

	def ksFragmentLibraryOperation(self, libName=defaultNamedNotOptArg, type=defaultNamedNotOptArg):
		'������� ������������ ����������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), ((8, 0), (3, 0)),libName
			, type)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksHatchLineParam(DispatchBaseClass):
	'��������� ���������� ����� ���������.'
	CLSID = IID('{3F715E27-97D9-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3F715E29-97D9-11D6-95CE-00C0262D30E3}')

	def GetCurPar(self):
		'������ ���������������� ����� �����.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurPar', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	def SetCurPar(self, curPar=defaultNamedNotOptArg):
		'�������� ���������������� ����� �����.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),curPar
			)

	_prop_map_get_ = {
		"ang": (5, 2, (5, 0), (), "ang", None),
		"dx": (3, 2, (5, 0), (), "dx", None),
		"dy": (4, 2, (5, 0), (), "dy", None),
		"style": (7, 2, (2, 0), (), "style", None),
		"typeCurvStyle": (6, 2, (2, 0), (), "typeCurvStyle", None),
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"ang" : ((5, LCID, 4, 0),()),
		"dx" : ((3, LCID, 4, 0),()),
		"dy" : ((4, LCID, 4, 0),()),
		"style" : ((7, LCID, 4, 0),()),
		"typeCurvStyle" : ((6, LCID, 4, 0),()),
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksHatchParam(DispatchBaseClass):
	'��������� ���������.'
	CLSID = IID('{7F7D6F93-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6F95-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ang": (4, 2, (5, 0), (), "ang", None),
		"boundaries": (6, 2, (3, 0), (), "boundaries", None),
		"color": (7, 2, (3, 0), (), "color", None),
		"sheeting": (8, 2, (2, 0), (), "sheeting", None),
		"step": (3, 2, (5, 0), (), "step", None),
		"style": (9, 2, (3, 0), (), "style", None),
		"width": (5, 2, (5, 0), (), "width", None),
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"ang" : ((4, LCID, 4, 0),()),
		"boundaries" : ((6, LCID, 4, 0),()),
		"color" : ((7, LCID, 4, 0),()),
		"sheeting" : ((8, LCID, 4, 0),()),
		"step" : ((3, LCID, 4, 0),()),
		"style" : ((9, LCID, 4, 0),()),
		"width" : ((5, LCID, 4, 0),()),
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksHatchStyleParam(DispatchBaseClass):
	'��������� ���������� ����� ���������.'
	CLSID = IID('{3F715E2A-97D9-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3F715E2C-97D9-11D6-95CE-00C0262D30E3}')

	def GetArrLineParam(self):
		'������ ������ �������� �������� �����, ����������� � ��������� ksHatchLineParam.'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetArrLineParam', None)
		return ret

	def GetRefPoint(self):
		'������ ������� �����.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetRefPoint', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), (),)

	def SetArrLineParam(self, arrLineParam=defaultNamedNotOptArg):
		'�������� ������ �������� �������� �����, ����������� � ��������� ksHatchLineParam.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((9, 0),),arrLineParam
			)

	def SetRefPoint(self, refPoint=defaultNamedNotOptArg):
		'�������� ������� �����.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0),),refPoint
			)

	_prop_map_get_ = {
		"ang": (3, 2, (5, 0), (), "ang", None),
		"color": (7, 2, (3, 0), (), "color", None),
		"isScalable": (11, 2, (2, 0), (), "isScalable", None),
		"mayChangeAngle": (8, 2, (2, 0), (), "mayChangeAngle", None),
		"mayChangeSpace": (10, 2, (2, 0), (), "mayChangeSpace", None),
		"mayChangeWidth": (9, 2, (2, 0), (), "mayChangeWidth", None),
		"name": (1, 2, (8, 0), (), "name", None),
		"step": (2, 2, (5, 0), (), "step", None),
		"width": (6, 2, (5, 0), (), "width", None),
	}
	_prop_map_put_ = {
		"ang" : ((3, LCID, 4, 0),()),
		"color" : ((7, LCID, 4, 0),()),
		"isScalable" : ((11, LCID, 4, 0),()),
		"mayChangeAngle" : ((8, LCID, 4, 0),()),
		"mayChangeSpace" : ((10, LCID, 4, 0),()),
		"mayChangeWidth" : ((9, LCID, 4, 0),()),
		"name" : ((1, LCID, 4, 0),()),
		"step" : ((2, LCID, 4, 0),()),
		"width" : ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksImportedSurfaceDefinition(DispatchBaseClass):
	'��������� ��������������� �����������.'
	CLSID = IID('{78A2C35E-A7DA-414E-B90A-F19998EC7BD1}')
	coclass_clsid = IID('{102FA83C-E0D6-4DB5-937A-FC149526899A}')

	def AddCurve(self, arr=defaultNamedNotOptArg):
		'�������� ������ � �������� �����.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((12, 0),),arr
			)

	def AddPoint(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg):
		'�������� ����� � ����������� ����� ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0)),x
			, y, z)

	def BeginCurve(self):
		'������� ����������� ����� ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	def Clear(self):
		'�������� ����������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	def EndCurve(self):
		'������� ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksInclineDefinition(DispatchBaseClass):
	'��������� �������� �����.'
	CLSID = IID('{DEEFEFF3-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFEFF5-C3E2-11D6-8734-00C0262CDD2C}')

	def FaceArray(self):
		'�������� ��������� ������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'FaceArray', None)
		return ret

	def GetPlane(self):
		'�������� ���������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'������ ���������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0),),plane
			)

	_prop_map_get_ = {
		"angle": (1, 2, (5, 0), (), "angle", None),
		"direction": (2, 2, (11, 0), (), "direction", None),
	}
	_prop_map_put_ = {
		"angle" : ((1, LCID, 4, 0),()),
		"direction" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksInertiaParam(DispatchBaseClass):
	'��������� ���������� ��� ������� ������� ��������-������������ �������������.'
	CLSID = IID('{EA92E649-239E-4105-BBD3-AEF4817BD783}')
	coclass_clsid = IID('{7B8B632E-5BDD-4EE5-B623-DF2880BE0EE4}')

	_prop_map_get_ = {
		"A": (12, 2, (5, 0), (), "A", None),
		"F": (3, 2, (5, 0), (), "F", None),
		"jx": (10, 2, (5, 0), (), "jx", None),
		"jy": (11, 2, (5, 0), (), "jy", None),
		"lx": (5, 2, (5, 0), (), "lx", None),
		"lxy": (6, 2, (5, 0), (), "lxy", None),
		"ly": (4, 2, (5, 0), (), "ly", None),
		"mx": (7, 2, (5, 0), (), "mx", None),
		"mxy": (9, 2, (5, 0), (), "mxy", None),
		"my": (8, 2, (5, 0), (), "my", None),
		"xc": (1, 2, (5, 0), (), "xc", None),
		"yc": (2, 2, (5, 0), (), "yc", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksInsertFragmentParam(DispatchBaseClass):
	'��������� ������� ����������.'
	CLSID = IID('{7F7D6FB1-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FB3-97DA-11D6-8732-00C0262CDD2C}')

	def GetPlace(self):
		'���������� ��������� ��������������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlace', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	def SetPlace(self, val=defaultNamedNotOptArg):
		'�������� ��������� ��������������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"comment": (2, 2, (8, 0), (), "comment", None),
		"fileName": (1, 2, (8, 0), (), "fileName", None),
		"insertType": (3, 2, (2, 0), (), "insertType", None),
		"multiLayer": (4, 2, (11, 0), (), "multiLayer", None),
	}
	_prop_map_put_ = {
		"comment" : ((2, LCID, 4, 0),()),
		"fileName" : ((1, LCID, 4, 0),()),
		"insertType" : ((3, LCID, 4, 0),()),
		"multiLayer" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksInsertFragmentParamEx(DispatchBaseClass):
	'��������� ������� ����������.'
	CLSID = IID('{7F7D6FC3-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FC5-97DA-11D6-8732-00C0262CDD2C}')

	def GetPlace(self):
		'���������� ��������� ��������������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlace', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	def SetPlace(self, val=defaultNamedNotOptArg):
		'�������� ��������� ��������������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"comment": (2, 2, (8, 0), (), "comment", None),
		"fileName": (1, 2, (8, 0), (), "fileName", None),
		"insertType": (3, 2, (2, 0), (), "insertType", None),
		"multiLayer": (4, 2, (11, 0), (), "multiLayer", None),
		"scaleProjLinesSize": (5, 2, (2, 0), (), "scaleProjLinesSize", None),
	}
	_prop_map_put_ = {
		"comment" : ((2, LCID, 4, 0),()),
		"fileName" : ((1, LCID, 4, 0),()),
		"insertType" : ((3, LCID, 4, 0),()),
		"multiLayer" : ((4, LCID, 4, 0),()),
		"scaleProjLinesSize" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksIntersectionResult(DispatchBaseClass):
	'��������� ����������� �����������.'
	CLSID = IID('{ABC7F8EE-CF07-4AA8-98A1-0DE35DB35B9E}')
	coclass_clsid = IID('{ED41E352-E8A8-4B12-893F-17F064985CEE}')

	def GetCount(self):
		'�������� ���������� �����������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetIntersectionType(self, index=defaultNamedNotOptArg):
		'�������� ��� ����������� �� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), ((3, 0),),index
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksIterator(DispatchBaseClass):
	'�������� �� �������� ��������� ����.'
	CLSID = IID('{D06C9101-98CA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{D06C9103-98CA-11D6-8732-00C0262CDD2C}')

	def ksCreateAttrIterator(self, obj=defaultNamedNotOptArg, key1=defaultNamedNotOptArg, key2=defaultNamedNotOptArg, key3=defaultNamedNotOptArg
			, key4=defaultNamedNotOptArg, numb=defaultNamedNotOptArg):
		'������� �������� �� ���������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((3, 0), (3, 0), (3, 0), (3, 0), (3, 0), (5, 0)),obj
			, key1, key2, key3, key4, numb
			)

	def ksCreateIterator(self, tipSeartch=defaultNamedNotOptArg, parent=defaultNamedNotOptArg):
		'������� �������� ��� �������� �� ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((3, 0), (3, 0)),tipSeartch
			, parent)

	def ksCreateQualityIterator(self, system=defaultNamedNotOptArg, withLimitation=defaultNamedNotOptArg):
		'������� �������� �� ����������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((2, 0), (2, 0)),system
			, withLimitation)

	def ksCreateSpcIterator(self, nameLib=defaultNamedNotOptArg, styleNumb=defaultNamedNotOptArg, spcObjType=defaultNamedNotOptArg):
		'������� �������� �� �������� ������������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((8, 0), (3, 0), (3, 0)),nameLib
			, styleNumb, spcObjType)

	def ksDeleteIterator(self):
		'������� ��������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	def ksMoveAttrIterator(self, ch=defaultNamedNotOptArg, pObj=defaultNamedNotOptArg):
		'���������  �� ���������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), ((8, 0), (16387, 0)),ch
			, pObj)

	def ksMoveIterator(self, ksMoveIterator=defaultNamedNotOptArg):
		'��������� �� ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((8, 0),),ksMoveIterator
			)

	def ksMoveQualityIterator(self, param=defaultNamedNotOptArg, inMM=defaultNamedNotOptArg, ch=defaultNamedNotOptArg):
		'��������� �� ����������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((9, 0), (2, 0), (8, 0)),param
			, inMM, ch)

	_prop_map_get_ = {
		"reference": (1, 2, (3, 0), (), "reference", None),
	}
	_prop_map_put_ = {
		"reference" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksKompasObjectNotify:
	'C������ ����������.'
	CLSID = CLSID_Sink = IID('{C7CB743A-C59D-4C27-8CB6-971C2A393F2F}')
	coclass_clsid = IID('{FBE002A6-1E06-4703-AEC5-9AD8A10FA1FA}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCreateDocument",
		        2 : "OnBeginOpenDocument",
		        3 : "OnOpenDocument",
		        4 : "OnChangeActiveDocument",
		        5 : "OnApplicationDestroy",
		        6 : "OnBeginCreate",
		        7 : "OnBeginOpenFile",
		        8 : "OnBeginCloseAllDocument",
		        9 : "OnKeyDown",
		       10 : "OnKeyUp",
		       11 : "OnKeyPress",
		       12 : "OnBeginReguestFiles",
		       13 : "OnBeginChoiceMaterial",
		       14 : "OnChoiceMaterial",
		       15 : "OnIsNeedConvertToSavePrevious",
		       16 : "OnBeginConvertToSavePrevious",
		       17 : "OnEndConvertToSavePrevious",
		       18 : "OnChangeTheme",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnCreateDocument(self, newDoc=defaultNamedNotOptArg, docType=defaultNamedNotOptArg):
#		'�������� ������.'
#	def OnBeginOpenDocument(self, fileName=defaultNamedNotOptArg):
#		'������ �������� ���������.'
#	def OnOpenDocument(self, newDoc=defaultNamedNotOptArg, docType=defaultNamedNotOptArg):
#		'�������� ������.'
#	def OnChangeActiveDocument(self, newDoc=defaultNamedNotOptArg, docType=defaultNamedNotOptArg):
#		'������������ �� ������ �������� ��������.'
#	def OnApplicationDestroy(self):
#		'�������� ����������.'
#	def OnBeginCreate(self, docType=defaultNamedNotOptArg):
#		'������ �������� ���������(�� ������� ������ ����).'
#	def OnBeginOpenFile(self):
#		'������ �������� ���������(�� ������� ������ �����).'
#	def OnBeginCloseAllDocument(self):
#		'������ �������� ���� �������� ����������.'
#	def OnKeyDown(self, key=defaultNamedNotOptArg, flags=defaultNamedNotOptArg, systemKey=defaultNamedNotOptArg):
#		'������� ������� ���������� - ������ �������.'
#	def OnKeyUp(self, key=defaultNamedNotOptArg, flags=defaultNamedNotOptArg, systemKey=defaultNamedNotOptArg):
#		'������� ������� ���������� - ��������� �������.'
#	def OnKeyPress(self, key=defaultNamedNotOptArg, systemKey=defaultNamedNotOptArg):
#		'������� ������� ���������� - ������ �������.'
#	def OnBeginReguestFiles(self, requestID=defaultNamedNotOptArg, files=defaultNamedNotOptArg):
#		'������ ���� ������.'
#	def OnBeginChoiceMaterial(self, MaterialPropertyId=defaultNamedNotOptArg):
#		'������ ������ ���������.'
#	def OnChoiceMaterial(self, MaterialPropertyId=defaultNamedNotOptArg, material=defaultNamedNotOptArg, density=defaultNamedNotOptArg):
#		'�������� ����� ���������.'
#	def OnIsNeedConvertToSavePrevious(self, pDoc=defaultNamedNotOptArg, docType=defaultNamedNotOptArg, saveVersion=defaultNamedNotOptArg, saveToPreviusParam=defaultNamedNotOptArg
#			, needConvert=defaultNamedNotOptArg):
#		'������ ���������� ��������� � ���������� �����.'
#	def OnBeginConvertToSavePrevious(self, pDoc=defaultNamedNotOptArg, docType=defaultNamedNotOptArg, saveVersion=defaultNamedNotOptArg, saveToPreviusParam=defaultNamedNotOptArg):
#		'������ ����������� ��������� ����� ������� � ���������� �����.'
#	def OnEndConvertToSavePrevious(self, pDoc=defaultNamedNotOptArg, docType=defaultNamedNotOptArg, saveVersion=defaultNamedNotOptArg, saveToPreviusParam=defaultNamedNotOptArg):
#		'���������� ����������� ��������� ����� ������� � ���������� �����.'
#	def OnChangeTheme(self, newTheme=defaultNamedNotOptArg):
#		'������� ��������� ����.'


class ksLBreakDimParam(DispatchBaseClass):
	'��������� ��������� ������� � �������.'
	CLSID = IID('{7F7D6FBD-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FBF-97DA-11D6-8732-00C0262CDD2C}')

	def GetDPar(self):
		'���������� ��������� ����������� �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDPar', None)
		return ret

	def GetSPar(self):
		'���������� ��������� �������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSPar', None)
		return ret

	def GetTPar(self):
		'���������� ��������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTPar', None)
		return ret

	def SetDPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ����������� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetSPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� �������� ��������� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetTPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLBreakDimSource(DispatchBaseClass):
	'��������� �������� ��������� ������� � �������.'
	CLSID = IID('{7F7D6FB7-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FB9-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"x1": (1, 2, (5, 0), (), "x1", None),
		"x2": (3, 2, (5, 0), (), "x2", None),
		"x3": (5, 2, (5, 0), (), "x3", None),
		"y1": (2, 2, (5, 0), (), "y1", None),
		"y2": (4, 2, (5, 0), (), "y2", None),
		"y3": (6, 2, (5, 0), (), "y3", None),
	}
	_prop_map_put_ = {
		"x1" : ((1, LCID, 4, 0),()),
		"x2" : ((3, LCID, 4, 0),()),
		"x3" : ((5, LCID, 4, 0),()),
		"y1" : ((2, LCID, 4, 0),()),
		"y2" : ((4, LCID, 4, 0),()),
		"y3" : ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLDimParam(DispatchBaseClass):
	'��������� ��������� �������.'
	CLSID = IID('{7F7D6FD5-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FD7-97DA-11D6-8732-00C0262CDD2C}')

	def GetDPar(self):
		'���������� ��������� ����������� �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDPar', None)
		return ret

	def GetSPar(self):
		'���������� ��������� �������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSPar', None)
		return ret

	def GetTPar(self):
		'���������� ��������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTPar', None)
		return ret

	def SetDPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ����������� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetSPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� �������� ��������� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetTPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLDimSourceParam(DispatchBaseClass):
	'��������� �������� ��������� �������.'
	CLSID = IID('{7F7D6FCF-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FD1-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"basePoint": (8, 2, (2, 0), (), "basePoint", None),
		"dx": (5, 2, (5, 0), (), "dx", None),
		"dy": (6, 2, (5, 0), (), "dy", None),
		"ps": (7, 2, (2, 0), (), "ps", None),
		"x1": (1, 2, (5, 0), (), "x1", None),
		"x2": (3, 2, (5, 0), (), "x2", None),
		"y1": (2, 2, (5, 0), (), "y1", None),
		"y2": (4, 2, (5, 0), (), "y2", None),
	}
	_prop_map_put_ = {
		"basePoint" : ((8, LCID, 4, 0),()),
		"dx" : ((5, LCID, 4, 0),()),
		"dy" : ((6, LCID, 4, 0),()),
		"ps" : ((7, LCID, 4, 0),()),
		"x1" : ((1, LCID, 4, 0),()),
		"x2" : ((3, LCID, 4, 0),()),
		"y1" : ((2, LCID, 4, 0),()),
		"y2" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLayerParam(DispatchBaseClass):
	'��������� ����.'
	CLSID = IID('{E79C2507-9584-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{E79C2509-9584-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"color": (2, 2, (3, 0), (), "color", None),
		"name": (3, 2, (8, 0), (), "name", None),
		"state": (1, 2, (2, 0), (), "state", None),
	}
	_prop_map_put_ = {
		"color" : ((2, LCID, 4, 0),()),
		"name" : ((3, LCID, 4, 0),()),
		"state" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLeaderParam(DispatchBaseClass):
	'��������� ���������� ��� ������� ����� �������.'
	CLSID = IID('{3F715E40-97D9-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3F715E42-97D9-11D6-95CE-00C0262D30E3}')

	def GetpPolyline(self):
		'�������� ��������� �� ��������� ������������� ������� ����������� �����-�������.'
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpPolyline', None)
		return ret

	def GetpTextline(self):
		'������������ ������ ����� ������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpTextline', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), (),)

	def SetpPolyline(self, pPolyline=defaultNamedNotOptArg):
		'���������� ��������� �� ��������� ������������� ������� ����������� �����-�������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((9, 0),),pPolyline
			)

	def SetpTextline(self, pTextLine=defaultNamedNotOptArg):
		'������������ ������ ����� ������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((9, 0),),pTextLine
			)

	_prop_map_get_ = {
		"around": (6, 2, (2, 0), (), "around", None),
		"arrowType": (3, 2, (2, 0), (), "arrowType", None),
		"cText0": (7, 2, (2, 0), (), "cText0", None),
		"cText1": (8, 2, (2, 0), (), "cText1", None),
		"cText2": (9, 2, (2, 0), (), "cText2", None),
		"cText3": (10, 2, (2, 0), (), "cText3", None),
		"dirX": (4, 2, (3, 0), (), "dirX", None),
		"signType": (5, 2, (2, 0), (), "signType", None),
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"around" : ((6, LCID, 4, 0),()),
		"arrowType" : ((3, LCID, 4, 0),()),
		"cText0" : ((7, LCID, 4, 0),()),
		"cText1" : ((8, LCID, 4, 0),()),
		"cText2" : ((9, LCID, 4, 0),()),
		"cText3" : ((10, LCID, 4, 0),()),
		"dirX" : ((4, LCID, 4, 0),()),
		"signType" : ((5, LCID, 4, 0),()),
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLibStyle(DispatchBaseClass):
	'C�������� ���������� ��� ����������� ����� �� ����������.'
	CLSID = IID('{4FD7CEAE-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CEB0-9968-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"fileName": (1, 2, (8, 0), (), "fileName", None),
		"styleNumber": (2, 2, (3, 0), (), "styleNumber", None),
		"typeAllocation": (3, 2, (2, 0), (), "typeAllocation", None),
	}
	_prop_map_put_ = {
		"fileName" : ((1, LCID, 4, 0),()),
		"styleNumber" : ((2, LCID, 4, 0),()),
		"typeAllocation" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLibraryAttrTypeParam(DispatchBaseClass):
	'��������� ��� ���� �������� ���������� ����� ���������.'
	CLSID = IID('{FA93AA21-9B3D-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{FA93AA23-9B3D-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"name": (1, 2, (8, 0), (), "name", None),
		"typeId": (2, 2, (5, 0), (), "typeId", None),
	}
	_prop_map_put_ = {
		"name" : ((1, LCID, 4, 0),()),
		"typeId" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLibraryStyleParam(DispatchBaseClass):
	'��������� ���������� ��� ����� � ���������� ������.'
	CLSID = IID('{FBCC5B9F-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5BA1-996C-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"styleId": (2, 2, (3, 0), (), "styleId", None),
		"styleName": (1, 2, (8, 0), (), "styleName", None),
	}
	_prop_map_put_ = {
		"styleId" : ((2, LCID, 4, 0),()),
		"styleName" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLineParam(DispatchBaseClass):
	'��������� ��������������� �����.'
	CLSID = IID('{E79C250A-9584-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{E79C250C-9584-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"angle": (3, 2, (5, 0), (), "angle", None),
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"angle" : ((3, LCID, 4, 0),()),
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLineSeg3dParam(DispatchBaseClass):
	'��������� ���������� 3d LineSeg.'
	CLSID = IID('{DC8F6A7B-FF16-46FF-986D-2F7E1F6B25C4}')
	coclass_clsid = IID('{4D295A34-4F20-4231-8806-78E40213FA72}')

	def GetPointFirst(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ������ ����� �����.'
		return self._ApplyTypes_(1, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetPointFirst', None,x
			, y, z)

	def GetPointLast(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ��������� ����� �����.'
		return self._ApplyTypes_(2, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetPointLast', None,x
			, y, z)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLineSegParam(DispatchBaseClass):
	'��������� �������.'
	CLSID = IID('{7F7D6F84-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6F86-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"style": (5, 2, (3, 0), (), "style", None),
		"x1": (1, 2, (5, 0), (), "x1", None),
		"x2": (3, 2, (5, 0), (), "x2", None),
		"y1": (2, 2, (5, 0), (), "y1", None),
		"y2": (4, 2, (5, 0), (), "y2", None),
	}
	_prop_map_put_ = {
		"style" : ((5, LCID, 4, 0),()),
		"x1" : ((1, LCID, 4, 0),()),
		"x2" : ((3, LCID, 4, 0),()),
		"y1" : ((2, LCID, 4, 0),()),
		"y2" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLoftSurfaceDefinition(DispatchBaseClass):
	'����������� �� ��������.'
	CLSID = IID('{E04339B5-AA08-4717-8E50-90ED0E375624}')
	coclass_clsid = IID('{5E1EB940-4CAE-43DE-B56D-8733FF6707DF}')

	def GetDirectionalLine(self):
		'�������� ������������ �����. ����� � ������� ����� ������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDirectionalLine', None)
		return ret

	def GetLoftParam(self, closed=pythoncom.Missing, flipVertex=pythoncom.Missing, autoPath=pythoncom.Missing):
		'�������� ��������� ��������.'
		return self._ApplyTypes_(2, 1, (11, 0), ((16395, 2), (16395, 2), (16395, 2)), 'GetLoftParam', None,closed
			, flipVertex, autoPath)

	def SetDirectionalLine(self, sketch=defaultNamedNotOptArg):
		'���������� ������������ �����. ����� � ������� ����� ������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetLoftParam(self, closed=defaultNamedNotOptArg, flipVertex=defaultNamedNotOptArg, autoPath=defaultNamedNotOptArg):
		'���������� ��������� ��������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((11, 0), (11, 0), (11, 0)),closed
			, flipVertex, autoPath)

	def Sketchs(self):
		'������ �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Sketchs', None)
		return ret

	_prop_map_get_ = {
		"closedShell": (1, 2, (2, 0), (), "closedShell", None),
	}
	_prop_map_put_ = {
		"closedShell" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLoop(DispatchBaseClass):
	'��������� �����.'
	CLSID = IID('{22BC5C86-CF58-45E4-AA46-5E8D5A825798}')
	coclass_clsid = IID('{38386E28-C404-431E-9F30-5BE44B0F283F}')

	def EdgeCollection(self):
		'�������� ������ �����.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'EdgeCollection', None)
		return ret

	def GetLength(self, bitVector=defaultNamedNotOptArg):
		'�������� ����� ����� �����.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (5, 0), ((19, 0),),bitVector
			)

	def IsOuter(self):
		'TRUE - ���� �������, FALSE - ���� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def OrientedEdgeCollection(self, edge=defaultNamedNotOptArg):
		'�������� ������ ��������������� �����.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), ((9, 0),),edge
			)
		if ret is not None:
			ret = Dispatch(ret, 'OrientedEdgeCollection', None)
		return ret

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLoopCollection(DispatchBaseClass):
	'��������� ������� ������.'
	CLSID = IID('{1BD7207E-36AA-47DF-913E-AD26DE6C16E8}')
	coclass_clsid = IID('{3EA3B143-96A5-408A-897E-27D852E6EE9B}')

	def First(self):
		'�������� ������ �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetCount(self):
		'�������� ���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'�������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def refresh(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksLtVariant(DispatchBaseClass):
	'��������� ���� ������.'
	CLSID = IID('{E79C2516-9584-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{E79C2518-9584-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"charVal": (8, 2, (2, 0), (), "charVal", None),
		"doubleVal": (7, 2, (5, 0), (), "doubleVal", None),
		"floatVal": (6, 2, (4, 0), (), "floatVal", None),
		"intVal": (4, 2, (3, 0), (), "intVal", None),
		"longVal": (5, 2, (3, 0), (), "longVal", None),
		"shortVal": (3, 2, (2, 0), (), "shortVal", None),
		"strVal": (2, 2, (8, 0), (), "strVal", None),
		"uCharVal": (9, 2, (2, 0), (), "uCharVal", None),
		"uIntVal": (10, 2, (3, 0), (), "uIntVal", None),
		"wstrVal": (12, 2, (8, 0), (), "wstrVal", None),
		"valType": (1, 2, (2, 0), (), "valType", None),
	}
	_prop_map_put_ = {
		"charVal" : ((8, LCID, 4, 0),()),
		"doubleVal" : ((7, LCID, 4, 0),()),
		"floatVal" : ((6, LCID, 4, 0),()),
		"intVal" : ((4, LCID, 4, 0),()),
		"longVal" : ((5, LCID, 4, 0),()),
		"shortVal" : ((3, LCID, 4, 0),()),
		"strVal" : ((2, LCID, 4, 0),()),
		"uCharVal" : ((9, LCID, 4, 0),()),
		"uIntVal" : ((10, LCID, 4, 0),()),
		"wstrVal" : ((12, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMacro3DDefinition(DispatchBaseClass):
	'��������� ������������ 3D.'
	CLSID = IID('{02556461-D088-4F00-AE61-D366082DB9BC}')
	coclass_clsid = IID('{DC7D3EDF-80EE-4BAF-930F-F221AC7E5A7A}')

	def Add(self, obj=defaultNamedNotOptArg):
		'�������� ������ � �����.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def ClearAllObj(self):
		'������� ��� ������� ���������� � ������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

	def Destroy(self):
		'��������� �����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	# Result is of type ksFeatureCollection
	def FeatureCollection(self):
		'�������� ������ �������� �������� � �����������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'FeatureCollection', '{CE6A46FF-02B4-4C7E-AF50-3F3707C8B122}')
		return ret

	def GetCountObj(self):
		'���-�� �������� ���������� � ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), (),)

	def GetObject(self, index=defaultNamedNotOptArg):
		'�������� ������ �� �������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObject', None)
		return ret

	def GetUserParam(self, userPars=defaultNamedNotOptArg):
		'�������� ��������� ������������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((9, 0),),userPars
			)

	def GetUserParamSize(self):
		'������ ��������� ���������� ������������, �������� � ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), (),)

	def SetObject(self, index=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'���������� ������ �� �������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((3, 0), (9, 0)),index
			, obj)

	def SetUserParam(self, userPars=defaultNamedNotOptArg):
		'���������� ��������� ������������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0),),userPars
			)

	_prop_map_get_ = {
		"DoubleClickEditOff": (12, 2, (11, 0), (), "DoubleClickEditOff", None),
		"PropertyObjectEditable": (13, 2, (11, 0), (), "PropertyObjectEditable", None),
		"StaffVisible": (1, 2, (11, 0), (), "StaffVisible", None),
	}
	_prop_map_put_ = {
		"DoubleClickEditOff" : ((12, LCID, 4, 0),()),
		"PropertyObjectEditable" : ((13, LCID, 4, 0),()),
		"StaffVisible" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMarkerLeaderParam(DispatchBaseClass):
	'����� ������� ��� ����������� ������������.'
	CLSID = IID('{9AF8E341-98A0-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{9AF8E343-98A0-11D6-95CE-00C0262D30E3}')

	def GetpPolyline(self):
		'������������ ������ ����������� �����-�������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpPolyline', None)
		return ret

	def GetpTextline(self):
		'������������ ������ ����� ������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpTextline', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), (),)

	def SetpPolyline(self, pPolyline=defaultNamedNotOptArg):
		'������������ ������ ����������� �����-�������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((9, 0),),pPolyline
			)

	def SetpTextline(self, pTextLine=defaultNamedNotOptArg):
		'������������ ������ ����� ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),pTextLine
			)

	_prop_map_get_ = {
		"arrowType": (3, 2, (2, 0), (), "arrowType", None),
		"cText0": (6, 2, (2, 0), (), "cText0", None),
		"cText1": (7, 2, (2, 0), (), "cText1", None),
		"cText2": (8, 2, (2, 0), (), "cText2", None),
		"style1": (4, 2, (3, 0), (), "style1", None),
		"style2": (5, 2, (3, 0), (), "style2", None),
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"arrowType" : ((3, LCID, 4, 0),()),
		"cText0" : ((6, LCID, 4, 0),()),
		"cText1" : ((7, LCID, 4, 0),()),
		"cText2" : ((8, LCID, 4, 0),()),
		"style1" : ((4, LCID, 4, 0),()),
		"style2" : ((5, LCID, 4, 0),()),
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMassInertiaParam(DispatchBaseClass):
	'��������� ���������� ��� ������� �����-������������ �������������.'
	CLSID = IID('{283F77EB-7E2C-4F71-8B16-4D286FA4857E}')
	coclass_clsid = IID('{4693323B-42A7-42CC-902E-7123DD916FB4}')

	def GetAxisX(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'������� ����������� ������� ����������� ���� �������.'
		return self._ApplyTypes_(27, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetAxisX', None,x
			, y, z)

	def GetAxisY(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'������� ����������� ������� ����������� ���� �������.'
		return self._ApplyTypes_(28, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetAxisY', None,x
			, y, z)

	def GetAxisZ(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'������� ����������� ������� ����������� ���� �������.'
		return self._ApplyTypes_(29, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetAxisZ', None,x
			, y, z)

	def SetBitVectorValue(self, val=defaultNamedNotOptArg, setState=defaultNamedNotOptArg):
		'�������� �������� �������� �������.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (11, 0), ((3, 0), (11, 0)),val
			, setState)

	_prop_map_get_ = {
		"F": (23, 2, (5, 0), (), "F", None),
		"jx": (7, 2, (5, 0), (), "jx", None),
		"jx0": (24, 2, (5, 0), (), "jx0", None),
		"jx0y": (15, 2, (5, 0), (), "jx0y", None),
		"jx0z": (13, 2, (5, 0), (), "jx0z", None),
		"jxy": (10, 2, (5, 0), (), "jxy", None),
		"jxz": (11, 2, (5, 0), (), "jxz", None),
		"jy": (8, 2, (5, 0), (), "jy", None),
		"jy0": (25, 2, (5, 0), (), "jy0", None),
		"jy0z": (14, 2, (5, 0), (), "jy0z", None),
		"jyz": (12, 2, (5, 0), (), "jyz", None),
		"jz": (9, 2, (5, 0), (), "jz", None),
		"jz0": (26, 2, (5, 0), (), "jz0", None),
		"lx": (4, 2, (5, 0), (), "lx", None),
		"lxy": (16, 2, (5, 0), (), "lxy", None),
		"lxz": (17, 2, (5, 0), (), "lxz", None),
		"ly": (5, 2, (5, 0), (), "ly", None),
		"lyz": (18, 2, (5, 0), (), "lyz", None),
		"lz": (6, 2, (5, 0), (), "lz", None),
		"m": (20, 2, (5, 0), (), "m", None),
		"r": (19, 2, (5, 0), (), "r", None),
		"v": (21, 2, (5, 0), (), "v", None),
		"xc": (1, 2, (5, 0), (), "xc", None),
		"yc": (2, 2, (5, 0), (), "yc", None),
		"zc": (3, 2, (5, 0), (), "zc", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMateConstraint(DispatchBaseClass):
	'3D ������ - ����������.'
	CLSID = IID('{508A0CC4-9D74-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{508A0CC6-9D74-11D6-95CE-00C0262D30E3}')

	def Create(self):
		'������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	def GetBaseObj(self, number=defaultNamedNotOptArg):
		'��������� �� ��������� ������� ��� ���������� �� ������ 1 ��� 2.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((2, 0),),number
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetBaseObj', None)
		return ret

	def GetEntityParams(self, number=defaultNamedNotOptArg, params=pythoncom.Missing):
		'�������� ��������� ��� �������������� �������� ������������ � ���������� �� ������ 1 ��� 2.'
		return self._ApplyTypes_(9, 1, (3, 0), ((2, 1), (16396, 2)), 'GetEntityParams', None,number
			, params)

	def GetFeature(self):
		'�������� ������ ������, ��������� � ������ ��������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFeature', None)
		return ret

	def SetBaseObj(self, number=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'���������� ��������� �� ��������� ������� ��� ���������� �� ������ 1 ��� 2.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((2, 0), (9, 0)),number
			, obj)

	_prop_map_get_ = {
		"constraintType": (1, 2, (2, 0), (), "constraintType", None),
		"direction": (2, 2, (2, 0), (), "direction", None),
		"distance": (4, 2, (5, 0), (), "distance", None),
		"fixed": (3, 2, (2, 0), (), "fixed", None),
	}
	_prop_map_put_ = {
		"constraintType" : ((1, LCID, 4, 0),()),
		"direction" : ((2, LCID, 4, 0),()),
		"distance" : ((4, LCID, 4, 0),()),
		"fixed" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMateConstraintCollection(DispatchBaseClass):
	'������ ����������.'
	CLSID = IID('{03CEAC84-C0B8-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{03CEAC86-C0B8-11D6-8734-00C0262CDD2C}')

	def AddMateConstraint(self, mate=defaultNamedNotOptArg):
		'�������� ���������� � ������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((9, 0),),mate
			)

	def Clear(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	def FindIt(self, entity=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((9, 0),),entity
			)

	def First(self):
		'�������� ��������� �� ��������� ������� ��������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ��������� �� ��������� �������� �� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetCount(self):
		'���������� ��������� � �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetSafeArrayByObj(self, obj=defaultNamedNotOptArg, pArray=pythoncom.Missing):
		'������������ SAFEARRAY ���������� ���������� �� �������.'
		return self._ApplyTypes_(12, 1, (11, 0), ((9, 1), (16396, 2)), 'GetSafeArrayByObj', None,obj
			, pArray)

	def Last(self):
		'�������� ��������� �� ��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'�������� ��������� �� ��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'�������� ��������� �� ��������� ����������� ��������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def RemoveMateConstraint(self, mate=defaultNamedNotOptArg):
		'������� ���������� �� �������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((9, 0),),mate
			)

	def refresh(self):
		'�������� ������ ����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMathPointParam(DispatchBaseClass):
	'��������� ���������� �������������� �����.'
	CLSID = IID('{3198E121-9585-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3198E123-9585-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMathematic2D(DispatchBaseClass):
	'2D �������������� �������.'
	CLSID = IID('{F2D5AE01-45DE-4496-B01B-9958CAEF5943}')
	coclass_clsid = IID('{C77421D3-13EC-4595-A198-677EFB45AEF3}')

	def ksAngle(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg):
		'������ ���� � ��������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (5, 0), ((5, 0), (5, 0), (5, 0), (5, 0)),x1
			, y1, x2, y2)

	def ksAtanD(self, x=defaultNamedNotOptArg):
		'����������. ���������� �������� ���� � ��������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (5, 0), ((5, 0),),x
			)

	def ksCalcInertiaProperties(self, p=defaultNamedNotOptArg, prop=defaultNamedNotOptArg, dimension=defaultNamedNotOptArg):
		'������� ���������� ��������-������������ ��������������.'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (3, 0), ((3, 0), (9, 0), (2, 0)),p
			, prop, dimension)

	def ksCalcMassInertiaProperties(self, p=defaultNamedNotOptArg, prop=defaultNamedNotOptArg, density=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'������� ���������� �������� �����-������������ ��������������.'
		return self._oleobj_.InvokeTypes(39, LCID, 1, (3, 0), ((3, 0), (9, 0), (5, 0), (5, 0)),p
			, prop, density, param)

	def ksCosD(self, x=defaultNamedNotOptArg):
		'���������� ������� ���������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (5, 0), ((5, 0),),x
			)

	def ksCouplingCircleCircle(self, xc1=defaultNamedNotOptArg, yc1=defaultNamedNotOptArg, radc1=defaultNamedNotOptArg, xc2=defaultNamedNotOptArg
			, yc2=defaultNamedNotOptArg, radc2=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'������� ����������  ����������� ���������� ������������� ������� � ����� ���������� ��� ���� �����������.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),xc1
			, yc1, radc1, xc2, yc2, radc2
			, rad, param)

	def ksCouplingLineCircle(self, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, radc=defaultNamedNotOptArg, x1=defaultNamedNotOptArg
			, y1=defaultNamedNotOptArg, angle1=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'������� ����������  ����������� ���������� ������������� ������� � ����� ����������.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),xc
			, yc, radc, x1, y1, angle1
			, rad, param)

	def ksCouplingLineLine(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, angle1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg
			, y2=defaultNamedNotOptArg, angle2=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����������  ��� ���� ������.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),x1
			, y1, angle1, x2, y2, angle2
			, rad, param)

	def ksDistanceCurveCurve(self, p1=defaultNamedNotOptArg, p2=defaultNamedNotOptArg, distanse=pythoncom.Missing, t1=pythoncom.Missing
			, t2=pythoncom.Missing):
		'���������� ����� ����� �������.'
		return self._ApplyTypes_(53, 1, (3, 0), ((3, 1), (3, 1), (16389, 2), (16389, 2), (16389, 2)), 'ksDistanceCurveCurve', None,p1
			, p2, distanse, t1, t2)

	def ksDistancePntArc(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, xac=defaultNamedNotOptArg, yac=defaultNamedNotOptArg
			, rada=defaultNamedNotOptArg, fa1=defaultNamedNotOptArg, fa2=defaultNamedNotOptArg, directa=defaultNamedNotOptArg):
		'���������� ����� ������ � �����.'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (5, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (2, 0)),x
			, y, xac, yac, rada, fa1
			, fa2, directa)

	def ksDistancePntCircle(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg
			, rad=defaultNamedNotOptArg):
		'���������� ����� ������ � �����������.'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (5, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0)),x
			, y, xc, yc, rad)

	def ksDistancePntLine(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg
			, angle=defaultNamedNotOptArg):
		'���������� ����� ������ � ������, �������� ������ � �����.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (5, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0)),x
			, y, x1, y1, angle)

	def ksDistancePntLineForPoint(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg
			, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg):
		'���������� ����� ������ � ������, �������� �������.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (5, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0)),x
			, y, x1, y1, x2, y2
			)

	def ksDistancePntLineSeg(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg
			, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg):
		'���������� ����� ������ � ��������.'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (5, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0)),x
			, y, x1, y1, x2, y2
			)

	def ksDistancePntPnt(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg):
		'���������� ����� ����� �������.'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (5, 0), ((5, 0), (5, 0), (5, 0), (5, 0)),x1
			, y1, x2, y2)

	def ksDistancePntPntOnCurve(self, curve=defaultNamedNotOptArg, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg
			, y2=defaultNamedNotOptArg):
		'������� ���������� ���������� ����� ����� ������� �� ������.'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (5, 0), ((3, 0), (5, 0), (5, 0), (5, 0), (5, 0)),curve
			, x1, y1, x2, y2)

	def ksDistanceT1T2OnCurve(self, curve=defaultNamedNotOptArg, t1=defaultNamedNotOptArg, t2=defaultNamedNotOptArg):
		'������� ���������� ���������� ����� ����� ������� �� ������.'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (5, 0), ((3, 0), (5, 0), (5, 0)),curve
			, t1, t2)

	def ksEqualPoints(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg):
		'���������� ��������������� ���� �����.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((5, 0), (5, 0), (5, 0), (5, 0)),x1
			, y1, x2, y2)

	def ksGetCurveMinMaxParametr(self, curve=defaultNamedNotOptArg, tMin=pythoncom.Missing, tMax=pythoncom.Missing):
		'������� ���������� ����������� � ������������ �������� ������.'
		return self._ApplyTypes_(45, 1, (3, 0), ((3, 1), (16389, 2), (16389, 2)), 'ksGetCurveMinMaxParametr', None,curve
			, tMin, tMax)

	def ksGetCurvePerimeter(self, curve=defaultNamedNotOptArg, dimension=defaultNamedNotOptArg):
		'������� ���������� �������� ������.'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (5, 0), ((3, 0), (2, 0)),curve
			, dimension)

	def ksGetCurvePerpendicular(self, curve=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg):
		'������� ���������� ���� ������� � ������ � �������� �����.'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (5, 0), ((3, 0), (5, 0), (5, 0)),curve
			, x, y)

	def ksGetCurvePerpendicularByT(self, curve=defaultNamedNotOptArg, t=defaultNamedNotOptArg):
		'������� ���������� ���� ������� � ������ � �������� ����� �� ��������� ������.'
		return self._oleobj_.InvokeTypes(52, LCID, 1, (5, 0), ((3, 1), (5, 1)),curve
			, t)

	def ksGetCurvePoint(self, curve=defaultNamedNotOptArg, t=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing):
		'������� ����������� �������� ������ t � ���������� ����.'
		return self._ApplyTypes_(44, 1, (3, 0), ((3, 1), (5, 1), (16389, 2), (16389, 2)), 'ksGetCurvePoint', None,curve
			, t, x, y)

	def ksGetCurvePointProjection(self, curve=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, kx=pythoncom.Missing
			, ky=pythoncom.Missing):
		'������� ���������� ���������� �������� ����� �� ������.'
		return self._ApplyTypes_(36, 1, (3, 0), ((3, 1), (5, 1), (5, 1), (16389, 2), (16389, 2)), 'ksGetCurvePointProjection', None,curve
			, x, y, kx, ky)

	def ksGetCurvePointProjectionEx(self, curve=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, kx=pythoncom.Missing
			, ky=pythoncom.Missing, t=pythoncom.Missing):
		'������� ���������� ���������� �������� ����� �� ������.'
		return self._ApplyTypes_(43, 1, (3, 0), ((3, 1), (5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'ksGetCurvePointProjectionEx', None,curve
			, x, y, kx, ky, t
			)

	def ksIntersectArcArc(self, xac=defaultNamedNotOptArg, yac=defaultNamedNotOptArg, rada=defaultNamedNotOptArg, fa1=defaultNamedNotOptArg
			, fa2=defaultNamedNotOptArg, directa=defaultNamedNotOptArg, xbc=defaultNamedNotOptArg, ybc=defaultNamedNotOptArg, radb=defaultNamedNotOptArg
			, fb1=defaultNamedNotOptArg, fb2=defaultNamedNotOptArg, directb=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����������� ���� ���.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (2, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (3, 0), (9, 0)),xac
			, yac, rada, fa1, fa2, directa
			, xbc, ybc, radb, fb1, fb2
			, directb, param)

	def ksIntersectArcLin(self, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, f1=defaultNamedNotOptArg
			, f2=defaultNamedNotOptArg, n=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, ang=defaultNamedNotOptArg
			, param=defaultNamedNotOptArg):
		'����������� ���� ���������� � ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (3, 0), (5, 0), (5, 0), (5, 0), (9, 0)),xc
			, yc, rad, f1, f2, n
			, x, y, ang, param)

	def ksIntersectCirArc(self, xcc=defaultNamedNotOptArg, ycc=defaultNamedNotOptArg, radc=defaultNamedNotOptArg, xac=defaultNamedNotOptArg
			, yac=defaultNamedNotOptArg, rada=defaultNamedNotOptArg, fa1=defaultNamedNotOptArg, fa2=defaultNamedNotOptArg, directa=defaultNamedNotOptArg
			, param=defaultNamedNotOptArg):
		'����������� ���������� � ����.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (2, 0), (9, 0)),xcc
			, ycc, radc, xac, yac, rada
			, fa1, fa2, directa, param)

	def ksIntersectCirCir(self, xc1=defaultNamedNotOptArg, yc1=defaultNamedNotOptArg, radius1=defaultNamedNotOptArg, xc2=defaultNamedNotOptArg
			, yc2=defaultNamedNotOptArg, radius2=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����������� ���� �����������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),xc1
			, yc1, radius1, xc2, yc2, radius2
			, param)

	def ksIntersectCirLin(self, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, xl=defaultNamedNotOptArg
			, yl=defaultNamedNotOptArg, angle=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����������� ���������� � ������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),xc
			, yc, rad, xl, yl, angle
			, param)

	def ksIntersectCurvCurv(self, p1=defaultNamedNotOptArg, p2=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����������� ���� ������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((3, 0), (3, 0), (9, 0)),p1
			, p2, param)

	def ksIntersectCurvCurvEx(self, p1=defaultNamedNotOptArg, p2=defaultNamedNotOptArg, param=defaultNamedNotOptArg, touchInclude=defaultNamedNotOptArg):
		'����������� ���� ������.'
		return self._oleobj_.InvokeTypes(48, LCID, 1, (3, 0), ((3, 0), (3, 0), (9, 0), (11, 0)),p1
			, p2, param, touchInclude)

	def ksIntersectLinLin(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, angle1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg
			, y2=defaultNamedNotOptArg, angle2=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����������� ���� ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),x1
			, y1, angle1, x2, y2, angle2
			, param)

	def ksIntersectLinSArc(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg
			, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, f1=defaultNamedNotOptArg, f2=defaultNamedNotOptArg
			, direct=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����������� ������� � ����.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (2, 0), (9, 0)),x1
			, y1, x2, y2, xc, yc
			, rad, f1, f2, direct, param
			)

	def ksIntersectLinSCir(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg
			, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����������� ������� � ����������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),x1
			, y1, x2, y2, xc, yc
			, rad, param)

	def ksIntersectLinSLinS(self, x11=defaultNamedNotOptArg, y11=defaultNamedNotOptArg, x12=defaultNamedNotOptArg, y12=defaultNamedNotOptArg
			, x21=defaultNamedNotOptArg, y21=defaultNamedNotOptArg, x22=defaultNamedNotOptArg, y22=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����������� ���� ��������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),x11
			, y11, x12, y12, x21, y21
			, x22, y22, param)

	def ksIntersectLinSLine(self, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg
			, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, ang=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����������� ������� � ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),x1
			, y1, x2, y2, x, y
			, ang, param)

	def ksLinePointTangentCurve(self, p=defaultNamedNotOptArg, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'������� ������� ������ ����� ����� ��������������� ������ ������.'
		return self._oleobj_.InvokeTypes(50, LCID, 1, (11, 0), ((3, 0), (5, 0), (5, 0), (9, 0)),p
			, xc, yc, param)

	def ksMovePointOnCurve(self, curve=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, len=defaultNamedNotOptArg
			, dir=defaultNamedNotOptArg):
		'������� ���������� ����� �� ���������� len �� ������.'
		return self._ApplyTypes_(37, 1, (3, 0), ((3, 1), (16389, 3), (16389, 3), (5, 1), (3, 1)), 'ksMovePointOnCurve', None,curve
			, x, y, len, dir)

	def ksMovePointOnCurveEx(self, curve=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, t=defaultNamedNotOptArg
			, len=defaultNamedNotOptArg, dir=defaultNamedNotOptArg, ext=defaultNamedNotOptArg):
		'������� ���������� ����� �� ���������� len �� ������.'
		return self._ApplyTypes_(51, 1, (3, 0), ((3, 1), (16389, 3), (16389, 3), (16389, 3), (5, 1), (3, 1), (3, 1)), 'ksMovePointOnCurveEx', None,curve
			, x, y, t, len, dir
			, ext)

	def ksPerpendicular(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg
			, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg, xp=pythoncom.Missing, yp=pythoncom.Missing):
		'���������� ����� ����������� ������� � �������������� � ���� �� �������� �����.'
		return self._ApplyTypes_(33, 1, (11, 0), ((5, 1), (5, 1), (5, 1), (5, 1), (5, 1), (5, 1), (16389, 2), (16389, 2)), 'ksPerpendicular', None,x
			, y, x1, y1, x2, y2
			, xp, yp)

	def ksPointsOnCurve(self, curve=defaultNamedNotOptArg, count=defaultNamedNotOptArg):
		'������� ���������� ������ ���������� ������������� �� ������ �����.'
		ret = self._oleobj_.InvokeTypes(34, LCID, 1, (9, 0), ((3, 0), (3, 0)),curve
			, count)
		if ret is not None:
			ret = Dispatch(ret, 'ksPointsOnCurve', None)
		return ret

	def ksPointsOnCurveByStep(self, curve=defaultNamedNotOptArg, step=defaultNamedNotOptArg):
		'������� ���������� ������ ����� ������������� �� ������ � �������� �����.'
		ret = self._oleobj_.InvokeTypes(41, LCID, 1, (9, 0), ((3, 0), (5, 0)),curve
			, step)
		if ret is not None:
			ret = Dispatch(ret, 'ksPointsOnCurveByStep', None)
		return ret

	def ksRotate(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg
			, ang=defaultNamedNotOptArg, xr=pythoncom.Missing, yr=pythoncom.Missing):
		'��������� ����� ������������ ������.'
		return self._ApplyTypes_(26, 1, (11, 0), ((5, 1), (5, 1), (5, 1), (5, 1), (5, 1), (16389, 2), (16389, 2)), 'ksRotate', None,x
			, y, xc, yc, ang, xr
			, yr)

	def ksSinD(self, x=defaultNamedNotOptArg):
		'���������� ����� ���������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (5, 0), ((5, 0),),x
			)

	def ksSymmetry(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, x1=defaultNamedNotOptArg, y1=defaultNamedNotOptArg
			, x2=defaultNamedNotOptArg, y2=defaultNamedNotOptArg, xc=pythoncom.Missing, yc=pythoncom.Missing):
		'��������� ����� ������������ ���.'
		return self._ApplyTypes_(25, 1, (11, 0), ((5, 1), (5, 1), (5, 1), (5, 1), (5, 1), (5, 1), (16389, 2), (16389, 2)), 'ksSymmetry', None,x
			, y, x1, y1, x2, y2
			, xc, yc)

	def ksTanCircleCircle(self, xc1=defaultNamedNotOptArg, yc1=defaultNamedNotOptArg, radius1=defaultNamedNotOptArg, xc2=defaultNamedNotOptArg
			, yc2=defaultNamedNotOptArg, radius2=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'������� ���������� ����� ������� ������ � ���� �����������.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),xc1
			, yc1, radius1, xc2, yc2, radius2
			, param)

	def ksTanCurvCurv(self, p1=defaultNamedNotOptArg, p2=defaultNamedNotOptArg, pointArr1=defaultNamedNotOptArg, pointArr2=defaultNamedNotOptArg):
		'������� ����������� ��� ���� ������.'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (3, 0), ((3, 0), (3, 0), (9, 0), (9, 0)),p1
			, p2, pointArr1, pointArr2)

	def ksTanD(self, x=defaultNamedNotOptArg):
		'���������� ������� ���������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (5, 0), ((5, 0),),x
			)

	def ksTanLineAngCircle(self, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg, rad=defaultNamedNotOptArg, ang=defaultNamedNotOptArg
			, param=defaultNamedNotOptArg):
		'����� ������� ���������� � ������ ��� �������� �����.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),xc
			, yc, rad, ang, param)

	def ksTanLineAngCurve(self, p=defaultNamedNotOptArg, ang=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����� ������� ���������� � ������ ��� �������� �����.'
		return self._oleobj_.InvokeTypes(49, LCID, 1, (11, 0), ((3, 0), (5, 0), (9, 0)),p
			, ang, param)

	def ksTanLinePointCircle(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, xc=defaultNamedNotOptArg, yc=defaultNamedNotOptArg
			, rad=defaultNamedNotOptArg, param=defaultNamedNotOptArg):
		'����� ������� ���������� � ������ �� ��������� �����.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (9, 0)),x
			, y, xc, yc, rad, param
			)

	def ksTanLinePointCurve(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, pCur=defaultNamedNotOptArg, array=defaultNamedNotOptArg):
		'����� ������� ������ � ������ �� ��������� �����.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), ((5, 0), (5, 0), (3, 0), (9, 0)),x
			, y, pCur, array)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMeasurer(DispatchBaseClass):
	'��������� ��� ��������� ���������� � ���� ����� ����� ����������� (�������, �������, ���������).'
	CLSID = IID('{ABC84FE5-3945-4A0B-820A-719BF4B79224}')
	coclass_clsid = IID('{E07C6920-E361-4A4D-9140-95969C26A9ED}')

	def Calc(self):
		'���������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	def GetMaxPoint1(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ������ ����� ������� ������������� ����������.'
		return self._ApplyTypes_(16, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetMaxPoint1', None,x
			, y, z)

	def GetMaxPoint2(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ������ ����� ������� ������������� ����������.'
		return self._ApplyTypes_(17, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetMaxPoint2', None,x
			, y, z)

	def GetMinPoint1(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ������ ����� ������� ������������ ����������.'
		return self._ApplyTypes_(22, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetMinPoint1', None,x
			, y, z)

	def GetMinPoint2(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ������ ����� ������� ������������ ����������.'
		return self._ApplyTypes_(23, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetMinPoint2', None,x
			, y, z)

	def GetNormalPoint1(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ������ ����� ������� ���������� �� �������.'
		return self._ApplyTypes_(18, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetNormalPoint1', None,x
			, y, z)

	def GetNormalPoint2(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ������ ����� ������� ���������� �� �������.'
		return self._ApplyTypes_(19, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetNormalPoint2', None,x
			, y, z)

	def GetObject1(self):
		'�������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObject1', None)
		return ret

	def GetObject2(self):
		'�������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObject2', None)
		return ret

	def GetPoint1(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ��������� ����� �� ������� ��� �� ����������� �������.'
		return self._ApplyTypes_(12, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetPoint1', None,x
			, y, z)

	def GetPoint2(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ��������� ����� �� ������� ��� �� ����������� �������.'
		return self._ApplyTypes_(13, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetPoint2', None,x
			, y, z)

	def IsAngleValid(self):
		'TRUE - ��� ������ �������� ���� ����� �����.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	def SetObject1(self, obj=defaultNamedNotOptArg):
		'������ ������ ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def SetObject2(self, obj=defaultNamedNotOptArg):
		'������ ������ ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),obj
			)

	_prop_map_get_ = {
		"extendObject1": (6, 2, (11, 0), (), "extendObject1", None),
		"extendObject2": (7, 2, (11, 0), (), "extendObject2", None),
		"unit": (5, 2, (19, 0), (), "unit", None),
		"MaxDistance": (14, 2, (5, 0), (), "MaxDistance", None),
		"MeasureResult": (20, 2, (3, 0), (), "MeasureResult", None),
		"MinDistance": (21, 2, (5, 0), (), "MinDistance", None),
		"NormalDistance": (15, 2, (5, 0), (), "NormalDistance", None),
		"angle": (10, 2, (5, 0), (), "angle", None),
		"distance": (11, 2, (5, 0), (), "distance", None),
	}
	_prop_map_put_ = {
		"extendObject1" : ((6, LCID, 4, 0),()),
		"extendObject2" : ((7, LCID, 4, 0),()),
		"unit" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMeshCopyDefinition(DispatchBaseClass):
	'��������� �������� ����������� �� �����.'
	CLSID = IID('{0307BB8D-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BB8F-C193-11D6-8734-00C0262CDD2C}')

	def DeletedCollection(self):
		'�������� ������ �������� ��������� �����.'
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DeletedCollection', None)
		return ret

	def GetAxis1(self):
		'�������� ��� �������� ����������� 1.'
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAxis1', None)
		return ret

	def GetAxis2(self):
		'�������� ��� �������� ����������� 2.'
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAxis2', None)
		return ret

	def GetCopyParamAlongAxis(self, firstAxis=defaultNamedNotOptArg, angle=pythoncom.Missing, count=pythoncom.Missing, step=pythoncom.Missing
			, factor=pythoncom.Missing):
		'�������� ��������� ����������� ����� ����� ���.'
		return self._ApplyTypes_(11, 1, (11, 0), ((11, 1), (16389, 2), (16387, 2), (16389, 2), (16395, 2)), 'GetCopyParamAlongAxis', None,firstAxis
			, angle, count, step, factor)

	def OperationArray(self):
		'�������� ��������� ������� �������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'OperationArray', None)
		return ret

	def SetAxis1(self, axis=defaultNamedNotOptArg):
		'���������� ��� �������� ����������� 1.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((9, 0),),axis
			)

	def SetAxis2(self, axis=defaultNamedNotOptArg):
		'���������� ��� �������� ����������� 2.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((9, 0),),axis
			)

	def SetCopyParamAlongAxis(self, firstAxis=defaultNamedNotOptArg, angle=defaultNamedNotOptArg, count=defaultNamedNotOptArg, step=defaultNamedNotOptArg
			, factor=defaultNamedNotOptArg):
		'���������� ��������� ����������� ����� ����� ���.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((11, 0), (5, 0), (3, 0), (5, 0), (11, 0)),firstAxis
			, angle, count, step, factor)

	_prop_map_get_ = {
		"angle1": (1, 2, (5, 0), (), "angle1", None),
		"angle2": (5, 2, (5, 0), (), "angle2", None),
		"count1": (2, 2, (3, 0), (), "count1", None),
		"count2": (6, 2, (3, 0), (), "count2", None),
		"factor1": (4, 2, (11, 0), (), "factor1", None),
		"factor2": (8, 2, (11, 0), (), "factor2", None),
		"geomArray": (14, 2, (11, 0), (), "geomArray", None),
		"insideFlag": (9, 2, (11, 0), (), "insideFlag", None),
		"step1": (3, 2, (5, 0), (), "step1", None),
		"step2": (7, 2, (5, 0), (), "step2", None),
	}
	_prop_map_put_ = {
		"angle1" : ((1, LCID, 4, 0),()),
		"angle2" : ((5, LCID, 4, 0),()),
		"count1" : ((2, LCID, 4, 0),()),
		"count2" : ((6, LCID, 4, 0),()),
		"factor1" : ((4, LCID, 4, 0),()),
		"factor2" : ((8, LCID, 4, 0),()),
		"geomArray" : ((14, LCID, 4, 0),()),
		"insideFlag" : ((9, LCID, 4, 0),()),
		"step1" : ((3, LCID, 4, 0),()),
		"step2" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMeshPartArrayDefinition(DispatchBaseClass):
	'��������� �������� ������ ����������� �� �����.'
	CLSID = IID('{E6E78D61-C0FA-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{E6E78D63-C0FA-11D6-8734-00C0262CDD2C}')

	def DeletedCollection(self):
		'�������� ������ �������� ��������� �����.'
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DeletedCollection', None)
		return ret

	def GetAxis1(self):
		'�������� ������ ��� �������� �����������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAxis1', None)
		return ret

	def GetAxis2(self):
		'�������� ������ ��� �������� �����������.'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAxis2', None)
		return ret

	def GetCopyParamAlongAxis(self, firstAxis=defaultNamedNotOptArg, angle=pythoncom.Missing, count=pythoncom.Missing, step=pythoncom.Missing
			, factor=pythoncom.Missing):
		'�������� ��������� ����������� ����� ����� ���.'
		return self._ApplyTypes_(15, 1, (11, 0), ((11, 1), (16389, 2), (16387, 2), (16389, 2), (16395, 2)), 'GetCopyParamAlongAxis', None,firstAxis
			, angle, count, step, factor)

	def PartArray(self):
		'�������� ��������� ������� �������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PartArray', None)
		return ret

	def SetAxis1(self, axis=defaultNamedNotOptArg):
		'������ ������ ��� �������� �����������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 0),),axis
			)

	def SetAxis2(self, axis=defaultNamedNotOptArg):
		'������ ������ ��� �������� �����������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((9, 0),),axis
			)

	def SetCopyParamAlongAxis(self, firstAxis=defaultNamedNotOptArg, angle=defaultNamedNotOptArg, count=defaultNamedNotOptArg, step=defaultNamedNotOptArg
			, factor=defaultNamedNotOptArg):
		'���������� ��������� ����������� ����� ����� ���.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((11, 0), (5, 0), (3, 0), (5, 0), (11, 0)),firstAxis
			, angle, count, step, factor)

	_prop_map_get_ = {
		"angle1": (1, 2, (5, 0), (), "angle1", None),
		"angle2": (5, 2, (5, 0), (), "angle2", None),
		"count1": (2, 2, (3, 0), (), "count1", None),
		"count2": (6, 2, (3, 0), (), "count2", None),
		"factor1": (4, 2, (11, 0), (), "factor1", None),
		"factor2": (8, 2, (11, 0), (), "factor2", None),
		"insideFlag": (9, 2, (11, 0), (), "insideFlag", None),
		"step1": (3, 2, (5, 0), (), "step1", None),
		"step2": (7, 2, (5, 0), (), "step2", None),
	}
	_prop_map_put_ = {
		"angle1" : ((1, LCID, 4, 0),()),
		"angle2" : ((5, LCID, 4, 0),()),
		"count1" : ((2, LCID, 4, 0),()),
		"count2" : ((6, LCID, 4, 0),()),
		"factor1" : ((4, LCID, 4, 0),()),
		"factor2" : ((8, LCID, 4, 0),()),
		"insideFlag" : ((9, LCID, 4, 0),()),
		"step1" : ((3, LCID, 4, 0),()),
		"step2" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMirrorCopyAllDefinition(DispatchBaseClass):
	'��������� �������� ��������� ���������� ���.'
	CLSID = IID('{0307BB99-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BB9B-C193-11D6-8734-00C0262CDD2C}')

	def ChooseBodies(self):
		'�������� ��������� �� ��������� ��� ������ � �������� ���������� ��� ���.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChooseBodies', None)
		return ret

	def GetPlane(self):
		'�������� ���������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'������ ���������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),plane
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMirrorCopyDefinition(DispatchBaseClass):
	'��������� �������� ���������� �����.'
	CLSID = IID('{0307BB96-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BB98-C193-11D6-8734-00C0262CDD2C}')

	def GetOperationArray(self):
		'�������� ��������� ������� �������� ��� �����������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetOperationArray', None)
		return ret

	def GetPlane(self):
		'�������� ���������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'������ ���������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),plane
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksModelLibrary(DispatchBaseClass):
	'��������� ���������� �������.'
	CLSID = IID('{111CEFE4-A0A7-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{111CEFE6-A0A7-11D6-95CE-00C0262D30E3}')

	def AddD3DocumentToLibrary(self, libName=defaultNamedNotOptArg, fileName=defaultNamedNotOptArg):
		'�������� ������ � ������ �����  fileName � ���������� ������� � ������ libName.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), ((8, 0), (8, 0)),libName
			, fileName)

	def CheckModelLibrary(self, libName=defaultNamedNotOptArg, possibleMessage=defaultNamedNotOptArg):
		'��������� ������� �� ���������� ������� � ������ ������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), ((8, 0), (11, 0)),libName
			, possibleMessage)

	def ChoiceModelFromLib(self, libFile=defaultNamedNotOptArg, type=pythoncom.Missing):
		'����� ������ �� ���������� �������.'
		return self._ApplyTypes_(2, 1, (8, 0), ((8, 1), (16387, 2)), 'ChoiceModelFromLib', None,libFile
			, type)

	def ExistModelInLibrary(self, name=defaultNamedNotOptArg):
		'��������� ���������� �� ������ � ������ name � ���������� �������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((8, 0),),name
			)

	def ModelLibraryOperation(self, libName=defaultNamedNotOptArg, type=defaultNamedNotOptArg):
		'�������� ��� ����������� �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), ((8, 0), (3, 0)),libName
			, type)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksMoldCavityDefinition(DispatchBaseClass):
	'��������� �������� ������� ����������.'
	CLSID = IID('{BE5F10F5-B198-49D9-9140-B2B91E060533}')
	coclass_clsid = IID('{FC4D7C29-C608-44D5-B927-1EC9FC147B18}')

	def GetScaleCentre(self):
		'�������� ������� ������������ ������� ����������� ���������������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetScaleCentre', None)
		return ret

	def PartArray(self):
		'�������� ��������� ������� ���������� �����������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PartArray', None)
		return ret

	def SetScaleCentre(self, vert=defaultNamedNotOptArg):
		'���������� ������� ������������ ������� ����������� ���������������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),vert
			)

	_prop_map_get_ = {
		"scale": (1, 2, (5, 0), (), "scale", None),
	}
	_prop_map_put_ = {
		"scale" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksNumberTypeAttrParam(DispatchBaseClass):
	'����������� ��� ���� �������� DOUBLE_ATTR_TYPE � LINT_ATTR_TYPE.'
	CLSID = IID('{4FD7CE90-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CE92-9968-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"maxValue": (2, 2, (5, 0), (), "maxValue", None),
		"minValue": (1, 2, (5, 0), (), "minValue", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksNurbs3dParam(DispatchBaseClass):
	'��������� ���������� Nurbs-������� 3D.'
	CLSID = IID('{4DDDAEDB-2819-42D9-BDBB-4CCBC98D76DF}')
	coclass_clsid = IID('{F829344F-B49F-43A3-AC93-E817EF8D3319}')

	def GetKnotCollection(self):
		'������ ����� ��� Nurbs 3D.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetKnotCollection', None)
		return ret

	def GetMinMaxParameters(self, closed=defaultNamedNotOptArg, tMin=pythoncom.Missing, tMax=pythoncom.Missing):
		'�������� ��������� ������.'
		return self._ApplyTypes_(7, 1, (11, 0), ((11, 1), (16389, 2), (16389, 2)), 'GetMinMaxParameters', None,closed
			, tMin, tMax)

	def GetNurbsPoints3DParams(self, closed=defaultNamedNotOptArg, points=pythoncom.Missing, weights=pythoncom.Missing, knots=pythoncom.Missing):
		'�������� �������� ����� ��� Nurbs 3D.'
		return self._ApplyTypes_(6, 1, (11, 0), ((11, 1), (16396, 2), (16396, 2), (16396, 2)), 'GetNurbsPoints3DParams', None,closed
			, points, weights, knots)

	def GetPointCollection(self):
		'������ ����� ��� Nurbs 3D.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPointCollection', None)
		return ret

	_prop_map_get_ = {
		"close": (2, 2, (11, 0), (), "close", None),
		"degree": (1, 2, (2, 0), (), "degree", None),
		"periodic": (5, 2, (11, 0), (), "periodic", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksNurbsKnotCollection(DispatchBaseClass):
	'��������� ������� ����� ��� Nurbs 3D.'
	CLSID = IID('{483E9889-E1CA-4CA5-BE4E-ECB3D5CF0126}')
	coclass_clsid = IID('{81317653-9BBA-46FE-9877-AEEE62BD8AA4}')

	def Add(self, entity=defaultNamedNotOptArg):
		'�������� ������� � ����� �������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((5, 0),),entity
			)

	def AddAt(self, entity=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� ������� ����� �������� � ��������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((5, 0), (3, 0)),entity
			, index)

	def AddBefore(self, entity=defaultNamedNotOptArg, base=defaultNamedNotOptArg):
		'�������� ������� ����� ���������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((5, 0), (5, 0)),entity
			, base)

	def Clear(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	def DetachByBody(self, entity=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((5, 0),),entity
			)

	def DetachByIndex(self, index=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((3, 0),),index
			)

	def First(self):
		'������ �������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (5, 0), (),)

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������� �� �������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (5, 0), ((3, 0),),index
			)

	def GetCount(self):
		'�������� ���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'��������� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (5, 0), (),)

	def Next(self):
		'��������� �������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (5, 0), (),)

	def Prev(self):
		'���������� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (5, 0), (),)

	def SetByIndex(self, entity=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((5, 0), (3, 0)),entity
			, index)

	def refresh(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksNurbsParam(DispatchBaseClass):
	'��������� Nurbs-�������.'
	CLSID = IID('{7F7D6F9F-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FA1-97DA-11D6-8732-00C0262CDD2C}')

	def GetPKnot(self):
		'������ ������������ ������ ����� �������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPKnot', None)
		return ret

	def GetPPoint(self):
		'������ ������������ ������ ����� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPPoint', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	def SetPKnot(self, val=defaultNamedNotOptArg):
		'�������� ������������ ������ ����� �������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetPPoint(self, val=defaultNamedNotOptArg):
		'�������� ������������ ������  ����� �������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"close": (2, 2, (11, 0), (), "close", None),
		"degree": (1, 2, (2, 0), (), "degree", None),
		"style": (3, 2, (3, 0), (), "style", None),
		"periodic": (4, 2, (11, 0), (), "periodic", None),
	}
	_prop_map_put_ = {
		"close" : ((2, LCID, 4, 0),()),
		"degree" : ((1, LCID, 4, 0),()),
		"style" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksNurbsPoint3dCollCollection(DispatchBaseClass):
	'��������� ������� �������� ����� ��� Nurbs 3D Surface.'
	CLSID = IID('{84AF9C81-1795-4631-B58A-101732262E75}')
	coclass_clsid = IID('{A2BD36E2-C99B-40FE-A6A7-E5A9CCDCF63D}')

	def Add(self, entity=defaultNamedNotOptArg):
		'�������� ������� � ����� �������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),entity
			)

	def AddAt(self, entity=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� ������� ����� �������� � ��������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0), (3, 0)),entity
			, index)

	def AddBefore(self, entity=defaultNamedNotOptArg, base=defaultNamedNotOptArg):
		'�������� ������� ����� ���������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 0), (9, 0)),entity
			, base)

	def Clear(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	def DetachByBody(self, entity=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((9, 0),),entity
			)

	def DetachByIndex(self, index=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((3, 0),),index
			)

	def FindIt(self, entity=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((9, 0),),entity
			)

	def First(self):
		'������ �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetCount(self):
		'�������� ���������� ����� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'���������� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def SetByIndex(self, entity=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((9, 0), (3, 0)),entity
			, index)

	def refresh(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksNurbsPoint3dCollection(DispatchBaseClass):
	'��������� ������� ����� ��� Nurbs 3D.'
	CLSID = IID('{3AD5E519-74E2-4D3B-B6A3-B1E81F1006F1}')
	coclass_clsid = IID('{25AE92BA-055F-431E-AC3E-EA2E793D446C}')

	def Add(self, entity=defaultNamedNotOptArg):
		'�������� ������� � ����� �������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),entity
			)

	def AddAt(self, entity=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� ������� ����� �������� � ��������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0), (3, 0)),entity
			, index)

	def AddBefore(self, entity=defaultNamedNotOptArg, base=defaultNamedNotOptArg):
		'�������� ������� ����� ���������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 0), (9, 0)),entity
			, base)

	def Clear(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	def DetachByBody(self, entity=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((9, 0),),entity
			)

	def DetachByIndex(self, index=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((3, 0),),index
			)

	def FindIt(self, entity=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((9, 0),),entity
			)

	def First(self):
		'������ �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetCount(self):
		'�������� ���������� ����� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'���������� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def SetByIndex(self, entity=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((9, 0), (3, 0)),entity
			, index)

	def refresh(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksNurbsPoint3dParam(DispatchBaseClass):
	'��������� ���������� ����� ��� Nurbs 3D.'
	CLSID = IID('{F1CD604D-1D26-4F6B-8F94-F112133E6162}')
	coclass_clsid = IID('{4F3C6D95-FBDC-4C53-AE82-9AF9C05093FF}')

	def GetPoint(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ���������� ������� �����.'
		return self._ApplyTypes_(1, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetPoint', None,x
			, y, z)

	_prop_map_get_ = {
		"weight": (2, 2, (5, 0), (), "weight", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksNurbsPointParam(DispatchBaseClass):
	'��������� ���� ��� Nurbs - ������.'
	CLSID = IID('{7F7D6F99-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6F9B-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"weight": (3, 2, (5, 0), (), "weight", None),
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"weight" : ((3, LCID, 4, 0),()),
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksNurbsSurfaceParam(DispatchBaseClass):
	'��������� ���������� Nurbs-�����������.'
	CLSID = IID('{A12B63E8-9E0A-4854-B724-E18275B9FF20}')
	coclass_clsid = IID('{BA13BE42-059B-4EEB-9C39-673732763EE3}')

	def GetBoundaryCount(self):
		'�������� ���������� ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), (),)

	def GetBoundaryUVNurbs(self, uv=defaultNamedNotOptArg, closed=defaultNamedNotOptArg, loopIndex=defaultNamedNotOptArg, edgeIndex=defaultNamedNotOptArg
			, degree=pythoncom.Missing, points=pythoncom.Missing, weights=pythoncom.Missing, knots=pythoncom.Missing, tMin=pythoncom.Missing
			, tMax=pythoncom.Missing):
		'�������� ��������� ������� ����������� � UV NURBS-�������������.'
		return self._ApplyTypes_(7, 1, (11, 0), ((11, 1), (11, 1), (3, 1), (3, 1), (16387, 2), (16396, 2), (16396, 2), (16396, 2), (16389, 2), (16389, 2)), 'GetBoundaryUVNurbs', None,uv
			, closed, loopIndex, edgeIndex, degree, points
			, weights, knots, tMin, tMax)

	def GetClose(self, paramU=defaultNamedNotOptArg):
		'��� ��������� ������� 0-����������� 1-���������'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((11, 0),),paramU
			)

	def GetDegree(self, paramU=defaultNamedNotOptArg):
		'������� ������� > 2 && < 9.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (2, 0), ((11, 0),),paramU
			)

	def GetEdgesCount(self, loopIndex=defaultNamedNotOptArg):
		'�������� ���������� ����� � �������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((3, 0),),loopIndex
			)

	def GetKnotCollection(self, paramU=defaultNamedNotOptArg):
		'������ ����� ��� Nurbs-�����������'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((11, 0),),paramU
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetKnotCollection', None)
		return ret

	def GetMinMaxParameters(self, closedV=defaultNamedNotOptArg, closedU=defaultNamedNotOptArg, uMin=pythoncom.Missing, uMax=pythoncom.Missing
			, vMin=pythoncom.Missing, vMax=pythoncom.Missing):
		'�������� ��������� �����������.'
		return self._ApplyTypes_(10, 1, (11, 0), ((11, 1), (11, 1), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetMinMaxParameters', None,closedV
			, closedU, uMin, uMax, vMin, vMax
			)

	def GetNurbsParams(self, closedV=defaultNamedNotOptArg, closedU=defaultNamedNotOptArg, degreeV=pythoncom.Missing, degreeU=pythoncom.Missing
			, nPV=pythoncom.Missing, nPU=pythoncom.Missing, points=pythoncom.Missing, weights=pythoncom.Missing, knotsV=pythoncom.Missing
			, knotsU=pythoncom.Missing):
		'�������� ��������� Nurbs-�����������.'
		return self._ApplyTypes_(6, 1, (11, 0), ((11, 1), (11, 1), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16396, 2), (16396, 2), (16396, 2), (16396, 2)), 'GetNurbsParams', None,closedV
			, closedU, degreeV, degreeU, nPV, nPU
			, points, weights, knotsV, knotsU)

	def GetPeriodic(self, paramU=defaultNamedNotOptArg):
		'1-������ ������������� 0-�� �������������-������ GetObjParam'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((11, 0),),paramU
			)

	def GetPointCollection(self):
		'������ �������� ����� ��� Nurbs-�����������'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPointCollection', None)
		return ret

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksObject2DNotify:
	'������� ������� 2D ���������.'
	CLSID = CLSID_Sink = IID('{2E29C343-C521-4B0F-B37D-587D0347B7BA}')
	coclass_clsid = IID('{C7EBA9A1-9E76-436E-B362-A80C5763944C}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChangeActive",
		        2 : "OnBeginDelete",
		        3 : "OnDelete",
		        4 : "OnBeginMove",
		        5 : "OnMove",
		        6 : "OnBeginRotate",
		        7 : "OnRotate",
		        8 : "OnBeginScale",
		        9 : "Onscale",
		       10 : "OnBeginTransform",
		       11 : "OnTransform",
		       12 : "OnBeginCopy",
		       13 : "Oncopy",
		       14 : "OnBeginSymmetry",
		       15 : "OnSymmetry",
		       16 : "OnBeginProcess",
		       17 : "OnEndProcess",
		       18 : "OnCreateObject",
		       19 : "OnUpdateObject",
		       20 : "OnBeginDestroyObject",
		       21 : "OnDestroyObject",
		       22 : "OnBeginPropertyChanged",
		       23 : "OnPropertyChanged",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnChangeActive(self, objRef=defaultNamedNotOptArg):
#		'������������ ���������� �������( ���, ����).'
#	def OnBeginDelete(self, objRef=defaultNamedNotOptArg):
#		'������ �������� �������, false - ��������� ��������.'
#	def OnDelete(self, objRef=defaultNamedNotOptArg):
#		'�������� �������.'
#	def OnBeginMove(self, objRef=defaultNamedNotOptArg):
#		'������ ������ �������, false - ��������� �����.'
#	def OnMove(self, objRef=defaultNamedNotOptArg):
#		'����� �������.'
#	def OnBeginRotate(self, objRef=defaultNamedNotOptArg):
#		'������ �������� �������, false - ��������� �������.'
#	def OnRotate(self, objRef=defaultNamedNotOptArg):
#		'������� �������.'
#	def OnBeginScale(self, objRef=defaultNamedNotOptArg):
#		'������ ��������������� �������, false - ��������� �������.'
#	def Onscale(self, objRef=defaultNamedNotOptArg):
#		'��������������� �������.'
#	def OnBeginTransform(self, objRef=defaultNamedNotOptArg):
#		'������ ������������� �������, false - ��������� �������������.'
#	def OnTransform(self, objRef=defaultNamedNotOptArg):
#		'������������� �������.'
#	def OnBeginCopy(self, objRef=defaultNamedNotOptArg):
#		'������ ����������� �������, false - ��������� �����������.'
#	def Oncopy(self, objRef=defaultNamedNotOptArg):
#		'����������� �������.'
#	def OnBeginSymmetry(self, objRef=defaultNamedNotOptArg):
#		'������ ���������  �������, false - ��������� ���������.'
#	def OnSymmetry(self, objRef=defaultNamedNotOptArg):
#		'���������  �������.'
#	def OnBeginProcess(self, pType=defaultNamedNotOptArg, objRef=defaultNamedNotOptArg):
#		'������ ���������������������� �������.false - ��������� �������'
#	def OnEndProcess(self, pType=defaultNamedNotOptArg):
#		'����� ���������������������� �������.'
#	def OnCreateObject(self, objRef=defaultNamedNotOptArg):
#		'�������� �������.'
#	def OnUpdateObject(self, objRef=defaultNamedNotOptArg):
#		'�������������� �������.'
#	def OnBeginDestroyObject(self, objRef=defaultNamedNotOptArg):
#		'������ ���������� �������, false - ��������� ����������.'
#	def OnDestroyObject(self, objRef=defaultNamedNotOptArg):
#		'���������� �������.'
#	def OnBeginPropertyChanged(self, objRef=defaultNamedNotOptArg):
#		'������ ��������� ������� �������.'
#	def OnPropertyChanged(self, objRef=defaultNamedNotOptArg):
#		'��������� ������� �������.'


class ksObject2DNotifyResult(DispatchBaseClass):
	'��������� ����������� �������������� �������.'
	CLSID = IID('{1FE1EB28-CD28-4700-8E46-25CCFE9C0EC8}')
	coclass_clsid = IID('{DE8219EC-0A9F-44E1-AC2B-F17269484FFF}')

	def GetAngle(self):
		'�������� ���� �������� �������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (5, 0), (),)

	def GetCopyObject(self):
		'�������� ����� �������, ���� ����������� ��������������� ������������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	def GetNotifyType(self):
		'��� �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetProcessType(self):
		'��� ��������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), (),)

	def GetScale(self, sx=pythoncom.Missing, sy=pythoncom.Missing):
		'�������� ������� �� ��� X � Y.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16389, 2), (16389, 2)), 'GetScale', None,sx
			, sy)

	def GetSheetPoint(self, From=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing):
		'�������� �������� ���������� �����.'
		return self._ApplyTypes_(3, 1, (11, 0), ((11, 1), (16389, 2), (16389, 2)), 'GetSheetPoint', None,From
			, x, y)

	def IsCopy(self):
		'������� ����������� �������� ��������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	def IsRedoMode(self):
		'������� ������ ������� Redo.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	def IsUndoMode(self):
		'������� ������ ������� Undo.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksObject3DNotify:
	'������� ��� ������� 3D ���������.'
	CLSID = CLSID_Sink = IID('{BFA024B6-679E-4A95-B6C2-1EA47A7CD0E9}')
	coclass_clsid = IID('{CA35F3C6-7E2D-4700-BE12-BAA26DC1945B}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnBeginDelete",
		        2 : "OnDelete",
		        3 : "Onexcluded",
		        4 : "Onhidden",
		        5 : "OnBeginPropertyChanged",
		        6 : "OnPropertyChanged",
		        7 : "OnBeginPlacementChanged",
		        8 : "OnPlacementChanged",
		        9 : "OnBeginProcess",
		       10 : "OnEndProcess",
		       11 : "OnCreateObject",
		       12 : "OnUpdateObject",
		       13 : "OnBeginLoadStateChange",
		       14 : "OnLoadStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnBeginDelete(self, obj=defaultNamedNotOptArg):
#		'������ �������� ��������.'
#	def OnDelete(self, obj=defaultNamedNotOptArg):
#		'O������ �������.'
#	def Onexcluded(self, obj=defaultNamedNotOptArg, excluded=defaultNamedNotOptArg):
#		'O����� ��������/������� � ������.'
#	def Onhidden(self, obj=defaultNamedNotOptArg, _hidden=defaultNamedNotOptArg):
#		'O����� �����/�������.'
#	def OnBeginPropertyChanged(self, obj=defaultNamedNotOptArg):
#		'������ ��������� ������� ������.'
#	def OnPropertyChanged(self, obj=defaultNamedNotOptArg):
#		'�������� �������� ������.'
#	def OnBeginPlacementChanged(self, obj=defaultNamedNotOptArg):
#		'������ ��������� ��������� ������ .'
#	def OnPlacementChanged(self, obj=defaultNamedNotOptArg):
#		'�������� ��������� ������.'
#	def OnBeginProcess(self, pType=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
#		'������ ���������������������� �������.false - ��������� �������'
#	def OnEndProcess(self, pType=defaultNamedNotOptArg):
#		'����� ���������������������� �������.'
#	def OnCreateObject(self, obj=defaultNamedNotOptArg):
#		'�������� �������.'
#	def OnUpdateObject(self, obj=defaultNamedNotOptArg):
#		'�������������� �������.'
#	def OnBeginLoadStateChange(self, obj=defaultNamedNotOptArg, loadState=defaultNamedNotOptArg):
#		'������ ��������� ���� ��������.'
#	def OnLoadStateChange(self, obj=defaultNamedNotOptArg, loadState=defaultNamedNotOptArg):
#		'���������� ��������� ���� ��������.'


class ksObject3DNotifyResult(DispatchBaseClass):
	'��������� ����������� �������������� ������� 3D ���������.'
	CLSID = IID('{9C3ECC92-E72F-4892-8921-7886F34CA9AD}')
	coclass_clsid = IID('{600F12DF-D8B8-4CA8-A476-D2A7E425C740}')

	# Result is of type ksFeatureCollection
	def GetFeatureCollection(self):
		'�������� ������ ��������� ��������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFeatureCollection', '{CE6A46FF-02B4-4C7E-AF50-3F3707C8B122}')
		return ret

	def GetNotifyType(self):
		'��� �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	# Result is of type ksPlacement
	def GetPlacement(self):
		'�������� �������� ��������� ������� ���������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', '{2DFACC64-C4A4-11D6-8734-00C0262CDD2C}')
		return ret

	def GetProcessType(self):
		'��� ��������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	def IsRedoMode(self):
		'������� ������ ������� Redo.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	def IsUndoMode(self):
		'������� ������ ������� Undo.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksObjectsFilter3D(DispatchBaseClass):
	'��������� ���������� �������� 3D.'
	CLSID = IID('{ABBA6CE0-CB4C-4A32-98B4-B639352C75BA}')
	coclass_clsid = IID('{ABBA6CE1-CB4C-4A32-98B4-B639352C75BA}')

	_prop_map_get_ = {
		"filterAll": (1, 2, (11, 0), (), "filterAll", None),
		"filterCAxis": (6, 2, (11, 0), (), "filterCAxis", None),
		"filterCPlanes": (5, 2, (11, 0), (), "filterCPlanes", None),
		"filterEdges": (3, 2, (11, 0), (), "filterEdges", None),
		"filterFaces": (2, 2, (11, 0), (), "filterFaces", None),
		"filterVertexs": (4, 2, (11, 0), (), "filterVertexs", None),
	}
	_prop_map_put_ = {
		"filterAll" : ((1, LCID, 4, 0),()),
		"filterCAxis" : ((6, LCID, 4, 0),()),
		"filterCPlanes" : ((5, LCID, 4, 0),()),
		"filterEdges" : ((3, LCID, 4, 0),()),
		"filterFaces" : ((2, LCID, 4, 0),()),
		"filterVertexs" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksOrdinatedDimParam(DispatchBaseClass):
	'��������� ������� ������.'
	CLSID = IID('{FBCC5B87-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5B89-996C-11D6-8732-00C0262CDD2C}')

	def GetDPar(self):
		'���������� ��������� ����������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDPar', None)
		return ret

	def GetSPar(self):
		'���������� ��������� �������� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSPar', None)
		return ret

	def GetTPar(self):
		'���������� ��������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTPar', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	def SetDPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ����������� �������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetSPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� �������� �������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetTPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ��������� �������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksOrdinatedDrawingParam(DispatchBaseClass):
	'��������� ����������� ������� ������.'
	CLSID = IID('{FBCC5B8A-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5B8C-996C-11D6-8732-00C0262CDD2C}')

	_prop_map_get_ = {
		"type": (1, 2, (3, 0), (), "type", None),
	}
	_prop_map_put_ = {
		"type" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksOrdinatedSourceParam(DispatchBaseClass):
	'��������� �������� ������� ������.'
	CLSID = IID('{FBCC5B84-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5B86-996C-11D6-8732-00C0262CDD2C}')

	_prop_map_get_ = {
		"x0": (1, 2, (5, 0), (), "x0", None),
		"x1": (2, 2, (5, 0), (), "x1", None),
		"x2": (5, 2, (5, 0), (), "x2", None),
		"y0": (4, 2, (5, 0), (), "y0", None),
		"y1": (3, 2, (5, 0), (), "y1", None),
		"y2": (6, 2, (5, 0), (), "y2", None),
	}
	_prop_map_put_ = {
		"x0" : ((1, LCID, 4, 0),()),
		"x1" : ((2, LCID, 4, 0),()),
		"x2" : ((5, LCID, 4, 0),()),
		"y0" : ((4, LCID, 4, 0),()),
		"y1" : ((3, LCID, 4, 0),()),
		"y2" : ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksOrientedEdge(DispatchBaseClass):
	'��������� ���������������� �����.'
	CLSID = IID('{88C32A80-3735-4E18-A02E-9B2A8F0A90E3}')
	coclass_clsid = IID('{C66FB80F-97BE-4437-A8A0-AEDCFCBCF982}')

	def GetAdjacentFace(self, facePlus=defaultNamedNotOptArg):
		'�������� �����, � ������� ����� ������ � loop (TRUE - ����������� ����).'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((3, 0),),facePlus
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetAdjacentFace', None)
		return ret

	def GetEdge(self):
		'�������� ��������� �������� �����.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEdge', None)
		return ret

	def GetNext(self):
		'�������� ��������� ��������������� �����.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNext', None)
		return ret

	def GetOrientation(self):
		'�������� ����������� ������������ �������� �����.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	def GetOwnerEntity(self):
		'�������� ��������� 3D �������, ������������ �� �����.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetOwnerEntity', None)
		return ret

	def GetSameSense(self):
		'�������� ����������� ������������ ������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	def IsPole(self):
		'�������� �� ����� ��������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	def IsSeam(self):
		'�������� �� ����� ����'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), (),)

	def IsStraight(self):
		'�������� �� ����� ������'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksOrientedEdgeCollection(DispatchBaseClass):
	'��������� ������� ��������������� �����.'
	CLSID = IID('{5CE8909D-CF3D-418F-A9B9-0A12B23916C0}')
	coclass_clsid = IID('{6EF08DCB-A1D4-43A2-ACAF-AF32FDE5F338}')

	def FindIt(self, entity=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((9, 0),),entity
			)

	def First(self):
		'�������� ������ �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetCount(self):
		'�������� ���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'�������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def refresh(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksOverlapObjectOptions(DispatchBaseClass):
	'��������� ���������� ��������������� ��������.'
	CLSID = IID('{F78E6B71-BEF3-4A4D-AE50-FE96426F6FD1}')
	coclass_clsid = IID('{E41D019C-2D40-452D-8F7B-3FB5FE2D3E8E}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"gap": (2, 2, (5, 0), (), "gap", None),
		"overlap": (1, 2, (11, 0), (), "overlap", None),
	}
	_prop_map_put_ = {
		"gap" : ((2, LCID, 4, 0),()),
		"overlap" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksParagraphParam(DispatchBaseClass):
	'��������� ���������.'
	CLSID = IID('{364521B2-94B5-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{364521B4-94B5-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ang": (4, 2, (5, 0), (), "ang", None),
		"hFormat": (8, 2, (3, 0), (), "hFormat", None),
		"height": (6, 2, (5, 0), (), "height", None),
		"style": (1, 2, (3, 0), (), "style", None),
		"vFormat": (7, 2, (3, 0), (), "vFormat", None),
		"width": (5, 2, (5, 0), (), "width", None),
		"x": (2, 2, (5, 0), (), "x", None),
		"y": (3, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"ang" : ((4, LCID, 4, 0),()),
		"hFormat" : ((8, LCID, 4, 0),()),
		"height" : ((6, LCID, 4, 0),()),
		"style" : ((1, LCID, 4, 0),()),
		"vFormat" : ((7, LCID, 4, 0),()),
		"width" : ((5, LCID, 4, 0),()),
		"x" : ((2, LCID, 4, 0),()),
		"y" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksParametrizationParam(DispatchBaseClass):
	'��������� ���������� ��������������.'
	CLSID = IID('{ABBA6CE0-CB4C-4A32-98B4-B639352C75BB}')
	coclass_clsid = IID('{ABBA6CE1-CB4C-4A32-98B4-B639352C75BB}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"angleLimit": (7, 2, (5, 0), (), "angleLimit", None),
		"horizontal": (3, 2, (11, 0), (), "horizontal", None),
		"nearestPoints": (1, 2, (11, 0), (), "nearestPoints", None),
		"parallel": (5, 2, (11, 0), (), "parallel", None),
		"perpendicular": (6, 2, (11, 0), (), "perpendicular", None),
		"pointsLimit": (2, 2, (5, 0), (), "pointsLimit", None),
		"vertical": (4, 2, (11, 0), (), "vertical", None),
	}
	_prop_map_put_ = {
		"angleLimit" : ((7, LCID, 4, 0),()),
		"horizontal" : ((3, LCID, 4, 0),()),
		"nearestPoints" : ((1, LCID, 4, 0),()),
		"parallel" : ((5, LCID, 4, 0),()),
		"perpendicular" : ((6, LCID, 4, 0),()),
		"pointsLimit" : ((2, LCID, 4, 0),()),
		"vertical" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPart(DispatchBaseClass):
	'3D ���������.'
	CLSID = IID('{508A0CCD-9D74-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{508A0CCF-9D74-11D6-95CE-00C0262D30E3}')

	def BeginEdit(self):
		'����� � ����� �������������� ���������� �� �����.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'BeginEdit', None)
		return ret

	def BodyCollection(self):
		'�������� ������ ������� ���.'
		ret = self._oleobj_.InvokeTypes(33, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'BodyCollection', None)
		return ret

	def CalcMassInertiaProperties(self, bitVector=defaultNamedNotOptArg):
		'���������� �����-������������ �������������� (bitVector - ���������� ����������� �����, ����������� �����, ����� ��������� � ��������� [ST_MIX_MM..ST_MIX_KG] ) ������: �����|��| ST_MIX_M|ST_MIX_KG.'
		ret = self._oleobj_.InvokeTypes(35, LCID, 1, (9, 0), ((19, 0),),bitVector
			)
		if ret is not None:
			ret = Dispatch(ret, 'CalcMassInertiaProperties', None)
		return ret

	def ClearAllObj(self):
		'������� ��� ������� ���������� � ������.'
		return self._oleobj_.InvokeTypes(50, LCID, 1, (11, 0), (),)

	def ColorParam(self):
		'��������� ����� ����������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ColorParam', None)
		return ret

	def CreateOrEditObject(self, objType=defaultNamedNotOptArg, editObj=defaultNamedNotOptArg):
		'������ �������� �������� ��� �������������� �������.'
		ret = self._oleobj_.InvokeTypes(51, LCID, 1, (9, 0), ((2, 0), (9, 0)),objType
			, editObj)
		if ret is not None:
			ret = Dispatch(ret, 'CreateOrEditObject', None)
		return ret

	def CurveIntersection(self, curve=defaultNamedNotOptArg, parts=defaultNamedNotOptArg, fases=defaultNamedNotOptArg, points=defaultNamedNotOptArg):
		'������� ����������� � ������.'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (11, 0), ((9, 0), (9, 0), (9, 0), (9, 0)),curve
			, parts, fases, points)

	def EndEdit(self, Rebuild=defaultNamedNotOptArg):
		'����� �� ������ �������������� ����������.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), ((11, 0),),Rebuild
			)

	def EntityCollection(self, objType=defaultNamedNotOptArg):
		'������ ��������.'
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), ((2, 0),),objType
			)
		if ret is not None:
			ret = Dispatch(ret, 'EntityCollection', None)
		return ret

	def GetAdvancedColor(self, color=pythoncom.Missing, ambient=pythoncom.Missing, diffuse=pythoncom.Missing, specularity=pythoncom.Missing
			, shininess=pythoncom.Missing, transparency=pythoncom.Missing, emission=pythoncom.Missing):
		'�������� ��������� ����� ����������.'
		return self._ApplyTypes_(19, 1, (11, 0), ((16387, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetAdvancedColor', None,color
			, ambient, diffuse, specularity, shininess, transparency
			, emission)

	def GetCountObj(self):
		'���-�� �������� ���������� � ������.'
		return self._oleobj_.InvokeTypes(49, LCID, 1, (3, 0), (),)

	def GetDefaultEntity(self, objType=defaultNamedNotOptArg):
		'�������� ��������� �������������� �������.'
		ret = self._oleobj_.InvokeTypes(16, LCID, 1, (9, 0), ((2, 0),),objType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetDefaultEntity', None)
		return ret

	def GetFeature(self):
		'�������� ������ ������, ��������� � ������ ��������.'
		ret = self._oleobj_.InvokeTypes(34, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFeature', None)
		return ret

	def GetGabarit(self, full=defaultNamedNotOptArg, customizable=defaultNamedNotOptArg, x1=pythoncom.Missing, y1=pythoncom.Missing
			, z1=pythoncom.Missing, x2=pythoncom.Missing, y2=pythoncom.Missing, z2=pythoncom.Missing):
		'������ �������.'
		return self._ApplyTypes_(58, 1, (11, 0), ((11, 1), (11, 1), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetGabarit', None,full
			, customizable, x1, y1, z1, x2
			, y2, z2)

	def GetMainBody(self):
		'�������� ��������� ��������������� ����.'
		ret = self._oleobj_.InvokeTypes(37, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetMainBody', None)
		return ret

	def GetMass(self):
		'�������� �����.'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (5, 0), (),)

	def GetMateConstraintObjects(self):
		'�������� ������ ����������.'
		ret = self._oleobj_.InvokeTypes(29, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetMateConstraintObjects', None)
		return ret

	def GetMeasurer(self):
		'������� ��������� ���������.'
		ret = self._oleobj_.InvokeTypes(36, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetMeasurer', None)
		return ret

	def GetObject(self, index=defaultNamedNotOptArg):
		'�������� ������ �� �������.'
		ret = self._oleobj_.InvokeTypes(48, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObject', None)
		return ret

	# Result is of type Object3DNotify
	def GetObject3DNotify(self, objType=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'�������� �������� ������� ��� ������� 3D ���������.'
		ret = self._oleobj_.InvokeTypes(39, LCID, 1, (13, 0), ((3, 0), (9, 0)),objType
			, obj)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetObject3DNotify', '{CA35F3C6-7E2D-4700-BE12-BAA26DC1945B}')
		return ret

	# Result is of type ksObject3DNotifyResult
	def GetObject3DNotifyResult(self):
		'��������� ����������� �������������� �������.'
		ret = self._oleobj_.InvokeTypes(40, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObject3DNotifyResult', '{9C3ECC92-E72F-4892-8921-7886F34CA9AD}')
		return ret

	def GetObjectByName(self, name=defaultNamedNotOptArg, objType=defaultNamedNotOptArg, testFullName=defaultNamedNotOptArg, testIgnoreCase=defaultNamedNotOptArg):
		'�������� ��������� �� �����.'
		ret = self._oleobj_.InvokeTypes(57, LCID, 1, (9, 0), ((8, 0), (2, 0), (11, 0), (11, 0)),name
			, objType, testFullName, testIgnoreCase)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectByName', None)
		return ret

	def GetPart(self, type=defaultNamedNotOptArg):
		'������ ����������� ���������.'
		ret = self._oleobj_.InvokeTypes(25, LCID, 1, (9, 0), ((2, 0),),type
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPart', None)
		return ret

	def GetPlacement(self):
		'�������� �������������� �������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	def GetSummMatrix(self, part1=defaultNamedNotOptArg):
		'�������� ��������� ������� �������������� ���������.'
		return self._ApplyTypes_(54, 1, (12, 0), ((9, 0),), 'GetSummMatrix', None,part1
			)

	def GetUserParam(self, userPars=defaultNamedNotOptArg):
		'�������� ��������� ������������.'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (11, 0), ((9, 0),),userPars
			)

	def GetUserParamSize(self):
		'������ ��������� ���������� ������������, �������� � ����������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), (),)

	def IsDetail(self):
		'TRUE - �������� �������� �������.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (11, 0), (),)

	def NewEntity(self, objType=defaultNamedNotOptArg):
		'������� ����� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((2, 0),),objType
			)
		if ret is not None:
			ret = Dispatch(ret, 'NewEntity', None)
		return ret

	def PutStorage(self, fileName=defaultNamedNotOptArg, type=defaultNamedNotOptArg, mirror=defaultNamedNotOptArg):
		'������ ���������.'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (11, 0), ((8, 0), (3, 0), (11, 0)),fileName
			, type, mirror)

	def RebuildModel(self):
		'����������� ��������� � ������������ � ������ ���������� ������� ����������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), (),)

	def RebuildModelEx(self, redraw=defaultNamedNotOptArg):
		'����������� ������.'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (11, 0), ((11, 0),),redraw
			)

	def SetAdvancedColor(self, color=defaultNamedNotOptArg, ambient=-47.0, diffuse=-47.0, specularity=-47.0
			, shininess=-47.0, transparency=1.0, emission=-47.0):
		'���������� ��������� ����� ����������.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((3, 1), (5, 49), (5, 49), (5, 49), (5, 49), (5, 49), (5, 49)),color
			, ambient, diffuse, specularity, shininess, transparency
			, emission)

	def SetMateConstraintObjects(self, collection=defaultNamedNotOptArg):
		'���������� ������ ����������.'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (11, 0), ((9, 0),),collection
			)

	def SetMaterial(self, material=defaultNamedNotOptArg, density=defaultNamedNotOptArg):
		'�������� ��������.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (11, 0), ((8, 0), (5, 0)),material
			, density)

	def SetObject(self, index=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'���������� ������ �� �������.'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (11, 0), ((3, 0), (9, 0)),index
			, obj)

	def SetPlacement(self, placement=defaultNamedNotOptArg):
		'���������� �������������� �������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((9, 0),),placement
			)

	def SetSourceVariables(self, Rebuild=defaultNamedNotOptArg):
		'���������� �������� ���������� �� ���������.'
		return self._oleobj_.InvokeTypes(56, LCID, 1, (11, 0), ((11, 0),),Rebuild
			)

	def SetUserParam(self, userPars=defaultNamedNotOptArg):
		'���������� ��������� ������������.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), ((9, 0),),userPars
			)

	def TransformPoint(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg, part1=defaultNamedNotOptArg):
		'������� ��������� ����� ���������� ������ part1 � ������� ��������� ������.'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (11, 0), ((16389, 0), (16389, 0), (16389, 0), (9, 0)),x
			, y, z, part1)

	def TransformPoints(self, points=defaultNamedNotOptArg, part1=defaultNamedNotOptArg):
		'������� ��������� ����� ���������� ������ part1 � ������� ��������� ������.'
		return self._ApplyTypes_(53, 1, (11, 0), ((16396, 3), (9, 1)), 'TransformPoints', None,points
			, part1)

	def Update(self):
		'�������� ���������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

	def UpdatePlacement(self):
		'�������� �������������� �������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), (),)

	def UpdatePlacementEx(self, redraw=defaultNamedNotOptArg):
		'���������� ��������� ������� ��������� ������.'
		return self._oleobj_.InvokeTypes(41, LCID, 1, (11, 0), ((11, 0),),redraw
			)

	def VariableCollection(self):
		'������ ������� ���������� ����������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'VariableCollection', None)
		return ret

	_prop_map_get_ = {
		"DoubleClickEditOff": (52, 2, (11, 0), (), "DoubleClickEditOff", None),
		"PropertyObjectEditable": (59, 2, (11, 0), (), "PropertyObjectEditable", None),
		"excluded": (7, 2, (11, 0), (), "excluded", None),
		"fileName": (6, 2, (8, 0), (), "fileName", None),
		"fixedComponent": (3, 2, (11, 0), (), "fixedComponent", None),
		"hidden": (46, 2, (11, 0), (), "hidden", None),
		"marking": (2, 2, (8, 0), (), "marking", None),
		"name": (1, 2, (8, 0), (), "name", None),
		"needRebuild": (43, 2, (11, 0), (), "needRebuild", None),
		"standardComponent": (4, 2, (11, 0), (), "standardComponent", None),
		"useColor": (38, 2, (3, 0), (), "useColor", None),
		"MultiBodyParts": (55, 2, (11, 0), (), "MultiBodyParts", None),
		"density": (31, 2, (5, 0), (), "density", None),
		"material": (5, 2, (8, 0), (), "material", None),
	}
	_prop_map_put_ = {
		"DoubleClickEditOff" : ((52, LCID, 4, 0),()),
		"PropertyObjectEditable" : ((59, LCID, 4, 0),()),
		"excluded" : ((7, LCID, 4, 0),()),
		"fileName" : ((6, LCID, 4, 0),()),
		"fixedComponent" : ((3, LCID, 4, 0),()),
		"hidden" : ((46, LCID, 4, 0),()),
		"marking" : ((2, LCID, 4, 0),()),
		"name" : ((1, LCID, 4, 0),()),
		"needRebuild" : ((43, LCID, 4, 0),()),
		"standardComponent" : ((4, LCID, 4, 0),()),
		"useColor" : ((38, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPartCollection(DispatchBaseClass):
	'������ ����������� ������.'
	CLSID = IID('{03CEAC87-C0B8-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{03CEAC89-C0B8-11D6-8734-00C0262CDD2C}')

	def Add(self, part=defaultNamedNotOptArg):
		'�������� ������ � ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),part
			)

	def AddAt(self, part=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� ������ � ������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0), (3, 0)),part
			, index)

	def AddBefore(self, part=defaultNamedNotOptArg, base=defaultNamedNotOptArg):
		'�������� ������ � ������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 0), (9, 0)),part
			, base)

	def Clear(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), (),)

	def DetachByBody(self, part=defaultNamedNotOptArg):
		'������� ������ �� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((9, 0),),part
			)

	def DetachByIndex(self, index=defaultNamedNotOptArg):
		'������� ������ �� �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((3, 0),),index
			)

	def FindIt(self, entity=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((9, 0),),entity
			)

	def First(self):
		'�������� ��������� �� ��������� ������� ��������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ��������� �� ��������� �������� �� �������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetByName(self, name=defaultNamedNotOptArg, testFullName=False, testIgnoreCase=True):
		'�������� ��������� �� ��������� �������� �� �����.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((8, 0), (11, 48), (11, 48)),name
			, testFullName, testIgnoreCase)
		if ret is not None:
			ret = Dispatch(ret, 'GetByName', None)
		return ret

	def GetCount(self):
		'�������� ���������� ��������� � �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'�������� ��������� �� ��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'�������� ��������� �� ��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'�������� ��������� �� ��������� ����������� ��������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def SetByIndex(self, part=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'�������� ������ �� �������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), ((9, 0), (3, 0)),part
			, index)

	def refresh(self):
		'�������� ������ ����������� �������� ���������� ������ (����, ���������� � �.�.).'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPhantom(DispatchBaseClass):
	'��������� �������.'
	CLSID = IID('{9AF8E353-98A0-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{9AF8E355-98A0-11D6-95CE-00C0262D30E3}')

	def GetPhantomParam(self):
		'�������� ��������� �� ��������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPhantomParam', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"phantom": (1, 2, (2, 0), (), "phantom", None),
	}
	_prop_map_put_ = {
		"phantom" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlacement(DispatchBaseClass):
	'��������� ��������� ������� ��������� (��������� �������).'
	CLSID = IID('{2DFACC64-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{2DFACC66-C4A4-11D6-8734-00C0262CDD2C}')

	def GetAxis(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing, type=defaultNamedNotOptArg):
		'�������� �����, ����� ������� �������� ��������� ���.'
		return self._ApplyTypes_(3, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2), (3, 1)), 'GetAxis', None,x
			, y, z, type)

	def GetMatrix3D(self, Result=pythoncom.Missing):
		'�������� ������� ������� ��������� � ���� �������. SAFEARRAY double (VT_ARRAY | VT_R8).'
		return self._ApplyTypes_(12, 1, (11, 0), ((16396, 2),), 'GetMatrix3D', None,Result
			)

	def GetOrigin(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ���������� ������ ��������� ������� ���������.'
		return self._ApplyTypes_(1, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetOrigin', None,x
			, y, z)

	def GetVector(self, type=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ������ ��� ��������� ���.'
		return self._ApplyTypes_(9, 1, (11, 0), ((3, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetVector', None,type
			, x, y, z)

	def InitByMatrix3D(self, mtr=defaultNamedNotOptArg):
		'���������� ������� ��������� �� �������. SAFEARRAY double (VT_ARRAY | VT_R8).'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((12, 1),),mtr
			)

	def PointOn(self, XIn=defaultNamedNotOptArg, YIn=defaultNamedNotOptArg, XOut=pythoncom.Missing, YOut=pythoncom.Missing
			, ZOut=pythoncom.Missing):
		'�������� ���������������� ����� �� ����� �� ���������� xy.'
		return self._ApplyTypes_(8, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'PointOn', None,XIn
			, YIn, XOut, YOut, ZOut)

	def PointProjection(self, XIn=defaultNamedNotOptArg, YIn=defaultNamedNotOptArg, ZIn=defaultNamedNotOptArg, XOut=pythoncom.Missing
			, YOut=pythoncom.Missing):
		'�������� ����� �� ���������� xy.'
		return self._ApplyTypes_(7, 1, (11, 0), ((5, 1), (5, 1), (5, 1), (16389, 2), (16389, 2)), 'PointProjection', None,XIn
			, YIn, ZIn, XOut, YOut)

	def SetAxes(self, Xx=defaultNamedNotOptArg, Xy=defaultNamedNotOptArg, Xz=defaultNamedNotOptArg, Yx=defaultNamedNotOptArg
			, Yy=defaultNamedNotOptArg, Yz=defaultNamedNotOptArg):
		'����������  ��� X � Y.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0), (5, 0), (5, 0)),Xx
			, Xy, Xz, Yx, Yy, Yz
			)

	def SetAxis(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg, type=defaultNamedNotOptArg):
		'�������� �����, ����� ������� �������� ��������� ���.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (3, 0)),x
			, y, z, type)

	def SetOrigin(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg):
		'�������� ���������� ������ ��������� ������� ���������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0)),x
			, y, z)

	def SetPlacement(self, placement=defaultNamedNotOptArg):
		'�������� ��������� ������� ���������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 1),),placement
			)

	def SetVector(self, type=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg):
		'������ ������ ��� ��������� ���.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((3, 1), (5, 1), (5, 1), (5, 1)),type
			, x, y, z)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlacementParam(DispatchBaseClass):
	'��������� ��������������.'
	CLSID = IID('{7F7D6FA8-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FAA-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"angle": (4, 2, (5, 0), (), "angle", None),
		"scale_": (3, 2, (5, 0), (), "scale_", None),
		"xBase": (1, 2, (5, 0), (), "xBase", None),
		"yBase": (2, 2, (5, 0), (), "yBase", None),
	}
	_prop_map_put_ = {
		"angle" : ((4, LCID, 4, 0),()),
		"scale_" : ((3, LCID, 4, 0),()),
		"xBase" : ((1, LCID, 4, 0),()),
		"yBase" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlane3PointsDefinition(DispatchBaseClass):
	'��������� ��������� �� 3 ������.'
	CLSID = IID('{DEEFF011-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF013-C3E2-11D6-8734-00C0262CDD2C}')

	def GetPoint(self, number=defaultNamedNotOptArg):
		'�������� ��������� ������� ����� ������� �������� ���������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((3, 0),),number
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPoint', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetPoint(self, number=defaultNamedNotOptArg, point=defaultNamedNotOptArg):
		'���������� ��������� ������� ����� ������� �������� ���������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((3, 0), (9, 0)),number
			, point)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlaneAngleDefinition(DispatchBaseClass):
	'��������� ��������� ��� �����.'
	CLSID = IID('{DEEFF00E-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF010-C3E2-11D6-8734-00C0262CDD2C}')

	def GetAxis(self):
		'�������� ��������� ������� ���.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAxis', None)
		return ret

	def GetPlane(self):
		'�������� ��������� ������� ���������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetAxis(self, axis=defaultNamedNotOptArg):
		'�������� ������� ���.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),axis
			)

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'�������� ������� ���������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),plane
			)

	_prop_map_get_ = {
		"angle": (1, 2, (5, 0), (), "angle", None),
	}
	_prop_map_put_ = {
		"angle" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlaneEdgePointDefinition(DispatchBaseClass):
	'��������� ��������� ����� ����� � �������.'
	CLSID = IID('{DEEFF01A-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF01C-C3E2-11D6-8734-00C0262CDD2C}')

	def GetEdge(self):
		'�������� ��������� �����.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEdge', None)
		return ret

	def GetPoint(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPoint', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetEdge(self, edge=defaultNamedNotOptArg):
		'�������� �����.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((9, 0),),edge
			)

	def SetPoint(self, point=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),point
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlaneLineToEdgeDefinition(DispatchBaseClass):
	'��������� ��������� ����� ����� ���-��/���-�� ������� �����.'
	CLSID = IID('{DEEFF023-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF025-C3E2-11D6-8734-00C0262CDD2C}')

	def GetEdgeFirst(self):
		'�������� ��������� ������� �����.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEdgeFirst', None)
		return ret

	def GetEdgeSecond(self):
		'�������� ��������� ������� �����.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEdgeSecond', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetEdgeFirst(self, edge1=defaultNamedNotOptArg):
		'�������� ������ �����.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),edge1
			)

	def SetEdgeSecond(self, edge2=defaultNamedNotOptArg):
		'�������� ������ �����.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),edge2
			)

	_prop_map_get_ = {
		"parallel": (1, 2, (11, 0), (), "parallel", None),
	}
	_prop_map_put_ = {
		"parallel" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlaneLineToPlaneDefinition(DispatchBaseClass):
	'��������� ��������� ����� ����� ���-��/���-�� �����.'
	CLSID = IID('{DEEFF026-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF028-C3E2-11D6-8734-00C0262CDD2C}')

	def GetEdge(self):
		'�������� ��������� �����.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEdge', None)
		return ret

	def GetPlane(self):
		'�������� ��������� ���������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetEdge(self, edge=defaultNamedNotOptArg):
		'�������� �����.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),edge
			)

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'�������� ���������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),plane
			)

	_prop_map_get_ = {
		"parallel": (1, 2, (11, 0), (), "parallel", None),
	}
	_prop_map_put_ = {
		"parallel" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlaneMiddleDefinition(DispatchBaseClass):
	"��������� ��������������� ��������� '������� ���������'."
	CLSID = IID('{CC5E3539-5B35-46FC-AFE1-19BB0168D52F}')
	coclass_clsid = IID('{D7844AFC-91B0-4C08-8622-0E4595BA6551}')

	def GetObject(self, number=defaultNamedNotOptArg):
		'�������� ��������� �� ��������� �������� ������� � ��������� �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), ((3, 0),),number
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObject', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetObject(self, number=defaultNamedNotOptArg, val=defaultNamedNotOptArg):
		'���������� ��������� �� ��������� �������� ������� � ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((3, 0), (9, 0)),number
			, val)

	_prop_map_get_ = {
		"position": (1, 2, (11, 0), (), "position", None),
	}
	_prop_map_put_ = {
		"position" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlaneNormalToSurfaceDefinition(DispatchBaseClass):
	'��������� ���������� ���������.'
	CLSID = IID('{DEEFF014-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF016-C3E2-11D6-8734-00C0262CDD2C}')

	def GetFace(self):
		'�������� ��������� ���������� ��� �������������� �����.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFace', None)
		return ret

	def GetPlane(self):
		'�������� ��������� ������� ����� ��� �������������� ���������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetFace(self, face=defaultNamedNotOptArg):
		'�������� ���������� ��� �������������� �����.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),face
			)

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'�������� ������� ����� ��� �������������� ���������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),plane
			)

	_prop_map_get_ = {
		"angle": (1, 2, (5, 0), (), "angle", None),
		"autoBuilding": (7, 2, (5, 0), (), "autoBuilding", None),
	}
	_prop_map_put_ = {
		"angle" : ((1, LCID, 4, 0),()),
		"autoBuilding" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlaneOffsetDefinition(DispatchBaseClass):
	'��������� ��������� ���������.'
	CLSID = IID('{DEEFF00B-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF00D-C3E2-11D6-8734-00C0262CDD2C}')

	def GetPlane(self):
		'�������� ��������� ������� ���������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'�������� ������� ���������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),plane
			)

	_prop_map_get_ = {
		"direction": (2, 2, (11, 0), (), "direction", None),
		"offset": (1, 2, (5, 0), (), "offset", None),
	}
	_prop_map_put_ = {
		"direction" : ((2, LCID, 4, 0),()),
		"offset" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlaneParallelDefinition(DispatchBaseClass):
	'��������� ��������� ����� ������� ����������� ������ ���������.'
	CLSID = IID('{DEEFF01D-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF01F-C3E2-11D6-8734-00C0262CDD2C}')

	def GetPlane(self):
		'�������� ��������� ���������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def GetPoint(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPoint', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'�������� ���������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((9, 0),),plane
			)

	def SetPoint(self, point=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),point
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlaneParam(DispatchBaseClass):
	'��������� ���������� ���������.'
	CLSID = IID('{6A6F6B95-D100-4D54-A430-70A42D342917}')
	coclass_clsid = IID('{94A91D78-30AE-4B04-AEE2-B098D3270602}')

	def GetPlacement(self):
		'�������� �� ���������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlanePerpendicularDefinition(DispatchBaseClass):
	'��������� ��������� ����� ������� ��������������� �����.'
	CLSID = IID('{DEEFF020-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF022-C3E2-11D6-8734-00C0262CDD2C}')

	def GetEdge(self):
		'�������� ��������� �����.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEdge', None)
		return ret

	def GetPoint(self):
		'�������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPoint', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetEdge(self, edge=defaultNamedNotOptArg):
		'�������� �����.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((9, 0),),edge
			)

	def SetPoint(self, point=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),point
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPlaneTangentToSurfaceDefinition(DispatchBaseClass):
	'��������� ����������� ���������.'
	CLSID = IID('{DEEFF017-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF019-C3E2-11D6-8734-00C0262CDD2C}')

	def GetFace(self):
		'�������� ��������� ���������� ��� �������������� �����.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFace', None)
		return ret

	def GetPlane(self):
		'�������� ��������� ������� ����� ��� �������������� ���������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetFace(self, face=defaultNamedNotOptArg):
		'�������� ���������� ��� �������������� �����.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),face
			)

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'�������� ������� ����� ��� �������������� ���������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),plane
			)

	_prop_map_get_ = {
		"angle": (7, 2, (5, 0), (), "angle", None),
		"choosePlane": (1, 2, (2, 0), (), "choosePlane", None),
	}
	_prop_map_put_ = {
		"angle" : ((7, LCID, 4, 0),()),
		"choosePlane" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPointParam(DispatchBaseClass):
	'��������� �����.'
	CLSID = IID('{7F7D6F90-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6F92-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"style": (3, 2, (3, 0), (), "style", None),
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"style" : ((3, LCID, 4, 0),()),
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPolyLineDefinition(DispatchBaseClass):
	'�������.'
	CLSID = IID('{0307BBA2-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BBA4-C193-11D6-8734-00C0262CDD2C}')

	# Result is of type ksPolyLineVertexParam
	def AddPointWithParams(self, index=defaultNamedNotOptArg):
		'�������� ����� �������'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddPointWithParams', '{1BCC4F0F-1091-41A3-895B-0608D20715B7}')
		return ret

	def AddVertex(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg, radius=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0)),x
			, y, z, radius)

	def DeleteVertex(self, index=defaultNamedNotOptArg):
		'������� �������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((3, 0),),index
			)

	def EdgeCollection(self):
		'�������� ������ �����.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'EdgeCollection', None)
		return ret

	def Flush(self):
		'�������� ������ ������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), (),)

	def GetCountVertex(self):
		'�������� ���������� ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def GetCurve3D(self):
		'�������� ��������� �� ��������� �������������� ������.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCurve3D', None)
		return ret

	def GetParamVertex(self, index=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing
			, radius=pythoncom.Missing):
		'����� ��������� �������.'
		return self._ApplyTypes_(6, 1, (11, 0), ((3, 1), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetParamVertex', None,index
			, x, y, z, radius)

	# Result is of type ksPolyLineVertexParam
	def GetPointParams(self, index=defaultNamedNotOptArg):
		'��������� ���������� ������� �������'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPointParams', '{1BCC4F0F-1091-41A3-895B-0608D20715B7}')
		return ret

	def InsertVertex(self, index=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg
			, radius=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((3, 0), (5, 0), (5, 0), (5, 0), (5, 0)),index
			, x, y, z, radius)

	def ReadFromFile(self, fileName=defaultNamedNotOptArg):
		'��������� ���� � �������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((8, 0),),fileName
			)

	def WriteToFile(self, fileName=defaultNamedNotOptArg):
		'�������� ���� � �������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((8, 0),),fileName
			)

	_prop_map_get_ = {
		"closed": (1, 2, (11, 0), (), "closed", None),
		"vertexVisible": (13, 2, (11, 0), (), "vertexVisible", None),
	}
	_prop_map_put_ = {
		"closed" : ((1, LCID, 4, 0),()),
		"vertexVisible" : ((13, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPolyLineVertexParam(DispatchBaseClass):
	'��������� ���������� ������� �������'
	CLSID = IID('{1BCC4F0F-1091-41A3-895B-0608D20715B7}')
	coclass_clsid = None

	# Result is of type ksEntity
	def GetAssociation(self):
		'�������� ��������������� �������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAssociation', '{508A0CCA-9D74-11D6-95CE-00C0262D30E3}')
		return ret

	# Result is of type ksEntity
	def GetBuildingObject(self):
		'�������� ������ ������������ �������� ������� ����������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetBuildingObject', '{508A0CCA-9D74-11D6-95CE-00C0262D30E3}')
		return ret

	def GetIndex(self):
		'�������� ������ �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), (),)

	def GetParamByDistance(self, distance=pythoncom.Missing, radius=pythoncom.Missing):
		'�������� ���������� � ������.'
		return self._ApplyTypes_(5, 1, (11, 0), ((16389, 2), (16389, 2)), 'GetParamByDistance', None,distance
			, radius)

	def GetParamVertex(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing, radius=pythoncom.Missing):
		'�������� ��������� �������.'
		return self._ApplyTypes_(2, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetParamVertex', None,x
			, y, z, radius)

	# Result is of type ksEntity
	def GetVertex(self):
		'�������� �������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetVertex', '{508A0CCA-9D74-11D6-95CE-00C0262D30E3}')
		return ret

	def SetAssociation(self, vertex=defaultNamedNotOptArg):
		'���������� ��������������� �������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),vertex
			)

	def SetBuildingObject(self, object=defaultNamedNotOptArg):
		'���������� ������ ������������ �������� ������� ����������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((9, 0),),object
			)

	def SetParamByDistance(self, distance=defaultNamedNotOptArg, radius=defaultNamedNotOptArg):
		'���������� ���������� � ������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((5, 0), (5, 0)),distance
			, radius)

	def SetParamByVertex(self, vertex=defaultNamedNotOptArg, radius=defaultNamedNotOptArg):
		'���������� ��������� ������� �� ��������� �� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0), (5, 0)),vertex
			, radius)

	def SetParamVertex(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg, radius=defaultNamedNotOptArg):
		'���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0)),x
			, y, z, radius)

	_prop_map_get_ = {
		"buildingType": (1, 2, (3, 0), (), "buildingType", None),
	}
	_prop_map_put_ = {
		"buildingType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPolylineParam(DispatchBaseClass):
	'��������� ���������.'
	CLSID = IID('{7F7D6FAE-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FB0-97DA-11D6-8732-00C0262CDD2C}')

	def GetpMathPoint(self):
		'���������� ������ �����.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpMathPoint', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	def SetpMathPoint(self, val=defaultNamedNotOptArg):
		'�������� ������ �����.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"closed": (5, 2, (11, 0), (), "closed", None),
		"style": (1, 2, (3, 0), (), "style", None),
	}
	_prop_map_put_ = {
		"closed" : ((5, LCID, 4, 0),()),
		"style" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksPosLeaderParam(DispatchBaseClass):
	'����� ������� ��� ����������� �������.'
	CLSID = IID('{3F715E43-97D9-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3F715E45-97D9-11D6-95CE-00C0262D30E3}')

	def GetpPolyline(self):
		'������������ ������ ����������� �����-�������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpPolyline', None)
		return ret

	def GetpTextline(self):
		'������������ ������ ����� ������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpTextline', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

	def SetpPolyline(self, polyline=defaultNamedNotOptArg):
		'������������ ������ ����������� �����-�������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),polyline
			)

	def SetpTextline(self, textline=defaultNamedNotOptArg):
		'������������ ������ ����� ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((9, 0),),textline
			)

	_prop_map_get_ = {
		"arrowType": (4, 2, (2, 0), (), "arrowType", None),
		"dirX": (5, 2, (3, 0), (), "dirX", None),
		"dirY": (6, 2, (3, 0), (), "dirY", None),
		"style": (1, 2, (3, 0), (), "style", None),
		"x": (2, 2, (5, 0), (), "x", None),
		"y": (3, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"arrowType" : ((4, LCID, 4, 0),()),
		"dirX" : ((5, LCID, 4, 0),()),
		"dirY" : ((6, LCID, 4, 0),()),
		"style" : ((1, LCID, 4, 0),()),
		"x" : ((2, LCID, 4, 0),()),
		"y" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksQualityContensParam(DispatchBaseClass):
	'��������� ���������� ���������.'
	CLSID = IID('{7F7D6FEA-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FEC-97DA-11D6-8732-00C0262CDD2C}')

	def GetpQualityItems(self):
		'���������� ������ ����������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpQualityItems', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	def SetpQualityItems(self, val=defaultNamedNotOptArg):
		'�������� ������ ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"kindQuality": (2, 2, (2, 0), (), "kindQuality", None),
		"name": (3, 2, (8, 0), (), "name", None),
		"systemQuality": (1, 2, (2, 0), (), "systemQuality", None),
	}
	_prop_map_put_ = {
		"kindQuality" : ((2, LCID, 4, 0),()),
		"name" : ((3, LCID, 4, 0),()),
		"systemQuality" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksQualityItemParam(DispatchBaseClass):
	'������ �� ����� ��������� ��� ���������.'
	CLSID = IID('{7F7D6FE7-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FE9-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"high": (3, 2, (5, 0), (), "high", None),
		"low": (4, 2, (5, 0), (), "low", None),
		"maxLimit": (2, 2, (2, 0), (), "maxLimit", None),
		"minLimit": (1, 2, (2, 0), (), "minLimit", None),
	}
	_prop_map_put_ = {
		"high" : ((3, LCID, 4, 0),()),
		"low" : ((4, LCID, 4, 0),()),
		"maxLimit" : ((2, LCID, 4, 0),()),
		"minLimit" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRBreakDimParam(DispatchBaseClass):
	'��������� ����������� ������� � �������.'
	CLSID = IID('{7F7D6FE4-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FE6-97DA-11D6-8732-00C0262CDD2C}')

	def GetDPar(self):
		'���������� ��������� ����������� �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDPar', None)
		return ret

	def GetSPar(self):
		'���������� ��������� �������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSPar', None)
		return ret

	def GetTPar(self):
		'���������� ��������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTPar', None)
		return ret

	def SetDPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ����������� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetSPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� �������� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetTPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRBreakDrawingParam(DispatchBaseClass):
	'��������� �������� �������������� � ����������� ��������.'
	CLSID = IID('{7F7D6FE1-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FE3-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ang": (2, 2, (5, 0), (), "ang", None),
		"pb": (3, 2, (3, 0), (), "pb", None),
		"pt": (1, 2, (2, 0), (), "pt", None),
	}
	_prop_map_put_ = {
		"ang" : ((2, LCID, 4, 0),()),
		"pb" : ((3, LCID, 4, 0),()),
		"pt" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRDimDrawingParam(DispatchBaseClass):
	'��������� ��������� �������������� � ����������� ��������.'
	CLSID = IID('{2A4D4542-95B3-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{2A4D4544-95B3-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ang": (4, 2, (5, 0), (), "ang", None),
		"pt1": (1, 2, (2, 0), (), "pt1", None),
		"pt2": (2, 2, (2, 0), (), "pt2", None),
		"shelfDir": (5, 2, (3, 0), (), "shelfDir", None),
		"textPos": (3, 2, (3, 0), (), "textPos", None),
	}
	_prop_map_put_ = {
		"ang" : ((4, LCID, 4, 0),()),
		"pt1" : ((1, LCID, 4, 0),()),
		"pt2" : ((2, LCID, 4, 0),()),
		"shelfDir" : ((5, LCID, 4, 0),()),
		"textPos" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRDimParam(DispatchBaseClass):
	'��������� �������������� � ����������� �������.'
	CLSID = IID('{7F7D6F81-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6F83-97DA-11D6-8732-00C0262CDD2C}')

	def GetDPar(self):
		'���������� ��������� ����������� �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDPar', None)
		return ret

	def GetSPar(self):
		'���������� ��������� �������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSPar', None)
		return ret

	def GetTPar(self):
		'���������� ��������� ��������� �������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTPar', None)
		return ret

	def SetDPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ����������� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetSPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� �������� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetTPar(self, val=defaultNamedNotOptArg):
		'�������� ��������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRDimSourceParam(DispatchBaseClass):
	'��������� �������� �������������� � ����������� ��������.'
	CLSID = IID('{2A4D4545-95B3-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{2A4D4547-95B3-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"rad": (3, 2, (5, 0), (), "rad", None),
		"xc": (1, 2, (5, 0), (), "xc", None),
		"yc": (2, 2, (5, 0), (), "yc", None),
	}
	_prop_map_put_ = {
		"rad" : ((3, LCID, 4, 0),()),
		"xc" : ((1, LCID, 4, 0),()),
		"yc" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRasterFormatParam(DispatchBaseClass):
	'��������� ��� ����������� � ��������� ������.'
	CLSID = IID('{1A91A8AB-AF8C-4EE3-86D4-0A9C00123195}')
	coclass_clsid = IID('{CD6054FC-D754-4139-8CD9-381F7488A6C7}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"colorBPP": (2, 2, (2, 0), (), "colorBPP", None),
		"colorType": (6, 2, (2, 0), (), "colorType", None),
		"extResolution": (4, 2, (3, 0), (), "extResolution", None),
		"extScale": (5, 2, (5, 0), (), "extScale", None),
		"format": (1, 2, (2, 0), (), "format", None),
		"greyScale": (3, 2, (11, 0), (), "greyScale", None),
		"multiPageOutput": (10, 2, (11, 0), (), "multiPageOutput", None),
		"onlyThinLine": (7, 2, (11, 0), (), "onlyThinLine", None),
		"pages": (8, 2, (8, 0), (), "pages", None),
		"rangeIndex": (9, 2, (2, 0), (), "rangeIndex", None),
		"saveWorkArea": (12, 2, (11, 0), (), "saveWorkArea", None),
	}
	_prop_map_put_ = {
		"colorBPP" : ((2, LCID, 4, 0),()),
		"colorType" : ((6, LCID, 4, 0),()),
		"extResolution" : ((4, LCID, 4, 0),()),
		"extScale" : ((5, LCID, 4, 0),()),
		"format" : ((1, LCID, 4, 0),()),
		"greyScale" : ((3, LCID, 4, 0),()),
		"multiPageOutput" : ((10, LCID, 4, 0),()),
		"onlyThinLine" : ((7, LCID, 4, 0),()),
		"pages" : ((8, LCID, 4, 0),()),
		"rangeIndex" : ((9, LCID, 4, 0),()),
		"saveWorkArea" : ((12, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRasterParam(DispatchBaseClass):
	'��������� ���������� �������.'
	CLSID = IID('{7F7D6FAB-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FAD-97DA-11D6-8732-00C0262CDD2C}')

	def GetPlace(self):
		'���������� ��������� ��������������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlace', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetPlace(self, val=defaultNamedNotOptArg):
		'�������� ��������� ��������������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"embeded": (2, 2, (11, 0), (), "embeded", None),
		"fileName": (1, 2, (8, 0), (), "fileName", None),
	}
	_prop_map_put_ = {
		"embeded" : ((2, LCID, 4, 0),()),
		"fileName" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRecordTypeAttrParam(DispatchBaseClass):
	'����������� ��� ���� �������� RECORD_ATTR_TYPE.'
	CLSID = IID('{4FD7CE8D-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CE8F-9968-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"attrLibName": (1, 2, (8, 0), (), "attrLibName", None),
		"key1": (2, 2, (3, 0), (), "key1", None),
		"key2": (3, 2, (3, 0), (), "key2", None),
		"key3": (4, 2, (3, 0), (), "key3", None),
		"key4": (5, 2, (3, 0), (), "key4", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRectParam(DispatchBaseClass):
	'��������� ���������� ����������� ��������������.'
	CLSID = IID('{3F715E2D-97D9-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3F715E2F-97D9-11D6-95CE-00C0262D30E3}')

	def GetpBot(self):
		'����� ����� ������ ����� ��������������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpBot', None)
		return ret

	def GetpTop(self):
		'����� ������ ������ ����� ��������������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpTop', None)
		return ret

	def SetpBot(self, pBot=defaultNamedNotOptArg):
		'���������� ����� ������ ����� ��������������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),pBot
			)

	def SetpTop(self, pTop=defaultNamedNotOptArg):
		'���������� ������ ������ ����� ��������������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),pTop
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRectangleParam(DispatchBaseClass):
	'��������� ��������������.'
	CLSID = IID('{E79C2510-9584-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{E79C2512-9584-11D6-8732-00C0262CDD2C}')

	def GetPCorner(self):
		'������ ������ �����.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPCorner', None)
		return ret

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	def SetPCorner(self, val=defaultNamedNotOptArg):
		'�������� ������ �����.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"ang": (3, 2, (5, 0), (), "ang", None),
		"height": (4, 2, (5, 0), (), "height", None),
		"style": (6, 2, (3, 0), (), "style", None),
		"width": (5, 2, (5, 0), (), "width", None),
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"ang" : ((3, LCID, 4, 0),()),
		"height" : ((4, LCID, 4, 0),()),
		"style" : ((6, LCID, 4, 0),()),
		"width" : ((5, LCID, 4, 0),()),
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRegularPolygonParam(DispatchBaseClass):
	'��������� ����������� ��������������.'
	CLSID = IID('{E79C250D-9584-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{E79C250F-9584-11D6-8732-00C0262CDD2C}')

	def GetPCorner(self):
		'������ ������ �����.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPCorner', None)
		return ret

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	def SetPCorner(self, val=defaultNamedNotOptArg):
		'�������� ������ �����.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"ang": (4, 2, (5, 0), (), "ang", None),
		"count": (1, 2, (3, 0), (), "count", None),
		"describe": (6, 2, (11, 0), (), "describe", None),
		"radius": (5, 2, (5, 0), (), "radius", None),
		"style": (7, 2, (3, 0), (), "style", None),
		"xc": (2, 2, (5, 0), (), "xc", None),
		"yc": (3, 2, (5, 0), (), "yc", None),
	}
	_prop_map_put_ = {
		"ang" : ((4, LCID, 4, 0),()),
		"count" : ((1, LCID, 4, 0),()),
		"describe" : ((6, LCID, 4, 0),()),
		"radius" : ((5, LCID, 4, 0),()),
		"style" : ((7, LCID, 4, 0),()),
		"xc" : ((2, LCID, 4, 0),()),
		"yc" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ksRemoteElementParam(DispatchBaseClass):
	'��������� ���������� ��������� ��������.'
	CLSID = IID('{25076616-4949-455E-A45C-1B801884D825}')
	coclass_clsid = IID('{F37A40F6-4E15-4E01-B4F0-25C49175227A}')

	def GetpText(self):
		'�������� ������������ ������ ����� ������.'
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpText', None)
		return ret

	def Init(self, style=defaultNamedNotOptArg):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((3, 0),),style
			)

	def SetpText(self, pText=defaultNamedNotOptArg):
		'���������� ������������ ������ ����� ������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((9, 0),),pText
			)

	_prop_map_get_ = {
		"height": (7, 2, (5, 0), (), "height", None),
		"radius": (8, 2, (5, 0), (), "radius", None),
		"shelfDir": (12, 2, (2, 0), (), "shelfDir", None),
		"shelfX": (10, 2, (5, 0), (), "shelfX", None),
		"shelfY": (11, 2, (5, 0), (), "shelfY", None),
		"signType": (3, 2, (3, 0), (), "signType", None),
		"smooth": (9, 2, (5, 0), (), "smooth", None),
		"style": (2, 2, (3, 0), (), "style", None),
		"width": (6, 2, (5, 0), (), "width", None),
		"x": (4, 2, (5, 0), (), "x", None),
		"y": (5, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"height" : ((7, LCID, 4, 0),()),
		"radius" : ((8, LCID, 4, 0),()),
		"shelfDir" : ((12, LCID, 4, 0),()),
		"shelfX" : ((10, LCID, 4, 0),()),
		"shelfY" : ((11, LCID, 4, 0),()),
		"signType" : ((3, LCID, 4, 0),()),
		"smooth" : ((9, LCID, 4, 0),()),
		"style" : ((2, LCID, 4, 0),()),
		"width" : ((6, LCID, 4, 0),()),
		"x" : ((4, LCID, 4, 0),()),
		"y" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRequestInfo(DispatchBaseClass):
	'��������� ������� � �������.'
	CLSID = IID('{9AF8E356-98A0-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{9AF8E358-98A0-11D6-95CE-00C0262D30E3}')

	def GetCallBackC(self):
		'���������� CallBack-������� ��� �������� Cursor.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(11, LCID, 1, (8, 0), (),)

	def GetCallBackCm(self):
		'���������� CallBack-������� ��� �������� CommandWindow.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(15, LCID, 1, (8, 0), (),)

	def GetCallBackP(self):
		'���������� CallBack-������� ��� �������� Placement.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(13, LCID, 1, (8, 0), (),)

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), (),)

	def SetCallBackC(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'������������� CallBack-������� ��� �������� Cursor.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((8, 0), (3, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetCallBackCEx(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'������������� CallBack-������� ��� �������� Cursor.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((8, 0), (12, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetCallBackCm(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'������������� CallBack-������� ��� �������� CommandWindow.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((8, 0), (3, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetCallBackCmEx(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'������������� CallBack-������� ��� �������� CommandWindow.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (11, 0), ((8, 0), (12, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetCallBackP(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'������������� CallBack-������� ��� �������� Placement.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((8, 0), (3, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetCallBackPEx(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'������������� CallBack-������� ��� �������� Placement.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), ((8, 0), (12, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetCursorText(self, text=defaultNamedNotOptArg):
		'���������� ����� �������.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((8, 0),),text
			)

	_prop_map_get_ = {
		"commInstance": (6, 2, (3, 0), (), "commInstance", None),
		"commInstanceEx": (19, 2, (12, 0), (), "commInstanceEx", None),
		"commandsString": (3, 2, (8, 0), (), "commandsString", None),
		"cursor": (4, 2, (8, 0), (), "cursor", None),
		"cursorId": (10, 2, (3, 0), (), "cursorId", None),
		"dynamic": (5, 2, (3, 0), (), "dynamic", None),
		"menuId": (7, 2, (3, 0), (), "menuId", None),
		"prompt": (1, 2, (8, 0), (), "prompt", None),
		"promptId": (9, 2, (3, 0), (), "promptId", None),
		"title": (2, 2, (8, 0), (), "title", None),
		"titleId": (8, 2, (3, 0), (), "titleId", None),
	}
	_prop_map_put_ = {
		"commInstance" : ((6, LCID, 4, 0),()),
		"commInstanceEx" : ((19, LCID, 4, 0),()),
		"commandsString" : ((3, LCID, 4, 0),()),
		"cursor" : ((4, LCID, 4, 0),()),
		"cursorId" : ((10, LCID, 4, 0),()),
		"dynamic" : ((5, LCID, 4, 0),()),
		"menuId" : ((7, LCID, 4, 0),()),
		"prompt" : ((1, LCID, 4, 0),()),
		"promptId" : ((9, LCID, 4, 0),()),
		"title" : ((2, LCID, 4, 0),()),
		"titleId" : ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRequestInfo3D(DispatchBaseClass):
	'��������� �������.'
	CLSID = IID('{E9807824-9D55-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{E9807826-9D55-11D6-95CE-00C0262D30E3}')

	def CreatePhantom(self):
		'������� ������.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), (),)

	def GetCallBack(self):
		'�������� ��� ������� �������� �����.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(8, LCID, 1, (8, 0), (),)

	def GetCallBackFeature(self):
		'�������� ��������� �� ������ ������ � ������� �������� ����� ��� �������� UserGetPlacementAndEntity.'
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCallBackFeature', None)
		return ret

	def GetCurrentCommand(self):
		'����� ������� ������� �� ���������� ����.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), (),)

	def GetEntityCollection(self):
		'������ ��������� ��������.'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEntityCollection', None)
		return ret

	def GetFilterCallBack(self):
		'�������� ��� ������� �������� ����� ��� ���������� ��������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(7, LCID, 1, (8, 0), (),)

	def GetIPhantom(self):
		'��������� �������.'
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetIPhantom', None)
		return ret

	def GetMateConstraintCollection(self):
		'������ ���������� ������ ��� �������.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetMateConstraintCollection', None)
		return ret

	def GetObjectsFilter3D(self, filterType=defaultNamedNotOptArg):
		'������ ���������� 3D �������� � ��������.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (11, 0), ((3, 0),),filterType
			)

	def GetPlacement(self):
		'��������������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	def GetProcessParam(self):
		'�������� ��������� �� ��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (13, 0), (),)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetProcessParam', None)
		return ret

	def GetProcessingGroupObjectsCallBack(self):
		'�������� ��� (� Automation) ��� ����� (� COM) ������� �������� ����� ��� ��������� ��������, ��������� ��� �������������� ������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(30, LCID, 1, (8, 0), (),)

	def GetTakeObjectCallBack(self):
		'�������� ��� ������� �������� ����� ��� ������������ ��������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(25, LCID, 1, (8, 0), (),)

	def GetTakeProcessObject(self):
		'�������� ������ ������������� � �����������.'
		ret = self._oleobj_.InvokeTypes(27, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTakeProcessObject', None)
		return ret

	def SetCallBack(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'���������� ������� �������� �����.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((8, 0), (3, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetCallBackEx(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'���������� ������� �������� �����.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), ((8, 0), (12, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetCursorText(self, text=defaultNamedNotOptArg):
		'���������� ����� �������.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), ((8, 0),),text
			)

	def SetFilterCallBack(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'���������� ������� �������� ����� ��� ���������� ��������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((8, 0), (3, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetFilterCallBackEx(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'���������� ������� �������� ����� ��� ���������� ��������.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (11, 0), ((8, 0), (12, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetObjectsFilter3D(self, filterType=defaultNamedNotOptArg, newVal=defaultNamedNotOptArg):
		'������ ���������� 3D �������� � ��������.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (11, 0), ((3, 0), (11, 0)),filterType
			, newVal)

	def SetProcessParam(self, param=defaultNamedNotOptArg):
		'���������� ��������� �� ��������� ���������� ��������.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((13, 0),),param
			)

	def SetProcessingGroupObjectsCallBack(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'�������� ��� (� Automation) ��� ����� (� COM) ������� �������� ����� ��� ��������� ��������, ��������� ��� �������������� ������.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (11, 0), ((8, 0), (12, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetTakeObjectCallBack(self, methodName=defaultNamedNotOptArg, hInst=defaultNamedNotOptArg, dispatchOCX=defaultNamedNotOptArg):
		'���������� ������� �������� ����� ��� ������������ ��������.'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (11, 0), ((8, 0), (12, 0), (9, 0)),methodName
			, hInst, dispatchOCX)

	def SetTakeProcessObject(self, param=defaultNamedNotOptArg):
		'���������� ������ ��� �������������� � �����������.'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (11, 0), ((9, 0),),param
			)

	_prop_map_get_ = {
		"DynamicFiltering": (20, 2, (11, 0), (), "DynamicFiltering", None),
		"SelectionBandMode": (29, 2, (3, 0), (), "SelectionBandMode", None),
		"ShowCommandWindow": (22, 2, (11, 0), (), "ShowCommandWindow", None),
		"commandsString": (4, 2, (8, 0), (), "commandsString", None),
		"cursorId": (5, 2, (3, 0), (), "cursorId", None),
		"cursorName": (3, 2, (8, 0), (), "cursorName", None),
		"menuId": (6, 2, (3, 0), (), "menuId", None),
		"prompt": (1, 2, (8, 0), (), "prompt", None),
		"title": (2, 2, (8, 0), (), "title", None),
	}
	_prop_map_put_ = {
		"DynamicFiltering" : ((20, LCID, 4, 0),()),
		"SelectionBandMode" : ((29, LCID, 4, 0),()),
		"ShowCommandWindow" : ((22, LCID, 4, 0),()),
		"commandsString" : ((4, LCID, 4, 0),()),
		"cursorId" : ((5, LCID, 4, 0),()),
		"cursorName" : ((3, LCID, 4, 0),()),
		"menuId" : ((6, LCID, 4, 0),()),
		"prompt" : ((1, LCID, 4, 0),()),
		"title" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRibDefinition(DispatchBaseClass):
	'��������� �������� �����.'
	CLSID = IID('{DEEFF002-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF004-C3E2-11D6-8734-00C0262CDD2C}')

	def GetSketch(self):
		'�������� �����.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def GetThinParam(self, thinType=pythoncom.Missing, normalThickness=pythoncom.Missing, reverseTthickness=pythoncom.Missing):
		'�������� ��������� ������ ������.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16386, 2), (16389, 2), (16389, 2)), 'GetThinParam', None,thinType
			, normalThickness, reverseTthickness)

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'������ �����.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	def SetThinParam(self, thinType=0, normalThickness=1.0, reverseThickness=1.0):
		'���������� ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((2, 48), (5, 48), (5, 48)),thinType
			, normalThickness, reverseThickness)

	def ThinParam(self):
		'��������� ���������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ThinParam', None)
		return ret

	_prop_map_get_ = {
		"angle": (2, 2, (5, 0), (), "angle", None),
		"index": (1, 2, (3, 0), (), "index", None),
		"side": (3, 2, (3, 0), (), "side", None),
	}
	_prop_map_put_ = {
		"angle" : ((2, LCID, 4, 0),()),
		"index" : ((1, LCID, 4, 0),()),
		"side" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRotatedParam(DispatchBaseClass):
	'��������� ��������.'
	CLSID = IID('{DEEFF02F-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF031-C3E2-11D6-8734-00C0262CDD2C}')

	_prop_map_get_ = {
		"angleNormal": (1, 2, (5, 0), (), "angleNormal", None),
		"angleReverse": (2, 2, (5, 0), (), "angleReverse", None),
		"direction": (4, 2, (3, 0), (), "direction", None),
		"toroidShape": (3, 2, (11, 0), (), "toroidShape", None),
	}
	_prop_map_put_ = {
		"angleNormal" : ((1, LCID, 4, 0),()),
		"angleReverse" : ((2, LCID, 4, 0),()),
		"direction" : ((4, LCID, 4, 0),()),
		"toroidShape" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRotatedSurfaceDefinition(DispatchBaseClass):
	'����������� ��������.'
	CLSID = IID('{FD27841D-1374-4F7F-AE8A-C2A44F89120D}')
	coclass_clsid = IID('{8B9ECAF3-172D-4F4B-BF51-33C177B87FF2}')

	def GetSideParam(self, side1=defaultNamedNotOptArg, angle=pythoncom.Missing):
		'�������� ��������� �������� � ���� �������.'
		return self._ApplyTypes_(6, 1, (11, 0), ((11, 1), (16389, 2)), 'GetSideParam', None,side1
			, angle)

	def GetSketch(self):
		'�������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSketch', None)
		return ret

	def RotatedParam(self):
		'��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RotatedParam', None)
		return ret

	def SetSideParam(self, side1=False, angle=180.0):
		'���������� ��������� �������� � ���� �������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((11, 48), (5, 48)),side1
			, angle)

	def SetSketch(self, sketch=defaultNamedNotOptArg):
		'���������� ��������� ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),sketch
			)

	_prop_map_get_ = {
		"closedShell": (3, 2, (2, 0), (), "closedShell", None),
		"directionType": (1, 2, (2, 0), (), "directionType", None),
		"toroidShapeType": (2, 2, (11, 0), (), "toroidShapeType", None),
	}
	_prop_map_put_ = {
		"closedShell" : ((3, LCID, 4, 0),()),
		"directionType" : ((1, LCID, 4, 0),()),
		"toroidShapeType" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRoughPar(DispatchBaseClass):
	'��������� ���������� �������������.'
	CLSID = IID('{3F715E33-97D9-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3F715E35-97D9-11D6-95CE-00C0262D30E3}')

	def GetpText(self):
		'����� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpText', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), (),)

	def InitEx(self, style=defaultNamedNotOptArg):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((3, 0),),style
			)

	def SetpText(self, pText=defaultNamedNotOptArg):
		'���������� ��������� ������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((9, 0),),pText
			)

	_prop_map_get_ = {
		"ang": (6, 2, (5, 0), (), "ang", None),
		"around": (3, 2, (2, 0), (), "around", None),
		"cText0": (7, 2, (2, 0), (), "cText0", None),
		"cText1": (8, 2, (2, 0), (), "cText1", None),
		"cText2": (9, 2, (2, 0), (), "cText2", None),
		"cText3": (10, 2, (2, 0), (), "cText3", None),
		"style": (1, 2, (3, 0), (), "style", None),
		"type": (2, 2, (2, 0), (), "type", None),
		"x": (4, 2, (5, 0), (), "x", None),
		"y": (5, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"ang" : ((6, LCID, 4, 0),()),
		"around" : ((3, LCID, 4, 0),()),
		"cText0" : ((7, LCID, 4, 0),()),
		"cText1" : ((8, LCID, 4, 0),()),
		"cText2" : ((9, LCID, 4, 0),()),
		"cText3" : ((10, LCID, 4, 0),()),
		"style" : ((1, LCID, 4, 0),()),
		"type" : ((2, LCID, 4, 0),()),
		"x" : ((4, LCID, 4, 0),()),
		"y" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksRoughParam(DispatchBaseClass):
	'��������� ���������� �������������.'
	CLSID = IID('{3F715E36-97D9-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3F715E38-97D9-11D6-95CE-00C0262D30E3}')

	def GetrPar(self):
		'������ ��������� ���������� ������ �������������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetrPar', None)
		return ret

	def GetshPar(self):
		'������ ��������� ���������� �������� �����.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetshPar', None)
		return ret

	def SetrPar(self, par=defaultNamedNotOptArg):
		'�������� ��������� ���������� ������ �������������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),par
			)

	def SetshPar(self, shPar=defaultNamedNotOptArg):
		'�������� ��������� ���������� �������� �����.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),shPar
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSaveToPreviusParam(DispatchBaseClass):
	'��������� ����������� ��� ���������� � ���������� ������.'
	CLSID = IID('{CF0E948C-5A9D-49A3-BC86-EEA3050193E0}')
	coclass_clsid = None

	def AddOption(self, uniqueID=defaultNamedNotOptArg, optionName=defaultNamedNotOptArg, options=defaultNamedNotOptArg, defaultValue=defaultNamedNotOptArg):
		'�������� ��������� ����������� � ������������ ������ �������� �����������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((8, 1), (8, 1), (12, 1), (8, 1)),uniqueID
			, optionName, options, defaultValue)

	def AddWarning(self, uniqueID=defaultNamedNotOptArg, optionName=defaultNamedNotOptArg, text=defaultNamedNotOptArg):
		'�������� ��������������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1)),uniqueID
			, optionName, text)

	def GetCurrentOptionValue(self, uniqueID=defaultNamedNotOptArg):
		'�������� ������� �������� ��������� � ������� ���������� �����������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(3, LCID, 1, (8, 0), ((8, 1),),uniqueID
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSelectionMng(DispatchBaseClass):
	'��������� ��������� ��������������� ��������.'
	CLSID = IID('{BE41850C-CFC5-40D4-AE49-37AA391BCF4B}')
	coclass_clsid = IID('{39EE8E9D-C228-4F61-9F66-DD58F20CD224}')

	def First(self):
		'������ ������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetCount(self):
		'�������� ����������� ��������������� ��������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), (),)

	def GetObjectByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������ �� �������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectByIndex', None)
		return ret

	def GetObjectType(self, index=defaultNamedNotOptArg):
		'�������� ��� ������� �� �������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((3, 0),),index
			)

	def IsSelected(self, obj=defaultNamedNotOptArg):
		'������������ �� ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def Last(self):
		'��������� ������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'��������� ������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'���������� ������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def Select(self, obj=defaultNamedNotOptArg):
		'������������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def Unselect(self, obj=defaultNamedNotOptArg):
		'����� �������������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def UnselectAll(self):
		'����� ��������������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSelectionMngNotify:
	'C������ ��� ��������� ��������������� ��������.'
	CLSID = CLSID_Sink = IID('{A421368A-34B6-4DDF-9A52-73B3488EE83F}')
	coclass_clsid = IID('{39EE8E9D-C228-4F61-9F66-DD58F20CD224}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnSelect",
		        2 : "OnUnselect",
		        3 : "OnUnselectAll",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnSelect(self, obj=defaultNamedNotOptArg):
#		'������ ������������.'
#	def OnUnselect(self, obj=defaultNamedNotOptArg):
#		'������ ���������������.'
#	def OnUnselectAll(self):
#		'��� ������� ����������������.'


class ksSheetOptions(DispatchBaseClass):
	'��������� ���������� ����������.'
	CLSID = IID('{FBCC5BA8-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5BAA-996C-11D6-8732-00C0262CDD2C}')

	def GetSheetParam(self, type=defaultNamedNotOptArg):
		'���������� ��������� �� ��������� ���������� �����(TRUE - ����������������, FALSE - �����������).'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((11, 0),),type
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSheetParam', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"layoutName": (2, 2, (8, 0), (), "layoutName", None),
		"sheetType": (5, 2, (11, 0), (), "sheetType", None),
		"shtType": (1, 2, (2, 0), (), "shtType", None),
	}
	_prop_map_put_ = {
		"layoutName" : ((2, LCID, 4, 0),()),
		"sheetType" : ((5, LCID, 4, 0),()),
		"shtType" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSheetPar(DispatchBaseClass):
	'��������� ���������� ����������.'
	CLSID = IID('{FBCC5B93-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5B95-996C-11D6-8732-00C0262CDD2C}')

	def GetSheetParam(self):
		'���������� ��������� �� ��������� ���������� ����������������� ��� ������������ �����.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSheetParam', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"layoutName": (1, 2, (8, 0), (), "layoutName", None),
		"shtType": (2, 2, (2, 0), (), "shtType", None),
	}
	_prop_map_put_ = {
		"layoutName" : ((1, LCID, 4, 0),()),
		"shtType" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSheetSize(DispatchBaseClass):
	'��������� �����.'
	CLSID = IID('{FBCC5B8D-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5B8F-996C-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"height": (2, 2, (5, 0), (), "height", None),
		"width": (1, 2, (5, 0), (), "width", None),
	}
	_prop_map_put_ = {
		"height" : ((2, LCID, 4, 0),()),
		"width" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksShelfPar(DispatchBaseClass):
	'��������� ���������� �������� �����.'
	CLSID = IID('{3F715E30-97D9-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3F715E32-97D9-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ang": (2, 2, (5, 0), (), "ang", None),
		"length": (3, 2, (3, 0), (), "length", None),
		"psh": (1, 2, (3, 0), (), "psh", None),
	}
	_prop_map_put_ = {
		"ang" : ((2, LCID, 4, 0),()),
		"length" : ((3, LCID, 4, 0),()),
		"psh" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksShellDefinition(DispatchBaseClass):
	'��������� �������� ��������.'
	CLSID = IID('{DEEFEFF6-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFEFF8-C3E2-11D6-8734-00C0262CDD2C}')

	def FaceArray(self):
		'�������� ��������� ������� ������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'FaceArray', None)
		return ret

	_prop_map_get_ = {
		"thickness": (1, 2, (5, 0), (), "thickness", None),
		"thinType": (2, 2, (11, 0), (), "thinType", None),
	}
	_prop_map_put_ = {
		"thickness" : ((1, LCID, 4, 0),()),
		"thinType" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSketchDefinition(DispatchBaseClass):
	'��������� ������.'
	CLSID = IID('{2DFACC70-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{2DFACC72-C4A4-11D6-8734-00C0262CDD2C}')

	def AddProjectionOf(self, entity=defaultNamedNotOptArg):
		'�������� � ����� �������� �������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), ((9, 0),),entity
			)

	def BeginEdit(self):
		'����� � ����� �������������� ������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'BeginEdit', None)
		return ret

	def BeginEditEx(self, readOnly=defaultNamedNotOptArg):
		'����� � ����� �������������� ������: readOnly = TRUE - ��� ������.'
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), ((3, 0),),readOnly
			)
		if ret is not None:
			ret = Dispatch(ret, 'BeginEditEx', None)
		return ret

	def EndEdit(self):
		'����� �� ������ �������������� ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	def GetLocation(self, x=pythoncom.Missing, y=pythoncom.Missing):
		'�������� �������� ������� ��������� ������.'
		return self._ApplyTypes_(5, 1, (11, 0), ((16389, 2), (16389, 2)), 'GetLocation', None,x
			, y)

	def GetLoftPoint(self, x=pythoncom.Missing, y=pythoncom.Missing):
		'�������� ���������� ����� � ��������� ������ ��� �������� �� ��������.'
		return self._ApplyTypes_(7, 1, (11, 0), ((16389, 2), (16389, 2)), 'GetLoftPoint', None,x
			, y)

	def GetPlane(self):
		'�������� ������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlane', None)
		return ret

	def GetSurface(self):
		'�������� ��������� �������������� �����������.'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurface', None)
		return ret

	def SetLocation(self, x=0.0, y=0.0):
		'�������� �������� ������� ��������� ������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((5, 48), (5, 48)),x
			, y)

	def SetLoftPoint(self, x=0.0, y=0.0):
		'�������� ���������� ����� � ��������� ������ ��� �������� �� ��������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((5, 48), (5, 48)),x
			, y)

	def SetPlane(self, plane=defaultNamedNotOptArg):
		'�������� ������� ��������� ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),plane
			)

	def UserSetPlacement(self, prompt=''):
		'������� �������� �������������� ������.'
		return self._ApplyTypes_(8, 1, (11, 32), ((8, 48),), 'UserSetPlacement', None,prompt
			)

	_prop_map_get_ = {
		"angle": (1, 2, (5, 0), (), "angle", None),
	}
	_prop_map_put_ = {
		"angle" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSnapInfo(DispatchBaseClass):
	'��������� ���������� � ������� ��������'
	CLSID = IID('{FEC5FF26-3F47-49B2-ABAE-5563A4D7AD94}')
	coclass_clsid = None

	def GetObject1(self):
		'������ ������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def GetObject2(self):
		'������ ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	def GetPoint(self, x=pythoncom.Missing, y=pythoncom.Missing):
		'����� ��������'
		return self._ApplyTypes_(5, 1, (11, 0), ((16389, 2), (16389, 2)), 'GetPoint', None,x
			, y)

	def GetSnapType1(self):
		'��� �������� �� ������ �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetSnapType2(self):
		'��� �������� �� ������ �������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSnapOptions(DispatchBaseClass):
	'��������� ���������� �������� � ����������� ���������.'
	CLSID = IID('{FBCC5B9C-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5B9E-996C-11D6-8732-00C0262CDD2C}')

	def GetCommonOptValue(self, val=defaultNamedNotOptArg):
		'���������� �������� �������� ������� � ������ ����������� ��������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((3, 0),),val
			)

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), (),)

	def SetCommonOptValue(self, val=defaultNamedNotOptArg, state=defaultNamedNotOptArg):
		'�������� �������� �������� ������� � ������ ����������� ��������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), ((3, 0), (11, 0)),val
			, state)

	_prop_map_get_ = {
		"angSnap": (8, 2, (11, 0), (), "angSnap", None),
		"angleStep": (11, 2, (5, 0), (), "angleStep", None),
		"commonOpt": (10, 2, (3, 0), (), "commonOpt", None),
		"grid": (6, 2, (11, 0), (), "grid", None),
		"intersect": (3, 2, (11, 0), (), "intersect", None),
		"localSnap": (12, 2, (2, 0), (), "localSnap", None),
		"nearestMiddle": (2, 2, (11, 0), (), "nearestMiddle", None),
		"nearestPoint": (1, 2, (11, 0), (), "nearestPoint", None),
		"normalToCurve": (5, 2, (11, 0), (), "normalToCurve", None),
		"pointOnCurve": (9, 2, (11, 0), (), "pointOnCurve", None),
		"tangentToCurve": (4, 2, (11, 0), (), "tangentToCurve", None),
		"xyAlign": (7, 2, (11, 0), (), "xyAlign", None),
	}
	_prop_map_put_ = {
		"angSnap" : ((8, LCID, 4, 0),()),
		"angleStep" : ((11, LCID, 4, 0),()),
		"commonOpt" : ((10, LCID, 4, 0),()),
		"grid" : ((6, LCID, 4, 0),()),
		"intersect" : ((3, LCID, 4, 0),()),
		"localSnap" : ((12, LCID, 4, 0),()),
		"nearestMiddle" : ((2, LCID, 4, 0),()),
		"nearestPoint" : ((1, LCID, 4, 0),()),
		"normalToCurve" : ((5, LCID, 4, 0),()),
		"pointOnCurve" : ((9, LCID, 4, 0),()),
		"tangentToCurve" : ((4, LCID, 4, 0),()),
		"xyAlign" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpcColumnParam(DispatchBaseClass):
	'��������� ���������� ��� ������� ������������.'
	CLSID = IID('{4FD7CE8A-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CE8C-9968-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"block": (3, 2, (3, 0), (), "block", None),
		"columnType": (1, 2, (3, 0), (), "columnType", None),
		"ispoln": (2, 2, (3, 0), (), "ispoln", None),
		"name": (5, 2, (8, 0), (), "name", None),
		"typeVal": (4, 2, (3, 0), (), "typeVal", None),
	}
	_prop_map_put_ = {
		"block" : ((3, LCID, 4, 0),()),
		"columnType" : ((1, LCID, 4, 0),()),
		"ispoln" : ((2, LCID, 4, 0),()),
		"name" : ((5, LCID, 4, 0),()),
		"typeVal" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpcDescrParam(DispatchBaseClass):
	'C�������� ���������� �������� ������������.'
	CLSID = IID('{4FD7CEA5-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CEA7-9968-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"layoutName": (1, 2, (8, 0), (), "layoutName", None),
		"spcName": (3, 2, (8, 0), (), "spcName", None),
		"styleId": (2, 2, (3, 0), (), "styleId", None),
	}
	_prop_map_put_ = {
		"layoutName" : ((1, LCID, 4, 0),()),
		"spcName" : ((3, LCID, 4, 0),()),
		"styleId" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpcDocument(DispatchBaseClass):
	'�������� ������������.'
	CLSID = IID('{51E74521-9A3A-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{51E74523-9A3A-11D6-95CE-00C0262D30E3}')

	# Result is of type SpcDocumentNotify
	def GetSpcDocumentNotify(self):
		'�������� �������� ������� ��� ��������� ������������.'
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (13, 0), (),)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetSpcDocumentNotify', '{DC32EB43-4615-4717-8C67-48875A357B06}')
		return ret

	def GetSpecification(self):
		'������� ��������� ��� ������ � ��������� ������������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSpecification', None)
		return ret

	def GetStamp(self):
		'������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetStamp', None)
		return ret

	def GetStampEx(self, SheetNumb=defaultNamedNotOptArg):
		'������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), ((3, 0),),SheetNumb
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetStampEx', None)
		return ret

	def RasterFormatParam(self):
		'�������� ��������� �� ��������� ���������� ���������� �������.'
		ret = self._oleobj_.InvokeTypes(16, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RasterFormatParam', None)
		return ret

	def SaveAsToRasterFormat(self, fileName=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'��������� �������� � ��������� ������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), ((8, 0), (9, 0)),fileName
			, par)

	def SaveAsToUncompressedRasterFormat(self, fileName=defaultNamedNotOptArg, rasterPar=defaultNamedNotOptArg):
		'��������� �������� ��� ������ � ��������� ������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), ((8, 0), (9, 0)),fileName
			, rasterPar)

	def ksCloseDocument(self):
		'������� ��������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	def ksCreateDocument(self, par=defaultNamedNotOptArg):
		'������� ��������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((9, 0),),par
			)

	def ksDeleteObj(self, ref=defaultNamedNotOptArg):
		'������� �� ��������� ������������ ������ � ���������� ref.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((3, 0),),ref
			)

	def ksExistObj(self, ref=defaultNamedNotOptArg):
		'���������, ���������� �� ������ � ���������� ref.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((3, 0),),ref
			)

	def ksGetObjParam(self, ref=defaultNamedNotOptArg, param=defaultNamedNotOptArg, parType=-1):
		'�������� ��������� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((3, 0), (9, 0), (3, 48)),ref
			, param, parType)

	def ksGetSpcDocumentPagesCount(self):
		'��� ��������� ������������ �������� ���������� ������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), (),)

	def ksGetSpcSheetSB(self):
		'�������� ������������ ������ ������ ���������� ������� (CHAR_STR_ARR), ������������ � ������������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ksGetSpcSheetSB', None)
		return ret

	def ksOpenDocument(self, nameDoc=defaultNamedNotOptArg, regim=defaultNamedNotOptArg):
		'������� ��������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((8, 0), (2, 0)),nameDoc
			, regim)

	def ksSaveDocument(self, fileName=defaultNamedNotOptArg):
		'��������� ��������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((8, 0),),fileName
			)

	def ksSaveDocumentEx(self, fileName=defaultNamedNotOptArg, SaveMode=defaultNamedNotOptArg):
		'��������� ��������.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((8, 0), (3, 0)),fileName
			, SaveMode)

	def ksSaveToDXF(self, DXFFileName=defaultNamedNotOptArg):
		'��������� �������� � ������� DXF.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), ((8, 0),),DXFFileName
			)

	def ksSetObjParam(self, ref=defaultNamedNotOptArg, param=defaultNamedNotOptArg, parType=-1):
		'������������� ����� ��������� �������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((3, 0), (9, 0), (3, 48)),ref
			, param, parType)

	def ksSetSpcSheetSB(self, arr=defaultNamedNotOptArg):
		'�������� ������������ ������ ������ ���������� �������, ������������ � ������������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), ((9, 0),),arr
			)

	_prop_map_get_ = {
		"reference": (1, 2, (3, 0), (), "reference", None),
	}
	_prop_map_put_ = {
		"reference" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpcDocumentNotify:
	'������� ��� ��������� ������������.'
	CLSID = CLSID_Sink = IID('{1BD030F4-4058-4A86-9F4F-1AEEF8BE8D23}')
	coclass_clsid = IID('{DC32EB43-4615-4717-8C67-48875A357B06}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnDocumentBeginAdd",
		        2 : "OnDocumentAdd",
		        3 : "OnDocumentBeginRemove",
		        4 : "OnDocumentRemove",
		        5 : "OnSpcStyleBeginChange",
		        6 : "OnSpcStyleChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnDocumentBeginAdd(self):
#		'������ ���������� ��������� ���������� �������.'
#	def OnDocumentAdd(self, docName=defaultNamedNotOptArg):
#		'���������� ��������� ���������� �������.'
#	def OnDocumentBeginRemove(self, docName=defaultNamedNotOptArg):
#		'������ �������� ��������� ���������� �������.'
#	def OnDocumentRemove(self, docName=defaultNamedNotOptArg):
#		'�������� ��������� ���������� �������.'
#	def OnSpcStyleBeginChange(self, libName=defaultNamedNotOptArg, numb=defaultNamedNotOptArg):
#		'������ ��������� ����� ������������.'
#	def OnSpcStyleChange(self, libName=defaultNamedNotOptArg, numb=defaultNamedNotOptArg):
#		'����� ������������ ���������.'


class ksSpcObjParam(DispatchBaseClass):
	'C�������� ���������� ������� ������������.'
	CLSID = IID('{4FD7CEAB-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CEAD-9968-11D6-95CE-00C0262D30E3}')

	def GetDocArr(self):
		'������ ������������ ������ DOC_SPCOBJ_ARR �������� ���������� ������������� ���������� � ������� ������������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDocArr', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), (),)

	def SetDocArr(self, docArr=defaultNamedNotOptArg):
		'���������� ������������ ������ DOC_SPCOBJ_ARR �������� ���������� ������������� ���������� � ������� ������������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((9, 0),),docArr
			)

	_prop_map_get_ = {
		"blockNumber": (5, 2, (3, 0), (), "blockNumber", None),
		"draw": (12, 2, (2, 0), (), "draw", None),
		"firstOnSheet": (8, 2, (2, 0), (), "firstOnSheet", None),
		"ispoln": (14, 2, (2, 0), (), "ispoln", None),
		"numbSubSection": (6, 2, (3, 0), (), "numbSubSection", None),
		"posInc": (10, 2, (2, 0), (), "posInc", None),
		"posNotDraw": (13, 2, (2, 0), (), "posNotDraw", None),
		"First": (11, 2, (2, 0), (), "First", None),
		"insFrgType": (9, 2, (2, 0), (), "insFrgType", None),
		"numbSection": (4, 2, (3, 0), (), "numbSection", None),
		"subSectionName": (7, 2, (8, 0), (), "subSectionName", None),
		"typeObj": (3, 2, (3, 0), (), "typeObj", None),
	}
	_prop_map_put_ = {
		"blockNumber" : ((5, LCID, 4, 0),()),
		"draw" : ((12, LCID, 4, 0),()),
		"firstOnSheet" : ((8, LCID, 4, 0),()),
		"ispoln" : ((14, LCID, 4, 0),()),
		"numbSubSection" : ((6, LCID, 4, 0),()),
		"posInc" : ((10, LCID, 4, 0),()),
		"posNotDraw" : ((13, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpcObjectNotify:
	'������� ��� ������� ������������.'
	CLSID = CLSID_Sink = IID('{AC5004D1-C240-41FC-AB84-7EB5C793AE7F}')
	coclass_clsid = IID('{02CBC423-BC8C-40DE-BE65-03A67DF1C834}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnBeginDelete",
		        2 : "OnDelete",
		        3 : "OnCellDblClick",
		        4 : "OnCellBeginEdit",
		        5 : "OnChangeCurrent",
		        6 : "OnDocumentBeginAdd",
		        7 : "OnDocumentAdd",
		        8 : "OnDocumentRemove",
		        9 : "OnBeginGeomChange",
		       10 : "OnGeomChange",
		       11 : "OnBeginProcess",
		       12 : "OnEndProcess",
		       13 : "OnCreateObject",
		       14 : "OnUpdateObject",
		       15 : "OnBeginCopy",
		       16 : "Oncopy",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnBeginDelete(self, objRef=defaultNamedNotOptArg):
#		'������ �������� �������.'
#	def OnDelete(self, objRef=defaultNamedNotOptArg):
#		'�������� �������.'
#	def OnCellDblClick(self, objRef=defaultNamedNotOptArg, number=defaultNamedNotOptArg):
#		'������� ���� � ������ .'
#	def OnCellBeginEdit(self, objRef=defaultNamedNotOptArg, number=defaultNamedNotOptArg):
#		'������ �������������� � ������ .'
#	def OnChangeCurrent(self, objRef=defaultNamedNotOptArg):
#		'��������� ������� ������.'
#	def OnDocumentBeginAdd(self, objRef=defaultNamedNotOptArg):
#		'������ ���������� ���������.'
#	def OnDocumentAdd(self, objRef=defaultNamedNotOptArg, docName=defaultNamedNotOptArg):
#		'���������� ��������� � ������� ��.'
#	def OnDocumentRemove(self, objRef=defaultNamedNotOptArg, docName=defaultNamedNotOptArg):
#		'�������� ��������� �� ������� ��.'
#	def OnBeginGeomChange(self, objRef=defaultNamedNotOptArg):
#		'������ ������� ��������� ������� ��.'
#	def OnGeomChange(self, objRef=defaultNamedNotOptArg):
#		'��������� ������� �� ����������.'
#	def OnBeginProcess(self, pType=defaultNamedNotOptArg, objRef=defaultNamedNotOptArg):
#		'������ ���������������������� �������.false - ��������� �������'
#	def OnEndProcess(self, pType=defaultNamedNotOptArg):
#		'����� ���������������������� �������.'
#	def OnCreateObject(self, objRef=defaultNamedNotOptArg):
#		'�������� �������.'
#	def OnUpdateObject(self, objRef=defaultNamedNotOptArg):
#		'�������������� �������.'
#	def OnBeginCopy(self, objRef=defaultNamedNotOptArg):
#		'������ ����������� �������, false - ��������� �����������.'
#	def Oncopy(self, objRef=defaultNamedNotOptArg):
#		'����������� �������.'


class ksSpcStyleColumnParam(DispatchBaseClass):
	'��������� ���������� ����� ������� ������� ������������.'
	CLSID = IID('{4FD7CE93-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CE95-9968-11D6-95CE-00C0262D30E3}')

	def GetAdditionalParam(self):
		'�������� ��������� �� ��������� �������������� ���������� � �������� �������.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAdditionalParam', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"columnType": (2, 2, (3, 0), (), "columnType", None),
		"createSum": (5, 2, (2, 0), (), "createSum", None),
		"edit": (4, 2, (2, 0), (), "edit", None),
		"ispoln": (3, 2, (3, 0), (), "ispoln", None),
		"linkId": (9, 2, (3, 0), (), "linkId", None),
		"multiplyToCount": (6, 2, (2, 0), (), "multiplyToCount", None),
		"nameColumn": (1, 2, (8, 0), (), "nameColumn", None),
		"textDn": (8, 2, (2, 0), (), "textDn", None),
		"typeVal": (10, 2, (3, 0), (), "typeVal", None),
		"useForSectionTitle": (7, 2, (2, 0), (), "useForSectionTitle", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpcStyleParam(DispatchBaseClass):
	'C�������� ���������� ����� ������������.'
	CLSID = IID('{4FD7CEA2-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CEA4-9968-11D6-95CE-00C0262D30E3}')

	def GetArrAdditionalColumn(self):
		'������ ������ �������������� ������� SpcStyleColumnParam.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetArrAdditionalColumn', None)
		return ret

	def GetArrColumn(self):
		'������ ������ ������� ��� ������������ -������������� �������� SpcStyleColumnParam.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetArrColumn', None)
		return ret

	def GetArrSection(self):
		'������ ������ �������� ��� ������������ SpcStyleSectionParam.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetArrSection', None)
		return ret

	def GetSheetParam(self):
		'�������� ��������� ���������� ����� ���������.'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSheetParam', None)
		return ret

	def GetTuning(self):
		'������ ������������� ���������, ��������� � ���������� ������������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTuning', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"layoutName1": (1, 2, (8, 0), (), "layoutName1", None),
		"layoutName2": (2, 2, (8, 0), (), "layoutName2", None),
		"sectionOn": (6, 2, (2, 0), (), "sectionOn", None),
		"shtType1": (3, 2, (3, 0), (), "shtType1", None),
		"shtType2": (4, 2, (3, 0), (), "shtType2", None),
		"type": (7, 2, (2, 0), (), "type", None),
		"variant": (5, 2, (2, 0), (), "variant", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpcStyleSectionParam(DispatchBaseClass):
	'��������� ���������� ����� ������a ������������.'
	CLSID = IID('{4FD7CE96-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CE98-9968-11D6-95CE-00C0262D30E3}')

	def GetArrAdditionalColumn(self):
		'�������� ������ �������� ���������� ����� ��� ���.�������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetArrAdditionalColumn', None)
		return ret

	def GetArrColumn(self):
		'�������� ������ �������� ���������� ����� ������� SpcStyleColumnParam.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetArrColumn', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"dataType": (5, 2, (2, 0), (), "dataType", None),
		"number": (2, 2, (3, 0), (), "number", None),
		"sectionName": (1, 2, (8, 0), (), "sectionName", None),
		"sortColumnType": (3, 2, (3, 0), (), "sortColumnType", None),
		"sortIspoln": (4, 2, (3, 0), (), "sortIspoln", None),
		"sortType": (6, 2, (3, 0), (), "sortType", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpcSubSectionParam(DispatchBaseClass):
	'C�������� ���������� ���������� ������������.'
	CLSID = IID('{4FD7CE99-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CE9B-9968-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"name": (1, 2, (8, 0), (), "name", None),
		"number": (2, 2, (3, 0), (), "number", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpcTuningSectionParam(DispatchBaseClass):
	'C�������� ���������� ��������� ������� ������������.'
	CLSID = IID('{4FD7CE9C-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CE9E-9968-11D6-95CE-00C0262D30E3}')

	def GetArrSubSection(self):
		'������ ������ ���������� ����������� SpcSubSectionParam ��� �������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetArrSubSection', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"firstOnSheet": (5, 2, (2, 0), (), "firstOnSheet", None),
		"geometryOn": (2, 2, (2, 0), (), "geometryOn", None),
		"number": (7, 2, (3, 0), (), "number", None),
		"positionOn": (3, 2, (2, 0), (), "positionOn", None),
		"rezervCount": (6, 2, (3, 0), (), "rezervCount", None),
		"sortOn": (4, 2, (2, 0), (), "sortOn", None),
		"subsectionOn": (1, 2, (2, 0), (), "subsectionOn", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpcTuningStyleParam(DispatchBaseClass):
	'C�������� ���������� ����� �������� ������������.'
	CLSID = IID('{4FD7CE9F-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CEA1-9968-11D6-95CE-00C0262D30E3}')

	def GetArrSection(self):
		'������ ������ �������� �������� ��� ������������ SpcTuningSectionParam.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetArrSection', None)
		return ret

	def GetObjectTextStyle(self):
		'������ ����� ������ ������� ������������.'
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTextStyle', None)
		return ret

	def GetSectionTextStyleFirst(self):
		'������ ����� ������ ��������� ������� - ������ ������.'
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSectionTextStyleFirst', None)
		return ret

	def GetSectionTextStyleNext(self):
		'������ ����� ������ ��������� ������� - ����������� ������.'
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSectionTextStyleNext', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), (),)

	def SetArrSection(self, arr=defaultNamedNotOptArg):
		'�������� ������ �������� �������� ��� ������������ SpcTuningSectionParam.'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (11, 0), ((9, 0),),arr
			)

	def SetObjectTextStyle(self, style=defaultNamedNotOptArg):
		'�������� ����� ������ ������� ������������.'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (11, 0), ((9, 0),),style
			)

	def SetSectionTextStyleFirst(self, style=defaultNamedNotOptArg):
		'�������� ����� ������ ��������� ������� - ������ ������.'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (11, 0), ((9, 0),),style
			)

	def SetSectionTextStyleNext(self, style=defaultNamedNotOptArg):
		'�������� ����� ������ ��������� ������� - ����������� ������.'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (11, 0), ((9, 0),),style
			)

	_prop_map_get_ = {
		"blocOnNewPage": (15, 2, (2, 0), (), "blocOnNewPage", None),
		"copySpcObjOnCopyGeometry": (30, 2, (2, 0), (), "copySpcObjOnCopyGeometry", None),
		"countBlock": (18, 2, (2, 0), (), "countBlock", None),
		"countIspoln": (17, 2, (2, 0), (), "countIspoln", None),
		"delSpcObjOnDelGeometry": (29, 2, (2, 0), (), "delSpcObjOnDelGeometry", None),
		"disableEmptyBlockStr": (11, 2, (2, 0), (), "disableEmptyBlockStr", None),
		"disableEmptyStr": (8, 2, (2, 0), (), "disableEmptyStr", None),
		"geometryDel": (5, 2, (2, 0), (), "geometryDel", None),
		"grToSP": (1, 2, (2, 0), (), "grToSP", None),
		"insertDash": (10, 2, (2, 0), (), "insertDash", None),
		"insertNull": (9, 2, (2, 0), (), "insertNull", None),
		"ispolnMarkFull": (14, 2, (2, 0), (), "ispolnMarkFull", None),
		"ispolnOn": (13, 2, (2, 0), (), "ispolnOn", None),
		"massCalc": (7, 2, (2, 0), (), "massCalc", None),
		"positionCalc": (4, 2, (2, 0), (), "positionCalc", None),
		"positionDel": (6, 2, (2, 0), (), "positionDel", None),
		"predefinedTextFileName": (19, 2, (8, 0), (), "predefinedTextFileName", None),
		"showInfoByDetBlock": (12, 2, (2, 0), (), "showInfoByDetBlock", None),
		"showSectionName": (3, 2, (2, 0), (), "showSectionName", None),
		"userTextStyle": (16, 2, (2, 0), (), "userTextStyle", None),
		"zoneCalc": (2, 2, (2, 0), (), "zoneCalc", None),
	}
	_prop_map_put_ = {
		"blocOnNewPage" : ((15, LCID, 4, 0),()),
		"copySpcObjOnCopyGeometry" : ((30, LCID, 4, 0),()),
		"countBlock" : ((18, LCID, 4, 0),()),
		"countIspoln" : ((17, LCID, 4, 0),()),
		"delSpcObjOnDelGeometry" : ((29, LCID, 4, 0),()),
		"disableEmptyBlockStr" : ((11, LCID, 4, 0),()),
		"disableEmptyStr" : ((8, LCID, 4, 0),()),
		"geometryDel" : ((5, LCID, 4, 0),()),
		"grToSP" : ((1, LCID, 4, 0),()),
		"insertDash" : ((10, LCID, 4, 0),()),
		"insertNull" : ((9, LCID, 4, 0),()),
		"ispolnMarkFull" : ((14, LCID, 4, 0),()),
		"ispolnOn" : ((13, LCID, 4, 0),()),
		"massCalc" : ((7, LCID, 4, 0),()),
		"positionCalc" : ((4, LCID, 4, 0),()),
		"positionDel" : ((6, LCID, 4, 0),()),
		"predefinedTextFileName" : ((19, LCID, 4, 0),()),
		"showInfoByDetBlock" : ((12, LCID, 4, 0),()),
		"showSectionName" : ((3, LCID, 4, 0),()),
		"userTextStyle" : ((16, LCID, 4, 0),()),
		"zoneCalc" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpecRoughParam(DispatchBaseClass):
	'��������� ��� ����������� ����������� �������������.'
	CLSID = IID('{364521A3-94B5-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{364521A5-94B5-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"s": (4, 2, (8, 0), (), "s", None),
		"sign": (2, 2, (2, 0), (), "sign", None),
		"style": (1, 2, (3, 0), (), "style", None),
		"t": (3, 2, (11, 0), (), "t", None),
	}
	_prop_map_put_ = {
		"s" : ((4, LCID, 4, 0),()),
		"sign" : ((2, LCID, 4, 0),()),
		"style" : ((1, LCID, 4, 0),()),
		"t" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpecification(DispatchBaseClass):
	'��������� ������ � ��������� ������������.'
	CLSID = IID('{51E74524-9A3A-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{51E74526-9A3A-11D6-95CE-00C0262D30E3}')

	def D3GetSpcObjForGeomWithLimit(self, nameLib=defaultNamedNotOptArg, numb=defaultNamedNotOptArg, part=defaultNamedNotOptArg, First=defaultNamedNotOptArg
			, section=defaultNamedNotOptArg, attrTypeNumb=defaultNamedNotOptArg):
		'�������� ��������� ������� �� �� 3D ��������� � ������������� �� ������ ������� � ���� ��������.'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (3, 0), ((8, 0), (3, 0), (9, 0), (2, 0), (2, 0), (5, 0)),nameLib
			, numb, part, First, section, attrTypeNumb
			)

	def D3GetSpcObjGeometry(self, spcObj=defaultNamedNotOptArg):
		'�������� 3D ��������� ������������ � ������� ������������'
		ret = self._oleobj_.InvokeTypes(34, LCID, 1, (9, 0), ((3, 0),),spcObj
			)
		if ret is not None:
			ret = Dispatch(ret, 'D3GetSpcObjGeometry', None)
		return ret

	def D3SpcIncludePart(self, part=defaultNamedNotOptArg, fillTexts=defaultNamedNotOptArg):
		'���������� 3D ��������� � ������� ��.'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (11, 0), ((9, 0), (11, 0)),part
			, fillTexts)

	# Result is of type SpcObjectNotify
	def GetSpcObjectNotify(self, objType=defaultNamedNotOptArg):
		'�������� �������� ������� ��� ������� ������������.'
		ret = self._oleobj_.InvokeTypes(37, LCID, 1, (13, 0), ((3, 0),),objType
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetSpcObjectNotify', '{02CBC423-BC8C-40DE-BE65-03A67DF1C834}')
		return ret

	def ksAddSpcDescription(self, param=defaultNamedNotOptArg):
		'��� ��������� pDoc ��������� �������� ������������.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (3, 0), ((9, 0),),param
			)

	def ksDeleteSpcDescription(self, index=defaultNamedNotOptArg):
		'��� ��������� pDoc ������� ��������� �������� ������������ � �������� index.'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (3, 0), ((3, 0),),index
			)

	def ksEditWindowSpcObject(self, obj=defaultNamedNotOptArg):
		'�������������� ������� ������������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((3, 0),),obj
			)

	def ksGetCurrentSpcObject(self):
		'��������  ���������  �������� ������� �� ( ����������� ��� �������������� � ������� �� ). ������� �������� ��� ������� ������ ��.'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (3, 0), (),)

	def ksGetSpcColumnNumb(self, spcObj=defaultNamedNotOptArg, columnType=defaultNamedNotOptArg, ispoln=defaultNamedNotOptArg, block=defaultNamedNotOptArg):
		'��� ������� ������� ������������ �� ���� ������� SPC_CLM_FORMAT...SPC_CLM_USER, ������ ���������� ������� ���� � ������ ����� �������� ����� �������.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), ((3, 0), (3, 0), (3, 0), (3, 0)),spcObj
			, columnType, ispoln, block)

	def ksGetSpcColumnType(self, spcObj=defaultNamedNotOptArg, colNumb=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'�� ������ ������� ��� ������� ������� ������������ �������� ��������� �������.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((3, 0), (3, 0), (9, 0)),spcObj
			, colNumb, par)

	def ksGetSpcDescription(self, index=defaultNamedNotOptArg, param=defaultNamedNotOptArg, state=pythoncom.Missing):
		'B��������� ��������� �������� ������������ ��� ��������� pDoc.'
		return self._ApplyTypes_(22, 1, (3, 0), ((3, 1), (9, 1), (16395, 2)), 'ksGetSpcDescription', None,index
			, param, state)

	def ksGetSpcObjForGeom(self, nameLib=defaultNamedNotOptArg, numb=defaultNamedNotOptArg, obj=defaultNamedNotOptArg, equal=defaultNamedNotOptArg
			, First=defaultNamedNotOptArg):
		'�������� ��������� ������� �� �� ��������� ��� �������� ������������ ���������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), ((8, 0), (3, 0), (3, 0), (2, 0), (2, 0)),nameLib
			, numb, obj, equal, First)

	def ksGetSpcObjForGeomWithLimit(self, nameLib=defaultNamedNotOptArg, numb=defaultNamedNotOptArg, obj=defaultNamedNotOptArg, equal=defaultNamedNotOptArg
			, First=defaultNamedNotOptArg, section=defaultNamedNotOptArg, attrTypeNumb=defaultNamedNotOptArg):
		'�������� ��������� ������� �� �� ��������� � ������������� �� ������ ������� � ���� ��������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((8, 0), (3, 0), (3, 0), (2, 0), (2, 0), (3, 0), (5, 0)),nameLib
			, numb, obj, equal, First, section
			, attrTypeNumb)

	def ksGetSpcObjGeometry(self, spcObj=defaultNamedNotOptArg):
		'�������� ��������� ������������ � ������� ������������'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (3, 0), ((3, 0),),spcObj
			)

	def ksGetSpcObjGeometryEx(self, spcObj=defaultNamedNotOptArg, geomMode=defaultNamedNotOptArg):
		'�������� ��������� ������������ � ������� ������������.'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (3, 0), ((3, 0), (3, 0)),spcObj
			, geomMode)

	def ksGetSpcObject(self, objNumb=defaultNamedNotOptArg):
		'������ ������ ������������ �� ������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((5, 0),),objNumb
			)

	def ksGetSpcObjectAttributeNumber(self, spcObj=defaultNamedNotOptArg):
		'�������� ����� �������� ������� ������������.'
		return self._oleobj_.InvokeTypes(41, LCID, 1, (5, 0), ((3, 0),),spcObj
			)

	def ksGetSpcObjectColumnText(self, spcObj=defaultNamedNotOptArg, columnType=defaultNamedNotOptArg, ispoln=defaultNamedNotOptArg, block=defaultNamedNotOptArg):
		'������ ��������� ������ ��� ������������� ���� ������� � ����������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(16, LCID, 1, (8, 0), ((3, 0), (3, 0), (3, 0), (3, 0)),spcObj
			, columnType, ispoln, block)

	def ksGetSpcObjectColumnTextAlign(self, spcObj=defaultNamedNotOptArg, columnNumber=defaultNamedNotOptArg, lineIndex=defaultNamedNotOptArg):
		'�������� ������������ ������� ������� ������� ������������.'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (3, 0), ((3, 0), (3, 0), (3, 0)),spcObj
			, columnNumber, lineIndex)

	def ksGetSpcObjectColumnTextEx(self, spcObj=defaultNamedNotOptArg, columnType=defaultNamedNotOptArg, ispoln=defaultNamedNotOptArg, block=defaultNamedNotOptArg):
		'������ ����� ��� ������������� ���� ������� � ����������.'
		ret = self._oleobj_.InvokeTypes(35, LCID, 1, (9, 0), ((3, 0), (3, 0), (3, 0), (3, 0)),spcObj
			, columnType, ispoln, block)
		if ret is not None:
			ret = Dispatch(ret, 'ksGetSpcObjectColumnTextEx', None)
		return ret

	def ksGetSpcObjectNumber(self, spcObj=defaultNamedNotOptArg):
		'������ ���������� ����� ������� ������������.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (5, 0), ((3, 0),),spcObj
			)

	def ksGetSpcObjectSummaryCount(self, spcObj=defaultNamedNotOptArg, ispoln=defaultNamedNotOptArg, blockNumber=defaultNamedNotOptArg):
		'��������� ���������� ��� ���������� ��������.'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (5, 0), ((3, 0), (3, 0), (3, 0)),spcObj
			, ispoln, blockNumber)

	def ksGetSpcPerformanceName(self, index=defaultNamedNotOptArg, ispoln=defaultNamedNotOptArg, block=defaultNamedNotOptArg):
		'�������� ��� ����������.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(45, LCID, 1, (8, 0), ((3, 0), (3, 0), (3, 0)),index
			, ispoln, block)

	def ksGetSpcPropertyFill(self, spcObj=defaultNamedNotOptArg):
		'�������� ���� ���������������� �� ���������� ����������'
		return self._oleobj_.InvokeTypes(49, LCID, 1, (11, 0), ((3, 0),),spcObj
			)

	def ksGetSpcSectionName(self, spcObj=defaultNamedNotOptArg):
		'�������� �������� ������� ������������ �� ��������� ������� ��.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(12, LCID, 1, (8, 0), ((3, 0),),spcObj
			)

	def ksGetSpcStyleParam(self, nameLib=defaultNamedNotOptArg, numb=defaultNamedNotOptArg, par=defaultNamedNotOptArg, tPar=defaultNamedNotOptArg):
		'�������� ��������� ��� ����� ������������ � ������� numb �� ���������� nameLib.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), ((8, 0), (3, 0), (9, 0), (3, 0)),nameLib
			, numb, par, tPar)

	def ksGetSpcTableColumn(self, nameLib=defaultNamedNotOptArg, numb=defaultNamedNotOptArg, additioanalCol=defaultNamedNotOptArg):
		'�������� ���������� ������� ��� ����� ������������ � ������� ���������.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), ((8, 0), (3, 0), (2, 0)),nameLib
			, numb, additioanalCol)

	def ksGetTuningSpcStyleParam(self, index=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'��������� ���������� �������� ������������ ���������'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (3, 0), ((3, 0), (9, 0)),index
			, par)

	def ksGetWidthColumnSpc(self, numColumn=defaultNamedNotOptArg, cellOrText=defaultNamedNotOptArg):
		'������ ������ �������.'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (5, 0), ((3, 0), (11, 0)),numColumn
			, cellOrText)

	def ksSetCurrentSpcObject(self, spcObj=defaultNamedNotOptArg, index=defaultNamedNotOptArg):
		'���������� ������� ������ ��, ���� �� ��������� �������, ���� �� ������� �������. ������� �������� ��� ������� ������ ��.'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (3, 0), ((3, 0), (3, 0)),spcObj
			, index)

	def ksSetSpcDescription(self, index=defaultNamedNotOptArg, param=defaultNamedNotOptArg, state=defaultNamedNotOptArg):
		'��� ��������� pDoc �������� ��������� �������� ������������ � �������� index.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (3, 0), ((3, 0), (9, 0), (2, 0)),index
			, param, state)

	def ksSetSpcObjectAttributeNumber(self, spcObj=defaultNamedNotOptArg, attrNumber=defaultNamedNotOptArg):
		'���������� ����� �������� ������� ������������.'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (11, 0), ((3, 0), (5, 0)),spcObj
			, attrNumber)

	def ksSetSpcObjectColumnText(self, columnType=defaultNamedNotOptArg, ispoln=defaultNamedNotOptArg, block=defaultNamedNotOptArg, str=defaultNamedNotOptArg):
		'�������� ����� � ������������� ���� ������� � ����������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((3, 0), (3, 0), (3, 0), (8, 0)),columnType
			, ispoln, block, str)

	def ksSetSpcObjectColumnTextAlign(self, spcObj=defaultNamedNotOptArg, columnNumber=defaultNamedNotOptArg, lineIndex=defaultNamedNotOptArg, align=defaultNamedNotOptArg):
		'���������� ������������ ������� ������� ������� ������������.'
		return self._oleobj_.InvokeTypes(39, LCID, 1, (11, 0), ((3, 0), (3, 0), (3, 0), (3, 0)),spcObj
			, columnNumber, lineIndex, align)

	def ksSetSpcObjectColumnTextEx(self, columnType=defaultNamedNotOptArg, ispoln=defaultNamedNotOptArg, block=defaultNamedNotOptArg, arr=defaultNamedNotOptArg):
		'�������� ����� � ������������� ���� ������� � ����������.'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (3, 0), ((3, 0), (3, 0), (3, 0), (9, 0)),columnType
			, ispoln, block, arr)

	def ksSetSpcObjectMaterial(self, spcObj=defaultNamedNotOptArg, material=defaultNamedNotOptArg, density=defaultNamedNotOptArg):
		'���������� �������� � ������ ������������ � ��������� � ��� ��������.'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (11, 0), ((3, 0), (8, 0), (5, 0)),spcObj
			, material, density)

	def ksSetSpcPerformanceName(self, index=defaultNamedNotOptArg, ispoln=defaultNamedNotOptArg, block=defaultNamedNotOptArg, name=defaultNamedNotOptArg):
		'���������� ��� ����������.'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (11, 0), ((3, 0), (3, 0), (3, 0), (8, 0)),index
			, ispoln, block, name)

	def ksSetSpcPropertyFill(self, spcObj=defaultNamedNotOptArg, val=defaultNamedNotOptArg):
		'���������� ���� ���������������� �� ���������� ����������'
		return self._oleobj_.InvokeTypes(50, LCID, 1, (11, 0), ((3, 0), (3, 0)),spcObj
			, val)

	def ksSetTuningSpcStyleParam(self, index=defaultNamedNotOptArg, par=defaultNamedNotOptArg):
		'��������� ���������� �������� ������������ ���������'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (3, 0), ((3, 0), (9, 0)),index
			, par)

	def ksSpcChangeValue(self, colNumb=defaultNamedNotOptArg, itemNumb=defaultNamedNotOptArg, userPars=defaultNamedNotOptArg, typeVal=defaultNamedNotOptArg):
		'������� ������ ������������ � ����������� ��������� ��� � ��.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), ((3, 0), (3, 0), (9, 0), (2, 0)),colNumb
			, itemNumb, userPars, typeVal)

	def ksSpcCount(self, ispoln=defaultNamedNotOptArg, sCount=defaultNamedNotOptArg):
		'���������� ���������� ������� ��� ������������� ����������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((2, 0), (8, 0)),ispoln
			, sCount)

	def ksSpcDocLinksClear(self, doc=defaultNamedNotOptArg):
		'������� ������ � ����������-���������� ������� ������������.'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (11, 0), ((3, 0),),doc
			)

	def ksSpcDocLinksClearEx(self, doc=defaultNamedNotOptArg, mode=defaultNamedNotOptArg):
		'������� ������ � ����������-���������� ������� ������������, mode = 1 - ���, 0 - �� ���������.'
		return self._oleobj_.InvokeTypes(48, LCID, 1, (11, 0), ((3, 0), (3, 0)),doc
			, mode)

	def ksSpcIncludeReference(self, obj=defaultNamedNotOptArg, Clear=defaultNamedNotOptArg):
		'�������� ��� �������� ��������� ��� ����� ������� � ������� ������������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((3, 0), (2, 0)),obj
			, Clear)

	def ksSpcMassa(self, sMassa=defaultNamedNotOptArg):
		'���������� ����� ������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((8, 0),),sMassa
			)

	def ksSpcObjectCreate(self, nameLib=defaultNamedNotOptArg, styleNumb=defaultNamedNotOptArg, secNumb=defaultNamedNotOptArg, subSecNumb=defaultNamedNotOptArg
			, numb=defaultNamedNotOptArg, typeObj=defaultNamedNotOptArg):
		'������� ������ ������������ � ����������� ��������� ��� � ��.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((8, 0), (3, 0), (3, 0), (3, 0), (5, 0), (2, 0)),nameLib
			, styleNumb, secNumb, subSecNumb, numb, typeObj
			)

	def ksSpcObjectEdit(self, spcObj=defaultNamedNotOptArg):
		'������� ������ ������������ ��� ��������������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), ((3, 0),),spcObj
			)

	def ksSpcObjectEnd(self):
		'��������� ������ ������������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def ksSpcPosition(self, pos=defaultNamedNotOptArg):
		'���������� ����� �������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((3, 0),),pos
			)

	def ksSpcVisible(self, colNumb=defaultNamedNotOptArg, itemNumb=defaultNamedNotOptArg, flagOn=defaultNamedNotOptArg):
		'�������� �������� ���������� � �������  itemNumb � ������� � �������  colNumb.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), ((3, 0), (3, 0), (2, 0)),colNumb
			, itemNumb, flagOn)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSpecificationNotify:
	'������� ���  ������������.'
	CLSID = CLSID_Sink = IID('{0331AB4B-F25B-4EB9-9C8A-BFEA414E3822}')
	coclass_clsid = IID('{51E74526-9A3A-11D6-95CE-00C0262D30E3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnTuningSpcStyleBeginChange",
		        2 : "OnTuningSpcStyleChange",
		        3 : "OnChangeCurrentSpcDescription",
		        4 : "OnSpcDescriptionAdd",
		        5 : "OnSpcDescriptionRemove",
		        6 : "OnSpcDescriptionBeginEdit",
		        7 : "OnSpcDescriptionEdit",
		        8 : "OnSynchronizationBegin",
		        9 : "OnSynchronization",
		       10 : "OnBeginCalcPositions",
		       11 : "OnCalcPositions",
		       12 : "OnBeginCreateObject",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnTuningSpcStyleBeginChange(self, libName=defaultNamedNotOptArg, numb=defaultNamedNotOptArg):
#		'������ ��������� �������� ������������.'
#	def OnTuningSpcStyleChange(self, libName=defaultNamedNotOptArg, numb=defaultNamedNotOptArg, isOk=defaultNamedNotOptArg):
#		'��������� ������������ ����������.'
#	def OnChangeCurrentSpcDescription(self, libName=defaultNamedNotOptArg, numb=defaultNamedNotOptArg):
#		'���������� ������� �������� ������������.'
#	def OnSpcDescriptionAdd(self, libName=defaultNamedNotOptArg, numb=defaultNamedNotOptArg):
#		'���������� �������� ������������.'
#	def OnSpcDescriptionRemove(self, libName=defaultNamedNotOptArg, numb=defaultNamedNotOptArg):
#		'��������� �������� ������������.'
#	def OnSpcDescriptionBeginEdit(self, libName=defaultNamedNotOptArg, numb=defaultNamedNotOptArg):
#		'������ �������������� �������� ������������.'
#	def OnSpcDescriptionEdit(self, libName=defaultNamedNotOptArg, numb=defaultNamedNotOptArg, isOk=defaultNamedNotOptArg):
#		'��������������� �������� ������������.'
#	def OnSynchronizationBegin(self):
#		'������ �������������.'
#	def OnSynchronization(self):
#		'������������� ���������.'
#	def OnBeginCalcPositions(self):
#		'������ ������� �������.'
#	def OnCalcPositions(self):
#		'�������� ������ �������.'
#	def OnBeginCreateObject(self, typeObj=defaultNamedNotOptArg):
#		'������ �������� ������� �� (�� ������� ������ ������� ).'


class ksSphereParam(DispatchBaseClass):
	'��������� ���������� �����.'
	CLSID = IID('{C32977F3-3CA7-4D56-8AE7-4963E6851B75}')
	coclass_clsid = IID('{C82A3D03-4BEE-467F-9240-C1C58FDB144E}')

	def GetPlacement(self):
		'�������� �� �����.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	_prop_map_get_ = {
		"radius": (1, 2, (5, 0), (), "radius", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSplineDefinition(DispatchBaseClass):
	'������.'
	CLSID = IID('{0307BBA5-C193-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{0307BBA7-C193-11D6-8734-00C0262CDD2C}')

	def AddVertex(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg, radius=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((5, 0), (5, 0), (5, 0), (5, 0)),x
			, y, z, radius)

	def AddVertexAndAssociation(self, index=defaultNamedNotOptArg, obj=defaultNamedNotOptArg, weight=defaultNamedNotOptArg):
		'�������� ������� �� �������� �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((3, 0), (9, 0), (5, 0)),index
			, obj, weight)

	def DeleteVertex(self, index=defaultNamedNotOptArg):
		'������� �������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((3, 0),),index
			)

	def Flush(self):
		'�������� ������ ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	def GetAssociation(self, index=defaultNamedNotOptArg):
		'�������� ������� ����� �� �������.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetAssociation', None)
		return ret

	def GetCountVertex(self):
		'�������� ���������� ������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	def GetParamVertex(self, index=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing
			, weight=pythoncom.Missing):
		'����� ��������� �������.'
		return self._ApplyTypes_(8, 1, (11, 0), ((3, 1), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetParamVertex', None,index
			, x, y, z, weight)

	def InsertVertex(self, index=defaultNamedNotOptArg, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg
			, weight=defaultNamedNotOptArg):
		'�������� �������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((3, 0), (5, 0), (5, 0), (5, 0), (5, 0)),index
			, x, y, z, weight)

	def ReadFromFile(self, fileName=defaultNamedNotOptArg):
		'��������� ���� � �������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((8, 0),),fileName
			)

	def SetAssociation(self, index=defaultNamedNotOptArg, obj=defaultNamedNotOptArg):
		'������ ������� ����� �� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((3, 0), (9, 0)),index
			, obj)

	def WriteToFile(self, fileName=defaultNamedNotOptArg):
		'�������� ���� � �������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((8, 0),),fileName
			)

	_prop_map_get_ = {
		"closed": (1, 2, (11, 0), (), "closed", None),
		"degree": (3, 2, (3, 0), (), "degree", None),
		"splineOnPoles": (2, 2, (11, 0), (), "splineOnPoles", None),
	}
	_prop_map_put_ = {
		"closed" : ((1, LCID, 4, 0),()),
		"degree" : ((3, LCID, 4, 0),()),
		"splineOnPoles" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksStamp(DispatchBaseClass):
	'�������������� ������.'
	CLSID = IID('{FBCC5BA5-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5BA7-996C-11D6-8732-00C0262CDD2C}')

	def ksClearStamp(self, numb=defaultNamedNotOptArg):
		'�������� ��������� ������ - �����.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), ((3, 0),),numb
			)

	def ksCloseStamp(self):
		'������� ��������� ������  - �����.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	def ksColumnNumber(self, numb=defaultNamedNotOptArg):
		'���������� ����� ������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((3, 0),),numb
			)

	def ksGetStampColumnText(self, numb=defaultNamedNotOptArg):
		'������ ����� �����.'
		return self._ApplyTypes_(5, 1, (9, 0), ((16387, 3),), 'ksGetStampColumnText', None,numb
			)

	def ksOpenStamp(self):
		'������� ��������� ������  - �����.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def ksSetStampColumnText(self, numb=defaultNamedNotOptArg, textArr=defaultNamedNotOptArg):
		'�������� ����� �����.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((3, 0), (9, 0)),numb
			, textArr)

	def ksSetTextLineAlign(self, align=defaultNamedNotOptArg):
		'���������� ������������ ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((2, 0),),align
			)

	def ksTextLine(self, textItem=defaultNamedNotOptArg):
		'������� ���������� ������ ������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((9, 0),),textItem
			)

	_prop_map_get_ = {
		"reference": (1, 2, (3, 0), (), "reference", None),
		"SheetNumb": (10, 2, (3, 0), (), "SheetNumb", None),
	}
	_prop_map_put_ = {
		"reference" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksStampNotify:
	'C������ ��������� - ������ � �������� ��������.'
	CLSID = CLSID_Sink = IID('{404E7D5A-A13F-4CFF-8214-FEA7012110CB}')
	coclass_clsid = IID('{FBCC5BA7-996C-11D6-8732-00C0262CDD2C}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnBeginEditStamp",
		        2 : "OnEndEditStamp",
		        3 : "OnStampCellDblClick",
		        4 : "OnStampCellBeginEdit",
		        5 : "OnStampBeginClearCells",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnBeginEditStamp(self):
#		'������ �������������� ������.'
#	def OnEndEditStamp(self, editResult=defaultNamedNotOptArg):
#		'���������� �������������� ������.'
#	def OnStampCellDblClick(self, number=defaultNamedNotOptArg):
#		'������� ���� � ������ ������.'
#	def OnStampCellBeginEdit(self, number=defaultNamedNotOptArg):
#		'������ �������������� � ������ ������.'
#	def OnStampBeginClearCells(self, cells=defaultNamedNotOptArg):
#		'������ �������������� � ������ ������.'


class ksStandartSheet(DispatchBaseClass):
	'��������� ���������� ������������ �����.'
	CLSID = IID('{FBCC5B90-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5B92-996C-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"direct": (3, 2, (11, 0), (), "direct", None),
		"format": (1, 2, (2, 0), (), "format", None),
		"multiply": (2, 2, (2, 0), (), "multiply", None),
	}
	_prop_map_put_ = {
		"direct" : ((3, LCID, 4, 0),()),
		"format" : ((1, LCID, 4, 0),()),
		"multiply" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksSurface(DispatchBaseClass):
	'�������������� ����������� � ���������� ������������.'
	CLSID = IID('{963CB6E1-B9BF-4234-964A-13BFE6C0282A}')
	coclass_clsid = IID('{B1C40242-CD49-4207-B728-B67057BEC339}')

	def CurveIntersection(self, curve=defaultNamedNotOptArg, points=defaultNamedNotOptArg, extSurf=defaultNamedNotOptArg, extCurve=defaultNamedNotOptArg):
		'������� ����������� � ������.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (11, 0), ((9, 0), (9, 0), (11, 0), (11, 0)),curve
			, points, extSurf, extCurve)

	def GetArea(self, bitVector=defaultNamedNotOptArg):
		'�������� ������� ����� (ST_MIX_MM..ST_MIX_M ������� ���������.'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (5, 0), ((19, 0),),bitVector
			)

	def GetBoundaryUVNurbs(self, uv=defaultNamedNotOptArg, closed=defaultNamedNotOptArg, loopIndex=defaultNamedNotOptArg, edgeIndex=defaultNamedNotOptArg
			, degree=pythoncom.Missing, points=pythoncom.Missing, weights=pythoncom.Missing, knots=pythoncom.Missing, tMin=pythoncom.Missing
			, tMax=pythoncom.Missing):
		'�������� ��������� ������� ����������� � UV NURBS-�������������.'
		return self._ApplyTypes_(34, 1, (11, 0), ((11, 1), (11, 1), (3, 1), (3, 1), (16387, 2), (16396, 2), (16396, 2), (16396, 2), (16389, 2), (16389, 2)), 'GetBoundaryUVNurbs', None,uv
			, closed, loopIndex, edgeIndex, degree, points
			, weights, knots, tMin, tMax)

	def GetDerivativeU(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ������ ����������� �� U.'
		return self._ApplyTypes_(6, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeU', None,paramU
			, paramV, x, y, z)

	def GetDerivativeUU(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ������ ����������� �� UU.'
		return self._ApplyTypes_(8, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeUU', None,paramU
			, paramV, x, y, z)

	def GetDerivativeUUU(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ������ ����������� �� UUU.'
		return self._ApplyTypes_(11, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeUUU', None,paramU
			, paramV, x, y, z)

	def GetDerivativeUUV(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ������ ����������� �� UUV.'
		return self._ApplyTypes_(14, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeUUV', None,paramU
			, paramV, x, y, z)

	def GetDerivativeUV(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ������ ����������� �� UV.'
		return self._ApplyTypes_(10, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeUV', None,paramU
			, paramV, x, y, z)

	def GetDerivativeUVV(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ������ ����������� �� UVV.'
		return self._ApplyTypes_(13, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeUVV', None,paramU
			, paramV, x, y, z)

	def GetDerivativeV(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ������ ����������� �� V.'
		return self._ApplyTypes_(7, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeV', None,paramU
			, paramV, x, y, z)

	def GetDerivativeVV(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ������ ����������� �� VV.'
		return self._ApplyTypes_(9, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeVV', None,paramU
			, paramV, x, y, z)

	def GetDerivativeVVV(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ������ ����������� �� VVV.'
		return self._ApplyTypes_(12, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetDerivativeVVV', None,paramU
			, paramV, x, y, z)

	def GetEdgesCount(self, loopIndex=defaultNamedNotOptArg):
		'���������� ����� � �������.'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (3, 0), ((3, 0),),loopIndex
			)

	def GetGabarit(self, x1=pythoncom.Missing, y1=pythoncom.Missing, z1=pythoncom.Missing, x2=pythoncom.Missing
			, y2=pythoncom.Missing, z2=pythoncom.Missing):
		'�������� �������.'
		return self._ApplyTypes_(1, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetGabarit', None,x1
			, y1, z1, x2, y2, z2
			)

	def GetNormal(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� �������.'
		return self._ApplyTypes_(3, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetNormal', None,paramU
			, paramV, x, y, z)

	def GetNurbsSurfaceParam(self):
		'�������� ��������� ����������� � Nurbs-�������������.'
		ret = self._oleobj_.InvokeTypes(33, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNurbsSurfaceParam', None)
		return ret

	def GetParamUMax(self):
		'�������� �������� ��������� U ��������.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (5, 0), (),)

	def GetParamUMin(self):
		'�������� �������� ��������� U ���������.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (5, 0), (),)

	def GetParamVMax(self):
		'�������� �������� ��������� V ��������.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (5, 0), (),)

	def GetParamVMin(self):
		'�������� �������� ��������� V ���������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (5, 0), (),)

	def GetPoint(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ����� �� �����������.'
		return self._ApplyTypes_(2, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetPoint', None,paramU
			, paramV, x, y, z)

	def GetSurfaceParam(self):
		'�������� ��������� ���������, ������, ��������, ����, �����, nurbs-����������� ��� NULL.'
		ret = self._oleobj_.InvokeTypes(29, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSurfaceParam', None)
		return ret

	def GetTangentVectorU(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ����������� ������ �� U.'
		return self._ApplyTypes_(4, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetTangentVectorU', None,paramU
			, paramV, x, y, z)

	def GetTangentVectorV(self, paramU=defaultNamedNotOptArg, paramV=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing
			, z=pythoncom.Missing):
		'�������� ����������� ������ �� V.'
		return self._ApplyTypes_(5, 1, (11, 0), ((5, 1), (5, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetTangentVectorV', None,paramU
			, paramV, x, y, z)

	def IsClosedU(self):
		'�������� ����������� ������.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), (),)

	def IsClosedV(self):
		'�������� ����������� ������.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), (),)

	def IsCone(self):
		'�������� �� ����� ����������.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (11, 0), (),)

	def IsCylinder(self):
		'�������� �� ����� ��������������.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (11, 0), (),)

	def IsNurbsSurface(self):
		'�������� �� ����� nurbs ������������.'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (11, 0), (),)

	def IsPlane(self):
		'�������� �� ����� �������.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), (),)

	def IsRevolved(self):
		'������������ �� ����� ������������ ��������.'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (11, 0), (),)

	def IsSphere(self):
		'�������� �� ����� �����������.'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (11, 0), (),)

	def IsSwept(self):
		'������������ �� ����� ������������ �� ����������.'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (11, 0), (),)

	def IsTorus(self):
		'�������� �� ����� �����.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), (),)

	def NearPointProjection(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg, z=defaultNamedNotOptArg, u=pythoncom.Missing
			, v=pythoncom.Missing, ext=defaultNamedNotOptArg):
		'�������� ��������� �������� ����� �� �����������.'
		return self._ApplyTypes_(31, 1, (11, 0), ((5, 1), (5, 1), (5, 1), (16389, 2), (16389, 2), (11, 0)), 'NearPointProjection', None,x
			, y, z, u, v, ext
			)

	_prop_map_get_ = {
		"BoundaryCount": (35, 2, (3, 0), (), "BoundaryCount", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksTAN(DispatchBaseClass):
	'������ ��������� ����� �������.'
	CLSID = IID('{8075EDE4-6C85-4711-8685-68FBE359D4C4}')
	coclass_clsid = IID('{9F8CA523-173C-4206-8F2A-AB221138692E}')

	# The method x1 is actually a property, but must be used as a method to correctly pass the arguments
	def x1(self, index=defaultNamedNotOptArg):
		'���������� ���������� �1 ����� �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 2, (5, 0), ((3, 0),),index
			)

	# The method x2 is actually a property, but must be used as a method to correctly pass the arguments
	def x2(self, index=defaultNamedNotOptArg):
		'���������� ���������� �2 ����� �������.'
		return self._oleobj_.InvokeTypes(3, LCID, 2, (5, 0), ((3, 0),),index
			)

	# The method y1 is actually a property, but must be used as a method to correctly pass the arguments
	def y1(self, index=defaultNamedNotOptArg):
		'���������� ���������� y1 ����� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 2, (5, 0), ((3, 0),),index
			)

	# The method y2 is actually a property, but must be used as a method to correctly pass the arguments
	def y2(self, index=defaultNamedNotOptArg):
		'���������� ���������� y2 ����� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 2, (5, 0), ((3, 0),),index
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksTechnicalDemandParam(DispatchBaseClass):
	'��������� ��� ����������� ����������� ����������.'
	CLSID = IID('{FBCC5B81-996C-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{FBCC5B83-996C-11D6-8732-00C0262CDD2C}')

	def GetPGab(self):
		'���������� ������������ ������ ���������� ���������������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPGab', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetPGab(self, val=defaultNamedNotOptArg):
		'�������� ������������ ������ ���������� ���������������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"strCount": (2, 2, (2, 0), (), "strCount", None),
		"style": (1, 2, (3, 0), (), "style", None),
	}
	_prop_map_put_ = {
		"strCount" : ((2, LCID, 4, 0),()),
		"style" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksTessellation(DispatchBaseClass):
	'��������� ������������.'
	CLSID = IID('{B810650E-7819-485C-90D2-ADEB647AE5E2}')
	coclass_clsid = IID('{923A48A1-C159-4959-B13E-E8C558534C89}')

	def GetFacet(self):
		'�������� ��������� ���������������� ��������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFacet', None)
		return ret

	def GetFacetAngle(self):
		'�������� ����������� �������� ���������� ����������� ( ���� 0, ������� ������������).'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (5, 0), (),)

	def GetFacetData(self, index=defaultNamedNotOptArg, facet=defaultNamedNotOptArg):
		'�������� ��������� ���������������� �������� �� ������� � ������� ���������������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((3, 0), (9, 0)),index
			, facet)

	def GetFacetNormals(self, normals=pythoncom.Missing):
		'�������� ��������� �������� ������������� ���������������� �����.'
		return self._ApplyTypes_(11, 1, (11, 0), ((16396, 2),), 'GetFacetNormals', None,normals
			)

	def GetFacetParams(self, params=pythoncom.Missing):
		'�������� ��������������� ���������� ������ ���������������� �����.'
		return self._ApplyTypes_(12, 1, (11, 0), ((16396, 2),), 'GetFacetParams', None,params
			)

	def GetFacetPoints(self, points=pythoncom.Missing, indexes=pythoncom.Missing):
		'�������� ��������� ������ ���������������� �����.'
		return self._ApplyTypes_(10, 1, (11, 0), ((16396, 2), (16396, 2)), 'GetFacetPoints', None,points
			, indexes)

	def GetFacetSag(self):
		'�������� ����������� ������� ����������� ( ���� 0, ������� ������������).'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (5, 0), (),)

	def GetFacetSize(self):
		'�������� ����������� ������� ����� ( ���� 0, ������� ������������).'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (5, 0), (),)

	def GetFacetsCount(self):
		'�������� ���������� ���������������� �������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetNeedParams(self):
		'�������� ������������� ���������� ���������� ������.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), (),)

	def GetNormal(self, index=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ������� ����������������� �����, index - ������ ������� � ������� ������.'
		return self._ApplyTypes_(5, 1, (11, 0), ((3, 1), (16388, 2), (16388, 2), (16388, 2)), 'GetNormal', None,index
			, x, y, z)

	def GetPoint(self, index=defaultNamedNotOptArg, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� ������� ����������������� �����, index - ������ ������� � ������� ������.'
		return self._ApplyTypes_(4, 1, (11, 0), ((3, 1), (16388, 2), (16388, 2), (16388, 2)), 'GetPoint', None,index
			, x, y, z)

	def GetPointsCount(self):
		'�������� ���������� ������ ����������������� �����.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	def SetFacetAngle(self, angle=defaultNamedNotOptArg):
		'������ ����������� �������� ���������� ���������������� �������� ( ���� 0, ������� ������������).'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), ((5, 0),),angle
			)

	def SetFacetSag(self, sag=defaultNamedNotOptArg):
		'������ ����������� ������� ����������� ���������������� �������� ( ���� 0, ������� ������������).'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((5, 0),),sag
			)

	def SetFacetSize(self, sag=defaultNamedNotOptArg):
		'������ ����������� ������� ����� ��� ���������������� �������� ( ���� 0, ������� ������������).'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((5, 0),),sag
			)

	def SetNeedParams(self, need=defaultNamedNotOptArg):
		'������ ������������� ���������� ���������� ������.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), ((11, 0),),need
			)

	def refresh(self):
		'�������� ������������, ���� ���������� ���������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksTextDocumentParam(DispatchBaseClass):
	'��������� ���������� ���������� ���������.'
	CLSID = IID('{33706D56-D085-4840-833B-435AEB00BE2A}')
	coclass_clsid = IID('{02286DB8-98D4-4D0B-97D7-E2EED32EEBD6}')

	def GetArrTailSheet(self):
		'������ ������ ���������� ������ �������������� �����.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetArrTailSheet', None)
		return ret

	def GetArrTitleSheet(self):
		'������ ������ ���������� ��������� ������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetArrTitleSheet', None)
		return ret

	def GetEvenSheet(self):
		'���������� ������ ������( ��� ���������� ������, ����� ����� � ����������).'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetEvenSheet', None)
		return ret

	def GetFirstSheet(self):
		'���������� ������� �����( ��� ���������� ������, ����� ����� � ����������).'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstSheet', None)
		return ret

	def GetOddSheet(self):
		'���������� �������� ������( ��� ���������� ������, ����� ����� � ����������).'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetOddSheet', None)
		return ret

	def GetSheetParam(self):
		'���������� ��������� �� ��������� ���������� ����������������� ��� ������������ �����.'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSheetParam', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"author": (3, 2, (8, 0), (), "author", None),
		"comment": (2, 2, (8, 0), (), "comment", None),
		"fileName": (1, 2, (8, 0), (), "fileName", None),
		"regime": (5, 2, (2, 0), (), "regime", None),
		"type": (4, 2, (2, 0), (), "type", None),
	}
	_prop_map_put_ = {
		"author" : ((3, LCID, 4, 0),()),
		"comment" : ((2, LCID, 4, 0),()),
		"fileName" : ((1, LCID, 4, 0),()),
		"regime" : ((5, LCID, 4, 0),()),
		"type" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksTextItemFont(DispatchBaseClass):
	'��������� ������ ���������� ������ ������.'
	CLSID = IID('{364521BD-94B5-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{364521BF-94B5-11D6-8732-00C0262CDD2C}')

	def GetBitVectorValue(self, val=defaultNamedNotOptArg):
		'���������� �������� �������� �������.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((3, 0),),val
			)

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	def SetBitVectorValue(self, val=defaultNamedNotOptArg, state=defaultNamedNotOptArg):
		'�������� �������� �������� �������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((3, 0), (11, 0)),val
			, state)

	_prop_map_get_ = {
		"bitVector": (5, 2, (3, 0), (), "bitVector", None),
		"color": (4, 2, (3, 0), (), "color", None),
		"fontName": (1, 2, (8, 0), (), "fontName", None),
		"height": (2, 2, (5, 0), (), "height", None),
		"ksu": (3, 2, (5, 0), (), "ksu", None),
	}
	_prop_map_put_ = {
		"bitVector" : ((5, LCID, 4, 0),()),
		"color" : ((4, LCID, 4, 0),()),
		"fontName" : ((1, LCID, 4, 0),()),
		"height" : ((2, LCID, 4, 0),()),
		"ksu" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksTextItemParam(DispatchBaseClass):
	'��������� ���������� ������ ������.'
	CLSID = IID('{364521B7-94B5-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{364521B9-94B5-11D6-8732-00C0262CDD2C}')

	def GetItemFont(self):
		'���������� ��������� ������ ��� ���������� ������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetItemFont', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	def SetItemFont(self, val=defaultNamedNotOptArg):
		'�������� ��������� ������ ��� ���������� ������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"iSNumb": (3, 2, (3, 0), (), "iSNumb", None),
		"s": (2, 2, (8, 0), (), "s", None),
		"type": (1, 2, (3, 0), (), "type", None),
	}
	_prop_map_put_ = {
		"iSNumb" : ((3, LCID, 4, 0),()),
		"s" : ((2, LCID, 4, 0),()),
		"type" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksTextLineParam(DispatchBaseClass):
	'��������� ������ ������.'
	CLSID = IID('{364521BA-94B5-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{364521BC-94B5-11D6-8732-00C0262CDD2C}')

	def GetTextItemArr(self):
		'�������� ������ ��������� ������ ������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTextItemArr', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	def SetTextItemArr(self, val=defaultNamedNotOptArg):
		'���������� ������ ��������� ������ ������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"style": (1, 2, (3, 0), (), "style", None),
	}
	_prop_map_put_ = {
		"style" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksTextParam(DispatchBaseClass):
	'��������� ������.'
	CLSID = IID('{7F7D6F96-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6F98-97DA-11D6-8732-00C0262CDD2C}')

	def GetParagraphParam(self):
		'�������� ��������� ���������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetParagraphParam', None)
		return ret

	def GetTextLineArr(self):
		'�������� ������ ����� ������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTextLineArr', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	def SetParagraphParam(self, val=defaultNamedNotOptArg):
		'���������� ��������� ���������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((9, 0),),val
			)

	def SetTextLineArr(self, val=defaultNamedNotOptArg):
		'���������� ������ ����� ������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksTextStyleParam(DispatchBaseClass):
	'����� ������.'
	CLSID = IID('{3F715E24-97D9-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{3F715E26-97D9-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"align": (7, 2, (2, 0), (), "align", None),
		"bold": (8, 2, (2, 0), (), "bold", None),
		"color": (6, 2, (3, 0), (), "color", None),
		"fontName": (5, 2, (8, 0), (), "fontName", None),
		"height": (2, 2, (5, 0), (), "height", None),
		"italic": (9, 2, (2, 0), (), "italic", None),
		"ksu": (3, 2, (5, 0), (), "ksu", None),
		"leftEdge": (14, 2, (5, 0), (), "leftEdge", None),
		"name": (1, 2, (8, 0), (), "name", None),
		"posKS": (11, 2, (5, 0), (), "posKS", None),
		"rightEdge": (15, 2, (5, 0), (), "rightEdge", None),
		"step": (4, 2, (5, 0), (), "step", None),
		"stepParPre": (12, 2, (5, 0), (), "stepParPre", None),
		"stepParPst": (13, 2, (5, 0), (), "stepParPst", None),
		"underline": (10, 2, (2, 0), (), "underline", None),
	}
	_prop_map_put_ = {
		"align" : ((7, LCID, 4, 0),()),
		"bold" : ((8, LCID, 4, 0),()),
		"color" : ((6, LCID, 4, 0),()),
		"fontName" : ((5, LCID, 4, 0),()),
		"height" : ((2, LCID, 4, 0),()),
		"italic" : ((9, LCID, 4, 0),()),
		"ksu" : ((3, LCID, 4, 0),()),
		"leftEdge" : ((14, LCID, 4, 0),()),
		"name" : ((1, LCID, 4, 0),()),
		"posKS" : ((11, LCID, 4, 0),()),
		"rightEdge" : ((15, LCID, 4, 0),()),
		"step" : ((4, LCID, 4, 0),()),
		"stepParPre" : ((12, LCID, 4, 0),()),
		"stepParPst" : ((13, LCID, 4, 0),()),
		"underline" : ((10, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksThinParam(DispatchBaseClass):
	'��������� ������ ������.'
	CLSID = IID('{DEEFF029-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{DEEFF02B-C3E2-11D6-8734-00C0262CDD2C}')

	_prop_map_get_ = {
		"normalThickness": (3, 2, (5, 0), (), "normalThickness", None),
		"reverseThickness": (4, 2, (5, 0), (), "reverseThickness", None),
		"thin": (1, 2, (11, 0), (), "thin", None),
		"thinType": (2, 2, (2, 0), (), "thinType", None),
	}
	_prop_map_put_ = {
		"normalThickness" : ((3, LCID, 4, 0),()),
		"reverseThickness" : ((4, LCID, 4, 0),()),
		"thin" : ((1, LCID, 4, 0),()),
		"thinType" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksThreadDefinition(DispatchBaseClass):
	'�������� ����������� ������.'
	CLSID = IID('{5DDB6B14-6F3D-431F-B62F-C5FCCAFC3632}')
	coclass_clsid = IID('{2A8AE692-45A3-4C22-88B5-76B4830F2235}')

	def GetBaseObject(self):
		'�������� ����� ��� �����, �� ������� �������� ������.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetBaseObject', None)
		return ret

	def GetFaceBegin(self):
		'�������� �����, �� ������� �������� ������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFaceBegin', None)
		return ret

	def GetFaceEnd(self):
		'�������� �����, �� ������� �������� ������.'
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFaceEnd', None)
		return ret

	def SetBaseObject(self, obj=defaultNamedNotOptArg):
		'���������� ����� ��� �����, �� ������� �������� ������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((9, 0),),obj
			)

	def SetFaceBegin(self, face=defaultNamedNotOptArg):
		'���������� �����, �� ������� �������� ������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 0),),face
			)

	def SetFaceEnd(self, face=defaultNamedNotOptArg):
		'���������� �����, �� ������� �������� ������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((9, 0),),face
			)

	_prop_map_get_ = {
		"allLength": (6, 2, (11, 0), (), "allLength", None),
		"autoDefinDr": (5, 2, (11, 0), (), "autoDefinDr", None),
		"dr": (1, 2, (5, 0), (), "dr", None),
		"faceValue": (7, 2, (11, 0), (), "faceValue", None),
		"length": (2, 2, (5, 0), (), "length", None),
		"p": (3, 2, (5, 0), (), "p", None),
		"outside": (4, 2, (11, 0), (), "outside", None),
	}
	_prop_map_put_ = {
		"allLength" : ((6, LCID, 4, 0),()),
		"autoDefinDr" : ((5, LCID, 4, 0),()),
		"dr" : ((1, LCID, 4, 0),()),
		"faceValue" : ((7, LCID, 4, 0),()),
		"length" : ((2, LCID, 4, 0),()),
		"p" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksToleranceBranch(DispatchBaseClass):
	'��������� ���������� ����� ������� �����.'
	CLSID = IID('{4FD7CE84-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CE86-9968-11D6-95CE-00C0262D30E3}')

	def GetpMathPoint(self):
		'�������� ������������ ������ �����.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpMathPoint', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	def SetpMathPoint(self, pMathPoint=defaultNamedNotOptArg):
		'�������� ������������ ������ �����.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((9, 0),),pMathPoint
			)

	_prop_map_get_ = {
		"arrowType": (1, 2, (2, 0), (), "arrowType", None),
		"tCorner": (2, 2, (2, 0), (), "tCorner", None),
	}
	_prop_map_put_ = {
		"arrowType" : ((1, LCID, 4, 0),()),
		"tCorner" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksToleranceParam(DispatchBaseClass):
	'��������� ���������� ������� �����.'
	CLSID = IID('{4FD7CE87-9968-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{4FD7CE89-9968-11D6-95CE-00C0262D30E3}')

	def GetBranchArr(self):
		'�������� ������������ ������ ���� ������� �����.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetBranchArr', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	def SetBranchArr(self, branchArr=defaultNamedNotOptArg):
		'�������� ������������ ������ ���� ������� �����.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((9, 0),),branchArr
			)

	_prop_map_get_ = {
		"style": (2, 2, (3, 0), (), "style", None),
		"tBase": (1, 2, (2, 0), (), "tBase", None),
		"type": (5, 2, (2, 0), (), "type", None),
		"x": (3, 2, (5, 0), (), "x", None),
		"y": (4, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"style" : ((2, LCID, 4, 0),()),
		"tBase" : ((1, LCID, 4, 0),()),
		"type" : ((5, LCID, 4, 0),()),
		"x" : ((3, LCID, 4, 0),()),
		"y" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksTorusParam(DispatchBaseClass):
	'��������� ���������� ����.'
	CLSID = IID('{FDA3B147-BAF1-4F75-99AA-39D11323EA97}')
	coclass_clsid = IID('{B7833CCA-936D-4689-BD90-90B5209D94E8}')

	def GetPlacement(self):
		'�������� �� ����.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	_prop_map_get_ = {
		"generatrixRadius": (2, 2, (5, 0), (), "generatrixRadius", None),
		"radius": (1, 2, (5, 0), (), "radius", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksTreeNodeParam(DispatchBaseClass):
	'��������� ���������� ���� ������.'
	CLSID = IID('{9F8DE1DC-1268-4785-9217-1B0DD59B85FA}')
	coclass_clsid = IID('{05A4578F-A41F-48F2-92F9-A0F0856BCBC0}')

	def GetComment(self):
		'�������� ������ ����� �����������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetComment', None)
		return ret

	def GetNodes(self):
		'�������� ������ �����.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNodes', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"name": (3, 2, (8, 0), (), "name", None),
		"type": (2, 2, (3, 0), (), "type", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksType1(DispatchBaseClass):
	'��������� ��� ������ ������.'
	CLSID = IID('{9AF8E344-98A0-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{9AF8E346-98A0-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"angle": (4, 2, (5, 0), (), "angle", None),
		"gr": (5, 2, (3, 0), (), "gr", None),
		"scale_": (3, 2, (5, 0), (), "scale_", None),
		"xBase": (1, 2, (5, 0), (), "xBase", None),
		"yBase": (2, 2, (5, 0), (), "yBase", None),
	}
	_prop_map_put_ = {
		"angle" : ((4, LCID, 4, 0),()),
		"gr" : ((5, LCID, 4, 0),()),
		"scale_" : ((3, LCID, 4, 0),()),
		"xBase" : ((1, LCID, 4, 0),()),
		"yBase" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksType2(DispatchBaseClass):
	'��������� ��� �������.'
	CLSID = IID('{9AF8E347-98A0-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{9AF8E349-98A0-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"xBase": (1, 2, (5, 0), (), "xBase", None),
		"yBase": (2, 2, (5, 0), (), "yBase", None),
	}
	_prop_map_put_ = {
		"xBase" : ((1, LCID, 4, 0),()),
		"yBase" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksType3(DispatchBaseClass):
	'��������� ��� �������������� � ��� ������� c �������� �����.'
	CLSID = IID('{9AF8E34A-98A0-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{9AF8E34C-98A0-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"angle": (3, 2, (5, 0), (), "angle", None),
		"xBase": (1, 2, (5, 0), (), "xBase", None),
		"yBase": (2, 2, (5, 0), (), "yBase", None),
	}
	_prop_map_put_ = {
		"angle" : ((3, LCID, 4, 0),()),
		"xBase" : ((1, LCID, 4, 0),()),
		"yBase" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksType5(DispatchBaseClass):
	'��������� ��� �������� �������������� c �������� �����.'
	CLSID = IID('{9AF8E34D-98A0-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{9AF8E34F-98A0-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"angle": (3, 2, (5, 0), (), "angle", None),
		"horizon": (4, 2, (11, 0), (), "horizon", None),
		"xBase": (1, 2, (5, 0), (), "xBase", None),
		"yBase": (2, 2, (5, 0), (), "yBase", None),
	}
	_prop_map_put_ = {
		"angle" : ((3, LCID, 4, 0),()),
		"horizon" : ((4, LCID, 4, 0),()),
		"xBase" : ((1, LCID, 4, 0),()),
		"yBase" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksType6(DispatchBaseClass):
	'��������� ��� ����������������� �������.'
	CLSID = IID('{9AF8E350-98A0-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{9AF8E352-98A0-11D6-95CE-00C0262D30E3}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"gr": (1, 2, (3, 0), (), "gr", None),
	}
	_prop_map_put_ = {
		"gr" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksUnionComponentsDefinition(DispatchBaseClass):
	'��������� �������� ����������� �����������.'
	CLSID = IID('{99797F89-FBA4-4582-812F-226AFB50ED7D}')
	coclass_clsid = IID('{BA53B169-1DC8-4CCA-BAA4-27B0FB87AE26}')

	def PartArray(self):
		'�������� ��������� ������� ������������ �����������.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PartArray', None)
		return ret

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksUserParam(DispatchBaseClass):
	'���������������� ��������� ����������.'
	CLSID = IID('{E79C2519-9584-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{E79C251B-9584-11D6-8732-00C0262CDD2C}')

	def GetUserArray(self):
		'���������� ������������ ������ LTVARIANT_ARR.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetUserArray', None)
		return ret

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	def SetUserArray(self, val=defaultNamedNotOptArg):
		'�������� ������������ ������ LTVARIANT_ARR.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((9, 0),),val
			)

	_prop_map_get_ = {
		"UserParams": (7, 2, (12, 0), (), "UserParams", None),
		"fileName": (1, 2, (8, 0), (), "fileName", None),
		"libName": (2, 2, (8, 0), (), "libName", None),
		"number": (3, 2, (3, 0), (), "number", None),
	}
	_prop_map_put_ = {
		"UserParams" : ((7, LCID, 4, 0),()),
		"fileName" : ((1, LCID, 4, 0),()),
		"libName" : ((2, LCID, 4, 0),()),
		"number" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksVariable(DispatchBaseClass):
	'��������� ����������.'
	CLSID = IID('{508A0CC1-9D74-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{508A0CC3-9D74-11D6-95CE-00C0262D30E3}')

	def SetLink(self, doc=defaultNamedNotOptArg, name=defaultNamedNotOptArg):
		'���������� ������ �� ����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((8, 0), (8, 0)),doc
			, name)

	_prop_map_get_ = {
		"Expression": (5, 2, (8, 0), (), "Expression", None),
		"Information": (12, 2, (11, 0), (), "Information", None),
		"Pseudonym": (4, 2, (8, 0), (), "Pseudonym", None),
		"external": (6, 2, (11, 0), (), "external", None),
		"note": (3, 2, (8, 0), (), "note", None),
		"value": (1, 2, (5, 0), (), "value", None),
		"displayName": (11, 2, (8, 0), (), "displayName", None),
		"linkDocName": (9, 2, (8, 0), (), "linkDocName", None),
		"linkVarName": (8, 2, (8, 0), (), "linkVarName", None),
		"name": (2, 2, (8, 0), (), "name", None),
		"parameterNote": (7, 2, (8, 0), (), "parameterNote", None),
	}
	_prop_map_put_ = {
		"Expression" : ((5, LCID, 4, 0),()),
		"Information" : ((12, LCID, 4, 0),()),
		"Pseudonym" : ((4, LCID, 4, 0),()),
		"external" : ((6, LCID, 4, 0),()),
		"note" : ((3, LCID, 4, 0),()),
		"value" : ((1, LCID, 4, 0),()),
	}
	# Default property for this class is 'value'
	def __call__(self):
		return self._ApplyTypes_(*(1, 2, (5, 0), (), "value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksVariableCollection(DispatchBaseClass):
	'������ ��������������� ����������.'
	CLSID = IID('{03CEAC81-C0B8-11D6-8734-00C0262CDD2C}')
	coclass_clsid = IID('{03CEAC83-C0B8-11D6-8734-00C0262CDD2C}')

	def AddNewVariable(self, name=defaultNamedNotOptArg, value=defaultNamedNotOptArg, note=defaultNamedNotOptArg):
		'�������� ����� ����������.'
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), ((8, 0), (5, 0), (8, 0)),name
			, value, note)
		if ret is not None:
			ret = Dispatch(ret, 'AddNewVariable', None)
		return ret

	def First(self):
		'�������� ��������� �� ��������� ������� ��������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ��������� �� ��������� �������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetByName(self, name=defaultNamedNotOptArg, testFullName=False, testIgnoreCase=True):
		'�������� ��������� �� ��������� �������� �� �����.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), ((8, 0), (11, 48), (11, 48)),name
			, testFullName, testIgnoreCase)
		if ret is not None:
			ret = Dispatch(ret, 'GetByName', None)
		return ret

	def GetCount(self):
		'���������� ��������� �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'�������� ��������� �� ��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def Next(self):
		'�������� ��������� �� ��������� ���������� ��������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'�������� ��������� �� ��������� ����������� ��������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def RemoveVariable(self, name=defaultNamedNotOptArg):
		'������� ����������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((8, 0),),name
			)

	def refresh(self):
		'�������� ������ ����������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksVertexDefinition(DispatchBaseClass):
	'�������� �������.'
	CLSID = IID('{A7257E73-EB61-4602-BC8B-2D00EA4AA062}')
	coclass_clsid = IID('{5CE6E053-3EC8-427B-BCB5-82B01D4BCBF3}')

	def GetOwnerEntity(self):
		'�������� ��������� 3D �������, ���������� �������.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetOwnerEntity', None)
		return ret

	def GetPoint(self, x=pythoncom.Missing, y=pythoncom.Missing, z=pythoncom.Missing):
		'�������� �����.'
		return self._ApplyTypes_(1, 1, (11, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetPoint', None,x
			, y, z)

	_prop_map_get_ = {
		"freeVertex": (4, 2, (11, 0), (), "freeVertex", None),
		"sketchVertex": (5, 2, (11, 0), (), "sketchVertex", None),
		"topologyVertex": (3, 2, (11, 0), (), "topologyVertex", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksViewColorParam(DispatchBaseClass):
	'��������� ���������� ����� ����.'
	CLSID = IID('{5A42B962-8F78-4557-B17A-1B871F8DBDB5}')
	coclass_clsid = IID('{34AFC10F-4FBB-40F0-8A23-74B1250F42EF}')

	def Init(self):
		'������� ���������.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"bottomColor": (4, 2, (3, 0), (), "bottomColor", None),
		"color": (1, 2, (3, 0), (), "color", None),
		"topColor": (3, 2, (3, 0), (), "topColor", None),
		"useGradient": (2, 2, (11, 0), (), "useGradient", None),
	}
	_prop_map_put_ = {
		"bottomColor" : ((4, LCID, 4, 0),()),
		"color" : ((1, LCID, 4, 0),()),
		"topColor" : ((3, LCID, 4, 0),()),
		"useGradient" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksViewParam(DispatchBaseClass):
	'��������� ����.'
	CLSID = IID('{7F7D6FB4-97DA-11D6-8732-00C0262CDD2C}')
	coclass_clsid = IID('{7F7D6FB6-97DA-11D6-8732-00C0262CDD2C}')

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"angle": (3, 2, (5, 0), (), "angle", None),
		"color": (5, 2, (3, 0), (), "color", None),
		"name": (7, 2, (8, 0), (), "name", None),
		"scale_": (4, 2, (5, 0), (), "scale_", None),
		"state": (6, 2, (2, 0), (), "state", None),
		"x": (1, 2, (5, 0), (), "x", None),
		"y": (2, 2, (5, 0), (), "y", None),
	}
	_prop_map_put_ = {
		"angle" : ((3, LCID, 4, 0),()),
		"color" : ((5, LCID, 4, 0),()),
		"name" : ((7, LCID, 4, 0),()),
		"scale_" : ((4, LCID, 4, 0),()),
		"state" : ((6, LCID, 4, 0),()),
		"x" : ((1, LCID, 4, 0),()),
		"y" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksViewPointerParam(DispatchBaseClass):
	'��������� ���������� ��� ������� ����.'
	CLSID = IID('{CD1C0144-98DC-11D6-95CE-00C0262D30E3}')
	coclass_clsid = IID('{CD1C0146-98DC-11D6-95CE-00C0262D30E3}')

	def GetpTextline(self):
		'������������ ������ ����� ������.'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetpTextline', None)
		return ret

	def Init(self):
		'������������� ����������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

	def SetpTextline(self, pTextLine=defaultNamedNotOptArg):
		'������������ ������ ����� ������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 0),),pTextLine
			)

	_prop_map_get_ = {
		"str": (9, 2, (8, 0), (), "str", None),
		"style": (1, 2, (3, 0), (), "style", None),
		"type": (8, 2, (2, 0), (), "type", None),
		"x1": (2, 2, (5, 0), (), "x1", None),
		"x2": (4, 2, (5, 0), (), "x2", None),
		"xt": (6, 2, (5, 0), (), "xt", None),
		"y1": (3, 2, (5, 0), (), "y1", None),
		"y2": (5, 2, (5, 0), (), "y2", None),
		"yt": (7, 2, (5, 0), (), "yt", None),
	}
	_prop_map_put_ = {
		"str" : ((9, LCID, 4, 0),()),
		"style" : ((1, LCID, 4, 0),()),
		"type" : ((8, LCID, 4, 0),()),
		"x1" : ((2, LCID, 4, 0),()),
		"x2" : ((4, LCID, 4, 0),()),
		"xt" : ((6, LCID, 4, 0),()),
		"y1" : ((3, LCID, 4, 0),()),
		"y2" : ((5, LCID, 4, 0),()),
		"yt" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksViewProjection(DispatchBaseClass):
	'��������� �������� ����������� ������ � ����.'
	CLSID = IID('{BF65B990-C2DC-4A12-9EB7-3E868608AF47}')
	coclass_clsid = IID('{0CA54EDF-BC8C-4A6A-94CF-EDBA74A6FA00}')

	def GetPlacement(self):
		'�������� ������� ��������� ����������� ������ � ����.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPlacement', None)
		return ret

	def GetViewProjectonType(self):
		'�������� ��� ��������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	def IsCurrent(self):
		'������� �������� �� ������ �������� �������.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetCurrent(self):
		'���������� ������ �������� ����������� ������ � ���� �������.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	def SetMatrix3D(self, Matrix3D=defaultNamedNotOptArg):
		'���������� ������� ��������� ����������� ������ � ���� �� �������.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((12, 0),),Matrix3D
			)

	def SetPlacement(self, place=defaultNamedNotOptArg):
		'���������� ������� ��������� ����������� ������ � ����.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((9, 0),),place
			)

	_prop_map_get_ = {
		"name": (1, 2, (8, 0), (), "name", None),
		"scale": (2, 2, (5, 0), (), "scale", None),
		"userProjectionIndex": (7, 2, (3, 0), (), "userProjectionIndex", None),
	}
	_prop_map_put_ = {
		"name" : ((1, LCID, 4, 0),()),
		"scale" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ksViewProjectionCollection(DispatchBaseClass):
	'��������� ������� �������� ����������� ������ � ����.'
	CLSID = IID('{A174F872-C800-409E-9FB2-FF5B89D8B4B8}')
	coclass_clsid = IID('{9A3E39C6-B6AB-42CF-9FBD-AC05F0B4B161}')

	def Add(self, entity=defaultNamedNotOptArg):
		'�������� ������� � ����� �������.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 0),),entity
			)

	def AddUnfoldProjection(self, place=defaultNamedNotOptArg):
		'�������� �������� ����������� - ���������.'
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), ((12, 0),),place
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddUnfoldProjection', None)
		return ret

	def DetachByBody(self, entity=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((9, 0),),entity
			)

	def DetachByIndex(self, index=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((3, 0),),index
			)

	def DetachByName(self, name=defaultNamedNotOptArg):
		'����������� �������.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((8, 0),),name
			)

	def FindIt(self, entity=defaultNamedNotOptArg):
		'�������� ������ ��������.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), ((9, 0),),entity
			)

	def First(self):
		'������ �������.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'First', None)
		return ret

	def GetBaseUserOrientation(self):
		'�������� ������� ���������������� ������� ���������� ������.'
		return self._ApplyTypes_(17, 1, (12, 0), (), 'GetBaseUserOrientation', None,)

	def GetByIndex(self, index=defaultNamedNotOptArg):
		'�������� ������� �� �������.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 0),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByIndex', None)
		return ret

	def GetByName(self, name=defaultNamedNotOptArg, testFullName=False, testIgnoreCase=True):
		'�������� ��������� �� ��������� �������� �� �����.'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), ((8, 0), (11, 48), (11, 48)),name
			, testFullName, testIgnoreCase)
		if ret is not None:
			ret = Dispatch(ret, 'GetByName', None)
		return ret

	def GetCount(self):
		'�������� ���������� �������� � �������.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def Last(self):
		'��������� �������.'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Last', None)
		return ret

	def NewViewProjection(self):
		'����� ��������, � ��������� �� �����������.'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'NewViewProjection', None)
		return ret

	def Next(self):
		'��������� �������.'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Next', None)
		return ret

	def Prev(self):
		'���������� �������.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Prev', None)
		return ret

	def SetBaseUserOrientation(self, place=defaultNamedNotOptArg):
		'���������� ���������������� ������� ���������� ������.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((12, 0),),place
			)

	def refresh(self):
		'�������� ������.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"viewProjectionScheme": (15, 2, (3, 0), (), "viewProjectionScheme", None),
	}
	_prop_map_put_ = {
		"viewProjectionScheme" : ((15, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
class ABreakDimParam(CoClassBaseClass): # A CoClass
	# ��������� �������� ������� � �������.
	CLSID = IID('{7F7D6FC2-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksABreakDimParam,
	]
	default_interface = ksABreakDimParam

class ADimParam(CoClassBaseClass): # A CoClass
	# ��������� �������� �������.
	CLSID = IID('{7F7D6FE0-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksADimParam,
	]
	default_interface = ksADimParam

class ADimSourceParam(CoClassBaseClass): # A CoClass
	# ��������� �������� �������� �������.
	CLSID = IID('{7F7D6FDA-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksADimSourceParam,
	]
	default_interface = ksADimSourceParam

class AdditionFormatParam(CoClassBaseClass): # A CoClass
	# ��������� ��� ����������� � �������������� ������� jgs, sat,xt,x_b, step, stl, VRML..
	CLSID = IID('{13DF9CCA-122C-4CEC-87FA-CF16818E013A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAdditionFormatParam,
	]
	default_interface = ksAdditionFormatParam

class AggregateDefinition(CoClassBaseClass): # A CoClass
	# ��������� ������� ��������
	CLSID = IID('{8E8A474C-5ED5-4C72-AED6-EB04C317C7DE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAggregateDefinition,
	]
	default_interface = ksAggregateDefinition

# This CoClass is known by the name 'KOMPAS.Application.5'
class Application(CoClassBaseClass): # A CoClass
	# ��������� ���������� ������ 3D.
	CLSID = IID('{6B0B5194-4ACD-4095-9BC1-11179FBBB05A}')
	coclass_sources = [
		ksKompasObjectNotify,
	]
	default_source = ksKompasObjectNotify
	coclass_interfaces = [
		KompasObject,
	]
	default_interface = KompasObject

class Arc3dParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� 3d Arc.
	CLSID = IID('{4CA2655E-EC4E-433C-9706-8E3864D5DBD2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksArc3dParam,
	]
	default_interface = ksArc3dParam

class ArcByAngleParam(CoClassBaseClass): # A CoClass
	# ��������� ���� �� ������ � ���� �����.
	CLSID = IID('{7F7D6F8C-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksArcByAngleParam,
	]
	default_interface = ksArcByAngleParam

class ArcByPointParam(CoClassBaseClass): # A CoClass
	# ��������� ���� �� ������ � ���� ������.
	CLSID = IID('{7F7D6F8F-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksArcByPointParam,
	]
	default_interface = ksArcByPointParam

class AssociationViewParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� �������������� ����.
	CLSID = IID('{7A86E2BA-6DE3-4DB3-AEB6-9738DAA69CFC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAssociationViewParam,
	]
	default_interface = ksAssociationViewParam

class Attribute3D(CoClassBaseClass): # A CoClass
	# ��������� ��������.
	CLSID = IID('{620BFE17-2F66-4102-A8EA-4DD33C081061}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAttribute3D,
	]
	default_interface = ksAttribute3D

class Attribute3DCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� ���������.
	CLSID = IID('{17CAB61A-770A-4FCE-8FC5-F291CDADF80A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAttribute3DCollection,
	]
	default_interface = ksAttribute3DCollection

class AttributeObject(CoClassBaseClass): # A CoClass
	# ��������� ��������.
	CLSID = IID('{FA93AA26-9B3D-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAttributeObject,
	]
	default_interface = ksAttributeObject

class AttributeParam(CoClassBaseClass): # A CoClass
	# ��������� ��������.
	CLSID = IID('{CE0D05E6-9B2A-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAttributeParam,
	]
	default_interface = ksAttributeParam

class AttributeTypeParam(CoClassBaseClass): # A CoClass
	# ��������� ���� ��������.
	CLSID = IID('{CC26DA63-9B22-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAttributeTypeParam,
	]
	default_interface = ksAttributeTypeParam

class Axis2PlanesDefinition(CoClassBaseClass): # A CoClass
	# ��� �� ���� ����������.
	CLSID = IID('{0307BB83-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAxis2PlanesDefinition,
	]
	default_interface = ksAxis2PlanesDefinition

class Axis2PointsDefinition(CoClassBaseClass): # A CoClass
	# ��� �� ���� ������.
	CLSID = IID('{0307BB89-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAxis2PointsDefinition,
	]
	default_interface = ksAxis2PointsDefinition

class AxisConefaceDefinition(CoClassBaseClass): # A CoClass
	# ��� ���������� �����.
	CLSID = IID('{C6BD0D90-C8BE-4378-9A71-835597A7D1E9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAxisConefaceDefinition,
	]
	default_interface = ksAxisConefaceDefinition

class AxisEdgeDefinition(CoClassBaseClass): # A CoClass
	# ��� �� �����.
	CLSID = IID('{0307BB8C-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAxisEdgeDefinition,
	]
	default_interface = ksAxisEdgeDefinition

class AxisLineParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ������ �����.
	CLSID = IID('{705962E9-5E9B-4379-8504-FA754D11FC66}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAxisLineParam,
	]
	default_interface = ksAxisLineParam

class AxisOperationsDefinition(CoClassBaseClass): # A CoClass
	# ��� ��������.
	CLSID = IID('{0307BB86-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksAxisOperationsDefinition,
	]
	default_interface = ksAxisOperationsDefinition

class BaseEvolutionDefinition(CoClassBaseClass): # A CoClass
	# ��������� ������� �������������� ��������.
	CLSID = IID('{DEEFEFFB-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBaseEvolutionDefinition,
	]
	default_interface = ksBaseEvolutionDefinition

class BaseExtrusionDefinition(CoClassBaseClass): # A CoClass
	# ��������� ������� �������� ������������.
	CLSID = IID('{DEEFEFE3-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBaseExtrusionDefinition,
	]
	default_interface = ksBaseExtrusionDefinition

class BaseLoftDefinition(CoClassBaseClass): # A CoClass
	# ������� �������� �� ��������.
	CLSID = IID('{DEEFEFEC-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBaseLoftDefinition,
	]
	default_interface = ksBaseLoftDefinition

class BaseParam(CoClassBaseClass): # A CoClass
	# ��������� ����������� ����.
	CLSID = IID('{E79C2515-9584-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBaseParam,
	]
	default_interface = ksBaseParam

class BaseRotatedDefinition(CoClassBaseClass): # A CoClass
	# ������� �������� ��������.
	CLSID = IID('{2DFACC69-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBaseRotatedDefinition,
	]
	default_interface = ksBaseRotatedDefinition

class BezierParam(CoClassBaseClass): # A CoClass
	# ��������� bezier �������.
	CLSID = IID('{7F7D6FC8-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBezierParam,
	]
	default_interface = ksBezierParam

class BezierPointParam(CoClassBaseClass): # A CoClass
	# ��������� ���� ��� Bezier - ������.
	CLSID = IID('{7F7D6FCB-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBezierPointParam,
	]
	default_interface = ksBezierPointParam

class BodyCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� ��� 3D.
	CLSID = IID('{EEEAB203-43D8-4F04-A7CE-010D9BA419C2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBodyCollection,
	]
	default_interface = ksBodyCollection

class BossEvolutionDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ��������� ��������������.
	CLSID = IID('{DEEFEFFE-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBossEvolutionDefinition,
	]
	default_interface = ksBossEvolutionDefinition

class BossExtrusionDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ������������.
	CLSID = IID('{DEEFEFE6-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBossExtrusionDefinition,
	]
	default_interface = ksBossExtrusionDefinition

class BossLoftDefinition(CoClassBaseClass): # A CoClass
	# �������� ������������ �� ��������.
	CLSID = IID('{DEEFEFEF-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBossLoftDefinition,
	]
	default_interface = ksBossLoftDefinition

class BossRotatedDefinition(CoClassBaseClass): # A CoClass
	# �������� ������������.
	CLSID = IID('{2DFACC6C-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBossRotatedDefinition,
	]
	default_interface = ksBossRotatedDefinition

class BreakDimDrawing(CoClassBaseClass): # A CoClass
	# ��������� ��������� ��������� � �������� ������� � �������.
	CLSID = IID('{7F7D6FBC-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBreakDimDrawing,
	]
	default_interface = ksBreakDimDrawing

class CON(CoClassBaseClass): # A CoClass
	# ������ ��������� ����� ����������.
	CLSID = IID('{9CC1A2E2-29A8-49BB-ABF6-792FA2D38014}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCON,
	]
	default_interface = ksCON

class CentreParam(CoClassBaseClass): # A CoClass
	# ��������� ������� ����������� ������.
	CLSID = IID('{7F7D6FA7-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCentreParam,
	]
	default_interface = ksCentreParam

class ChamferDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� �����.
	CLSID = IID('{0307BBB0-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksChamferDefinition,
	]
	default_interface = ksChamferDefinition

class ChangeLeaderParam(CoClassBaseClass): # A CoClass
	# ����� ������� ��� ����������� ������������.
	CLSID = IID('{BC662523-43E2-41FF-A04B-3D92F8097DF9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksChangeLeaderParam,
	]
	default_interface = ksChangeLeaderParam

class Char255(CoClassBaseClass): # A CoClass
	# ������ ������ ������� 255 ��������.
	CLSID = IID('{3F715E3B-97D9-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksChar255,
	]
	default_interface = ksChar255

class ChooseBodies(CoClassBaseClass): # A CoClass
	# ��������� ������� ����������	��� ��� ��������� � ��������.
	CLSID = IID('{9B59D68B-3502-4FE9-9E09-AC691443BF3E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksChooseBodies,
	]
	default_interface = ksChooseBodies

class ChooseMng(CoClassBaseClass): # A CoClass
	# ��������� ��������� ������ (���������) ��������.
	CLSID = IID('{2280DF87-5688-4082-8FAE-6E4C84249352}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksChooseMng,
	]
	default_interface = ksChooseMng

class ChooseParts(CoClassBaseClass): # A CoClass
	# ��������� ������� ���������� ��� ����������� ������ � ��������� ��������.
	CLSID = IID('{9FD4E52C-5B9B-4D07-B788-8D188EF940FD}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksChooseParts,
	]
	default_interface = ksChooseParts

class Circle3dParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� 3d Circle.
	CLSID = IID('{4E96B6C2-BF75-4B32-A4E7-7267F60A2593}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCircle3dParam,
	]
	default_interface = ksCircle3dParam

class CircleParam(CoClassBaseClass): # A CoClass
	# ��������� ����������.
	CLSID = IID('{7F7D6F89-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCircleParam,
	]
	default_interface = ksCircleParam

class CircularCopyDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ����������� �� ��������������� �����.
	CLSID = IID('{0307BB92-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCircularCopyDefinition,
	]
	default_interface = ksCircularCopyDefinition

class CircularPartArrayDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ������ ����������� �� ��������������� �����.
	CLSID = IID('{DDD05145-C180-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCircularPartArrayDefinition,
	]
	default_interface = ksCircularPartArrayDefinition

class ColorParam(CoClassBaseClass): # A CoClass
	# �������� ����� �������.
	CLSID = IID('{2DFACC63-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksColorParam,
	]
	default_interface = ksColorParam

class ColumnInfoParam(CoClassBaseClass): # A CoClass
	# �������������� ��������� ��� ������ ������� ���������� ��������.
	CLSID = IID('{CE0D05E3-9B2A-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksColumnInfoParam,
	]
	default_interface = ksColumnInfoParam

class ComponentPositioner(CoClassBaseClass): # A CoClass
	# ��������� ���������� ���������� ����������� � ������.
	CLSID = IID('{7DAB018D-9EF9-4D0F-84BB-54B3DC0558D3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksComponentPositioner,
	]
	default_interface = ksComponentPositioner

class ConeParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ���������� �����������.
	CLSID = IID('{3940C963-446D-4701-883C-A93BBDAC5469}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksConeParam,
	]
	default_interface = ksConeParam

class ConicArcParam(CoClassBaseClass): # A CoClass
	# ��������� ��� ���������� ����������� �������.
	CLSID = IID('{7F7D6FA4-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksConicArcParam,
	]
	default_interface = ksConicArcParam

class ConicSpiralDefinition(CoClassBaseClass): # A CoClass
	# ������� ����������.
	CLSID = IID('{0307BB9E-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksConicSpiralDefinition,
	]
	default_interface = ksConicSpiralDefinition

class ConjunctivePointDefinition(CoClassBaseClass): # A CoClass
	# ��������� ������� '����������������� �����'.
	CLSID = IID('{88BD7F23-21A6-4C90-B784-0B38FB7FD0F3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksConjunctivePointDefinition,
	]
	default_interface = ksConjunctivePointDefinition

class ConstraintParam(CoClassBaseClass): # A CoClass
	# ��������� ��� ��������������� �����������.
	CLSID = IID('{77C095F7-3ABC-4292-B9E1-C112620AFC56}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksConstraintParam,
	]
	default_interface = ksConstraintParam

class ContourParam(CoClassBaseClass): # A CoClass
	# ��������� �������.
	CLSID = IID('{E79C2506-9584-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksContourParam,
	]
	default_interface = ksContourParam

class ControlPointDefinition(CoClassBaseClass): # A CoClass
	# ��������� ������� '����������� �����'.
	CLSID = IID('{3DA1922B-1FAB-4990-8D9A-8F03AFDB18D9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksControlPointDefinition,
	]
	default_interface = ksControlPointDefinition

class Coordinate3dCollection(CoClassBaseClass): # A CoClass
	# ��������� ��������� ��������� ����� � 3D.
	CLSID = IID('{17150452-8320-4721-9765-13353F08AE7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCoordinate3dCollection,
	]
	default_interface = ksCoordinate3dCollection

class CopyObjectParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ��� ����������� ������� 2d ���������.
	CLSID = IID('{8867DEAC-C699-41B6-BD3D-C470A52B1B9C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCopyObjectParam,
	]
	default_interface = ksCopyObjectParam

class CornerParam(CoClassBaseClass): # A CoClass
	# ��������� ����� ��� ��������������� � ���������������.
	CLSID = IID('{E79C2503-9584-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCornerParam,
	]
	default_interface = ksCornerParam

class Curve3D(CoClassBaseClass): # A CoClass
	# ��������� �������������� ������ � ���������� ������������.
	CLSID = IID('{54152184-0B08-4DFB-8249-4579A7368BF4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCurve3D,
	]
	default_interface = ksCurve3D

class CurveCopyDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ����������� �� ������.
	CLSID = IID('{0307BB95-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCurveCopyDefinition,
	]
	default_interface = ksCurveCopyDefinition

class CurvePartArrayDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ������ ����������� ����� ������.
	CLSID = IID('{DDD05148-C180-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCurvePartArrayDefinition,
	]
	default_interface = ksCurvePartArrayDefinition

class CurvePattern(CoClassBaseClass): # A CoClass
	# ������� ��������� ������.
	CLSID = IID('{910EC546-958D-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCurvePattern,
	]
	default_interface = ksCurvePattern

class CurvePatternEx(CoClassBaseClass): # A CoClass
	# ��������� ������� ��������� ������ �����������.
	CLSID = IID('{910EC54B-958D-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCurvePatternEx,
	]
	default_interface = ksCurvePatternEx

class CurvePicture(CoClassBaseClass): # A CoClass
	# ��������� ���������� ��� �������� �����.
	CLSID = IID('{910EC543-958D-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCurvePicture,
	]
	default_interface = ksCurvePicture

class CurveStyleParam(CoClassBaseClass): # A CoClass
	# ����� ������.
	CLSID = IID('{910EC54E-958D-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCurveStyleParam,
	]
	default_interface = ksCurveStyleParam

class CutByPlaneDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ������� ����������.
	CLSID = IID('{DEEFF007-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCutByPlaneDefinition,
	]
	default_interface = ksCutByPlaneDefinition

class CutBySketchDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ������� �������.
	CLSID = IID('{DEEFF00A-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCutBySketchDefinition,
	]
	default_interface = ksCutBySketchDefinition

class CutEvolutionDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� �������� �������������.
	CLSID = IID('{DEEFF001-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCutEvolutionDefinition,
	]
	default_interface = ksCutEvolutionDefinition

class CutExtrusionDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ���������.
	CLSID = IID('{DEEFEFE9-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCutExtrusionDefinition,
	]
	default_interface = ksCutExtrusionDefinition

class CutLineParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����� �������/�������.
	CLSID = IID('{4FD7CE83-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCutLineParam,
	]
	default_interface = ksCutLineParam

class CutLoftDefinition(CoClassBaseClass): # A CoClass
	# �������� ��������� �� ��������.
	CLSID = IID('{DEEFEFF2-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCutLoftDefinition,
	]
	default_interface = ksCutLoftDefinition

class CutRotatedDefinition(CoClassBaseClass): # A CoClass
	# �������� ���������.
	CLSID = IID('{2DFACC6F-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCutRotatedDefinition,
	]
	default_interface = ksCutRotatedDefinition

class CylinderParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ���������� �����������.
	CLSID = IID('{379D658E-47BB-414F-A952-FB41037F17AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCylinderParam,
	]
	default_interface = ksCylinderParam

class CylindricSpiralDefinition(CoClassBaseClass): # A CoClass
	# ������� ��������������.
	CLSID = IID('{0307BBA1-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksCylindricSpiralDefinition,
	]
	default_interface = ksCylindricSpiralDefinition

class DataBaseObject(CoClassBaseClass): # A CoClass
	# �������� � ��.
	CLSID = IID('{0981CD03-9A49-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDataBaseObject,
	]
	default_interface = ksDataBaseObject

class DefaultObject(CoClassBaseClass): # A CoClass
	# ������������� ������.
	CLSID = IID('{508A0CC9-9D74-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDefaultObject,
	]
	default_interface = ksDefaultObject

class DeletedCopyCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� ��������� �������� ��� ������� ����������� � �������� ���������.
	CLSID = IID('{9807E658-53C5-4445-A389-3F800FB3BB8A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDeletedCopyCollection,
	]
	default_interface = ksDeletedCopyCollection

class DerivativePartArrayDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ������ ����������� �� �������.
	CLSID = IID('{DDD0514B-C180-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDerivativePartArrayDefinition,
	]
	default_interface = ksDerivativePartArrayDefinition

class DimDrawingParam(CoClassBaseClass): # A CoClass
	# ��������� ��������� ��������� � �������� ��������.
	CLSID = IID('{7F7D6FD4-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDimDrawingParam,
	]
	default_interface = ksDimDrawingParam

class DimTextParam(CoClassBaseClass): # A CoClass
	# ��������� ��������� �������.
	CLSID = IID('{7F7D6FCE-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDimTextParam,
	]
	default_interface = ksDimTextParam

class DimensionPartsParam(CoClassBaseClass): # A CoClass
	# ��������� ������������ �������� �������.
	CLSID = IID('{7F7D6FDD-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDimensionPartsParam,
	]
	default_interface = ksDimensionPartsParam

class DimensionsOptions(CoClassBaseClass): # A CoClass
	# ��������� ��� ����������� �������� ��������.
	CLSID = IID('{FBCC5B9B-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDimensionsOptions,
	]
	default_interface = ksDimensionsOptions

class DocAttachedSpcParam(CoClassBaseClass): # A CoClass
	# ��������� �������������� ��������� � ������� ������������.
	CLSID = IID('{4FD7CEAA-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDocAttachedSpcParam,
	]
	default_interface = ksDocAttachedSpcParam

class Document2D(CoClassBaseClass): # A CoClass
	# 2D ��������.
	CLSID = IID('{14FD27F5-B7FD-4276-AC2C-2804EDC3944F}')
	coclass_sources = [
		ksDocumentFileNotify,
	]
	default_source = ksDocumentFileNotify
	coclass_interfaces = [
		ksDocument2D,
	]
	default_interface = ksDocument2D

class Document2DNotify(CoClassBaseClass): # A CoClass
	# ������� 2D ���������.
	CLSID = IID('{1B9B9B4E-DCD7-496E-A583-547EC1E91E47}')
	coclass_sources = [
		ksDocument2DNotify,
	]
	default_source = ksDocument2DNotify
	coclass_interfaces = [
	]

class Document3D(CoClassBaseClass): # A CoClass
	# 3D ��������.
	CLSID = IID('{111CEFE3-A0A7-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
		ksDocumentFileNotify,
	]
	default_source = ksDocumentFileNotify
	coclass_interfaces = [
		ksDocument3D,
	]
	default_interface = ksDocument3D

class Document3DNotify(CoClassBaseClass): # A CoClass
	# ������� ��� 3D ���������.
	CLSID = IID('{22B81342-42D6-4907-A91E-F75A959F2270}')
	coclass_sources = [
		ksDocument3DNotify,
	]
	default_source = ksDocument3DNotify
	coclass_interfaces = [
	]

class Document3DNotifyResult(CoClassBaseClass): # A CoClass
	# �������������� ��������� ��� ������� ���������� 3D.
	CLSID = IID('{129E9083-E4D2-4991-B69F-70B696AD1A55}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDocument3DNotifyResult,
	]
	default_interface = ksDocument3DNotifyResult

class DocumentParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ���������.
	CLSID = IID('{FBCC5B98-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDocumentParam,
	]
	default_interface = ksDocumentParam

class DocumentTxt(CoClassBaseClass): # A CoClass
	# ��������� ��������.
	CLSID = IID('{74D745F3-9A3A-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
		ksDocumentFileNotify,
	]
	default_source = ksDocumentFileNotify
	coclass_interfaces = [
		ksDocumentTxt,
	]
	default_interface = ksDocumentTxt

class DoubleValue(CoClassBaseClass): # A CoClass
	# ��������� ����.
	CLSID = IID('{7F7D6F9E-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDoubleValue,
	]
	default_interface = ksDoubleValue

class DynamicArray(CoClassBaseClass): # A CoClass
	# ��������� ������������� �������.
	CLSID = IID('{FD30B325-9E27-42CA-ADCF-C30EEBE0BBB8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksDynamicArray,
	]
	default_interface = ksDynamicArray

class EdgeCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� �����.
	CLSID = IID('{7519BF63-27B3-415F-AC25-904910CB27B5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksEdgeCollection,
	]
	default_interface = ksEdgeCollection

class EdgeDefinition(CoClassBaseClass): # A CoClass
	# ��������� �����.
	CLSID = IID('{0307BBAD-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksEdgeDefinition,
	]
	default_interface = ksEdgeDefinition

class Ellipse3dParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� 3d Ellipse.
	CLSID = IID('{33583282-14FB-4975-B040-9267A639E340}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksEllipse3dParam,
	]
	default_interface = ksEllipse3dParam

class EllipseArcParam(CoClassBaseClass): # A CoClass
	# ��������� ���� ������� �� �����.
	CLSID = IID('{364521AB-94B5-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksEllipseArcParam,
	]
	default_interface = ksEllipseArcParam

class EllipseArcParam1(CoClassBaseClass): # A CoClass
	# ��������� ���� ������� �� ����������.
	CLSID = IID('{364521AE-94B5-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksEllipseArcParam1,
	]
	default_interface = ksEllipseArcParam1

class EllipseParam(CoClassBaseClass): # A CoClass
	# ��������� �������.
	CLSID = IID('{364521A8-94B5-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksEllipseParam,
	]
	default_interface = ksEllipseParam

class EntityCollection(CoClassBaseClass): # A CoClass
	# ������ ��������.
	CLSID = IID('{B0170143-C02C-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksEntityCollection,
	]
	default_interface = ksEntityCollection

class EquidistantParam(CoClassBaseClass): # A CoClass
	# ��������� ������������.
	CLSID = IID('{364521B1-94B5-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksEquidistantParam,
	]
	default_interface = ksEquidistantParam

class EvolutionSurfaceDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������������� �����������.
	CLSID = IID('{DB947005-AA19-4ED2-9775-E7BD80BE872E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksEvolutionSurfaceDefinition,
	]
	default_interface = ksEvolutionSurfaceDefinition

class ExtrusionParam(CoClassBaseClass): # A CoClass
	# ��������� ������������.
	CLSID = IID('{DEEFF02E-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksExtrusionParam,
	]
	default_interface = ksExtrusionParam

class ExtrusionSurfaceDefinition(CoClassBaseClass): # A CoClass
	# ��������� ����������� ������������.
	CLSID = IID('{31E66F64-B93D-4196-B3FE-B6CCB679610F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksExtrusionSurfaceDefinition,
	]
	default_interface = ksExtrusionSurfaceDefinition

class FaceCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� ������.
	CLSID = IID('{CB7B9677-9F62-473E-9663-AD516B5F37B5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksFaceCollection,
	]
	default_interface = ksFaceCollection

class Feature(CoClassBaseClass): # A CoClass
	# ��������� ������� ������.
	CLSID = IID('{1978BA1C-EE2F-48ED-86D7-B15065B36E4A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksFeature,
	]
	default_interface = ksFeature

class FeatureCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� �������� ������.
	CLSID = IID('{87CD4F95-083C-4514-B8B4-025C8907D8F1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksFeatureCollection,
	]
	default_interface = ksFeatureCollection

class FilletDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ����������.
	CLSID = IID('{0307BBB3-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksFilletDefinition,
	]
	default_interface = ksFilletDefinition

class Fragment(CoClassBaseClass): # A CoClass
	# ��������.
	CLSID = IID('{D06C9106-98CA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksFragment,
	]
	default_interface = ksFragment

class FragmentLib(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����������.
	CLSID = IID('{D06C910C-98CA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksFragmentLibrary,
	]
	default_interface = ksFragmentLibrary

class HatchLineParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����� ���������.
	CLSID = IID('{3F715E29-97D9-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksHatchLineParam,
	]
	default_interface = ksHatchLineParam

class HatchParam(CoClassBaseClass): # A CoClass
	# ��������� ���������.
	CLSID = IID('{7F7D6F95-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksHatchParam,
	]
	default_interface = ksHatchParam

class HatchStyleParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����� ���������.
	CLSID = IID('{3F715E2C-97D9-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksHatchStyleParam,
	]
	default_interface = ksHatchStyleParam

class ImportedSurfaceDefinition(CoClassBaseClass): # A CoClass
	# ��������� ��������������� �����������.
	CLSID = IID('{102FA83C-E0D6-4DB5-937A-FC149526899A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksImportedSurfaceDefinition,
	]
	default_interface = ksImportedSurfaceDefinition

class InclineDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� �����.
	CLSID = IID('{DEEFEFF5-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksInclineDefinition,
	]
	default_interface = ksInclineDefinition

class InertiaParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ��� ������� ������� ��������-������������ �������������.
	CLSID = IID('{7B8B632E-5BDD-4EE5-B623-DF2880BE0EE4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksInertiaParam,
	]
	default_interface = ksInertiaParam

class InsertFragmentParam(CoClassBaseClass): # A CoClass
	# ��������� ������� ����������.
	CLSID = IID('{7F7D6FB3-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksInsertFragmentParam,
	]
	default_interface = ksInsertFragmentParam

class InsertFragmentParamEx(CoClassBaseClass): # A CoClass
	# ��������� ������� ����������.
	CLSID = IID('{7F7D6FC5-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksInsertFragmentParamEx,
	]
	default_interface = ksInsertFragmentParamEx

class IntersectionResult(CoClassBaseClass): # A CoClass
	# ��������� ����������� �����������.
	CLSID = IID('{ED41E352-E8A8-4B12-893F-17F064985CEE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksIntersectionResult,
	]
	default_interface = ksIntersectionResult

class Iterator(CoClassBaseClass): # A CoClass
	# �������� �� �������� ��������� ����.
	CLSID = IID('{D06C9103-98CA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksIterator,
	]
	default_interface = ksIterator

# This CoClass is known by the name 'KSINVISIBLE.Application.5'
class KompasInvisible5(CoClassBaseClass): # A CoClass
	# KompasInvisible5.
	CLSID = IID('{FBE002A6-1E06-4703-AEC5-9AD8A10FA1FA}')
	coclass_sources = [
		ksKompasObjectNotify,
	]
	default_source = ksKompasObjectNotify
	coclass_interfaces = [
		KompasObject,
	]
	default_interface = KompasObject

class LBreakDimParam(CoClassBaseClass): # A CoClass
	# ��������� ��������� ������� � �������.
	CLSID = IID('{7F7D6FBF-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLBreakDimParam,
	]
	default_interface = ksLBreakDimParam

class LBreakDimSource(CoClassBaseClass): # A CoClass
	# ��������� �������� ��������� ������� � �������.
	CLSID = IID('{7F7D6FB9-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLBreakDimSource,
	]
	default_interface = ksLBreakDimSource

class LDimParam(CoClassBaseClass): # A CoClass
	# ��������� ��������� �������.
	CLSID = IID('{7F7D6FD7-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLDimParam,
	]
	default_interface = ksLDimParam

class LDimSourceParam(CoClassBaseClass): # A CoClass
	# ��������� �������� ��������� �������.
	CLSID = IID('{7F7D6FD1-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLDimSourceParam,
	]
	default_interface = ksLDimSourceParam

class LayerParam(CoClassBaseClass): # A CoClass
	# ��������� ����.
	CLSID = IID('{E79C2509-9584-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLayerParam,
	]
	default_interface = ksLayerParam

class LibStyle(CoClassBaseClass): # A CoClass
	# C�������� ���������� ��� ����������� ����� �� ����������.
	CLSID = IID('{4FD7CEB0-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLibStyle,
	]
	default_interface = ksLibStyle

class LibraryAttrTypeParam(CoClassBaseClass): # A CoClass
	# ��������� ��� ���� �������� ���������� ����� ���������.
	CLSID = IID('{FA93AA23-9B3D-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLibraryAttrTypeParam,
	]
	default_interface = ksLibraryAttrTypeParam

class LibraryStyleParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ��� ����� � ���������� ������.
	CLSID = IID('{FBCC5BA1-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLibraryStyleParam,
	]
	default_interface = ksLibraryStyleParam

class LineParam(CoClassBaseClass): # A CoClass
	# ��������� ��������������� �����.
	CLSID = IID('{E79C250C-9584-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLineParam,
	]
	default_interface = ksLineParam

class LineSeg3dParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� 3d LineSeg.
	CLSID = IID('{4D295A34-4F20-4231-8806-78E40213FA72}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLineSeg3dParam,
	]
	default_interface = ksLineSeg3dParam

class LineSegParam(CoClassBaseClass): # A CoClass
	# ��������� �������.
	CLSID = IID('{7F7D6F86-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLineSegParam,
	]
	default_interface = ksLineSegParam

class LoftSurfaceDefinition(CoClassBaseClass): # A CoClass
	# ����������� �� ��������.
	CLSID = IID('{5E1EB940-4CAE-43DE-B56D-8733FF6707DF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLoftSurfaceDefinition,
	]
	default_interface = ksLoftSurfaceDefinition

class Loop(CoClassBaseClass): # A CoClass
	# ��������� �����.
	CLSID = IID('{38386E28-C404-431E-9F30-5BE44B0F283F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLoop,
	]
	default_interface = ksLoop

class LoopCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� ������.
	CLSID = IID('{3EA3B143-96A5-408A-897E-27D852E6EE9B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLoopCollection,
	]
	default_interface = ksLoopCollection

class LtVariant(CoClassBaseClass): # A CoClass
	# ��������� ���� ������.
	CLSID = IID('{E79C2518-9584-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLtVariant,
	]
	default_interface = ksLtVariant

class Macro3DDefinition(CoClassBaseClass): # A CoClass
	# ��������� ������������ 3D.
	CLSID = IID('{DC7D3EDF-80EE-4BAF-930F-F221AC7E5A7A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMacro3DDefinition,
	]
	default_interface = ksMacro3DDefinition

class MassInertiaParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ��� ������� �����-������������ �������������.
	CLSID = IID('{4693323B-42A7-42CC-902E-7123DD916FB4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMassInertiaParam,
	]
	default_interface = ksMassInertiaParam

class MateConstraint(CoClassBaseClass): # A CoClass
	# 3D ������ - ����������.
	CLSID = IID('{508A0CC6-9D74-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMateConstraint,
	]
	default_interface = ksMateConstraint

class MateConstraintCollection(CoClassBaseClass): # A CoClass
	# ������ ����������.
	CLSID = IID('{03CEAC86-C0B8-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMateConstraintCollection,
	]
	default_interface = ksMateConstraintCollection

class MathPointParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� �������������� �����.
	CLSID = IID('{3198E123-9585-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMathPointParam,
	]
	default_interface = ksMathPointParam

class Mathematic2D(CoClassBaseClass): # A CoClass
	# 2D �������������� �������.
	CLSID = IID('{C77421D3-13EC-4595-A198-677EFB45AEF3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMathematic2D,
	]
	default_interface = ksMathematic2D

class Measurer(CoClassBaseClass): # A CoClass
	# ��������� ��� ��������� ���������� � ���� ����� ����� ����������� ( �������, �������, ���������).
	CLSID = IID('{E07C6920-E361-4A4D-9140-95969C26A9ED}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMeasurer,
	]
	default_interface = ksMeasurer

class MeshCopyDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ����������� �� �����.
	CLSID = IID('{0307BB8F-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMeshCopyDefinition,
	]
	default_interface = ksMeshCopyDefinition

class MeshPartArrayDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ������ ����������� �� �����.
	CLSID = IID('{E6E78D63-C0FA-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMeshPartArrayDefinition,
	]
	default_interface = ksMeshPartArrayDefinition

class MirrorCopyAllDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ��������� ���������� ���.
	CLSID = IID('{0307BB9B-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMirrorCopyAllDefinition,
	]
	default_interface = ksMirrorCopyAllDefinition

class MirrorCopyDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ���������� �����.
	CLSID = IID('{0307BB98-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMirrorCopyDefinition,
	]
	default_interface = ksMirrorCopyDefinition

class ModelLibrary(CoClassBaseClass): # A CoClass
	# ��������� ���������� �������.
	CLSID = IID('{111CEFE6-A0A7-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksModelLibrary,
	]
	default_interface = ksModelLibrary

class MoldCavityDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ������� ����������.
	CLSID = IID('{FC4D7C29-C608-44D5-B927-1EC9FC147B18}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMoldCavityDefinition,
	]
	default_interface = ksMoldCavityDefinition

class NumberTypeAttrParam(CoClassBaseClass): # A CoClass
	# ����������� ��� ���� �������� DOUBLE_ATTR_TYPE � LINT_ATTR_TYPE.
	CLSID = IID('{4FD7CE92-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksNumberTypeAttrParam,
	]
	default_interface = ksNumberTypeAttrParam

class Nurbs3dParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� Nurbs-������� 3D.
	CLSID = IID('{F829344F-B49F-43A3-AC93-E817EF8D3319}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksNurbs3dParam,
	]
	default_interface = ksNurbs3dParam

class NurbsKnotCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� ����� ��� Nurbs 3D.
	CLSID = IID('{81317653-9BBA-46FE-9877-AEEE62BD8AA4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksNurbsKnotCollection,
	]
	default_interface = ksNurbsKnotCollection

class NurbsParam(CoClassBaseClass): # A CoClass
	# ��������� Nurbs-�������.
	CLSID = IID('{7F7D6FA1-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksNurbsParam,
	]
	default_interface = ksNurbsParam

class NurbsPoint3dCollCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� �������� ����� ��� Nurbs 3D Surface.
	CLSID = IID('{A2BD36E2-C99B-40FE-A6A7-E5A9CCDCF63D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksNurbsPoint3dCollCollection,
	]
	default_interface = ksNurbsPoint3dCollCollection

class NurbsPoint3dCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� ����� ��� Nurbs 3D.
	CLSID = IID('{25AE92BA-055F-431E-AC3E-EA2E793D446C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksNurbsPoint3dCollection,
	]
	default_interface = ksNurbsPoint3dCollection

class NurbsPoint3dParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����� ���  Nurbs 3D.
	CLSID = IID('{4F3C6D95-FBDC-4C53-AE82-9AF9C05093FF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksNurbsPoint3dParam,
	]
	default_interface = ksNurbsPoint3dParam

class NurbsPointParam(CoClassBaseClass): # A CoClass
	# ��������� ���� ��� Nurbs - ������.
	CLSID = IID('{7F7D6F9B-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksNurbsPointParam,
	]
	default_interface = ksNurbsPointParam

class NurbsSurfaceParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� Nurbs-�����������.
	CLSID = IID('{BA13BE42-059B-4EEB-9C39-673732763EE3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksNurbsSurfaceParam,
	]
	default_interface = ksNurbsSurfaceParam

class Object2DNotify(CoClassBaseClass): # A CoClass
	# ������� ������� 2D ���������.
	CLSID = IID('{C7EBA9A1-9E76-436E-B362-A80C5763944C}')
	coclass_sources = [
		ksObject2DNotify,
	]
	default_source = ksObject2DNotify
	coclass_interfaces = [
	]

class Object2DNotifyResult(CoClassBaseClass): # A CoClass
	# ��������� ����������� �������������� �������.
	CLSID = IID('{DE8219EC-0A9F-44E1-AC2B-F17269484FFF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksObject2DNotifyResult,
	]
	default_interface = ksObject2DNotifyResult

class Object3DNotify(CoClassBaseClass): # A CoClass
	# ������� ��� ������� 3D ���������.
	CLSID = IID('{CA35F3C6-7E2D-4700-BE12-BAA26DC1945B}')
	coclass_sources = [
		ksObject3DNotify,
	]
	default_source = ksObject3DNotify
	coclass_interfaces = [
	]

class Object3DNotifyResult(CoClassBaseClass): # A CoClass
	# ��������� ����������� �������������� ������� 3D ���������.
	CLSID = IID('{600F12DF-D8B8-4CA8-A476-D2A7E425C740}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksObject3DNotifyResult,
	]
	default_interface = ksObject3DNotifyResult

class ObjectsFilter3D(CoClassBaseClass): # A CoClass
	# ��������� ���������� �������� 3D.
	CLSID = IID('{ABBA6CE1-CB4C-4A32-98B4-B639352C75BA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksObjectsFilter3D,
	]
	default_interface = ksObjectsFilter3D

class OrdinatedDimParam(CoClassBaseClass): # A CoClass
	# ��������� ������� ������.
	CLSID = IID('{FBCC5B89-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksOrdinatedDimParam,
	]
	default_interface = ksOrdinatedDimParam

class OrdinatedDrawingParam(CoClassBaseClass): # A CoClass
	# ��������� ����������� ������� ������.
	CLSID = IID('{FBCC5B8C-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksOrdinatedDrawingParam,
	]
	default_interface = ksOrdinatedDrawingParam

class OrdinatedSourceParam(CoClassBaseClass): # A CoClass
	# ��������� �������� ������� ������.
	CLSID = IID('{FBCC5B86-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksOrdinatedSourceParam,
	]
	default_interface = ksOrdinatedSourceParam

class OrientedEdge(CoClassBaseClass): # A CoClass
	# ��������� ���������������� �����.
	CLSID = IID('{C66FB80F-97BE-4437-A8A0-AEDCFCBCF982}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksOrientedEdge,
	]
	default_interface = ksOrientedEdge

class OrientedEdgeCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� ��������������� �����.
	CLSID = IID('{6EF08DCB-A1D4-43A2-ACAF-AF32FDE5F338}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksOrientedEdgeCollection,
	]
	default_interface = ksOrientedEdgeCollection

class OverlapObjectOptions(CoClassBaseClass): # A CoClass
	# ��������� ���������� ��������������� ��������.
	CLSID = IID('{E41D019C-2D40-452D-8F7B-3FB5FE2D3E8E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksOverlapObjectOptions,
	]
	default_interface = ksOverlapObjectOptions

class ParagraphParam(CoClassBaseClass): # A CoClass
	# ��������� ���������.
	CLSID = IID('{364521B4-94B5-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksParagraphParam,
	]
	default_interface = ksParagraphParam

class ParametrizationParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ��������������.
	CLSID = IID('{ABBA6CE1-CB4C-4A32-98B4-B639352C75BB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksParametrizationParam,
	]
	default_interface = ksParametrizationParam

class PartCollection(CoClassBaseClass): # A CoClass
	# ������ ����������� ������.
	CLSID = IID('{03CEAC89-C0B8-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPartCollection,
	]
	default_interface = ksPartCollection

class PlacementParam(CoClassBaseClass): # A CoClass
	# ��������� ��������������.
	CLSID = IID('{7F7D6FAA-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlacementParam,
	]
	default_interface = ksPlacementParam

class Plane3PointsDefinition(CoClassBaseClass): # A CoClass
	# ��������� ��������� �� 3 ������.
	CLSID = IID('{DEEFF013-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlane3PointsDefinition,
	]
	default_interface = ksPlane3PointsDefinition

class PlaneAngleDefinition(CoClassBaseClass): # A CoClass
	# ��������� ��������� ��� �����.
	CLSID = IID('{DEEFF010-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlaneAngleDefinition,
	]
	default_interface = ksPlaneAngleDefinition

class PlaneEdgePointDefinition(CoClassBaseClass): # A CoClass
	# ��������� ��������� ����� ����� � �������.
	CLSID = IID('{DEEFF01C-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlaneEdgePointDefinition,
	]
	default_interface = ksPlaneEdgePointDefinition

class PlaneLineToEdgeDefinition(CoClassBaseClass): # A CoClass
	# ��������� ��������� ����� ����� ���-��/���-�� ������� �����.
	CLSID = IID('{DEEFF025-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlaneLineToEdgeDefinition,
	]
	default_interface = ksPlaneLineToEdgeDefinition

class PlaneLineToPlaneDefinition(CoClassBaseClass): # A CoClass
	# ��������� ��������� ����� ����� ���-��/���-�� �����.
	CLSID = IID('{DEEFF028-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlaneLineToPlaneDefinition,
	]
	default_interface = ksPlaneLineToPlaneDefinition

class PlaneMiddleDefinition(CoClassBaseClass): # A CoClass
	# ��������� ��������������� ��������� '������� ���������'.
	CLSID = IID('{D7844AFC-91B0-4C08-8622-0E4595BA6551}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlaneMiddleDefinition,
	]
	default_interface = ksPlaneMiddleDefinition

class PlaneNormalToSurfaceDefinition(CoClassBaseClass): # A CoClass
	# ��������� ���������� ���������.
	CLSID = IID('{DEEFF016-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlaneNormalToSurfaceDefinition,
	]
	default_interface = ksPlaneNormalToSurfaceDefinition

class PlaneOffsetDefinition(CoClassBaseClass): # A CoClass
	# ��������� ��������� ���������.
	CLSID = IID('{DEEFF00D-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlaneOffsetDefinition,
	]
	default_interface = ksPlaneOffsetDefinition

class PlaneParallelDefinition(CoClassBaseClass): # A CoClass
	# ��������� ��������� ����� ������� ����������� ������ ���������.
	CLSID = IID('{DEEFF01F-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlaneParallelDefinition,
	]
	default_interface = ksPlaneParallelDefinition

class PlaneParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ���������.
	CLSID = IID('{94A91D78-30AE-4B04-AEE2-B098D3270602}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlaneParam,
	]
	default_interface = ksPlaneParam

class PlanePerpendicularDefinition(CoClassBaseClass): # A CoClass
	# ��������� ��������� ����� ������� ��������������� �����.
	CLSID = IID('{DEEFF022-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlanePerpendicularDefinition,
	]
	default_interface = ksPlanePerpendicularDefinition

class PlaneTangentToSurfaceDefinition(CoClassBaseClass): # A CoClass
	# ��������� ����������� ���������.
	CLSID = IID('{DEEFF019-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlaneTangentToSurfaceDefinition,
	]
	default_interface = ksPlaneTangentToSurfaceDefinition

class PointParam(CoClassBaseClass): # A CoClass
	# ��������� �����.
	CLSID = IID('{7F7D6F92-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPointParam,
	]
	default_interface = ksPointParam

class PolyLineDefinition(CoClassBaseClass): # A CoClass
	# �������.
	CLSID = IID('{0307BBA4-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPolyLineDefinition,
	]
	default_interface = ksPolyLineDefinition

class PolylineParam(CoClassBaseClass): # A CoClass
	# ��������� ���������.
	CLSID = IID('{7F7D6FB0-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPolylineParam,
	]
	default_interface = ksPolylineParam

class QualityContensParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ���������.
	CLSID = IID('{7F7D6FEC-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksQualityContensParam,
	]
	default_interface = ksQualityContensParam

class QualityItemParam(CoClassBaseClass): # A CoClass
	# ������ �� ����� ��������� ��� ���������.
	CLSID = IID('{7F7D6FE9-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksQualityItemParam,
	]
	default_interface = ksQualityItemParam

class RBreakDimParam(CoClassBaseClass): # A CoClass
	# ��������� ����������� ������� � �������.
	CLSID = IID('{7F7D6FE6-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRBreakDimParam,
	]
	default_interface = ksRBreakDimParam

class RBreakDrawingParam(CoClassBaseClass): # A CoClass
	# ��������� �������� �������������� � ����������� ��������.
	CLSID = IID('{7F7D6FE3-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRBreakDrawingParam,
	]
	default_interface = ksRBreakDrawingParam

class RDimDrawingParam(CoClassBaseClass): # A CoClass
	# ��������� ��������� �������������� � ����������� ��������.
	CLSID = IID('{2A4D4544-95B3-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRDimDrawingParam,
	]
	default_interface = ksRDimDrawingParam

class RDimParam(CoClassBaseClass): # A CoClass
	# ��������� �������������� � ����������� �������.
	CLSID = IID('{7F7D6F83-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRDimParam,
	]
	default_interface = ksRDimParam

class RDimSourceParam(CoClassBaseClass): # A CoClass
	# ��������� �������� �������������� � ����������� ��������.
	CLSID = IID('{2A4D4547-95B3-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRDimSourceParam,
	]
	default_interface = ksRDimSourceParam

class RasterFormatParam(CoClassBaseClass): # A CoClass
	# ��������� ��� ����������� � ��������� ������.
	CLSID = IID('{CD6054FC-D754-4139-8CD9-381F7488A6C7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRasterFormatParam,
	]
	default_interface = ksRasterFormatParam

class RasterParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� �������.
	CLSID = IID('{7F7D6FAD-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRasterParam,
	]
	default_interface = ksRasterParam

class RecordTypeAttrParam(CoClassBaseClass): # A CoClass
	# ����������� ��� ���� �������� RECORD_ATTR_TYPE.
	CLSID = IID('{4FD7CE8F-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRecordTypeAttrParam,
	]
	default_interface = ksRecordTypeAttrParam

class RectParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����������� ��������������.
	CLSID = IID('{3F715E2F-97D9-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRectParam,
	]
	default_interface = ksRectParam

class RectangleParam(CoClassBaseClass): # A CoClass
	# ��������� ��������������.
	CLSID = IID('{E79C2512-9584-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRectangleParam,
	]
	default_interface = ksRectangleParam

class RegularPolygonParam(CoClassBaseClass): # A CoClass
	# ��������� ����������� ��������������.
	CLSID = IID('{E79C250F-9584-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRegularPolygonParam,
	]
	default_interface = ksRegularPolygonParam

class RemoteElementParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ��������� ��������.
	CLSID = IID('{F37A40F6-4E15-4E01-B4F0-25C49175227A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRemoteElementParam,
	]
	default_interface = ksRemoteElementParam

class RequestInfo(CoClassBaseClass): # A CoClass
	# ��������� ������� � �������.
	CLSID = IID('{9AF8E358-98A0-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRequestInfo,
	]
	default_interface = ksRequestInfo

class RequestInfo3D(CoClassBaseClass): # A CoClass
	# ��������� �������.
	CLSID = IID('{E9807826-9D55-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRequestInfo3D,
	]
	default_interface = ksRequestInfo3D

class RibDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� �����.
	CLSID = IID('{DEEFF004-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRibDefinition,
	]
	default_interface = ksRibDefinition

class RotatedParam(CoClassBaseClass): # A CoClass
	# ��������� ��������.
	CLSID = IID('{DEEFF031-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRotatedParam,
	]
	default_interface = ksRotatedParam

class RotatedSurfaceDefinition(CoClassBaseClass): # A CoClass
	# ������� �������� ��������.
	CLSID = IID('{8B9ECAF3-172D-4F4B-BF51-33C177B87FF2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRotatedSurfaceDefinition,
	]
	default_interface = ksRotatedSurfaceDefinition

class RoughParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� �������������.
	CLSID = IID('{3F715E38-97D9-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRoughParam,
	]
	default_interface = ksRoughParam

class SelectionMng(CoClassBaseClass): # A CoClass
	# ��������� ��������� ��������������� ��������.
	CLSID = IID('{39EE8E9D-C228-4F61-9F66-DD58F20CD224}')
	coclass_sources = [
		ksSelectionMngNotify,
	]
	default_source = ksSelectionMngNotify
	coclass_interfaces = [
		ksSelectionMng,
	]
	default_interface = ksSelectionMng

class SelectionMngNotify(CoClassBaseClass): # A CoClass
	# C������ ��� ��������� ��������������� ��������.
	CLSID = IID('{DC2E4057-7F8E-4652-860D-6B9E1F6F43AA}')
	coclass_sources = [
		ksSelectionMngNotify,
	]
	default_source = ksSelectionMngNotify
	coclass_interfaces = [
	]

class SheetOptions(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����������.
	CLSID = IID('{FBCC5BAA-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSheetOptions,
	]
	default_interface = ksSheetOptions

class SheetPar(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����������.
	CLSID = IID('{FBCC5B95-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSheetPar,
	]
	default_interface = ksSheetPar

class SheetSize(CoClassBaseClass): # A CoClass
	# ��������� �����.
	CLSID = IID('{FBCC5B8F-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSheetSize,
	]
	default_interface = ksSheetSize

class ShelfPar(CoClassBaseClass): # A CoClass
	# ��������� ���������� �������� �����.
	CLSID = IID('{3F715E32-97D9-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksShelfPar,
	]
	default_interface = ksShelfPar

class ShellDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ��������.
	CLSID = IID('{DEEFEFF8-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksShellDefinition,
	]
	default_interface = ksShellDefinition

class SketchDefinition(CoClassBaseClass): # A CoClass
	# ��������� ������.
	CLSID = IID('{2DFACC72-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSketchDefinition,
	]
	default_interface = ksSketchDefinition

class SnapOptions(CoClassBaseClass): # A CoClass
	# ��������� ���������� �������� � ����������� ���������.
	CLSID = IID('{FBCC5B9E-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSnapOptions,
	]
	default_interface = ksSnapOptions

class SpcColumnParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ��� ������� ������������.
	CLSID = IID('{4FD7CE8C-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSpcColumnParam,
	]
	default_interface = ksSpcColumnParam

class SpcDescrParam(CoClassBaseClass): # A CoClass
	# C�������� ���������� �������� ������������.
	CLSID = IID('{4FD7CEA7-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSpcDescrParam,
	]
	default_interface = ksSpcDescrParam

class SpcDocument(CoClassBaseClass): # A CoClass
	# �������� ������������.
	CLSID = IID('{51E74523-9A3A-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
		ksDocumentFileNotify,
	]
	default_source = ksDocumentFileNotify
	coclass_interfaces = [
		ksSpcDocument,
	]
	default_interface = ksSpcDocument

class SpcDocumentNotify(CoClassBaseClass): # A CoClass
	# ������� ��� ��������� ������������.
	CLSID = IID('{DC32EB43-4615-4717-8C67-48875A357B06}')
	coclass_sources = [
		ksSpcDocumentNotify,
	]
	default_source = ksSpcDocumentNotify
	coclass_interfaces = [
	]

class SpcObjParam(CoClassBaseClass): # A CoClass
	# C�������� ���������� ������� ������������.
	CLSID = IID('{4FD7CEAD-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSpcObjParam,
	]
	default_interface = ksSpcObjParam

class SpcObjectNotify(CoClassBaseClass): # A CoClass
	# ������� ��� ������� ������������.
	CLSID = IID('{02CBC423-BC8C-40DE-BE65-03A67DF1C834}')
	coclass_sources = [
		ksSpcObjectNotify,
	]
	default_source = ksSpcObjectNotify
	coclass_interfaces = [
	]

class SpcStyleColumnParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����� ������� ������� ������������.
	CLSID = IID('{4FD7CE95-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSpcStyleColumnParam,
	]
	default_interface = ksSpcStyleColumnParam

class SpcStyleParam(CoClassBaseClass): # A CoClass
	# C�������� ���������� ����� ������������.
	CLSID = IID('{4FD7CEA4-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSpcStyleParam,
	]
	default_interface = ksSpcStyleParam

class SpcStyleSectionParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����� ������a ������������.
	CLSID = IID('{4FD7CE98-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSpcStyleSectionParam,
	]
	default_interface = ksSpcStyleSectionParam

class SpcSubSectionParam(CoClassBaseClass): # A CoClass
	# C�������� ���������� ���������� ������������.
	CLSID = IID('{4FD7CE9B-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSpcSubSectionParam,
	]
	default_interface = ksSpcSubSectionParam

class SpcTuningSectionParam(CoClassBaseClass): # A CoClass
	# C�������� ���������� ��������� ������� ������������.
	CLSID = IID('{4FD7CE9E-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSpcTuningSectionParam,
	]
	default_interface = ksSpcTuningSectionParam

class SpcTuningStyleParam(CoClassBaseClass): # A CoClass
	# C�������� ���������� ����� �������� ������������.
	CLSID = IID('{4FD7CEA1-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSpcTuningStyleParam,
	]
	default_interface = ksSpcTuningStyleParam

class SpecRoughParam(CoClassBaseClass): # A CoClass
	# ��������� ��� ����������� ����������� �������������.
	CLSID = IID('{364521A5-94B5-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSpecRoughParam,
	]
	default_interface = ksSpecRoughParam

class Specification(CoClassBaseClass): # A CoClass
	# ��������� ������ � ��������� ������������.
	CLSID = IID('{51E74526-9A3A-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
		ksSpecificationNotify,
	]
	default_source = ksSpecificationNotify
	coclass_interfaces = [
		ksSpecification,
	]
	default_interface = ksSpecification

class SphereParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� �����.
	CLSID = IID('{C82A3D03-4BEE-467F-9240-C1C58FDB144E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSphereParam,
	]
	default_interface = ksSphereParam

class SplineDefinition(CoClassBaseClass): # A CoClass
	# ������.
	CLSID = IID('{0307BBA7-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSplineDefinition,
	]
	default_interface = ksSplineDefinition

class Stamp(CoClassBaseClass): # A CoClass
	# �������������� ������.
	CLSID = IID('{FBCC5BA7-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
		ksStampNotify,
	]
	default_source = ksStampNotify
	coclass_interfaces = [
		ksStamp,
	]
	default_interface = ksStamp

class StandartSheet(CoClassBaseClass): # A CoClass
	# ��������� ���������� ������������ �����.
	CLSID = IID('{FBCC5B92-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksStandartSheet,
	]
	default_interface = ksStandartSheet

class Surface(CoClassBaseClass): # A CoClass
	# �������������� ����������� � ���������� ������������.
	CLSID = IID('{B1C40242-CD49-4207-B728-B67057BEC339}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksSurface,
	]
	default_interface = ksSurface

class TAN(CoClassBaseClass): # A CoClass
	# ������ ��������� ����� �������.
	CLSID = IID('{9F8CA523-173C-4206-8F2A-AB221138692E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksTAN,
	]
	default_interface = ksTAN

class TechnicalDemandParam(CoClassBaseClass): # A CoClass
	# ��������� ��� ����������� ����������� ����������.
	CLSID = IID('{FBCC5B83-996C-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksTechnicalDemandParam,
	]
	default_interface = ksTechnicalDemandParam

class Tessellation(CoClassBaseClass): # A CoClass
	# ��������� ������������.
	CLSID = IID('{923A48A1-C159-4959-B13E-E8C558534C89}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksTessellation,
	]
	default_interface = ksTessellation

class TextDocumentParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ���������� ���������.
	CLSID = IID('{02286DB8-98D4-4D0B-97D7-E2EED32EEBD6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksTextDocumentParam,
	]
	default_interface = ksTextDocumentParam

class TextItemFont(CoClassBaseClass): # A CoClass
	# ��������� ������ ���������� ������ ������.
	CLSID = IID('{364521BF-94B5-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksTextItemFont,
	]
	default_interface = ksTextItemFont

class TextItemParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ������ ������.
	CLSID = IID('{364521B9-94B5-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksTextItemParam,
	]
	default_interface = ksTextItemParam

class TextLineParam(CoClassBaseClass): # A CoClass
	# ��������� ������ ������.
	CLSID = IID('{364521BC-94B5-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksTextLineParam,
	]
	default_interface = ksTextLineParam

class TextParam(CoClassBaseClass): # A CoClass
	# ��������� ������.
	CLSID = IID('{7F7D6F98-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksTextParam,
	]
	default_interface = ksTextParam

class TextStyleParam(CoClassBaseClass): # A CoClass
	# ����� ������.
	CLSID = IID('{3F715E26-97D9-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksTextStyleParam,
	]
	default_interface = ksTextStyleParam

class ThinParam(CoClassBaseClass): # A CoClass
	# ��������� ������ ������.
	CLSID = IID('{DEEFF02B-C3E2-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksThinParam,
	]
	default_interface = ksThinParam

class ThreadDefinition(CoClassBaseClass): # A CoClass
	# �������� ����������� ������.
	CLSID = IID('{2A8AE692-45A3-4C22-88B5-76B4830F2235}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksThreadDefinition,
	]
	default_interface = ksThreadDefinition

class ToleranceBranch(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����� ������� �����.
	CLSID = IID('{4FD7CE86-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksToleranceBranch,
	]
	default_interface = ksToleranceBranch

class ToleranceParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ������� �����.
	CLSID = IID('{4FD7CE89-9968-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksToleranceParam,
	]
	default_interface = ksToleranceParam

class TorusParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����.
	CLSID = IID('{B7833CCA-936D-4689-BD90-90B5209D94E8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksTorusParam,
	]
	default_interface = ksTorusParam

class TreeNodeParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ���� ������.
	CLSID = IID('{05A4578F-A41F-48F2-92F9-A0F0856BCBC0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksTreeNodeParam,
	]
	default_interface = ksTreeNodeParam

class Type1(CoClassBaseClass): # A CoClass
	# ��������� ��� ������ ������.
	CLSID = IID('{9AF8E346-98A0-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksType1,
	]
	default_interface = ksType1

class Type2(CoClassBaseClass): # A CoClass
	# ��������� ��� �������.
	CLSID = IID('{9AF8E349-98A0-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksType2,
	]
	default_interface = ksType2

class Type3(CoClassBaseClass): # A CoClass
	# ��������� ��� �������������� � ��� ������� c �������� �����.
	CLSID = IID('{9AF8E34C-98A0-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksType3,
	]
	default_interface = ksType3

class Type5(CoClassBaseClass): # A CoClass
	# ��������� ��� �������� �������������� c �������� �����.
	CLSID = IID('{9AF8E34F-98A0-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksType5,
	]
	default_interface = ksType5

class Type6(CoClassBaseClass): # A CoClass
	# ��������� ��� ����������������� �������.
	CLSID = IID('{9AF8E352-98A0-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksType6,
	]
	default_interface = ksType6

class UnionComponentsDefinition(CoClassBaseClass): # A CoClass
	# ��������� �������� ����������� �����������.
	CLSID = IID('{BA53B169-1DC8-4CCA-BAA4-27B0FB87AE26}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksUnionComponentsDefinition,
	]
	default_interface = ksUnionComponentsDefinition

class UserParam(CoClassBaseClass): # A CoClass
	# ���������������� ��������� ����������.
	CLSID = IID('{E79C251B-9584-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksUserParam,
	]
	default_interface = ksUserParam

class Variable(CoClassBaseClass): # A CoClass
	# ��������� ����������.
	CLSID = IID('{508A0CC3-9D74-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksVariable,
	]
	default_interface = ksVariable

class VariableCollection(CoClassBaseClass): # A CoClass
	# ������ ��������������� ����������.
	CLSID = IID('{03CEAC83-C0B8-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksVariableCollection,
	]
	default_interface = ksVariableCollection

class VertexDefinition(CoClassBaseClass): # A CoClass
	# �������� �������.
	CLSID = IID('{5CE6E053-3EC8-427B-BCB5-82B01D4BCBF3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksVertexDefinition,
	]
	default_interface = ksVertexDefinition

class ViewColorParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ����� ����.
	CLSID = IID('{34AFC10F-4FBB-40F0-8A23-74B1250F42EF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksViewColorParam,
	]
	default_interface = ksViewColorParam

class ViewParam(CoClassBaseClass): # A CoClass
	# ��������� ����.
	CLSID = IID('{7F7D6FB6-97DA-11D6-8732-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksViewParam,
	]
	default_interface = ksViewParam

class ViewPointerParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ��� ������� ����.
	CLSID = IID('{CD1C0146-98DC-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksViewPointerParam,
	]
	default_interface = ksViewPointerParam

class ViewProjection(CoClassBaseClass): # A CoClass
	# ��������� �������� ����������� ������ � ����.
	CLSID = IID('{0CA54EDF-BC8C-4A6A-94CF-EDBA74A6FA00}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksViewProjection,
	]
	default_interface = ksViewProjection

class ViewProjectionCollection(CoClassBaseClass): # A CoClass
	# ��������� ������� �������� ����������� ������ � ����.
	CLSID = IID('{9A3E39C6-B6AB-42CF-9FBD-AC05F0B4B161}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksViewProjectionCollection,
	]
	default_interface = ksViewProjectionCollection

class body(CoClassBaseClass): # A CoClass
	# ���� 3D.
	CLSID = IID('{A99FFD41-AA46-4BFC-B6F2-32E1A956E0B1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBody,
	]
	default_interface = ksBody

class brandLeaderParam(CoClassBaseClass): # A CoClass
	# ����� ������� ��� ����������� ���������.
	CLSID = IID('{3F715E48-97D9-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksBrandLeaderParam,
	]
	default_interface = ksBrandLeaderParam

class entity(CoClassBaseClass): # A CoClass
	# 3D ������.
	CLSID = IID('{508A0CCC-9D74-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksEntity,
	]
	default_interface = ksEntity

class faceDefinition(CoClassBaseClass): # A CoClass
	# ��������� �����.
	CLSID = IID('{0307BBAA-C193-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksFaceDefinition,
	]
	default_interface = ksFaceDefinition

class facet(CoClassBaseClass): # A CoClass
	# ��������� ���������������� ��������.
	CLSID = IID('{F7F45063-0B37-40B1-B3AD-BB0A545EC2C8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksFacet,
	]
	default_interface = ksFacet

class leaderParam(CoClassBaseClass): # A CoClass
	# ��������� ���������� ��� ������� ����� �������.
	CLSID = IID('{3F715E42-97D9-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksLeaderParam,
	]
	default_interface = ksLeaderParam

class markerLeaderParam(CoClassBaseClass): # A CoClass
	# ����� ������� ��� ����������� ������������.
	CLSID = IID('{9AF8E343-98A0-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksMarkerLeaderParam,
	]
	default_interface = ksMarkerLeaderParam

class part(CoClassBaseClass): # A CoClass
	# 3D ���������.
	CLSID = IID('{508A0CCF-9D74-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPart,
	]
	default_interface = ksPart

class phantom(CoClassBaseClass): # A CoClass
	# ��������� �������.
	CLSID = IID('{9AF8E355-98A0-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPhantom,
	]
	default_interface = ksPhantom

class placement(CoClassBaseClass): # A CoClass
	# ��������� ��������� ������� ��������� (��������� �������).
	CLSID = IID('{2DFACC66-C4A4-11D6-8734-00C0262CDD2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPlacement,
	]
	default_interface = ksPlacement

class posLeaderParam(CoClassBaseClass): # A CoClass
	# ����� ������� ��� ����������� �������.
	CLSID = IID('{3F715E45-97D9-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksPosLeaderParam,
	]
	default_interface = ksPosLeaderParam

class roughPar(CoClassBaseClass): # A CoClass
	# ��������� ���������� �������������.
	CLSID = IID('{3F715E35-97D9-11D6-95CE-00C0262D30E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ksRoughPar,
	]
	default_interface = ksRoughPar

RecordMap = {
}

CLSIDToClassMap = {
	'{E36BC97C-39D6-4402-9C25-C7008A217E02}' : KompasObject,
	'{AF4E160D-5C89-4F21-B0F2-D53397BDAF78}' : ksDocument2D,
	'{2E29C343-C521-4B0F-B37D-587D0347B7BA}' : ksObject2DNotify,
	'{C7EBA9A1-9E76-436E-B362-A80C5763944C}' : Object2DNotify,
	'{A421368A-34B6-4DDF-9A52-73B3488EE83F}' : ksSelectionMngNotify,
	'{DC2E4057-7F8E-4652-860D-6B9E1F6F43AA}' : SelectionMngNotify,
	'{1FE1EB28-CD28-4700-8E46-25CCFE9C0EC8}' : ksObject2DNotifyResult,
	'{13F0BE95-3361-4AD9-90AF-D935EA64A127}' : ksDocument2DNotify,
	'{1B9B9B4E-DCD7-496E-A583-547EC1E91E47}' : Document2DNotify,
	'{111CEFE1-A0A7-11D6-95CE-00C0262D30E3}' : ksDocument3D,
	'{B6C1BCFD-68DA-4A0A-A95C-296084C6A01A}' : ksDocument3DNotify,
	'{22B81342-42D6-4907-A91E-F75A959F2270}' : Document3DNotify,
	'{508A0CCA-9D74-11D6-95CE-00C0262D30E3}' : ksEntity,
	'{EB61A981-F63E-47E1-BEE8-2D1612C78E78}' : ksAttribute3DCollection,
	'{3EEB2B43-56FF-49C0-AFCF-69E990A7D84C}' : ksAttribute3D,
	'{CE6A46FF-02B4-4C7E-AF50-3F3707C8B122}' : ksFeatureCollection,
	'{088BF9A8-37D3-4B15-A7CA-8C52FF1DBC41}' : ksFeature,
	'{B0170141-C02C-11D6-8734-00C0262CDD2C}' : ksEntityCollection,
	'{508A0CCD-9D74-11D6-95CE-00C0262D30E3}' : ksPart,
	'{BFA024B6-679E-4A95-B6C2-1EA47A7CD0E9}' : ksObject3DNotify,
	'{CA35F3C6-7E2D-4700-BE12-BAA26DC1945B}' : Object3DNotify,
	'{9C3ECC92-E72F-4892-8921-7886F34CA9AD}' : ksObject3DNotifyResult,
	'{2DFACC64-C4A4-11D6-8734-00C0262CDD2C}' : ksPlacement,
	'{508B5962-DF59-4CEE-8611-AD10FDF0C811}' : ksComponentPositioner,
	'{C7CB743A-C59D-4C27-8CB6-971C2A393F2F}' : ksKompasObjectNotify,
	'{324C1A45-67AD-41FB-BE57-624F930646F1}' : ksDocumentFileNotify,
	'{9F88CAAA-A50F-46F4-904A-846C792FA649}' : ksDocument3DNotifyResult,
	'{364521A3-94B5-11D6-8732-00C0262CDD2C}' : ksSpecRoughParam,
	'{364521A6-94B5-11D6-8732-00C0262CDD2C}' : ksEllipseParam,
	'{364521A9-94B5-11D6-8732-00C0262CDD2C}' : ksEllipseArcParam,
	'{364521AC-94B5-11D6-8732-00C0262CDD2C}' : ksEllipseArcParam1,
	'{364521AF-94B5-11D6-8732-00C0262CDD2C}' : ksEquidistantParam,
	'{364521B2-94B5-11D6-8732-00C0262CDD2C}' : ksParagraphParam,
	'{364521B7-94B5-11D6-8732-00C0262CDD2C}' : ksTextItemParam,
	'{364521BA-94B5-11D6-8732-00C0262CDD2C}' : ksTextLineParam,
	'{364521BD-94B5-11D6-8732-00C0262CDD2C}' : ksTextItemFont,
	'{E79C2501-9584-11D6-8732-00C0262CDD2C}' : ksCornerParam,
	'{E79C2504-9584-11D6-8732-00C0262CDD2C}' : ksContourParam,
	'{E79C2507-9584-11D6-8732-00C0262CDD2C}' : ksLayerParam,
	'{E79C250A-9584-11D6-8732-00C0262CDD2C}' : ksLineParam,
	'{E79C250D-9584-11D6-8732-00C0262CDD2C}' : ksRegularPolygonParam,
	'{E79C2510-9584-11D6-8732-00C0262CDD2C}' : ksRectangleParam,
	'{E79C2513-9584-11D6-8732-00C0262CDD2C}' : ksBaseParam,
	'{E79C2516-9584-11D6-8732-00C0262CDD2C}' : ksLtVariant,
	'{E79C2519-9584-11D6-8732-00C0262CDD2C}' : ksUserParam,
	'{3198E121-9585-11D6-95CE-00C0262D30E3}' : ksMathPointParam,
	'{910EC541-958D-11D6-95CE-00C0262D30E3}' : ksCurvePicture,
	'{910EC544-958D-11D6-95CE-00C0262D30E3}' : ksCurvePattern,
	'{8075EDE4-6C85-4711-8685-68FBE359D4C4}' : ksTAN,
	'{C175BFB8-D7D6-4325-BFDA-2A282B9D1119}' : ksCON,
	'{EA92E649-239E-4105-BBD3-AEF4817BD783}' : ksInertiaParam,
	'{283F77EB-7E2C-4F71-8B16-4D286FA4857E}' : ksMassInertiaParam,
	'{F2D5AE01-45DE-4496-B01B-9958CAEF5943}' : ksMathematic2D,
	'{4D91CD9A-6E02-409D-9360-CF7FEF60D31C}' : ksDynamicArray,
	'{2A4D4542-95B3-11D6-8732-00C0262CDD2C}' : ksRDimDrawingParam,
	'{2A4D4545-95B3-11D6-8732-00C0262CDD2C}' : ksRDimSourceParam,
	'{7F7D6F81-97DA-11D6-8732-00C0262CDD2C}' : ksRDimParam,
	'{7F7D6F84-97DA-11D6-8732-00C0262CDD2C}' : ksLineSegParam,
	'{7F7D6F87-97DA-11D6-8732-00C0262CDD2C}' : ksCircleParam,
	'{7F7D6F8A-97DA-11D6-8732-00C0262CDD2C}' : ksArcByAngleParam,
	'{7F7D6F8D-97DA-11D6-8732-00C0262CDD2C}' : ksArcByPointParam,
	'{7F7D6F90-97DA-11D6-8732-00C0262CDD2C}' : ksPointParam,
	'{7F7D6F93-97DA-11D6-8732-00C0262CDD2C}' : ksHatchParam,
	'{7F7D6F96-97DA-11D6-8732-00C0262CDD2C}' : ksTextParam,
	'{7F7D6F99-97DA-11D6-8732-00C0262CDD2C}' : ksNurbsPointParam,
	'{7F7D6F9C-97DA-11D6-8732-00C0262CDD2C}' : ksDoubleValue,
	'{7F7D6F9F-97DA-11D6-8732-00C0262CDD2C}' : ksNurbsParam,
	'{7F7D6FA2-97DA-11D6-8732-00C0262CDD2C}' : ksConicArcParam,
	'{7F7D6FA5-97DA-11D6-8732-00C0262CDD2C}' : ksCentreParam,
	'{7F7D6FA8-97DA-11D6-8732-00C0262CDD2C}' : ksPlacementParam,
	'{7F7D6FAB-97DA-11D6-8732-00C0262CDD2C}' : ksRasterParam,
	'{7F7D6FAE-97DA-11D6-8732-00C0262CDD2C}' : ksPolylineParam,
	'{7F7D6FB1-97DA-11D6-8732-00C0262CDD2C}' : ksInsertFragmentParam,
	'{7F7D6FB4-97DA-11D6-8732-00C0262CDD2C}' : ksViewParam,
	'{7F7D6FB7-97DA-11D6-8732-00C0262CDD2C}' : ksLBreakDimSource,
	'{7F7D6FBA-97DA-11D6-8732-00C0262CDD2C}' : ksBreakDimDrawing,
	'{7F7D6FBD-97DA-11D6-8732-00C0262CDD2C}' : ksLBreakDimParam,
	'{7F7D6FC0-97DA-11D6-8732-00C0262CDD2C}' : ksABreakDimParam,
	'{7F7D6FC3-97DA-11D6-8732-00C0262CDD2C}' : ksInsertFragmentParamEx,
	'{7F7D6FC6-97DA-11D6-8732-00C0262CDD2C}' : ksBezierParam,
	'{7F7D6FC9-97DA-11D6-8732-00C0262CDD2C}' : ksBezierPointParam,
	'{7F7D6FCC-97DA-11D6-8732-00C0262CDD2C}' : ksDimTextParam,
	'{7F7D6FCF-97DA-11D6-8732-00C0262CDD2C}' : ksLDimSourceParam,
	'{7F7D6FD2-97DA-11D6-8732-00C0262CDD2C}' : ksDimDrawingParam,
	'{7F7D6FD5-97DA-11D6-8732-00C0262CDD2C}' : ksLDimParam,
	'{7F7D6FD8-97DA-11D6-8732-00C0262CDD2C}' : ksADimSourceParam,
	'{7F7D6FDB-97DA-11D6-8732-00C0262CDD2C}' : ksDimensionPartsParam,
	'{7F7D6FDE-97DA-11D6-8732-00C0262CDD2C}' : ksADimParam,
	'{7F7D6FE1-97DA-11D6-8732-00C0262CDD2C}' : ksRBreakDrawingParam,
	'{7F7D6FE4-97DA-11D6-8732-00C0262CDD2C}' : ksRBreakDimParam,
	'{7F7D6FE7-97DA-11D6-8732-00C0262CDD2C}' : ksQualityItemParam,
	'{7F7D6FEA-97DA-11D6-8732-00C0262CDD2C}' : ksQualityContensParam,
	'{D06C9101-98CA-11D6-8732-00C0262CDD2C}' : ksIterator,
	'{D06C9104-98CA-11D6-8732-00C0262CDD2C}' : ksFragment,
	'{D06C910A-98CA-11D6-8732-00C0262CDD2C}' : ksFragmentLibrary,
	'{FBCC5B81-996C-11D6-8732-00C0262CDD2C}' : ksTechnicalDemandParam,
	'{FBCC5B84-996C-11D6-8732-00C0262CDD2C}' : ksOrdinatedSourceParam,
	'{FBCC5B87-996C-11D6-8732-00C0262CDD2C}' : ksOrdinatedDimParam,
	'{FBCC5B8A-996C-11D6-8732-00C0262CDD2C}' : ksOrdinatedDrawingParam,
	'{FBCC5B8D-996C-11D6-8732-00C0262CDD2C}' : ksSheetSize,
	'{FBCC5B90-996C-11D6-8732-00C0262CDD2C}' : ksStandartSheet,
	'{FBCC5B93-996C-11D6-8732-00C0262CDD2C}' : ksSheetPar,
	'{FBCC5B96-996C-11D6-8732-00C0262CDD2C}' : ksDocumentParam,
	'{FBCC5B99-996C-11D6-8732-00C0262CDD2C}' : ksDimensionsOptions,
	'{FBCC5B9C-996C-11D6-8732-00C0262CDD2C}' : ksSnapOptions,
	'{FBCC5B9F-996C-11D6-8732-00C0262CDD2C}' : ksLibraryStyleParam,
	'{404E7D5A-A13F-4CFF-8214-FEA7012110CB}' : ksStampNotify,
	'{FBCC5BA5-996C-11D6-8732-00C0262CDD2C}' : ksStamp,
	'{FBCC5BA8-996C-11D6-8732-00C0262CDD2C}' : ksSheetOptions,
	'{910EC549-958D-11D6-95CE-00C0262D30E3}' : ksCurvePatternEx,
	'{910EC54C-958D-11D6-95CE-00C0262D30E3}' : ksCurveStyleParam,
	'{3F715E24-97D9-11D6-95CE-00C0262D30E3}' : ksTextStyleParam,
	'{3F715E27-97D9-11D6-95CE-00C0262D30E3}' : ksHatchLineParam,
	'{3F715E2A-97D9-11D6-95CE-00C0262D30E3}' : ksHatchStyleParam,
	'{3F715E2D-97D9-11D6-95CE-00C0262D30E3}' : ksRectParam,
	'{3F715E30-97D9-11D6-95CE-00C0262D30E3}' : ksShelfPar,
	'{3F715E33-97D9-11D6-95CE-00C0262D30E3}' : ksRoughPar,
	'{3F715E36-97D9-11D6-95CE-00C0262D30E3}' : ksRoughParam,
	'{3F715E39-97D9-11D6-95CE-00C0262D30E3}' : ksChar255,
	'{3F715E40-97D9-11D6-95CE-00C0262D30E3}' : ksLeaderParam,
	'{3F715E43-97D9-11D6-95CE-00C0262D30E3}' : ksPosLeaderParam,
	'{3F715E46-97D9-11D6-95CE-00C0262D30E3}' : ksBrandLeaderParam,
	'{9AF8E341-98A0-11D6-95CE-00C0262D30E3}' : ksMarkerLeaderParam,
	'{9AF8E344-98A0-11D6-95CE-00C0262D30E3}' : ksType1,
	'{9AF8E347-98A0-11D6-95CE-00C0262D30E3}' : ksType2,
	'{9AF8E34A-98A0-11D6-95CE-00C0262D30E3}' : ksType3,
	'{9AF8E34D-98A0-11D6-95CE-00C0262D30E3}' : ksType5,
	'{9AF8E350-98A0-11D6-95CE-00C0262D30E3}' : ksType6,
	'{9AF8E353-98A0-11D6-95CE-00C0262D30E3}' : ksPhantom,
	'{9AF8E356-98A0-11D6-95CE-00C0262D30E3}' : ksRequestInfo,
	'{CD1C0144-98DC-11D6-95CE-00C0262D30E3}' : ksViewPointerParam,
	'{4FD7CE81-9968-11D6-95CE-00C0262D30E3}' : ksCutLineParam,
	'{4FD7CE84-9968-11D6-95CE-00C0262D30E3}' : ksToleranceBranch,
	'{4FD7CE87-9968-11D6-95CE-00C0262D30E3}' : ksToleranceParam,
	'{4FD7CE8A-9968-11D6-95CE-00C0262D30E3}' : ksSpcColumnParam,
	'{4FD7CE8D-9968-11D6-95CE-00C0262D30E3}' : ksRecordTypeAttrParam,
	'{4FD7CE90-9968-11D6-95CE-00C0262D30E3}' : ksNumberTypeAttrParam,
	'{4FD7CE93-9968-11D6-95CE-00C0262D30E3}' : ksSpcStyleColumnParam,
	'{4FD7CE96-9968-11D6-95CE-00C0262D30E3}' : ksSpcStyleSectionParam,
	'{4FD7CE99-9968-11D6-95CE-00C0262D30E3}' : ksSpcSubSectionParam,
	'{4FD7CE9C-9968-11D6-95CE-00C0262D30E3}' : ksSpcTuningSectionParam,
	'{4FD7CE9F-9968-11D6-95CE-00C0262D30E3}' : ksSpcTuningStyleParam,
	'{4FD7CEA2-9968-11D6-95CE-00C0262D30E3}' : ksSpcStyleParam,
	'{4FD7CEA5-9968-11D6-95CE-00C0262D30E3}' : ksSpcDescrParam,
	'{4FD7CEA8-9968-11D6-95CE-00C0262D30E3}' : ksDocAttachedSpcParam,
	'{4FD7CEAB-9968-11D6-95CE-00C0262D30E3}' : ksSpcObjParam,
	'{4FD7CEAE-9968-11D6-95CE-00C0262D30E3}' : ksLibStyle,
	'{0981CD01-9A49-11D6-8732-00C0262CDD2C}' : ksDataBaseObject,
	'{1BD030F4-4058-4A86-9F4F-1AEEF8BE8D23}' : ksSpcDocumentNotify,
	'{51E74521-9A3A-11D6-95CE-00C0262D30E3}' : ksSpcDocument,
	'{DC32EB43-4615-4717-8C67-48875A357B06}' : SpcDocumentNotify,
	'{AC5004D1-C240-41FC-AB84-7EB5C793AE7F}' : ksSpcObjectNotify,
	'{0331AB4B-F25B-4EB9-9C8A-BFEA414E3822}' : ksSpecificationNotify,
	'{51E74524-9A3A-11D6-95CE-00C0262D30E3}' : ksSpecification,
	'{02CBC423-BC8C-40DE-BE65-03A67DF1C834}' : SpcObjectNotify,
	'{74D745F1-9A3A-11D6-95CE-00C0262D30E3}' : ksDocumentTxt,
	'{CC26DA61-9B22-11D6-95CE-00C0262D30E3}' : ksAttributeTypeParam,
	'{CE0D05E1-9B2A-11D6-95CE-00C0262D30E3}' : ksColumnInfoParam,
	'{CE0D05E4-9B2A-11D6-95CE-00C0262D30E3}' : ksAttributeParam,
	'{508A0CC1-9D74-11D6-95CE-00C0262D30E3}' : ksVariable,
	'{FA93AA21-9B3D-11D6-95CE-00C0262D30E3}' : ksLibraryAttrTypeParam,
	'{FA93AA24-9B3D-11D6-95CE-00C0262D30E3}' : ksAttributeObject,
	'{E9807824-9D55-11D6-95CE-00C0262D30E3}' : ksRequestInfo3D,
	'{508A0CC4-9D74-11D6-95CE-00C0262D30E3}' : ksMateConstraint,
	'{508A0CC7-9D74-11D6-95CE-00C0262D30E3}' : ksDefaultObject,
	'{111CEFE4-A0A7-11D6-95CE-00C0262D30E3}' : ksModelLibrary,
	'{03CEAC81-C0B8-11D6-8734-00C0262CDD2C}' : ksVariableCollection,
	'{03CEAC84-C0B8-11D6-8734-00C0262CDD2C}' : ksMateConstraintCollection,
	'{03CEAC87-C0B8-11D6-8734-00C0262CDD2C}' : ksPartCollection,
	'{E6E78D61-C0FA-11D6-8734-00C0262CDD2C}' : ksMeshPartArrayDefinition,
	'{DDD05143-C180-11D6-8734-00C0262CDD2C}' : ksCircularPartArrayDefinition,
	'{DDD05146-C180-11D6-8734-00C0262CDD2C}' : ksCurvePartArrayDefinition,
	'{DDD05149-C180-11D6-8734-00C0262CDD2C}' : ksDerivativePartArrayDefinition,
	'{0307BB81-C193-11D6-8734-00C0262CDD2C}' : ksAxis2PlanesDefinition,
	'{0307BB84-C193-11D6-8734-00C0262CDD2C}' : ksAxisOperationsDefinition,
	'{0307BB87-C193-11D6-8734-00C0262CDD2C}' : ksAxis2PointsDefinition,
	'{0307BB8A-C193-11D6-8734-00C0262CDD2C}' : ksAxisEdgeDefinition,
	'{0307BB8D-C193-11D6-8734-00C0262CDD2C}' : ksMeshCopyDefinition,
	'{0307BB90-C193-11D6-8734-00C0262CDD2C}' : ksCircularCopyDefinition,
	'{0307BB93-C193-11D6-8734-00C0262CDD2C}' : ksCurveCopyDefinition,
	'{0307BB96-C193-11D6-8734-00C0262CDD2C}' : ksMirrorCopyDefinition,
	'{0307BB99-C193-11D6-8734-00C0262CDD2C}' : ksMirrorCopyAllDefinition,
	'{0307BB9C-C193-11D6-8734-00C0262CDD2C}' : ksConicSpiralDefinition,
	'{0307BB9F-C193-11D6-8734-00C0262CDD2C}' : ksCylindricSpiralDefinition,
	'{0307BBA2-C193-11D6-8734-00C0262CDD2C}' : ksPolyLineDefinition,
	'{1BCC4F0F-1091-41A3-895B-0608D20715B7}' : ksPolyLineVertexParam,
	'{0307BBA5-C193-11D6-8734-00C0262CDD2C}' : ksSplineDefinition,
	'{DEEFEFE1-C3E2-11D6-8734-00C0262CDD2C}' : ksBaseExtrusionDefinition,
	'{DEEFEFE4-C3E2-11D6-8734-00C0262CDD2C}' : ksBossExtrusionDefinition,
	'{DEEFEFE7-C3E2-11D6-8734-00C0262CDD2C}' : ksCutExtrusionDefinition,
	'{B20E24C3-5E4A-4CDA-A1ED-6BB8EBC81A29}' : ksExtrusionSurfaceDefinition,
	'{0307BBA8-C193-11D6-8734-00C0262CDD2C}' : ksFaceDefinition,
	'{0307BBAB-C193-11D6-8734-00C0262CDD2C}' : ksEdgeDefinition,
	'{0307BBAE-C193-11D6-8734-00C0262CDD2C}' : ksChamferDefinition,
	'{0307BBB1-C193-11D6-8734-00C0262CDD2C}' : ksFilletDefinition,
	'{DEEFEFEA-C3E2-11D6-8734-00C0262CDD2C}' : ksBaseLoftDefinition,
	'{DEEFEFED-C3E2-11D6-8734-00C0262CDD2C}' : ksBossLoftDefinition,
	'{DEEFEFF0-C3E2-11D6-8734-00C0262CDD2C}' : ksCutLoftDefinition,
	'{E04339B5-AA08-4717-8E50-90ED0E375624}' : ksLoftSurfaceDefinition,
	'{DEEFEFF3-C3E2-11D6-8734-00C0262CDD2C}' : ksInclineDefinition,
	'{DEEFEFF6-C3E2-11D6-8734-00C0262CDD2C}' : ksShellDefinition,
	'{DEEFEFF9-C3E2-11D6-8734-00C0262CDD2C}' : ksBaseEvolutionDefinition,
	'{DEEFEFFC-C3E2-11D6-8734-00C0262CDD2C}' : ksBossEvolutionDefinition,
	'{DEEFEFFF-C3E2-11D6-8734-00C0262CDD2C}' : ksCutEvolutionDefinition,
	'{2BD4C79E-E2C3-42E8-8FCC-B51FFBDE9F69}' : ksEvolutionSurfaceDefinition,
	'{DEEFF002-C3E2-11D6-8734-00C0262CDD2C}' : ksRibDefinition,
	'{DEEFF005-C3E2-11D6-8734-00C0262CDD2C}' : ksCutByPlaneDefinition,
	'{DEEFF008-C3E2-11D6-8734-00C0262CDD2C}' : ksCutBySketchDefinition,
	'{DEEFF00B-C3E2-11D6-8734-00C0262CDD2C}' : ksPlaneOffsetDefinition,
	'{DEEFF00E-C3E2-11D6-8734-00C0262CDD2C}' : ksPlaneAngleDefinition,
	'{DEEFF011-C3E2-11D6-8734-00C0262CDD2C}' : ksPlane3PointsDefinition,
	'{DEEFF014-C3E2-11D6-8734-00C0262CDD2C}' : ksPlaneNormalToSurfaceDefinition,
	'{DEEFF017-C3E2-11D6-8734-00C0262CDD2C}' : ksPlaneTangentToSurfaceDefinition,
	'{DEEFF01A-C3E2-11D6-8734-00C0262CDD2C}' : ksPlaneEdgePointDefinition,
	'{DEEFF01D-C3E2-11D6-8734-00C0262CDD2C}' : ksPlaneParallelDefinition,
	'{DEEFF020-C3E2-11D6-8734-00C0262CDD2C}' : ksPlanePerpendicularDefinition,
	'{DEEFF023-C3E2-11D6-8734-00C0262CDD2C}' : ksPlaneLineToEdgeDefinition,
	'{DEEFF026-C3E2-11D6-8734-00C0262CDD2C}' : ksPlaneLineToPlaneDefinition,
	'{DEEFF029-C3E2-11D6-8734-00C0262CDD2C}' : ksThinParam,
	'{DEEFF02C-C3E2-11D6-8734-00C0262CDD2C}' : ksExtrusionParam,
	'{DEEFF02F-C3E2-11D6-8734-00C0262CDD2C}' : ksRotatedParam,
	'{2DFACC61-C4A4-11D6-8734-00C0262CDD2C}' : ksColorParam,
	'{2DFACC67-C4A4-11D6-8734-00C0262CDD2C}' : ksBaseRotatedDefinition,
	'{2DFACC6A-C4A4-11D6-8734-00C0262CDD2C}' : ksBossRotatedDefinition,
	'{2DFACC6D-C4A4-11D6-8734-00C0262CDD2C}' : ksCutRotatedDefinition,
	'{FD27841D-1374-4F7F-AE8A-C2A44F89120D}' : ksRotatedSurfaceDefinition,
	'{2DFACC70-C4A4-11D6-8734-00C0262CDD2C}' : ksSketchDefinition,
	'{1A91A8AB-AF8C-4EE3-86D4-0A9C00123195}' : ksRasterFormatParam,
	'{0FD25FF9-AB0A-48F3-BAD4-F193116C0887}' : ksAdditionFormatParam,
	'{862E250D-9DB1-47E8-8EE2-9BE2D2453D5A}' : ksConstraintParam,
	'{78A2C35E-A7DA-414E-B90A-F19998EC7BD1}' : ksImportedSurfaceDefinition,
	'{0E95ACE0-0E73-406F-AE94-E8A0592E298D}' : ksFaceCollection,
	'{A7257E73-EB61-4602-BC8B-2D00EA4AA062}' : ksVertexDefinition,
	'{B810650E-7819-485C-90D2-ADEB647AE5E2}' : ksTessellation,
	'{EB6AFBC0-C387-4E07-B24E-DDF2B7926A26}' : ksFacet,
	'{ABC84FE5-3945-4A0B-820A-719BF4B79224}' : ksMeasurer,
	'{CFC49C01-7653-4845-93FD-13428F5D58EC}' : ksBodyCollection,
	'{03EFC9DD-E05A-4277-BC7C-4FD499A252DE}' : ksBody,
	'{963CB6E1-B9BF-4234-964A-13BFE6C0282A}' : ksSurface,
	'{6096A4FD-970B-468C-815E-37CA1970A203}' : ksEdgeCollection,
	'{88C32A80-3735-4E18-A02E-9B2A8F0A90E3}' : ksOrientedEdge,
	'{5CE8909D-CF3D-418F-A9B9-0A12B23916C0}' : ksOrientedEdgeCollection,
	'{22BC5C86-CF58-45E4-AA46-5E8D5A825798}' : ksLoop,
	'{1BD7207E-36AA-47DF-913E-AD26DE6C16E8}' : ksLoopCollection,
	'{7572648A-D4EE-41FE-8D74-EC7D1F91BDE2}' : ksCurve3D,
	'{DC8F6A7B-FF16-46FF-986D-2F7E1F6B25C4}' : ksLineSeg3dParam,
	'{82758442-C9EB-48F7-B304-083C5E64D4E0}' : ksCircle3dParam,
	'{5B8082B8-6AD3-4509-826D-D23B7F613213}' : ksEllipse3dParam,
	'{6A6F6B95-D100-4D54-A430-70A42D342917}' : ksPlaneParam,
	'{CCFA0D95-0834-4F92-988B-6E477AD67589}' : ksConeParam,
	'{5D462836-CF69-4995-AB78-8C7A83D09BD7}' : ksCylinderParam,
	'{C32977F3-3CA7-4D56-8AE7-4963E6851B75}' : ksSphereParam,
	'{FDA3B147-BAF1-4F75-99AA-39D11323EA97}' : ksTorusParam,
	'{F1CD604D-1D26-4F6B-8F94-F112133E6162}' : ksNurbsPoint3dParam,
	'{A12B63E8-9E0A-4854-B724-E18275B9FF20}' : ksNurbsSurfaceParam,
	'{4DDDAEDB-2819-42D9-BDBB-4CCBC98D76DF}' : ksNurbs3dParam,
	'{483E9889-E1CA-4CA5-BE4E-ECB3D5CF0126}' : ksNurbsKnotCollection,
	'{84AF9C81-1795-4631-B58A-101732262E75}' : ksNurbsPoint3dCollCollection,
	'{3AD5E519-74E2-4D3B-B6A3-B1E81F1006F1}' : ksNurbsPoint3dCollection,
	'{BF65B990-C2DC-4A12-9EB7-3E868608AF47}' : ksViewProjection,
	'{A174F872-C800-409E-9FB2-FF5B89D8B4B8}' : ksViewProjectionCollection,
	'{BE41850C-CFC5-40D4-AE49-37AA391BCF4B}' : ksSelectionMng,
	'{8F2AA755-D9D1-42A0-97BF-C92548CE7232}' : ksChooseMng,
	'{7DCBCC76-5041-4C1E-9B33-12B1352D6D57}' : ksArc3dParam,
	'{9F8DE1DC-1268-4785-9217-1B0DD59B85FA}' : ksTreeNodeParam,
	'{C81EB1DA-BCB0-491A-8D22-923BF817D572}' : ksAssociationViewParam,
	'{5A42B962-8F78-4557-B17A-1B871F8DBDB5}' : ksViewColorParam,
	'{AFE694D7-C1E5-468F-99B0-FE4C60C49899}' : ksAxisLineParam,
	'{33706D56-D085-4840-833B-435AEB00BE2A}' : ksTextDocumentParam,
	'{25076616-4949-455E-A45C-1B801884D825}' : ksRemoteElementParam,
	'{82F60797-D69C-4EB4-9F1A-24D625D5EAFA}' : ksDeletedCopyCollection,
	'{AACAD820-7790-46EB-B17F-06AE42215ED7}' : ksCopyObjectParam,
	'{5DDB6B14-6F3D-431F-B62F-C5FCCAFC3632}' : ksThreadDefinition,
	'{F78E6B71-BEF3-4A4D-AE50-FE96426F6FD1}' : ksOverlapObjectOptions,
	'{ABBA6CE0-CB4C-4A32-98B4-B639352C75BA}' : ksObjectsFilter3D,
	'{ABBA6CE0-CB4C-4A32-98B4-B639352C75BB}' : ksParametrizationParam,
	'{02556461-D088-4F00-AE61-D366082DB9BC}' : ksMacro3DDefinition,
	'{97337DAF-B7CD-4FB8-8E18-23F0230E5CBE}' : ksAxisConefaceDefinition,
	'{99797F89-FBA4-4582-812F-226AFB50ED7D}' : ksUnionComponentsDefinition,
	'{BE5F10F5-B198-49D9-9140-B2B91E060533}' : ksMoldCavityDefinition,
	'{E4091969-1C4E-4959-8D93-C2421564418B}' : ksCoordinate3dCollection,
	'{ABC7F8EE-CF07-4AA8-98A1-0DE35DB35B9E}' : ksIntersectionResult,
	'{CC5E3539-5B35-46FC-AFE1-19BB0168D52F}' : ksPlaneMiddleDefinition,
	'{BC4C15A4-16E9-4CFA-A33E-CC86BA2FB546}' : ksControlPointDefinition,
	'{177CBAF3-87E6-4376-B6A9-669C0E661BFF}' : ksConjunctivePointDefinition,
	'{E06B18BF-D2AF-4201-99BE-B7FA9EECF7A8}' : ksChooseBodies,
	'{44277B89-EEB4-456C-8EF9-2DC48D61EC91}' : ksAggregateDefinition,
	'{391938AE-79B6-4E3B-9815-AC1A31D9EA9D}' : ksChangeLeaderParam,
	'{6B0B5194-4ACD-4095-9BC1-11179FBBB05A}' : Application,
	'{FBE002A6-1E06-4703-AEC5-9AD8A10FA1FA}' : KompasInvisible5,
	'{DE8219EC-0A9F-44E1-AC2B-F17269484FFF}' : Object2DNotifyResult,
	'{87CD4F95-083C-4514-B8B4-025C8907D8F1}' : FeatureCollection,
	'{2DFACC66-C4A4-11D6-8734-00C0262CDD2C}' : placement,
	'{600F12DF-D8B8-4CA8-A476-D2A7E425C740}' : Object3DNotifyResult,
	'{129E9083-E4D2-4991-B69F-70B696AD1A55}' : Document3DNotifyResult,
	'{14FD27F5-B7FD-4276-AC2C-2804EDC3944F}' : Document2D,
	'{364521A5-94B5-11D6-8732-00C0262CDD2C}' : SpecRoughParam,
	'{364521A8-94B5-11D6-8732-00C0262CDD2C}' : EllipseParam,
	'{364521AB-94B5-11D6-8732-00C0262CDD2C}' : EllipseArcParam,
	'{364521AE-94B5-11D6-8732-00C0262CDD2C}' : EllipseArcParam1,
	'{364521B1-94B5-11D6-8732-00C0262CDD2C}' : EquidistantParam,
	'{364521B4-94B5-11D6-8732-00C0262CDD2C}' : ParagraphParam,
	'{364521B9-94B5-11D6-8732-00C0262CDD2C}' : TextItemParam,
	'{364521BC-94B5-11D6-8732-00C0262CDD2C}' : TextLineParam,
	'{364521BF-94B5-11D6-8732-00C0262CDD2C}' : TextItemFont,
	'{E79C2503-9584-11D6-8732-00C0262CDD2C}' : CornerParam,
	'{E79C2506-9584-11D6-8732-00C0262CDD2C}' : ContourParam,
	'{E79C2509-9584-11D6-8732-00C0262CDD2C}' : LayerParam,
	'{E79C250C-9584-11D6-8732-00C0262CDD2C}' : LineParam,
	'{E79C250F-9584-11D6-8732-00C0262CDD2C}' : RegularPolygonParam,
	'{E79C2512-9584-11D6-8732-00C0262CDD2C}' : RectangleParam,
	'{E79C2515-9584-11D6-8732-00C0262CDD2C}' : BaseParam,
	'{E79C2518-9584-11D6-8732-00C0262CDD2C}' : LtVariant,
	'{E79C251B-9584-11D6-8732-00C0262CDD2C}' : UserParam,
	'{3198E123-9585-11D6-95CE-00C0262D30E3}' : MathPointParam,
	'{910EC543-958D-11D6-95CE-00C0262D30E3}' : CurvePicture,
	'{910EC546-958D-11D6-95CE-00C0262D30E3}' : CurvePattern,
	'{9F8CA523-173C-4206-8F2A-AB221138692E}' : TAN,
	'{9CC1A2E2-29A8-49BB-ABF6-792FA2D38014}' : CON,
	'{7B8B632E-5BDD-4EE5-B623-DF2880BE0EE4}' : InertiaParam,
	'{4693323B-42A7-42CC-902E-7123DD916FB4}' : MassInertiaParam,
	'{C77421D3-13EC-4595-A198-677EFB45AEF3}' : Mathematic2D,
	'{FD30B325-9E27-42CA-ADCF-C30EEBE0BBB8}' : DynamicArray,
	'{2A4D4544-95B3-11D6-8732-00C0262CDD2C}' : RDimDrawingParam,
	'{2A4D4547-95B3-11D6-8732-00C0262CDD2C}' : RDimSourceParam,
	'{7F7D6F83-97DA-11D6-8732-00C0262CDD2C}' : RDimParam,
	'{7F7D6F86-97DA-11D6-8732-00C0262CDD2C}' : LineSegParam,
	'{7F7D6F89-97DA-11D6-8732-00C0262CDD2C}' : CircleParam,
	'{7F7D6F8C-97DA-11D6-8732-00C0262CDD2C}' : ArcByAngleParam,
	'{7F7D6F8F-97DA-11D6-8732-00C0262CDD2C}' : ArcByPointParam,
	'{7F7D6F92-97DA-11D6-8732-00C0262CDD2C}' : PointParam,
	'{7F7D6F95-97DA-11D6-8732-00C0262CDD2C}' : HatchParam,
	'{7F7D6F98-97DA-11D6-8732-00C0262CDD2C}' : TextParam,
	'{7F7D6F9B-97DA-11D6-8732-00C0262CDD2C}' : NurbsPointParam,
	'{7F7D6F9E-97DA-11D6-8732-00C0262CDD2C}' : DoubleValue,
	'{7F7D6FA1-97DA-11D6-8732-00C0262CDD2C}' : NurbsParam,
	'{7F7D6FA4-97DA-11D6-8732-00C0262CDD2C}' : ConicArcParam,
	'{7F7D6FA7-97DA-11D6-8732-00C0262CDD2C}' : CentreParam,
	'{7F7D6FAA-97DA-11D6-8732-00C0262CDD2C}' : PlacementParam,
	'{7F7D6FAD-97DA-11D6-8732-00C0262CDD2C}' : RasterParam,
	'{7F7D6FB0-97DA-11D6-8732-00C0262CDD2C}' : PolylineParam,
	'{7F7D6FB3-97DA-11D6-8732-00C0262CDD2C}' : InsertFragmentParam,
	'{7F7D6FB6-97DA-11D6-8732-00C0262CDD2C}' : ViewParam,
	'{7F7D6FB9-97DA-11D6-8732-00C0262CDD2C}' : LBreakDimSource,
	'{7F7D6FBC-97DA-11D6-8732-00C0262CDD2C}' : BreakDimDrawing,
	'{7F7D6FBF-97DA-11D6-8732-00C0262CDD2C}' : LBreakDimParam,
	'{7F7D6FC2-97DA-11D6-8732-00C0262CDD2C}' : ABreakDimParam,
	'{7F7D6FC5-97DA-11D6-8732-00C0262CDD2C}' : InsertFragmentParamEx,
	'{7F7D6FC8-97DA-11D6-8732-00C0262CDD2C}' : BezierParam,
	'{7F7D6FCB-97DA-11D6-8732-00C0262CDD2C}' : BezierPointParam,
	'{7F7D6FCE-97DA-11D6-8732-00C0262CDD2C}' : DimTextParam,
	'{7F7D6FD1-97DA-11D6-8732-00C0262CDD2C}' : LDimSourceParam,
	'{7F7D6FD4-97DA-11D6-8732-00C0262CDD2C}' : DimDrawingParam,
	'{7F7D6FD7-97DA-11D6-8732-00C0262CDD2C}' : LDimParam,
	'{7F7D6FDA-97DA-11D6-8732-00C0262CDD2C}' : ADimSourceParam,
	'{7F7D6FDD-97DA-11D6-8732-00C0262CDD2C}' : DimensionPartsParam,
	'{7F7D6FE0-97DA-11D6-8732-00C0262CDD2C}' : ADimParam,
	'{7F7D6FE3-97DA-11D6-8732-00C0262CDD2C}' : RBreakDrawingParam,
	'{7F7D6FE6-97DA-11D6-8732-00C0262CDD2C}' : RBreakDimParam,
	'{7F7D6FE9-97DA-11D6-8732-00C0262CDD2C}' : QualityItemParam,
	'{7F7D6FEC-97DA-11D6-8732-00C0262CDD2C}' : QualityContensParam,
	'{D06C9103-98CA-11D6-8732-00C0262CDD2C}' : Iterator,
	'{D06C9106-98CA-11D6-8732-00C0262CDD2C}' : Fragment,
	'{D06C910C-98CA-11D6-8732-00C0262CDD2C}' : FragmentLib,
	'{FBCC5B83-996C-11D6-8732-00C0262CDD2C}' : TechnicalDemandParam,
	'{FBCC5B86-996C-11D6-8732-00C0262CDD2C}' : OrdinatedSourceParam,
	'{FBCC5B89-996C-11D6-8732-00C0262CDD2C}' : OrdinatedDimParam,
	'{FBCC5B8C-996C-11D6-8732-00C0262CDD2C}' : OrdinatedDrawingParam,
	'{FBCC5B8F-996C-11D6-8732-00C0262CDD2C}' : SheetSize,
	'{FBCC5B92-996C-11D6-8732-00C0262CDD2C}' : StandartSheet,
	'{FBCC5B95-996C-11D6-8732-00C0262CDD2C}' : SheetPar,
	'{FBCC5B98-996C-11D6-8732-00C0262CDD2C}' : DocumentParam,
	'{FBCC5B9B-996C-11D6-8732-00C0262CDD2C}' : DimensionsOptions,
	'{FBCC5B9E-996C-11D6-8732-00C0262CDD2C}' : SnapOptions,
	'{FBCC5BA1-996C-11D6-8732-00C0262CDD2C}' : LibraryStyleParam,
	'{FBCC5BA7-996C-11D6-8732-00C0262CDD2C}' : Stamp,
	'{FBCC5BAA-996C-11D6-8732-00C0262CDD2C}' : SheetOptions,
	'{910EC54B-958D-11D6-95CE-00C0262D30E3}' : CurvePatternEx,
	'{910EC54E-958D-11D6-95CE-00C0262D30E3}' : CurveStyleParam,
	'{3F715E26-97D9-11D6-95CE-00C0262D30E3}' : TextStyleParam,
	'{3F715E29-97D9-11D6-95CE-00C0262D30E3}' : HatchLineParam,
	'{3F715E2C-97D9-11D6-95CE-00C0262D30E3}' : HatchStyleParam,
	'{3F715E2F-97D9-11D6-95CE-00C0262D30E3}' : RectParam,
	'{3F715E32-97D9-11D6-95CE-00C0262D30E3}' : ShelfPar,
	'{3F715E35-97D9-11D6-95CE-00C0262D30E3}' : roughPar,
	'{3F715E38-97D9-11D6-95CE-00C0262D30E3}' : RoughParam,
	'{3F715E3B-97D9-11D6-95CE-00C0262D30E3}' : Char255,
	'{3F715E42-97D9-11D6-95CE-00C0262D30E3}' : leaderParam,
	'{3F715E45-97D9-11D6-95CE-00C0262D30E3}' : posLeaderParam,
	'{3F715E48-97D9-11D6-95CE-00C0262D30E3}' : brandLeaderParam,
	'{9AF8E343-98A0-11D6-95CE-00C0262D30E3}' : markerLeaderParam,
	'{9AF8E346-98A0-11D6-95CE-00C0262D30E3}' : Type1,
	'{9AF8E349-98A0-11D6-95CE-00C0262D30E3}' : Type2,
	'{9AF8E34C-98A0-11D6-95CE-00C0262D30E3}' : Type3,
	'{9AF8E34F-98A0-11D6-95CE-00C0262D30E3}' : Type5,
	'{9AF8E352-98A0-11D6-95CE-00C0262D30E3}' : Type6,
	'{9AF8E355-98A0-11D6-95CE-00C0262D30E3}' : phantom,
	'{9AF8E358-98A0-11D6-95CE-00C0262D30E3}' : RequestInfo,
	'{CD1C0146-98DC-11D6-95CE-00C0262D30E3}' : ViewPointerParam,
	'{4FD7CE83-9968-11D6-95CE-00C0262D30E3}' : CutLineParam,
	'{4FD7CE86-9968-11D6-95CE-00C0262D30E3}' : ToleranceBranch,
	'{4FD7CE89-9968-11D6-95CE-00C0262D30E3}' : ToleranceParam,
	'{4FD7CE8C-9968-11D6-95CE-00C0262D30E3}' : SpcColumnParam,
	'{4FD7CE8F-9968-11D6-95CE-00C0262D30E3}' : RecordTypeAttrParam,
	'{4FD7CE92-9968-11D6-95CE-00C0262D30E3}' : NumberTypeAttrParam,
	'{4FD7CE95-9968-11D6-95CE-00C0262D30E3}' : SpcStyleColumnParam,
	'{4FD7CE98-9968-11D6-95CE-00C0262D30E3}' : SpcStyleSectionParam,
	'{4FD7CE9B-9968-11D6-95CE-00C0262D30E3}' : SpcSubSectionParam,
	'{4FD7CE9E-9968-11D6-95CE-00C0262D30E3}' : SpcTuningSectionParam,
	'{4FD7CEA1-9968-11D6-95CE-00C0262D30E3}' : SpcTuningStyleParam,
	'{4FD7CEA4-9968-11D6-95CE-00C0262D30E3}' : SpcStyleParam,
	'{4FD7CEA7-9968-11D6-95CE-00C0262D30E3}' : SpcDescrParam,
	'{4FD7CEAA-9968-11D6-95CE-00C0262D30E3}' : DocAttachedSpcParam,
	'{4FD7CEAD-9968-11D6-95CE-00C0262D30E3}' : SpcObjParam,
	'{4FD7CEB0-9968-11D6-95CE-00C0262D30E3}' : LibStyle,
	'{0981CD03-9A49-11D6-8732-00C0262CDD2C}' : DataBaseObject,
	'{51E74523-9A3A-11D6-95CE-00C0262D30E3}' : SpcDocument,
	'{51E74526-9A3A-11D6-95CE-00C0262D30E3}' : Specification,
	'{74D745F3-9A3A-11D6-95CE-00C0262D30E3}' : DocumentTxt,
	'{CC26DA63-9B22-11D6-95CE-00C0262D30E3}' : AttributeTypeParam,
	'{CE0D05E3-9B2A-11D6-95CE-00C0262D30E3}' : ColumnInfoParam,
	'{CE0D05E6-9B2A-11D6-95CE-00C0262D30E3}' : AttributeParam,
	'{508A0CC3-9D74-11D6-95CE-00C0262D30E3}' : Variable,
	'{FA93AA23-9B3D-11D6-95CE-00C0262D30E3}' : LibraryAttrTypeParam,
	'{FA93AA26-9B3D-11D6-95CE-00C0262D30E3}' : AttributeObject,
	'{E9807826-9D55-11D6-95CE-00C0262D30E3}' : RequestInfo3D,
	'{508A0CC6-9D74-11D6-95CE-00C0262D30E3}' : MateConstraint,
	'{508A0CC9-9D74-11D6-95CE-00C0262D30E3}' : DefaultObject,
	'{508A0CCC-9D74-11D6-95CE-00C0262D30E3}' : entity,
	'{508A0CCF-9D74-11D6-95CE-00C0262D30E3}' : part,
	'{111CEFE3-A0A7-11D6-95CE-00C0262D30E3}' : Document3D,
	'{111CEFE6-A0A7-11D6-95CE-00C0262D30E3}' : ModelLibrary,
	'{B0170143-C02C-11D6-8734-00C0262CDD2C}' : EntityCollection,
	'{03CEAC83-C0B8-11D6-8734-00C0262CDD2C}' : VariableCollection,
	'{03CEAC86-C0B8-11D6-8734-00C0262CDD2C}' : MateConstraintCollection,
	'{03CEAC89-C0B8-11D6-8734-00C0262CDD2C}' : PartCollection,
	'{E6E78D63-C0FA-11D6-8734-00C0262CDD2C}' : MeshPartArrayDefinition,
	'{DDD05145-C180-11D6-8734-00C0262CDD2C}' : CircularPartArrayDefinition,
	'{DDD05148-C180-11D6-8734-00C0262CDD2C}' : CurvePartArrayDefinition,
	'{DDD0514B-C180-11D6-8734-00C0262CDD2C}' : DerivativePartArrayDefinition,
	'{0307BB83-C193-11D6-8734-00C0262CDD2C}' : Axis2PlanesDefinition,
	'{0307BB86-C193-11D6-8734-00C0262CDD2C}' : AxisOperationsDefinition,
	'{0307BB89-C193-11D6-8734-00C0262CDD2C}' : Axis2PointsDefinition,
	'{0307BB8C-C193-11D6-8734-00C0262CDD2C}' : AxisEdgeDefinition,
	'{0307BB8F-C193-11D6-8734-00C0262CDD2C}' : MeshCopyDefinition,
	'{0307BB92-C193-11D6-8734-00C0262CDD2C}' : CircularCopyDefinition,
	'{0307BB95-C193-11D6-8734-00C0262CDD2C}' : CurveCopyDefinition,
	'{0307BB98-C193-11D6-8734-00C0262CDD2C}' : MirrorCopyDefinition,
	'{0307BB9B-C193-11D6-8734-00C0262CDD2C}' : MirrorCopyAllDefinition,
	'{0307BB9E-C193-11D6-8734-00C0262CDD2C}' : ConicSpiralDefinition,
	'{0307BBA1-C193-11D6-8734-00C0262CDD2C}' : CylindricSpiralDefinition,
	'{0307BBA4-C193-11D6-8734-00C0262CDD2C}' : PolyLineDefinition,
	'{0307BBA7-C193-11D6-8734-00C0262CDD2C}' : SplineDefinition,
	'{0307BBAA-C193-11D6-8734-00C0262CDD2C}' : faceDefinition,
	'{0307BBAD-C193-11D6-8734-00C0262CDD2C}' : EdgeDefinition,
	'{0307BBB0-C193-11D6-8734-00C0262CDD2C}' : ChamferDefinition,
	'{0307BBB3-C193-11D6-8734-00C0262CDD2C}' : FilletDefinition,
	'{DEEFEFE3-C3E2-11D6-8734-00C0262CDD2C}' : BaseExtrusionDefinition,
	'{DEEFEFE6-C3E2-11D6-8734-00C0262CDD2C}' : BossExtrusionDefinition,
	'{DEEFEFE9-C3E2-11D6-8734-00C0262CDD2C}' : CutExtrusionDefinition,
	'{31E66F64-B93D-4196-B3FE-B6CCB679610F}' : ExtrusionSurfaceDefinition,
	'{DEEFEFEC-C3E2-11D6-8734-00C0262CDD2C}' : BaseLoftDefinition,
	'{DEEFEFEF-C3E2-11D6-8734-00C0262CDD2C}' : BossLoftDefinition,
	'{DEEFEFF2-C3E2-11D6-8734-00C0262CDD2C}' : CutLoftDefinition,
	'{5E1EB940-4CAE-43DE-B56D-8733FF6707DF}' : LoftSurfaceDefinition,
	'{DEEFEFF5-C3E2-11D6-8734-00C0262CDD2C}' : InclineDefinition,
	'{DEEFEFF8-C3E2-11D6-8734-00C0262CDD2C}' : ShellDefinition,
	'{DEEFEFFB-C3E2-11D6-8734-00C0262CDD2C}' : BaseEvolutionDefinition,
	'{DEEFEFFE-C3E2-11D6-8734-00C0262CDD2C}' : BossEvolutionDefinition,
	'{DEEFF001-C3E2-11D6-8734-00C0262CDD2C}' : CutEvolutionDefinition,
	'{DB947005-AA19-4ED2-9775-E7BD80BE872E}' : EvolutionSurfaceDefinition,
	'{DEEFF004-C3E2-11D6-8734-00C0262CDD2C}' : RibDefinition,
	'{DEEFF007-C3E2-11D6-8734-00C0262CDD2C}' : CutByPlaneDefinition,
	'{DEEFF00A-C3E2-11D6-8734-00C0262CDD2C}' : CutBySketchDefinition,
	'{DEEFF00D-C3E2-11D6-8734-00C0262CDD2C}' : PlaneOffsetDefinition,
	'{DEEFF010-C3E2-11D6-8734-00C0262CDD2C}' : PlaneAngleDefinition,
	'{DEEFF013-C3E2-11D6-8734-00C0262CDD2C}' : Plane3PointsDefinition,
	'{DEEFF016-C3E2-11D6-8734-00C0262CDD2C}' : PlaneNormalToSurfaceDefinition,
	'{DEEFF019-C3E2-11D6-8734-00C0262CDD2C}' : PlaneTangentToSurfaceDefinition,
	'{DEEFF01C-C3E2-11D6-8734-00C0262CDD2C}' : PlaneEdgePointDefinition,
	'{DEEFF01F-C3E2-11D6-8734-00C0262CDD2C}' : PlaneParallelDefinition,
	'{DEEFF022-C3E2-11D6-8734-00C0262CDD2C}' : PlanePerpendicularDefinition,
	'{DEEFF025-C3E2-11D6-8734-00C0262CDD2C}' : PlaneLineToEdgeDefinition,
	'{DEEFF028-C3E2-11D6-8734-00C0262CDD2C}' : PlaneLineToPlaneDefinition,
	'{DEEFF02B-C3E2-11D6-8734-00C0262CDD2C}' : ThinParam,
	'{DEEFF02E-C3E2-11D6-8734-00C0262CDD2C}' : ExtrusionParam,
	'{DEEFF031-C3E2-11D6-8734-00C0262CDD2C}' : RotatedParam,
	'{2DFACC63-C4A4-11D6-8734-00C0262CDD2C}' : ColorParam,
	'{2DFACC69-C4A4-11D6-8734-00C0262CDD2C}' : BaseRotatedDefinition,
	'{2DFACC6C-C4A4-11D6-8734-00C0262CDD2C}' : BossRotatedDefinition,
	'{2DFACC6F-C4A4-11D6-8734-00C0262CDD2C}' : CutRotatedDefinition,
	'{8B9ECAF3-172D-4F4B-BF51-33C177B87FF2}' : RotatedSurfaceDefinition,
	'{2DFACC72-C4A4-11D6-8734-00C0262CDD2C}' : SketchDefinition,
	'{CD6054FC-D754-4139-8CD9-381F7488A6C7}' : RasterFormatParam,
	'{13DF9CCA-122C-4CEC-87FA-CF16818E013A}' : AdditionFormatParam,
	'{77C095F7-3ABC-4292-B9E1-C112620AFC56}' : ConstraintParam,
	'{102FA83C-E0D6-4DB5-937A-FC149526899A}' : ImportedSurfaceDefinition,
	'{CB7B9677-9F62-473E-9663-AD516B5F37B5}' : FaceCollection,
	'{5CE6E053-3EC8-427B-BCB5-82B01D4BCBF3}' : VertexDefinition,
	'{1978BA1C-EE2F-48ED-86D7-B15065B36E4A}' : Feature,
	'{923A48A1-C159-4959-B13E-E8C558534C89}' : Tessellation,
	'{F7F45063-0B37-40B1-B3AD-BB0A545EC2C8}' : facet,
	'{E07C6920-E361-4A4D-9140-95969C26A9ED}' : Measurer,
	'{EEEAB203-43D8-4F04-A7CE-010D9BA419C2}' : BodyCollection,
	'{A99FFD41-AA46-4BFC-B6F2-32E1A956E0B1}' : body,
	'{B1C40242-CD49-4207-B728-B67057BEC339}' : Surface,
	'{7519BF63-27B3-415F-AC25-904910CB27B5}' : EdgeCollection,
	'{C66FB80F-97BE-4437-A8A0-AEDCFCBCF982}' : OrientedEdge,
	'{6EF08DCB-A1D4-43A2-ACAF-AF32FDE5F338}' : OrientedEdgeCollection,
	'{38386E28-C404-431E-9F30-5BE44B0F283F}' : Loop,
	'{3EA3B143-96A5-408A-897E-27D852E6EE9B}' : LoopCollection,
	'{54152184-0B08-4DFB-8249-4579A7368BF4}' : Curve3D,
	'{4D295A34-4F20-4231-8806-78E40213FA72}' : LineSeg3dParam,
	'{4E96B6C2-BF75-4B32-A4E7-7267F60A2593}' : Circle3dParam,
	'{33583282-14FB-4975-B040-9267A639E340}' : Ellipse3dParam,
	'{94A91D78-30AE-4B04-AEE2-B098D3270602}' : PlaneParam,
	'{3940C963-446D-4701-883C-A93BBDAC5469}' : ConeParam,
	'{379D658E-47BB-414F-A952-FB41037F17AC}' : CylinderParam,
	'{C82A3D03-4BEE-467F-9240-C1C58FDB144E}' : SphereParam,
	'{B7833CCA-936D-4689-BD90-90B5209D94E8}' : TorusParam,
	'{4F3C6D95-FBDC-4C53-AE82-9AF9C05093FF}' : NurbsPoint3dParam,
	'{BA13BE42-059B-4EEB-9C39-673732763EE3}' : NurbsSurfaceParam,
	'{F829344F-B49F-43A3-AC93-E817EF8D3319}' : Nurbs3dParam,
	'{81317653-9BBA-46FE-9877-AEEE62BD8AA4}' : NurbsKnotCollection,
	'{A2BD36E2-C99B-40FE-A6A7-E5A9CCDCF63D}' : NurbsPoint3dCollCollection,
	'{25AE92BA-055F-431E-AC3E-EA2E793D446C}' : NurbsPoint3dCollection,
	'{0CA54EDF-BC8C-4A6A-94CF-EDBA74A6FA00}' : ViewProjection,
	'{9A3E39C6-B6AB-42CF-9FBD-AC05F0B4B161}' : ViewProjectionCollection,
	'{39EE8E9D-C228-4F61-9F66-DD58F20CD224}' : SelectionMng,
	'{2280DF87-5688-4082-8FAE-6E4C84249352}' : ChooseMng,
	'{4CA2655E-EC4E-433C-9706-8E3864D5DBD2}' : Arc3dParam,
	'{05A4578F-A41F-48F2-92F9-A0F0856BCBC0}' : TreeNodeParam,
	'{7A86E2BA-6DE3-4DB3-AEB6-9738DAA69CFC}' : AssociationViewParam,
	'{34AFC10F-4FBB-40F0-8A23-74B1250F42EF}' : ViewColorParam,
	'{705962E9-5E9B-4379-8504-FA754D11FC66}' : AxisLineParam,
	'{02286DB8-98D4-4D0B-97D7-E2EED32EEBD6}' : TextDocumentParam,
	'{F37A40F6-4E15-4E01-B4F0-25C49175227A}' : RemoteElementParam,
	'{9807E658-53C5-4445-A389-3F800FB3BB8A}' : DeletedCopyCollection,
	'{8867DEAC-C699-41B6-BD3D-C470A52B1B9C}' : CopyObjectParam,
	'{2A8AE692-45A3-4C22-88B5-76B4830F2235}' : ThreadDefinition,
	'{E41D019C-2D40-452D-8F7B-3FB5FE2D3E8E}' : OverlapObjectOptions,
	'{620BFE17-2F66-4102-A8EA-4DD33C081061}' : Attribute3D,
	'{17CAB61A-770A-4FCE-8FC5-F291CDADF80A}' : Attribute3DCollection,
	'{7DAB018D-9EF9-4D0F-84BB-54B3DC0558D3}' : ComponentPositioner,
	'{ABBA6CE1-CB4C-4A32-98B4-B639352C75BA}' : ObjectsFilter3D,
	'{ABBA6CE1-CB4C-4A32-98B4-B639352C75BB}' : ParametrizationParam,
	'{DC7D3EDF-80EE-4BAF-930F-F221AC7E5A7A}' : Macro3DDefinition,
	'{C6BD0D90-C8BE-4378-9A71-835597A7D1E9}' : AxisConefaceDefinition,
	'{BA53B169-1DC8-4CCA-BAA4-27B0FB87AE26}' : UnionComponentsDefinition,
	'{FC4D7C29-C608-44D5-B927-1EC9FC147B18}' : MoldCavityDefinition,
	'{17150452-8320-4721-9765-13353F08AE7E}' : Coordinate3dCollection,
	'{ED41E352-E8A8-4B12-893F-17F064985CEE}' : IntersectionResult,
	'{D7844AFC-91B0-4C08-8622-0E4595BA6551}' : PlaneMiddleDefinition,
	'{3DA1922B-1FAB-4990-8D9A-8F03AFDB18D9}' : ControlPointDefinition,
	'{88BD7F23-21A6-4C90-B784-0B38FB7FD0F3}' : ConjunctivePointDefinition,
	'{9B59D68B-3502-4FE9-9E09-AC691443BF3E}' : ChooseBodies,
	'{8E8A474C-5ED5-4C72-AED6-EB04C317C7DE}' : AggregateDefinition,
	'{BC662523-43E2-41FF-A04B-3D92F8097DF9}' : ChangeLeaderParam,
	'{08B7A093-D829-44A9-A238-2BFF31770112}' : ksChooseParts,
	'{9FD4E52C-5B9B-4D07-B788-8D188EF940FD}' : ChooseParts,
	'{1E3E9348-DB9B-4967-A62A-B412DF95146A}' : ksBodyParts,
	'{4F6A3404-8F06-4363-AF66-4CDCC4E09462}' : ksEmbodiment3D,
	'{FEC5FF26-3F47-49B2-ABAE-5563A4D7AD94}' : ksSnapInfo,
	'{CF0E948C-5A9D-49A3-BC86-EEA3050193E0}' : ksSaveToPreviusParam,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
}


NamesToIIDMap = {
	'KompasObject' : '{E36BC97C-39D6-4402-9C25-C7008A217E02}',
	'ksDocument2D' : '{AF4E160D-5C89-4F21-B0F2-D53397BDAF78}',
	'ksObject2DNotify' : '{2E29C343-C521-4B0F-B37D-587D0347B7BA}',
	'ksSelectionMngNotify' : '{A421368A-34B6-4DDF-9A52-73B3488EE83F}',
	'ksObject2DNotifyResult' : '{1FE1EB28-CD28-4700-8E46-25CCFE9C0EC8}',
	'ksDocument2DNotify' : '{13F0BE95-3361-4AD9-90AF-D935EA64A127}',
	'ksDocument3D' : '{111CEFE1-A0A7-11D6-95CE-00C0262D30E3}',
	'ksDocument3DNotify' : '{B6C1BCFD-68DA-4A0A-A95C-296084C6A01A}',
	'ksEntity' : '{508A0CCA-9D74-11D6-95CE-00C0262D30E3}',
	'ksAttribute3DCollection' : '{EB61A981-F63E-47E1-BEE8-2D1612C78E78}',
	'ksAttribute3D' : '{3EEB2B43-56FF-49C0-AFCF-69E990A7D84C}',
	'ksFeatureCollection' : '{CE6A46FF-02B4-4C7E-AF50-3F3707C8B122}',
	'ksFeature' : '{088BF9A8-37D3-4B15-A7CA-8C52FF1DBC41}',
	'ksEntityCollection' : '{B0170141-C02C-11D6-8734-00C0262CDD2C}',
	'ksPart' : '{508A0CCD-9D74-11D6-95CE-00C0262D30E3}',
	'ksObject3DNotify' : '{BFA024B6-679E-4A95-B6C2-1EA47A7CD0E9}',
	'ksObject3DNotifyResult' : '{9C3ECC92-E72F-4892-8921-7886F34CA9AD}',
	'ksPlacement' : '{2DFACC64-C4A4-11D6-8734-00C0262CDD2C}',
	'ksComponentPositioner' : '{508B5962-DF59-4CEE-8611-AD10FDF0C811}',
	'ksKompasObjectNotify' : '{C7CB743A-C59D-4C27-8CB6-971C2A393F2F}',
	'ksDocumentFileNotify' : '{324C1A45-67AD-41FB-BE57-624F930646F1}',
	'ksDocument3DNotifyResult' : '{9F88CAAA-A50F-46F4-904A-846C792FA649}',
	'ksSpecRoughParam' : '{364521A3-94B5-11D6-8732-00C0262CDD2C}',
	'ksEllipseParam' : '{364521A6-94B5-11D6-8732-00C0262CDD2C}',
	'ksEllipseArcParam' : '{364521A9-94B5-11D6-8732-00C0262CDD2C}',
	'ksEllipseArcParam1' : '{364521AC-94B5-11D6-8732-00C0262CDD2C}',
	'ksEquidistantParam' : '{364521AF-94B5-11D6-8732-00C0262CDD2C}',
	'ksParagraphParam' : '{364521B2-94B5-11D6-8732-00C0262CDD2C}',
	'ksTextItemParam' : '{364521B7-94B5-11D6-8732-00C0262CDD2C}',
	'ksTextLineParam' : '{364521BA-94B5-11D6-8732-00C0262CDD2C}',
	'ksTextItemFont' : '{364521BD-94B5-11D6-8732-00C0262CDD2C}',
	'ksCornerParam' : '{E79C2501-9584-11D6-8732-00C0262CDD2C}',
	'ksContourParam' : '{E79C2504-9584-11D6-8732-00C0262CDD2C}',
	'ksLayerParam' : '{E79C2507-9584-11D6-8732-00C0262CDD2C}',
	'ksLineParam' : '{E79C250A-9584-11D6-8732-00C0262CDD2C}',
	'ksRegularPolygonParam' : '{E79C250D-9584-11D6-8732-00C0262CDD2C}',
	'ksRectangleParam' : '{E79C2510-9584-11D6-8732-00C0262CDD2C}',
	'ksBaseParam' : '{E79C2513-9584-11D6-8732-00C0262CDD2C}',
	'ksLtVariant' : '{E79C2516-9584-11D6-8732-00C0262CDD2C}',
	'ksUserParam' : '{E79C2519-9584-11D6-8732-00C0262CDD2C}',
	'ksMathPointParam' : '{3198E121-9585-11D6-95CE-00C0262D30E3}',
	'ksCurvePicture' : '{910EC541-958D-11D6-95CE-00C0262D30E3}',
	'ksCurvePattern' : '{910EC544-958D-11D6-95CE-00C0262D30E3}',
	'ksTAN' : '{8075EDE4-6C85-4711-8685-68FBE359D4C4}',
	'ksCON' : '{C175BFB8-D7D6-4325-BFDA-2A282B9D1119}',
	'ksInertiaParam' : '{EA92E649-239E-4105-BBD3-AEF4817BD783}',
	'ksMassInertiaParam' : '{283F77EB-7E2C-4F71-8B16-4D286FA4857E}',
	'ksMathematic2D' : '{F2D5AE01-45DE-4496-B01B-9958CAEF5943}',
	'ksDynamicArray' : '{4D91CD9A-6E02-409D-9360-CF7FEF60D31C}',
	'ksRDimDrawingParam' : '{2A4D4542-95B3-11D6-8732-00C0262CDD2C}',
	'ksRDimSourceParam' : '{2A4D4545-95B3-11D6-8732-00C0262CDD2C}',
	'ksRDimParam' : '{7F7D6F81-97DA-11D6-8732-00C0262CDD2C}',
	'ksLineSegParam' : '{7F7D6F84-97DA-11D6-8732-00C0262CDD2C}',
	'ksCircleParam' : '{7F7D6F87-97DA-11D6-8732-00C0262CDD2C}',
	'ksArcByAngleParam' : '{7F7D6F8A-97DA-11D6-8732-00C0262CDD2C}',
	'ksArcByPointParam' : '{7F7D6F8D-97DA-11D6-8732-00C0262CDD2C}',
	'ksPointParam' : '{7F7D6F90-97DA-11D6-8732-00C0262CDD2C}',
	'ksHatchParam' : '{7F7D6F93-97DA-11D6-8732-00C0262CDD2C}',
	'ksTextParam' : '{7F7D6F96-97DA-11D6-8732-00C0262CDD2C}',
	'ksNurbsPointParam' : '{7F7D6F99-97DA-11D6-8732-00C0262CDD2C}',
	'ksDoubleValue' : '{7F7D6F9C-97DA-11D6-8732-00C0262CDD2C}',
	'ksNurbsParam' : '{7F7D6F9F-97DA-11D6-8732-00C0262CDD2C}',
	'ksConicArcParam' : '{7F7D6FA2-97DA-11D6-8732-00C0262CDD2C}',
	'ksCentreParam' : '{7F7D6FA5-97DA-11D6-8732-00C0262CDD2C}',
	'ksPlacementParam' : '{7F7D6FA8-97DA-11D6-8732-00C0262CDD2C}',
	'ksRasterParam' : '{7F7D6FAB-97DA-11D6-8732-00C0262CDD2C}',
	'ksPolylineParam' : '{7F7D6FAE-97DA-11D6-8732-00C0262CDD2C}',
	'ksInsertFragmentParam' : '{7F7D6FB1-97DA-11D6-8732-00C0262CDD2C}',
	'ksViewParam' : '{7F7D6FB4-97DA-11D6-8732-00C0262CDD2C}',
	'ksLBreakDimSource' : '{7F7D6FB7-97DA-11D6-8732-00C0262CDD2C}',
	'ksBreakDimDrawing' : '{7F7D6FBA-97DA-11D6-8732-00C0262CDD2C}',
	'ksLBreakDimParam' : '{7F7D6FBD-97DA-11D6-8732-00C0262CDD2C}',
	'ksABreakDimParam' : '{7F7D6FC0-97DA-11D6-8732-00C0262CDD2C}',
	'ksInsertFragmentParamEx' : '{7F7D6FC3-97DA-11D6-8732-00C0262CDD2C}',
	'ksBezierParam' : '{7F7D6FC6-97DA-11D6-8732-00C0262CDD2C}',
	'ksBezierPointParam' : '{7F7D6FC9-97DA-11D6-8732-00C0262CDD2C}',
	'ksDimTextParam' : '{7F7D6FCC-97DA-11D6-8732-00C0262CDD2C}',
	'ksLDimSourceParam' : '{7F7D6FCF-97DA-11D6-8732-00C0262CDD2C}',
	'ksDimDrawingParam' : '{7F7D6FD2-97DA-11D6-8732-00C0262CDD2C}',
	'ksLDimParam' : '{7F7D6FD5-97DA-11D6-8732-00C0262CDD2C}',
	'ksADimSourceParam' : '{7F7D6FD8-97DA-11D6-8732-00C0262CDD2C}',
	'ksDimensionPartsParam' : '{7F7D6FDB-97DA-11D6-8732-00C0262CDD2C}',
	'ksADimParam' : '{7F7D6FDE-97DA-11D6-8732-00C0262CDD2C}',
	'ksRBreakDrawingParam' : '{7F7D6FE1-97DA-11D6-8732-00C0262CDD2C}',
	'ksRBreakDimParam' : '{7F7D6FE4-97DA-11D6-8732-00C0262CDD2C}',
	'ksQualityItemParam' : '{7F7D6FE7-97DA-11D6-8732-00C0262CDD2C}',
	'ksQualityContensParam' : '{7F7D6FEA-97DA-11D6-8732-00C0262CDD2C}',
	'ksIterator' : '{D06C9101-98CA-11D6-8732-00C0262CDD2C}',
	'ksFragment' : '{D06C9104-98CA-11D6-8732-00C0262CDD2C}',
	'ksFragmentLibrary' : '{D06C910A-98CA-11D6-8732-00C0262CDD2C}',
	'ksTechnicalDemandParam' : '{FBCC5B81-996C-11D6-8732-00C0262CDD2C}',
	'ksOrdinatedSourceParam' : '{FBCC5B84-996C-11D6-8732-00C0262CDD2C}',
	'ksOrdinatedDimParam' : '{FBCC5B87-996C-11D6-8732-00C0262CDD2C}',
	'ksOrdinatedDrawingParam' : '{FBCC5B8A-996C-11D6-8732-00C0262CDD2C}',
	'ksSheetSize' : '{FBCC5B8D-996C-11D6-8732-00C0262CDD2C}',
	'ksStandartSheet' : '{FBCC5B90-996C-11D6-8732-00C0262CDD2C}',
	'ksSheetPar' : '{FBCC5B93-996C-11D6-8732-00C0262CDD2C}',
	'ksDocumentParam' : '{FBCC5B96-996C-11D6-8732-00C0262CDD2C}',
	'ksDimensionsOptions' : '{FBCC5B99-996C-11D6-8732-00C0262CDD2C}',
	'ksSnapOptions' : '{FBCC5B9C-996C-11D6-8732-00C0262CDD2C}',
	'ksLibraryStyleParam' : '{FBCC5B9F-996C-11D6-8732-00C0262CDD2C}',
	'ksStampNotify' : '{404E7D5A-A13F-4CFF-8214-FEA7012110CB}',
	'ksStamp' : '{FBCC5BA5-996C-11D6-8732-00C0262CDD2C}',
	'ksSheetOptions' : '{FBCC5BA8-996C-11D6-8732-00C0262CDD2C}',
	'ksCurvePatternEx' : '{910EC549-958D-11D6-95CE-00C0262D30E3}',
	'ksCurveStyleParam' : '{910EC54C-958D-11D6-95CE-00C0262D30E3}',
	'ksTextStyleParam' : '{3F715E24-97D9-11D6-95CE-00C0262D30E3}',
	'ksHatchLineParam' : '{3F715E27-97D9-11D6-95CE-00C0262D30E3}',
	'ksHatchStyleParam' : '{3F715E2A-97D9-11D6-95CE-00C0262D30E3}',
	'ksRectParam' : '{3F715E2D-97D9-11D6-95CE-00C0262D30E3}',
	'ksShelfPar' : '{3F715E30-97D9-11D6-95CE-00C0262D30E3}',
	'ksRoughPar' : '{3F715E33-97D9-11D6-95CE-00C0262D30E3}',
	'ksRoughParam' : '{3F715E36-97D9-11D6-95CE-00C0262D30E3}',
	'ksChar255' : '{3F715E39-97D9-11D6-95CE-00C0262D30E3}',
	'ksLeaderParam' : '{3F715E40-97D9-11D6-95CE-00C0262D30E3}',
	'ksPosLeaderParam' : '{3F715E43-97D9-11D6-95CE-00C0262D30E3}',
	'ksBrandLeaderParam' : '{3F715E46-97D9-11D6-95CE-00C0262D30E3}',
	'ksMarkerLeaderParam' : '{9AF8E341-98A0-11D6-95CE-00C0262D30E3}',
	'ksType1' : '{9AF8E344-98A0-11D6-95CE-00C0262D30E3}',
	'ksType2' : '{9AF8E347-98A0-11D6-95CE-00C0262D30E3}',
	'ksType3' : '{9AF8E34A-98A0-11D6-95CE-00C0262D30E3}',
	'ksType5' : '{9AF8E34D-98A0-11D6-95CE-00C0262D30E3}',
	'ksType6' : '{9AF8E350-98A0-11D6-95CE-00C0262D30E3}',
	'ksPhantom' : '{9AF8E353-98A0-11D6-95CE-00C0262D30E3}',
	'ksRequestInfo' : '{9AF8E356-98A0-11D6-95CE-00C0262D30E3}',
	'ksViewPointerParam' : '{CD1C0144-98DC-11D6-95CE-00C0262D30E3}',
	'ksCutLineParam' : '{4FD7CE81-9968-11D6-95CE-00C0262D30E3}',
	'ksToleranceBranch' : '{4FD7CE84-9968-11D6-95CE-00C0262D30E3}',
	'ksToleranceParam' : '{4FD7CE87-9968-11D6-95CE-00C0262D30E3}',
	'ksSpcColumnParam' : '{4FD7CE8A-9968-11D6-95CE-00C0262D30E3}',
	'ksRecordTypeAttrParam' : '{4FD7CE8D-9968-11D6-95CE-00C0262D30E3}',
	'ksNumberTypeAttrParam' : '{4FD7CE90-9968-11D6-95CE-00C0262D30E3}',
	'ksSpcStyleColumnParam' : '{4FD7CE93-9968-11D6-95CE-00C0262D30E3}',
	'ksSpcStyleSectionParam' : '{4FD7CE96-9968-11D6-95CE-00C0262D30E3}',
	'ksSpcSubSectionParam' : '{4FD7CE99-9968-11D6-95CE-00C0262D30E3}',
	'ksSpcTuningSectionParam' : '{4FD7CE9C-9968-11D6-95CE-00C0262D30E3}',
	'ksSpcTuningStyleParam' : '{4FD7CE9F-9968-11D6-95CE-00C0262D30E3}',
	'ksSpcStyleParam' : '{4FD7CEA2-9968-11D6-95CE-00C0262D30E3}',
	'ksSpcDescrParam' : '{4FD7CEA5-9968-11D6-95CE-00C0262D30E3}',
	'ksDocAttachedSpcParam' : '{4FD7CEA8-9968-11D6-95CE-00C0262D30E3}',
	'ksSpcObjParam' : '{4FD7CEAB-9968-11D6-95CE-00C0262D30E3}',
	'ksLibStyle' : '{4FD7CEAE-9968-11D6-95CE-00C0262D30E3}',
	'ksDataBaseObject' : '{0981CD01-9A49-11D6-8732-00C0262CDD2C}',
	'ksSpcDocumentNotify' : '{1BD030F4-4058-4A86-9F4F-1AEEF8BE8D23}',
	'ksSpcDocument' : '{51E74521-9A3A-11D6-95CE-00C0262D30E3}',
	'ksSpcObjectNotify' : '{AC5004D1-C240-41FC-AB84-7EB5C793AE7F}',
	'ksSpecificationNotify' : '{0331AB4B-F25B-4EB9-9C8A-BFEA414E3822}',
	'ksSpecification' : '{51E74524-9A3A-11D6-95CE-00C0262D30E3}',
	'ksDocumentTxt' : '{74D745F1-9A3A-11D6-95CE-00C0262D30E3}',
	'ksAttributeTypeParam' : '{CC26DA61-9B22-11D6-95CE-00C0262D30E3}',
	'ksColumnInfoParam' : '{CE0D05E1-9B2A-11D6-95CE-00C0262D30E3}',
	'ksAttributeParam' : '{CE0D05E4-9B2A-11D6-95CE-00C0262D30E3}',
	'ksVariable' : '{508A0CC1-9D74-11D6-95CE-00C0262D30E3}',
	'ksLibraryAttrTypeParam' : '{FA93AA21-9B3D-11D6-95CE-00C0262D30E3}',
	'ksAttributeObject' : '{FA93AA24-9B3D-11D6-95CE-00C0262D30E3}',
	'ksRequestInfo3D' : '{E9807824-9D55-11D6-95CE-00C0262D30E3}',
	'ksMateConstraint' : '{508A0CC4-9D74-11D6-95CE-00C0262D30E3}',
	'ksDefaultObject' : '{508A0CC7-9D74-11D6-95CE-00C0262D30E3}',
	'ksModelLibrary' : '{111CEFE4-A0A7-11D6-95CE-00C0262D30E3}',
	'ksVariableCollection' : '{03CEAC81-C0B8-11D6-8734-00C0262CDD2C}',
	'ksMateConstraintCollection' : '{03CEAC84-C0B8-11D6-8734-00C0262CDD2C}',
	'ksPartCollection' : '{03CEAC87-C0B8-11D6-8734-00C0262CDD2C}',
	'ksMeshPartArrayDefinition' : '{E6E78D61-C0FA-11D6-8734-00C0262CDD2C}',
	'ksCircularPartArrayDefinition' : '{DDD05143-C180-11D6-8734-00C0262CDD2C}',
	'ksCurvePartArrayDefinition' : '{DDD05146-C180-11D6-8734-00C0262CDD2C}',
	'ksDerivativePartArrayDefinition' : '{DDD05149-C180-11D6-8734-00C0262CDD2C}',
	'ksAxis2PlanesDefinition' : '{0307BB81-C193-11D6-8734-00C0262CDD2C}',
	'ksAxisOperationsDefinition' : '{0307BB84-C193-11D6-8734-00C0262CDD2C}',
	'ksAxis2PointsDefinition' : '{0307BB87-C193-11D6-8734-00C0262CDD2C}',
	'ksAxisEdgeDefinition' : '{0307BB8A-C193-11D6-8734-00C0262CDD2C}',
	'ksMeshCopyDefinition' : '{0307BB8D-C193-11D6-8734-00C0262CDD2C}',
	'ksCircularCopyDefinition' : '{0307BB90-C193-11D6-8734-00C0262CDD2C}',
	'ksCurveCopyDefinition' : '{0307BB93-C193-11D6-8734-00C0262CDD2C}',
	'ksMirrorCopyDefinition' : '{0307BB96-C193-11D6-8734-00C0262CDD2C}',
	'ksMirrorCopyAllDefinition' : '{0307BB99-C193-11D6-8734-00C0262CDD2C}',
	'ksConicSpiralDefinition' : '{0307BB9C-C193-11D6-8734-00C0262CDD2C}',
	'ksCylindricSpiralDefinition' : '{0307BB9F-C193-11D6-8734-00C0262CDD2C}',
	'ksPolyLineDefinition' : '{0307BBA2-C193-11D6-8734-00C0262CDD2C}',
	'ksPolyLineVertexParam' : '{1BCC4F0F-1091-41A3-895B-0608D20715B7}',
	'ksSplineDefinition' : '{0307BBA5-C193-11D6-8734-00C0262CDD2C}',
	'ksBaseExtrusionDefinition' : '{DEEFEFE1-C3E2-11D6-8734-00C0262CDD2C}',
	'ksBossExtrusionDefinition' : '{DEEFEFE4-C3E2-11D6-8734-00C0262CDD2C}',
	'ksCutExtrusionDefinition' : '{DEEFEFE7-C3E2-11D6-8734-00C0262CDD2C}',
	'ksExtrusionSurfaceDefinition' : '{B20E24C3-5E4A-4CDA-A1ED-6BB8EBC81A29}',
	'ksFaceDefinition' : '{0307BBA8-C193-11D6-8734-00C0262CDD2C}',
	'ksEdgeDefinition' : '{0307BBAB-C193-11D6-8734-00C0262CDD2C}',
	'ksChamferDefinition' : '{0307BBAE-C193-11D6-8734-00C0262CDD2C}',
	'ksFilletDefinition' : '{0307BBB1-C193-11D6-8734-00C0262CDD2C}',
	'ksBaseLoftDefinition' : '{DEEFEFEA-C3E2-11D6-8734-00C0262CDD2C}',
	'ksBossLoftDefinition' : '{DEEFEFED-C3E2-11D6-8734-00C0262CDD2C}',
	'ksCutLoftDefinition' : '{DEEFEFF0-C3E2-11D6-8734-00C0262CDD2C}',
	'ksLoftSurfaceDefinition' : '{E04339B5-AA08-4717-8E50-90ED0E375624}',
	'ksInclineDefinition' : '{DEEFEFF3-C3E2-11D6-8734-00C0262CDD2C}',
	'ksShellDefinition' : '{DEEFEFF6-C3E2-11D6-8734-00C0262CDD2C}',
	'ksBaseEvolutionDefinition' : '{DEEFEFF9-C3E2-11D6-8734-00C0262CDD2C}',
	'ksBossEvolutionDefinition' : '{DEEFEFFC-C3E2-11D6-8734-00C0262CDD2C}',
	'ksCutEvolutionDefinition' : '{DEEFEFFF-C3E2-11D6-8734-00C0262CDD2C}',
	'ksEvolutionSurfaceDefinition' : '{2BD4C79E-E2C3-42E8-8FCC-B51FFBDE9F69}',
	'ksRibDefinition' : '{DEEFF002-C3E2-11D6-8734-00C0262CDD2C}',
	'ksCutByPlaneDefinition' : '{DEEFF005-C3E2-11D6-8734-00C0262CDD2C}',
	'ksCutBySketchDefinition' : '{DEEFF008-C3E2-11D6-8734-00C0262CDD2C}',
	'ksPlaneOffsetDefinition' : '{DEEFF00B-C3E2-11D6-8734-00C0262CDD2C}',
	'ksPlaneAngleDefinition' : '{DEEFF00E-C3E2-11D6-8734-00C0262CDD2C}',
	'ksPlane3PointsDefinition' : '{DEEFF011-C3E2-11D6-8734-00C0262CDD2C}',
	'ksPlaneNormalToSurfaceDefinition' : '{DEEFF014-C3E2-11D6-8734-00C0262CDD2C}',
	'ksPlaneTangentToSurfaceDefinition' : '{DEEFF017-C3E2-11D6-8734-00C0262CDD2C}',
	'ksPlaneEdgePointDefinition' : '{DEEFF01A-C3E2-11D6-8734-00C0262CDD2C}',
	'ksPlaneParallelDefinition' : '{DEEFF01D-C3E2-11D6-8734-00C0262CDD2C}',
	'ksPlanePerpendicularDefinition' : '{DEEFF020-C3E2-11D6-8734-00C0262CDD2C}',
	'ksPlaneLineToEdgeDefinition' : '{DEEFF023-C3E2-11D6-8734-00C0262CDD2C}',
	'ksPlaneLineToPlaneDefinition' : '{DEEFF026-C3E2-11D6-8734-00C0262CDD2C}',
	'ksThinParam' : '{DEEFF029-C3E2-11D6-8734-00C0262CDD2C}',
	'ksExtrusionParam' : '{DEEFF02C-C3E2-11D6-8734-00C0262CDD2C}',
	'ksRotatedParam' : '{DEEFF02F-C3E2-11D6-8734-00C0262CDD2C}',
	'ksColorParam' : '{2DFACC61-C4A4-11D6-8734-00C0262CDD2C}',
	'ksBaseRotatedDefinition' : '{2DFACC67-C4A4-11D6-8734-00C0262CDD2C}',
	'ksBossRotatedDefinition' : '{2DFACC6A-C4A4-11D6-8734-00C0262CDD2C}',
	'ksCutRotatedDefinition' : '{2DFACC6D-C4A4-11D6-8734-00C0262CDD2C}',
	'ksRotatedSurfaceDefinition' : '{FD27841D-1374-4F7F-AE8A-C2A44F89120D}',
	'ksSketchDefinition' : '{2DFACC70-C4A4-11D6-8734-00C0262CDD2C}',
	'ksRasterFormatParam' : '{1A91A8AB-AF8C-4EE3-86D4-0A9C00123195}',
	'ksAdditionFormatParam' : '{0FD25FF9-AB0A-48F3-BAD4-F193116C0887}',
	'ksConstraintParam' : '{862E250D-9DB1-47E8-8EE2-9BE2D2453D5A}',
	'ksImportedSurfaceDefinition' : '{78A2C35E-A7DA-414E-B90A-F19998EC7BD1}',
	'ksFaceCollection' : '{0E95ACE0-0E73-406F-AE94-E8A0592E298D}',
	'ksVertexDefinition' : '{A7257E73-EB61-4602-BC8B-2D00EA4AA062}',
	'ksTessellation' : '{B810650E-7819-485C-90D2-ADEB647AE5E2}',
	'ksFacet' : '{EB6AFBC0-C387-4E07-B24E-DDF2B7926A26}',
	'ksMeasurer' : '{ABC84FE5-3945-4A0B-820A-719BF4B79224}',
	'ksBodyCollection' : '{CFC49C01-7653-4845-93FD-13428F5D58EC}',
	'ksBody' : '{03EFC9DD-E05A-4277-BC7C-4FD499A252DE}',
	'ksSurface' : '{963CB6E1-B9BF-4234-964A-13BFE6C0282A}',
	'ksEdgeCollection' : '{6096A4FD-970B-468C-815E-37CA1970A203}',
	'ksOrientedEdge' : '{88C32A80-3735-4E18-A02E-9B2A8F0A90E3}',
	'ksOrientedEdgeCollection' : '{5CE8909D-CF3D-418F-A9B9-0A12B23916C0}',
	'ksLoop' : '{22BC5C86-CF58-45E4-AA46-5E8D5A825798}',
	'ksLoopCollection' : '{1BD7207E-36AA-47DF-913E-AD26DE6C16E8}',
	'ksCurve3D' : '{7572648A-D4EE-41FE-8D74-EC7D1F91BDE2}',
	'ksLineSeg3dParam' : '{DC8F6A7B-FF16-46FF-986D-2F7E1F6B25C4}',
	'ksCircle3dParam' : '{82758442-C9EB-48F7-B304-083C5E64D4E0}',
	'ksEllipse3dParam' : '{5B8082B8-6AD3-4509-826D-D23B7F613213}',
	'ksPlaneParam' : '{6A6F6B95-D100-4D54-A430-70A42D342917}',
	'ksConeParam' : '{CCFA0D95-0834-4F92-988B-6E477AD67589}',
	'ksCylinderParam' : '{5D462836-CF69-4995-AB78-8C7A83D09BD7}',
	'ksSphereParam' : '{C32977F3-3CA7-4D56-8AE7-4963E6851B75}',
	'ksTorusParam' : '{FDA3B147-BAF1-4F75-99AA-39D11323EA97}',
	'ksNurbsPoint3dParam' : '{F1CD604D-1D26-4F6B-8F94-F112133E6162}',
	'ksNurbsSurfaceParam' : '{A12B63E8-9E0A-4854-B724-E18275B9FF20}',
	'ksNurbs3dParam' : '{4DDDAEDB-2819-42D9-BDBB-4CCBC98D76DF}',
	'ksNurbsKnotCollection' : '{483E9889-E1CA-4CA5-BE4E-ECB3D5CF0126}',
	'ksNurbsPoint3dCollCollection' : '{84AF9C81-1795-4631-B58A-101732262E75}',
	'ksNurbsPoint3dCollection' : '{3AD5E519-74E2-4D3B-B6A3-B1E81F1006F1}',
	'ksViewProjection' : '{BF65B990-C2DC-4A12-9EB7-3E868608AF47}',
	'ksViewProjectionCollection' : '{A174F872-C800-409E-9FB2-FF5B89D8B4B8}',
	'ksSelectionMng' : '{BE41850C-CFC5-40D4-AE49-37AA391BCF4B}',
	'ksChooseMng' : '{8F2AA755-D9D1-42A0-97BF-C92548CE7232}',
	'ksArc3dParam' : '{7DCBCC76-5041-4C1E-9B33-12B1352D6D57}',
	'ksTreeNodeParam' : '{9F8DE1DC-1268-4785-9217-1B0DD59B85FA}',
	'ksAssociationViewParam' : '{C81EB1DA-BCB0-491A-8D22-923BF817D572}',
	'ksViewColorParam' : '{5A42B962-8F78-4557-B17A-1B871F8DBDB5}',
	'ksAxisLineParam' : '{AFE694D7-C1E5-468F-99B0-FE4C60C49899}',
	'ksTextDocumentParam' : '{33706D56-D085-4840-833B-435AEB00BE2A}',
	'ksRemoteElementParam' : '{25076616-4949-455E-A45C-1B801884D825}',
	'ksDeletedCopyCollection' : '{82F60797-D69C-4EB4-9F1A-24D625D5EAFA}',
	'ksCopyObjectParam' : '{AACAD820-7790-46EB-B17F-06AE42215ED7}',
	'ksThreadDefinition' : '{5DDB6B14-6F3D-431F-B62F-C5FCCAFC3632}',
	'ksOverlapObjectOptions' : '{F78E6B71-BEF3-4A4D-AE50-FE96426F6FD1}',
	'ksObjectsFilter3D' : '{ABBA6CE0-CB4C-4A32-98B4-B639352C75BA}',
	'ksParametrizationParam' : '{ABBA6CE0-CB4C-4A32-98B4-B639352C75BB}',
	'ksMacro3DDefinition' : '{02556461-D088-4F00-AE61-D366082DB9BC}',
	'ksAxisConefaceDefinition' : '{97337DAF-B7CD-4FB8-8E18-23F0230E5CBE}',
	'ksUnionComponentsDefinition' : '{99797F89-FBA4-4582-812F-226AFB50ED7D}',
	'ksMoldCavityDefinition' : '{BE5F10F5-B198-49D9-9140-B2B91E060533}',
	'ksCoordinate3dCollection' : '{E4091969-1C4E-4959-8D93-C2421564418B}',
	'ksIntersectionResult' : '{ABC7F8EE-CF07-4AA8-98A1-0DE35DB35B9E}',
	'ksPlaneMiddleDefinition' : '{CC5E3539-5B35-46FC-AFE1-19BB0168D52F}',
	'ksControlPointDefinition' : '{BC4C15A4-16E9-4CFA-A33E-CC86BA2FB546}',
	'ksConjunctivePointDefinition' : '{177CBAF3-87E6-4376-B6A9-669C0E661BFF}',
	'ksChooseBodies' : '{E06B18BF-D2AF-4201-99BE-B7FA9EECF7A8}',
	'ksAggregateDefinition' : '{44277B89-EEB4-456C-8EF9-2DC48D61EC91}',
	'ksChangeLeaderParam' : '{391938AE-79B6-4E3B-9815-AC1A31D9EA9D}',
	'ksChooseParts' : '{08B7A093-D829-44A9-A238-2BFF31770112}',
	'ksBodyParts' : '{1E3E9348-DB9B-4967-A62A-B412DF95146A}',
	'ksEmbodiment3D' : '{4F6A3404-8F06-4363-AF66-4CDCC4E09462}',
	'ksSnapInfo' : '{FEC5FF26-3F47-49B2-ABAE-5563A4D7AD94}',
	'ksSaveToPreviusParam' : '{CF0E948C-5A9D-49A3-BC86-EEA3050193E0}',
}


