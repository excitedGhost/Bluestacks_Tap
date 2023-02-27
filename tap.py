import subprocess #Import subprocess
from pynput import keyboard #Import pynput


index = 0 #Indexer
adb_command = "adb shell input tap x y" #Command

dim_x,dim_y = (1920,1080) #Screen dimensions
percent_x = [66,68,72,79] # X_Percentages
percent_y = [75,64,54,45] # Y_Percentages

def tapper(): #This Function Taps the screen
    x = (percent_x[index]/100) * dim_x
    y = (percent_y[index]/100) * dim_y
    global adb_command
    command = adb_command.replace("x", str(x)).replace("y", str(y))
    subprocess.run(command.split())

#Key process
def on_key_press(key):
    global index
    try:
        if key.char == '1': #Pressing 1 goes down instead
            tapper()
            if index < 0:
                index = len(percent_x) -1
            index -= 1
            #1 reduces indexer by one
        elif key.char == '2':
            tapper()
            index += 1
            index = index % (len(percent_x))
            #2 Increases Indexer by 1 #Pressing 2 goes up instead
        elif key.char == '0':
            exit()
            
    except AttributeError:
        pass

#Listener
listener = keyboard.Listener(on_press=on_key_press)

listener.start()

listener.join()