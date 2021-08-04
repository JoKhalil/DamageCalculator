import math
import tkinter as tk

window = tk.Tk()
window.title("Pokemon Damage Calculator")

labelArray = [tk.Label(text="Enter your pokemon's level"),
              tk.Label(text="Enter the move's power points"),
              tk.Label(text="Enter your pokemon's attack stats"),
              tk.Label(text="Enter the enemy's defense stats"),
              tk.Label(text="Enter the number of target (0.75 if more than 1 else 1):"),
              tk.Label(text="Enter the weather stats (1.50 if weather helps 0.50 if weather cuts):"),
              tk.Label(text="Enter the badge stat (Gen 2 ONLY)"),
              tk.Label(text="Enter the crit multiplier (Gen 3-5 is x2 Gen 6-8 is x1.5)"),
              tk.Label(text="Enter the STAB multiplier (1.5 if same type and 2 if pokemon has Adaptability)"),
              tk.Label(text="Enter the type multiplier (0.25, 0.50, 1 , 2 or 4)"),
              tk.Label(text="Enter the burn multiplier (0.50 if ability is not Guts and move is physical)"),
              tk.Label(text="Enter the other multiplier (item multiplier)")]

entryArray = [tk.Entry(),
              tk.Entry(),
              tk.Entry(),
              tk.Entry(),
              tk.Entry(),
              tk.Entry(),
              tk.Entry(),
              tk.Entry(),
              tk.Entry(),
              tk.Entry(),
              tk.Entry(),
              tk.Entry()]


def calculateDamage():
    lPAD = math.floor(((2 * int(entryArray[0].get()) / 5 + 2) * int(entryArray[1].get()) * int(
        entryArray[2].get()) / int(entryArray[3].get()) / 50 + 2))

    pourcentageLPAD = [math.floor(0.85 * lPAD), math.floor(lPAD)]

    targets = [math.floor(pourcentageLPAD[0] * int(entryArray[4].get())),
               math.floor(pourcentageLPAD[1] * int(entryArray[4].get()))]

    weather = [math.floor(targets[0] * float(entryArray[5].get())),
               math.floor(targets[1] * float(entryArray[5].get()))]

    badge = [math.floor(weather[0] * float(entryArray[6].get())),
             math.floor(weather[1] * float(entryArray[6].get()))]
    # we are skipping crit to keep it for the end result
    sTAB = [math.floor(badge[0] * float(entryArray[8].get())),
            math.floor(badge[1] * float(entryArray[8].get()))]

    type = [math.floor(sTAB[0] * float(entryArray[9].get())),
            math.floor(sTAB[1] * float(entryArray[9].get()))]

    burn = [math.floor(type[0] * float(entryArray[10].get())),
            math.floor(type[1] * float(entryArray[10].get()))]

    totalDamage = [math.floor(burn[0] * float(entryArray[11].get())),
                   math.floor(burn[1] * float(entryArray[11].get()))]

    crit = [math.floor(totalDamage[0] * float(entryArray[7].get())),
            math.floor(totalDamage[1] * float(entryArray[7].get()))]

    total.config(text="[" + str(totalDamage[0]) + "," + str(totalDamage[1]) + "]\n" + "[" + str(crit[0]) + "," + str(
        crit[1]) + "]")


total = tk.Label(text="")

calcButton = tk.Button(text="Calculate", width=25, command=calculateDamage)

labelArray[0].pack()
entryArray[0].pack()
labelArray[1].pack()
entryArray[1].pack()
labelArray[2].pack()
entryArray[2].pack()
labelArray[3].pack()
entryArray[3].pack()
labelArray[4].pack()
entryArray[4].pack()
labelArray[5].pack()
entryArray[5].pack()
labelArray[6].pack()
entryArray[6].pack()
labelArray[7].pack()
entryArray[7].pack()
labelArray[8].pack()
entryArray[8].pack()
labelArray[9].pack()
entryArray[9].pack()
labelArray[10].pack()
entryArray[10].pack()
labelArray[11].pack()
entryArray[11].pack()
calcButton.pack()
total.pack()

window.mainloop()
