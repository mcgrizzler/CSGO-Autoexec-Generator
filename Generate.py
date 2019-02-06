#
#   AutoExec Generator
#

def main():
    intro()
    cross_hair()
    tick_rate()
    display_damage()
    defaults()

def intro():
    print("CS:GO Auto-Exec Generator")

def cross_hair():
    outFile = open("autoexec.cfg", "a")
    outFile.write("//Cross-Hair" + "\n")
    print("Crosshair Configuration")
    options = ["crosshairalpha", "crosshaircolor", "crosshaircolor_r", "crosshaircolor_g", "crosshaircolor_b", "crosshairdot", "crosshairgap", "crosshairsize", "crosshairstyle", "crosshairusealpha", "crosshairthickness", "fixedcrosshairgap", "crosshair_outlinethickness", "crosshair_drawoutline"]
    for i in options:
        print("Set", i)
        userInput = input("Enter a value: ")
        outFile.write("cl_" + i + " " + '"' + userInput + '"' + "\n")
    outFile.close()

def tick_rate():
    outFile = open("autoexec.cfg", "a")
    outFile.write("\n" + "//Tick Rate" + "\n")
    print("Tick-Rate")
    print("Choose 64 or 128")
    options = ["cmdrate", "interp", "interp_ratio", "updaterate"]
    sixtyFour = ["64", "0", "1", "64", "64000"]
    onetwentyeight = ["128", "0", "1", "128", "128000"]
    userInput = input("Enter: ")
    counter = 0
    if userInput == "64":
        for i in options:
            outFile.write("cl_" + i + " " + '"' + sixtyFour[counter] + '"' + "\n")
    elif userInput == "128":
        for i in options:
            outFile.write("cl_" + i + " " + '"' + onetwentyeight[counter] + '"' + "\n")
    outFile.write("rate" + " " + '"' + onetwentyeight[counter] + '"' + "\n")
    outFile.close()

def display_damage():
    outFile = open("autoexec.cfg", "a")
    print("Would you like to show damage in the top left? (Y/N)")
    userInput = input("Enter: ")
    if userInput.lower() == "y":
        outFile.write("\n" + "//Display Damage" + "\n")
        outFile.write('con_filter_text "Damage Given To"' + '\n')
        outFile.write('con_filter_text_out "Player:"' + '\n')
        outFile.write('con_filter_enable "2"' + '\n')
        outFile.write('developer "1"' + '\n')
    outFile.close()

def defaults():
    outFile = open("autoexec.cfg", "a")
    print("Loading Remaining Values")
    outFile.write("\n" + "//Default Values" + "\n")
    outFile.write('bind "KP_MINUS" "incrementvar cl_radar_scale 0.25 1.0 -0.05"' + '\n')
    outFile.write('bind "KP_PLUS" "incrementvar cl_radar_scale 0.25 1.0 0.05"' + '\n')
    outFile.write('cl_radar_always_centered 0' + '\n')
    outFile.close()

main()