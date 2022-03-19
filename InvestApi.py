import requests

headers = {
    'accept': 'application/json',
}


def deal(type, id, amount, year):
    return requests.put(f"http://217.28.230.77:8080/v1/oper/deal?type={type}&id={id}&amount={amount}&year={year}",
                        headers=headers).json()['message']


def resetAccount():
    return requests.put("http://217.28.230.77:8080/v1/account/reset", headers=headers).json()['message']


def initAccount(summa):
    return requests.put(f"http://217.28.230.77:8080/v1/account?summa={summa}", headers=headers).json()['message']


def infoAccount():
    return requests.get("http://217.28.230.77:8080/v1/accoun",
                        headers=headers).json()


def getAllBonds():
    return requests.get("http://217.28.230.77:8080/v1/listing/getall",
                        headers=headers).json()


def getIdBonds(id):
    return requests.get(f"http://217.28.230.77:8080/v1/listing/get?id={id}",
                        headers=headers).json()


def getIdOper(id):
    return requests.get(f"http://217.28.230.77:8080/v1/oper/get?id={id}", headers=headers).json()


def getAllOper():
    return requests.get(f"http://217.28.230.77:8080/v1/oper/getall", headers=headers).json()


def finish(year):
    return requests.put(f"http://217.28.230.77:8080/v1/oper/finish?year={year}",
                        headers=headers).json()['message']


def delete(id):
    return requests.delete(f"http://217.28.230.77:8080/v1/oper/del?id={id}",
                           headers=headers).json()['message']
