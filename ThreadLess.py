# Matin Nasouri 9911329

import requests
import pandas
import time
from bs4 import BeautifulSoup
from unidecode import unidecode
from statistics import mean


def emalls():
    Names = []
    Prices = []
    data_pairs = {}

    result = requests.get(
        "https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA~Category~39"
    )

    if result.status_code == 200:
        soup = BeautifulSoup(result.text, "lxml")

        list_of_names = soup.select("div h2 .maintitle")

        for item in list_of_names:
            Names.append(
                item.getText().replace(" Mobile Phone", "").replace(" mobile phone", "")
            )

        list_of_prices = soup.select(".prd-price span")

        for item in list_of_prices:
            Prices.append(int(unidecode(item.getText().replace(",", ""))))

        for i in range(len(Names)):
            data_pairs[Names[i]] = Prices[i]

        max_price = max(data_pairs.values())

        for item in data_pairs.items():
            if item[1] == max_price:
                ME_phone = item[0]

        min_price = min(data_pairs.values())

        for item in data_pairs.items():
            if item[1] == min_price:
                Ch_phone = item[0]

        pandas.DataFrame.from_dict(data=data_pairs, orient="index").to_csv(
            "emalls.csv", header=False
        )

        print("emalls")
        print("-----------------------------------------------------")
        print(f"Most expensive phone: {ME_phone} -> {max_price}")
        print(f"Cheapest phone: {Ch_phone} -> {min_price}")
        print(f"Average Price: {mean(data_pairs.values())}")
        print("\n")

    else:
        print(f"Request was denied by code: {result.status_code}")


def MoboNews():
    Names = []
    Prices = []
    data_pairs = {}

    result = requests.get("https://mobo.news/pricelist/")

    if result.status_code == 200:
        soup = BeautifulSoup(result.text, "lxml")

        list_of_names = soup.select("a div .title-phone-span")

        for item in list_of_names:
            Names.append(
                item.getText().replace(" Mobile Phone", "").replace(" mobile phone", "")
            )

        list_of_prices = soup.select("a .details-phone-price")

        for item in list_of_prices:
            Prices.append(int(item.getText().replace(",", "").replace("تومان", "")))

        for i in range(len(Names)):
            data_pairs[Names[i]] = Prices[i]

        max_price = max(data_pairs.values())

        for item in data_pairs.items():
            if item[1] == max_price:
                ME_phone = item[0]

        min_price = min(data_pairs.values())

        for item in data_pairs.items():
            if item[1] == min_price:
                Ch_phone = item[0]

        pandas.DataFrame.from_dict(data=data_pairs, orient="index").to_csv(
            "MoboNews.csv", header=False
        )

        print("Mobo News")
        print("-----------------------------------------------------")
        print(f"Most expensive phone: {ME_phone} -> {max_price}")
        print(f"Cheapest phone: {Ch_phone} -> {min_price}")
        print(f"Average Price: {mean(data_pairs.values())}")
        print("\n")

    else:
        print(f"Request was denied by code: {result.status_code}")


def MobileIr():
    Names = []
    Prices = []
    data_pairs = {}

    result = requests.get("https://www.mobile.ir/phones/prices.aspx")

    if result.status_code == 200:
        soup = BeautifulSoup(result.text, "lxml")

        list_of_names = soup.select("tr td .phone")

        for item in list_of_names:
            Names.append(
                item.getText().replace(" Mobile Phone", "").replace(" mobile phone", "")
            )

        list_of_prices = soup.select("tr .price")

        for item in list_of_prices:
            Prices.append(int(item.getText().replace(",", "")))

        for i in range(len(Names)):
            data_pairs[Names[i]] = Prices[i]

        max_price = max(data_pairs.values())

        for item in data_pairs.items():
            if item[1] == max_price:
                ME_phone = item[0]

        min_price = min(data_pairs.values())

        for item in data_pairs.items():
            if item[1] == min_price:
                Ch_phone = item[0]

        pandas.DataFrame.from_dict(data=data_pairs, orient="index").to_csv(
            "MobileIr.csv", header=False
        )

        print("MobileIr")
        print("-----------------------------------------------------")
        print(f"Most expensive phone: {ME_phone} -> {max_price}")
        print(f"Cheapest phone: {Ch_phone} -> {min_price}")
        print(f"Average Price: {mean(data_pairs.values())}")
        print("\n")

    else:
        print(f"Request was denied by code: {result.status_code}")


starting_time = time.time()

emalls()
MoboNews()
MobileIr()

ending_time = time.time()

print(f"Run-time: {ending_time-starting_time}")
