a = [
  {
    "id": 1,
    "name": "Облигация 1",
    "nominal": 1000,
    "price": 900,
    "prc": 5,
    "year": 2025
  },
  {
    "id": 2,
    "name": "Облигация 2",
    "nominal": 1000,
    "price": 950,
    "prc": 6,
    "year": 2025
  },
  {
    "id": 3,
    "name": "Облигация 3",
    "nominal": 1000,
    "price": 1000,
    "prc": 7,
    "year": 2024
  },
  {
    "id": 4,
    "name": "Облигация 4",
    "nominal": 1000,
    "price": 1050,
    "prc": 8,
    "year": 2024
  },
  {
    "id": 5,
    "name": "Облигация 5",
    "nominal": 1000,
    "price": 950,
    "prc": 6.5,
    "year": 2023
  },
  {
    "id": 6,
    "name": "Облигация 6",
    "nominal": 1000,
    "price": 1200,
    "prc": 10,
    "year": 2023
  },
  {
    "id": 7,
    "name": "Облигация 7",
    "nominal": 1000,
    "price": 800,
    "prc": 3,
    "year": 2023
  },
  {
    "id": 8,
    "name": "Облигация 8",
    "nominal": 1000,
    "price": 900,
    "prc": 5.5,
    "year": 2022
  },
  {
    "id": 9,
    "name": "Облигация 9",
    "nominal": 1000,
    "price": 700,
    "prc": 2,
    "year": 2022
  },
  {
    "id": 10,
    "name": "Облигация 10",
    "nominal": 1000,
    "price": 900,
    "prc": 5,
    "year": 2022
  }
]

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
  year_now=year_now+1
  prc1=0
  prc2=0


