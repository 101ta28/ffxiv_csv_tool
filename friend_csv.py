import requests
import sys
import csv
import re
from bs4 import BeautifulSoup


def check_page(url):
	if not re.match("https://jp.finalfantasyxiv.com/lodestone/character/[\w/:%#\$&\?\(\)~\.=\+\-]+/friend", url):
		print("フレンドリストのURLではありません")
		sys.exit(1)
	res = requests.get(url)
	soup = BeautifulSoup(res.text, "html.parser")

	try:
		soup.find(class_="heading--md").text
		get_friend_list(url)
	except AttributeError:
			print("フレンドリストが非公開または、エラーにより情報を取得できませんでした")
			print("フレンド情報を公開になっているのを確認してから再度実行してください")
			sys.exit()

def get_friend_list(url):
	g_friend_list = list()
	g_world_list = list()
	g_fc_list = list()

	res = requests.get(url)
	soup = BeautifulSoup(res.text, "html.parser")

	f_window = soup.find_all(class_="ldst__window")
	f_count_source = soup.find(class_="btn__pager__current")
	f_page_count = re.sub(r'\D', "", f_count_source.text.rsplit("/" ,1)[1])

	for i in range(int(f_page_count) + 1):
		friend_list = f_window[0].find_all(class_="entry__name")
		world_list = f_window[0].find_all(class_="entry__world")
		fc_list = f_window[0].find_all(class_="entry")
		for f_name in friend_list:
			g_friend_list.append(f_name.text)

		for w_name in world_list:
			g_world_list.append(w_name.text.split("\xa0")[0])

		for fc_attr in fc_list:
			try:
				fc_name = fc_attr.find(class_="entry__freecompany__link")
				g_fc_list.append(fc_name.find("span").text)
			except AttributeError:
				g_fc_list.append("FC not joined")

		res = requests.get(url + "?page=" + str(i + 1))
		soup = BeautifulSoup(res.text, "html.parser")
		f_window = soup.find_all(class_="ldst__window")


	for name, world, fc in zip(g_friend_list, g_world_list, g_fc_list):
		with open("friend_list.csv", "a") as f:
			writer = csv.writer(f)
			writer.writerow([name, world, fc])
	print("CSVファイルに保存しました")


if __name__ == '__main__':
	print("CSVファイルはこのプログラムのあるフォルダに保存されます。")
	url = input("フレンドリストのURLを入力してください: ")
	check_page(url)
