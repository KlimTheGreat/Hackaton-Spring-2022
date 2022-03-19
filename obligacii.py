import InvestApi

a = InvestApi.getAllBonds()


p = {}
for item in a:
    p[item["id"]] = ((item["nominal"] - item["price"]) + (
                item["prc"] / 100 * item["nominal"] * (item["year"] - 2021))) / item["price"] * 365 / (
                                365 * (item["year"] - 2021)) * 100
print(p)
prc1=0
prc2=0
vvod = 50000
gorizont=2025
year_now=2022
while gorizont>=year_now:
  for item in a:
    if item["year"]<=gorizont:
      if item["price"]>(item["nominal"]*0.75): #не обязательно, проверка на дефолт
        if prc1<p[item["id"]] and year_now<=item["year"]:
          prc1=p[item["id"]]
          year1=item["year"]
          id1=item["id"]
        if prc2<p[item["id"]] and prc1!=p[item["id"]] and year_now<=item["year"]:
          prc2=p[item["id"]]
          year2=item["year"]
          id2=item["id"]
  print("Покупаем облигацию ",id1," и ",id2,"с процентами годовых ",prc1," и ",prc2,"до ",year1," и ",year2)
  if year_now<=year1: print("Покупаем акцию", id1)
  InvestApi.finish(year_now)
  year_now=year_now+1
  prc1=0
  prc2=0


