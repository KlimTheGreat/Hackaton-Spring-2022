import InvestApi


def createPortfolio(all_bonds, invest_horizon_year, year_now):
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


def getBoundAmount(all_bonds, year_plans, year, invest_horizon_year, deposit):
    dic = {}
    quot = deposit / 5
    for y in range(year+1, invest_horizon_year + 1):
        for one_bond in all_bonds:
            if one_bond["id"] == year_plans[y]:
                dic[one_bond[id]] = int(quot // one_bond["price"])
    return dic


if __name__ == "__main__":  # главная функция

    all_bonds_plus_revenue = InvestApi.getAllBonds()
    for bond in all_bonds_plus_revenue:
        bond["revenue"] = round(((bond["nominal"] - bond["price"]) + (
                bond["prc"] / 100 * bond["nominal"] * (bond["year"] - 2021))) / bond["price"] * 365 / (
                                        365 * (bond["year"] - 2021)) * 100, 2)

    year = 2022  # какой сейчас год
    user_year = 2025  # todo: задает пользователь
    user_money = 50000  # todo: задает пользователь
    a = createPortfolio(all_bonds_plus_revenue, year, user_year)
    #b = getBoundAmount(all_bonds_plus_revenue, a, year, user_year, user_money)

    print(a)
    #print(b)
