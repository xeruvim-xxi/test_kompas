
import pythoncom
import subprocess
from win32com.client import Dispatch, gencache
from win32com.client.dynamic import debug_print

from libs.KompasAPI7 import *
from libs.Kompas6API5 import *
# import libs.ksConstants
# import libs.ksConstants3D
# import libs.LDefin2D
# import libs.MiscellaneousHelpers as MH

# Подключение к API5 программы Kompas 3D
def get_kompas_api5():
    kompas6_api5_module = gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)
    kompas_object = KompasObject(kompas6_api5_module.KompasObject(Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(kompas6_api5_module.KompasObject.CLSID, pythoncom.IID_IDispatch)))
    #MH.iKompasObject  = kompas_object
    return kompas6_api5_module, kompas_object

# Подключение к API7 программы Kompas 3D
def get_kompas_api7():
    kompas_api7_module = gencache.EnsureModule("{69AC2981-37C0-4379-84FD-5DD2F3C0A520}", 0, 1, 0)
    kompas_api7_object = IKompasAPIObject(kompas_api7_module.IKompasAPIObject(Dispatch("Kompas.Application.7")._oleobj_.QueryInterface(kompas_api7_module.IKompasAPIObject.CLSID, pythoncom.IID_IDispatch)))
    #MH.iApplication  = application    
    return kompas_api7_module, kompas_api7_object

#  Подключим константы API Компас
def get_kompas_constants():
    kompas6_constants = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants
    return kompas6_constants

#  Подключим константы 3D API Компас
def get_kompas_constants3D():
    kompas6_constants_3d = gencache.EnsureModule("{2CAF168C-7961-4B90-9DA2-701419BEEFE3}", 0, 1, 0).constants
    return kompas6_constants_3d

# Функция проверяет, запущена ли программа Kompas 3D
def is_running():    
    proc_list = str(subprocess.Popen('tasklist /NH /FI "IMAGENAME eq KOMPAS*"',
                                 shell=False,
                                 stdout=subprocess.PIPE).communicate()[0])  
    if (proc_list.find("KOMPAS.Exe") == -1):
        return False
    else:
        return True

is_run = is_running()                           # Установим флаг, который нам говорит, запущена ли программа до запуска нашего скрипта

module_api5, kompas5 = get_kompas_api5()
module_api7, kompas_api7_object = get_kompas_api7()
constants = get_kompas_constants()
constants3D = get_kompas_constants3D()

komp7 = IApplication(kompas_api7_object.Application)
komp7.Visible = True
#komp7.HideMessage = constants.ksHideMessageNo   # Отвечаем НЕТ на любые вопросы программы

Documents = komp7.Documents

kompas5.ksMessage("Привет")

print(komp7.ApplicationName(FullName=True))

if not is_run: komp7.Quit()                     # Выходим из программы
