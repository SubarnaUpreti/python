FACTOR = 1.60934

print("Swallow Speed Analysis: Version 1.0")

speed_eu = []
speed_br = []

while True:
    x = input("Enter the Next Reading: ")
    if x.isspace() or x == '':
        break
    else:
        try:
            if x[0] in ['U', 'E']:
                if x[0] == 'U':
                    speed_br.append(float(x[1:]))
                    speed_eu.append(float(x[1:]) * FACTOR)
                else:
                    speed_br.append(float(x[1:]) / FACTOR)
                    speed_eu.append(float(x[1:]))
            else:
                raise Exception
        except:
            print("Error in reading value!!!")

if not speed_eu:
    print("No readings entered. Nothing to do.")
else:
    print(f"\nResults Summary\n\n{len(speed_eu)} Readings Analysed.\n")
    print(f"Max Speed: {round(max(speed_br), 1)} MPH, {round(max(speed_eu), 1)} KPH.")
    print(f"Min Speed: {round(min(speed_br), 1)} MPH, {round(min(speed_eu), 1)} KPH.")
    print(f"Avg Speed: {round(sum(speed_br)/len(speed_br), 1)} MPH, {round(sum(speed_eu)/len(speed_eu), 1)} KPH.")
