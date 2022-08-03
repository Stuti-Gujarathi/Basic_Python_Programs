pi=22/7
height=float(input('Height of cylinder: '))
radian=float(input('Radian of cylinder: '))
volume=pi*radian*radian*height
sur_area=((2*pi*radian)*height)+((pi*radian**2)*2)
print("Volume of cylinder: ", volume)
print("Surface Area: ",sur_area)
