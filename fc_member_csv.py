import requests
import sys
import csv
import re
import os
from bs4 import BeautifulSoup


def check_page(url):
	if not re.match("https://jp.finalfantasyxiv.com/lodestone/freecompany[\w/:%#\$&\?\(\)~\.=\+\-]+/member", url):
		print("FCメンバー一覧のURLではありません")
		sys.exit(1)
	res = requests.get(url)
	soup = BeautifulSoup(res.text, "html.parser")

	try:
		soup.find(class_="heading--lg").text
		get_friend_list(url)
	except AttributeError:
			print("メンバー一覧を取得できませんでした")
			sys.exit()

def get_friend_list(url):
	g_fc_mem_list = list()
	g_fc_class_list = list()

	res = requests.get(url)
	soup = BeautifulSoup(res.text, "html.parser")

	f_window = soup.find_all(class_="ldst__window")
	f_count_source = soup.find(class_="btn__pager__current")
	f_page_count = re.sub(r'\D', "", f_count_source.text.rsplit("/" ,1)[1])

	file_name = f_window[0].find(class_="entry__freecompany__name").text
	file_name = file_name + ".csv"

	for i in range(int(f_page_count) + 1):
		fc_mem_list = f_window[0].find_all(class_="entry__name")
		fc_class_list = f_window[0].find_all(class_="entry__freecompany__info")
		for mem_name in fc_mem_list:
			g_fc_mem_list.append(mem_name.text)

		for class_name in fc_class_list:
			g_fc_class_list.append(class_name.find("span").text)

		res = requests.get(url + "?page=" + str(i + 1))
		soup = BeautifulSoup(res.text, "html.parser")
		f_window = soup.find_all(class_="ldst__window")

	if os.path.exists(f"./{file_name}"):
		os.remove(f"./{file_name}")

	for name, class_name in zip(g_fc_mem_list, g_fc_class_list):
		with open(file_name, "a") as f:
			writer = csv.writer(f)
			writer.writerow([name, class_name])
	print("CSVファイルに保存しました")


if __name__ == '__main__':
	print("CSVファイルはこのプログラムのあるフォルダに保存されます。")
	url = input("FCメンバー一覧のURLを入力してください: ")
	check_page(url)
