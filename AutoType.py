from pynput.keyboard import Key, Listener, Controller

import time



keyboard = Controller()

# for Full Autotype make sure disable auto indentation vscode etc "editor.autoIndent": "none"
type_style = input('1 = Full AutoType | 2 = Line by line best programmers: ')
#  ======== settings ========
file = open('data.py','r',encoding="utf-8")


resume_key = Key.f4
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause
 
    
    if key == resume_key and pause:
        pause = False
        print("[Pause]")
    elif key == resume_key and not pause:
        pause = True
        print('Resume')
    else:
        pass


def display_controls():
    print("// AutoTyper")
    print("// - Settings: ")
    
    

    print("// - Controls:")
    print("\t press F4 twoice to start or once F4 to pause and resume")
    
    print("-----------------------------")
    print('Press F4 to start ...')


def line_by_line():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        while not pause:
            for i in file.readline():
                for char in i:
                    if i == "\n":
                        continue
                    else:
                        i = char

                    keyboard.press(char)
                    keyboard.release(char)
                    time.sleep(0.09)
                    while not pause:
                        continue
                    else:
                        pass          
    lis.stop()        

def all_lines():
    lis = Listener(on_press=on_press)
    lis.start()
    display_controls()
    while running:
        while not pause:
            for i in file.read():
                for char in i:
                    if i == "\n":
                        keyboard.press(Key.enter)
                    else:
                        i = char

                    keyboard.press(char)
                    keyboard.release(char)
                    time.sleep(0.12)
                    while not pause:
                        continue
                    else:
                        pass          
            

    lis.stop()


if __name__ == "__main__":
    if type_style == '1':
        all_lines()
    else:
        line_by_line()
   