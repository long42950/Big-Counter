from pynput import keyboard
import sys
import os
import big_number as BN

number = 0
clear = lambda: os.system('cls')
BN.set_front_margin(35)

def main():
    print("Press up to increase, down to decrease, Esc to stop counting:")
    print("==================================================================================")
    print("   _____                          _     _____ _                 _   _             ")
    print("  / ____|                        | |   |_   _| |               | | (_)            ")
    print(" | |    _   _ _ __ _ __ ___ _ __ | |_    | | | |_ ___ _ __ __ _| |_ _  ___  _ __  ")
    print(" | |   | | | | '__| '__/ _ \ '_ \| __|   | | | __/ _ \ '__/ _` | __| |/ _ \| '_ \ ")
    print(" | |___| |_| | |  | | |  __/ | | | |_   _| |_| ||  __/ | | (_| | |_| | (_) | | | |")
    print("  \_____\__,_|_|  |_|  \___|_| |_|\__| |_____|\__\___|_|  \__,_|\__|_|\___/|_| |_|")
    print("                                                                                  ")
    print("==================================================================================")

def percentage():
    size = 250000
    for i in range(size):
        progress = i / size * 100
        output = str(i)+" out of " + str(size) + " product checked..."
        sys.stdout.write(output+"\r" if i != size else "")
        if i != size:
                sys.stdout.flush()         
    print("All products checked...")    

main()

def on_release(key):
    global number, clear
    clear()
    main()
    if key == keyboard.Key.up:
        number += 1
    elif key == keyboard.Key.down and number > 0:
        number -= 1
    #sys.stdout.write("Current number: {0}\r".format(number))
    sys.stdout.write(BN.show_number(number))
    sys.stdout.flush()

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()


