#Traffic light program


light = input("Enter the colour of light: ")
if light == "red":
    print("stop")
elif light == "yellow":
    print("ready")
elif light == "green":
    print("go")
else:
    print("Invalid light color")