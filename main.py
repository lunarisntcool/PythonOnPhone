import re

amount = input("Put amount here (use $ or £ sign): ")

if("£" in amount):
    amount = amount.replace("£", "")
    newone = round(float(amount) * 1.2, 2)
    print(f"£{format(newone, '.2f')}")
else:
    amount = amount.replace("$", "")
    newone = round(float(amount) / 1.2, 2)
    print(f"£{format(newone, '.2f')}")
