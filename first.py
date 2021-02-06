sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error")
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40) * (fr * 1.5)
    xp = reg + otp
else:
    xp = fh * fr
print(xp)
