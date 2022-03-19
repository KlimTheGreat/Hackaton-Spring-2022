import builtins

import InvestApi

a = InvestApi.getAllBonds()
for item in a:
    item["true_prc"] = round(((item["nominal"] - item["price"]) + (
            item["prc"] / 100 * item["nominal"] * (item["year"] - 2021))) / item["price"] * 365 / (
                                     365 * (item["year"] - 2021)) * 100, 2)

vvod = 50000
gorizont = 2025
year_now = 2022

b = list(sorted(a, key=lambda d: d["true_prc"]))

b.reverse()
for _ in b:
    print(_)
History = set()
#udl=5
while year_now <= gorizont:
    print(year_now)
    #i =5-udl
    i=0
    potolok = 5
    if len(b) < 5:
        potolok = len(b)
    IdToBuy = set()
    while i < potolok:
        if year_now <= b[i]["year"]:
            IdToBuy.add(b[i]["id"])
            IdToBuy -= History
        i += 1
        if IdToBuy and i == potolok:
            print(*IdToBuy)
    History |= IdToBuy
    j = 0
    #udl=0
    while j < len(b):
        if year_now == b[j]["year"]:
            b.pop(j)
            j -= 1
            #udl+=1
        j += 1
    year_now += 1