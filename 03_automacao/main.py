import pyautogui as auto

def main():
    auto.PRESS = 0.75
    # NOTE AUTO.PRESS: adiciona um delay para todos os comandos!!!!
    auto.press("win") #NOTE AUTO PRESS: pressiona a tetcla
    auto.write("firefox") #NOTE: AUTO.WRITE: digita pelo computador
    auto.press("enter")
    auto.sleep(2) #NOTE AUTO.SLEEP: 
    auto.write("globo.com")
    auto.press("enter")
    auto.hotkey("ctrl","t") # NOTE AUTO.HOTKEY: é usado para teclas de atalho
    auto.sleep(3)
    auto.write("sistemafibra.org.br/senai")
    auto.press("enter")
    auto.hotkey("ctrl","shift","n")
    auto.sleep(3)
    auto.write("metropoles.com")
    auto.press("enter")

               