import InvestApi


def createUserPortfolio(Portfolio, user_year, user_money):
    userPortfolio = {}
    tempkey = []
    procent = 0
    userPortfolioYear = {}
    all_bonds = InvestApi.getAllBonds();
    year = 2022
    last_money = 0.;
    portfolioYear = Portfolio[year]
    oneBondsMoney = user_money // len(portfolioYear)
    for i in portfolioYear:
        priceBond = InvestApi.getIdBonds(i)
        countBuyBonds = oneBondsMoney // priceBond['price']
        last_money += oneBondsMoney % priceBond['price']
        userPortfolio[i] = countBuyBonds
    userPortfolioYear[year] = userPortfolio
    for currYear in range(year + 1, user_year):
        userPortfolio = {}
        for i in range(year, currYear):
            for k in userPortfolioYear[i]:
                bond = InvestApi.getIdBonds(k);
                if (bond['year'] == currYear):
                    last_money += bond['nominal'] * userPortfolioYear[i][k];
                    tempkey.append(userPortfolioYear[i][k])
                if (bond['year'] > currYear):
                    last_money += int(bond['nominal']) / 100 * bond['prc']
                    procent += int(bond['nominal']) / 100 * bond['prc']
            portfolioYear = Portfolio[currYear]
            oneBondsMoney = last_money // len(portfolioYear)
            for i in portfolioYear:
                user_money = last_money
                last_money = 0
                priceBond = InvestApi.getIdBonds(i)
                countBuyBonds = oneBondsMoney // priceBond['price']
                last_money += oneBondsMoney % priceBond['price']
                userPortfolio[i] = countBuyBonds
            userPortfolioYear[currYear] = userPortfolio
    return userPortfolioYear


def createPortfolio(all_bonds, year_now, invest_horizon_year):
    year_plans = {}
    suitable_bonds = list(sorted(all_bonds, key=lambda d: d["revenue"]))
    suitable_bonds.reverse()
    portfolio_all_years = set()
    while year_now <= invest_horizon_year:
        i = 0
        max_i = 5
        if len(suitable_bonds) < 5:
            max_i = len(suitable_bonds)
        portfolio_one_year = set()
        while i < max_i:
            if year_now <= suitable_bonds[i]["year"]:
                portfolio_one_year.add(suitable_bonds[i]["id"])
                portfolio_one_year -= portfolio_all_years
            i += 1
            if portfolio_one_year and i == max_i:
                year_plans[year_now] = portfolio_one_year
        portfolio_all_years |= portfolio_one_year
        j = 0
        while j < len(suitable_bonds):
            if year_now == suitable_bonds[j]["year"]:
                suitable_bonds.pop(j)
                j -= 1
            j += 1
        year_now += 1
    year_plans["all"] = portfolio_all_years
    return year_plans


'''
def getBoundAmount(all_bonds, year_plans, year, invest_horizon_year, deposit):
=======

def getBoundAmount(all_bonds, year_plans, year_now, invest_horizon_year, deposit):
>>>>>>> f9c7080c4f7866ae26fd54f7ff3bc8fb46053d4f
    dic = {}
    quot = deposit / 5
    for y in range(year_now + 1, invest_horizon_year + 1):
        for one_bond in all_bonds:
            if one_bond["id"] == year_plans[y]:
                dic[one_bond[id]] = int(quot // one_bond["price"])
    return dic
'''


def getDictUserBuy(countYear, user_money):
    all_bonds_plus_revenue = InvestApi.getAllBonds()
    for bond in all_bonds_plus_revenue:
        bond["revenue"] = round(((bond["nominal"] - bond["price"]) + (
                bond["prc"] / 100 * bond["nominal"] * (bond["year"] - 2021))) / bond["price"] * 365 / (
                                        365 * (bond["year"] - 2021)) * 100, 2)
    year = 2022  # какой сейчас год
    user_year = 2022 + int(countYear)
    # user_year = 2024  # todo: задает пользователь
    # user_money = 50000  # todo: задает пользователь
    a = createPortfolio(all_bonds_plus_revenue, year, user_year)
    r = createUserPortfolio(a, user_year, int(user_money))
    return r