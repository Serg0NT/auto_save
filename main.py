from pathlib import Path
import pyclip
import pyautogui as pag

BASE_DIR = str(Path(__file__).resolve().parent) + "\\images"
check_image = BASE_DIR + "\\check.png"

pag.PAUSE = 1


def click_and_save(image) -> str:
    locate = pag.locateOnScreen(image)
    pag.moveTo(locate[0] + 90, locate[1])
    
    # pag.moveRel()
    pag.click(clicks=2)
    # pag.click(locate, clicks=2)
    

    # pag.hotkey("ctrl", "a")
    # pag.hotkey("ctrl", "c")

    # check = pyclip.paste().decode("utf-8").lstrip("0")

    # print(check, type(check))


click_and_save(check_image)
