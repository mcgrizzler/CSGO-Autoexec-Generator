import  os
def main():
    first_run = readState()
    if first_run is True:
        print("Auto Exec Already Backed Up")
        autoexec_path = findInstall() + "\csgo\cfg"
        print("Auto-Exec Located at: ", autoexec_path)
    else:
        print("It looks like this is the first time you've run this program.")
        userInput = input("Would you like to backup your current autoexec? (Y/N): ")
        if userInput.lower() == "y":
            print("Auto Exec Backed up")
            autoexec_path = findInstall() + "\csgo\cfg"
            print("Auto-Exec Located at: ", autoexec_path)
        else:
            print("Auto Exec Not Backed up")
            autoexec_path = findInstall() + "\csgo\cfg"
            print("Auto-Exec Located at: ", autoexec_path)

def findInstall():
    regular_path = "C:\Program Files (x86)\Steam\steamapps\common"
    dirs = os.listdir(regular_path)
    signal = 0
    custom_signal = 0
    done = False
    while not done:
        for i in dirs:
            if i == "csgo.exe":
                signal = signal +1
        if signal == 1:
            print("CSGO Install Successfully Detected")
            return regular_path
            done = True
        else:
            path = input("No CSGO Install Detected, Please specify the path to your install: ")
            regular_path = path
            custom_dir = os.listdir(regular_path)
            for i in custom_dir:
                if i == "csgo.exe":
                    custom_signal = custom_signal + 1
        if custom_signal == 1:
            print("CSGO Install Now Successfully Detected")
            return regular_path
            done = True
        else:
            print("Install still not detected, please try again.")

def readState():
    inFile = open("State.txt", "r")
    state = inFile.readlines()
    inFile.close()
    for i in state:
        i = i.rstrip("\n")
        if i == "0":
            outFile = open("State.txt", "w")
            outFile.write("1")
            outFile.close()
            return False
        else:
            return True
main()