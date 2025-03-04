import pywhatkit
import pyautogui
import time


try:
    minha_msg: str = 'Òla bom dia'
    sicred: str = "+5511959233423"

    pywhatkit.sendwhatmsg_instantly(sicred, minha_msg, wait_time=14, close_time=13, tab_close=False)
    time.sleep(5)
    pywhatkit.sendwhatmsg_instantly(sicred, sicred, 15, close_time= 14, tab_close=False)


    fot = pyautogui.locateOnScreen('set.PNG', minSearchTime=3)

except:
    print("Fim da Lista")




























