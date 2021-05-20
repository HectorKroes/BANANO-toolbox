from bs4 import BeautifulSoup
import requests

def list_replace(data_string, replace_list):
	for element in replace_list:
		data_string = data_string.replace(element, "")
	return data_string

class user_data:
	def __init__(self, data_string):
		self.ds = data_string

	def extract_data(self):
		self.ds = list_replace(self.ds, ["\n", "<tr>", "<td>", " "])
		self.dl = self.ds.replace("</td>", " ")[:-1].split(" ")
		self.resume = [int(self.dl[0]), int(self.dl[1]), self.dl[2], int(self.dl[3]), int(self.dl[4])]

def web_requests(username):
	error_status = False
	try:
		page1 = requests.get("https://apps.foldingathome.org/teamstats/team234980.html")
	except:
		page1 = "Error 404"; error_status = True
		print("Failed to reach team stats at https://apps.foldingathome.org/teamstats/team234980.html")
	try:
		page2 = requests.get(f"https://bananominer.com/user_name/{username}")
	except:
		page2 = "Error 404"; error_status = True
		print(f"Failed to reach payment info at https://bananominer.com/user_name/{username}")
	try:
		page3 = requests.get(f"https://api.foldingathome.org/user/{username}")
	except:
		page3 = "Error 404" ; error_status = True
		print(f"Failed to reach user info at https://api.foldingathome.org/user/{username}")
	try:
		page4 = requests.get("https://coinmarketcap.com/currencies/banano/")
	except:
		page4 = "Error 404" ; error_status = True
		print("Failed to reach price info at https://coinmarketcap.com/currencies/banano/")

	return page1, page2, page3, page4, error_status

def basic_data(username):
	try:
		page3 = requests.get(f"https://api.foldingathome.org/user/{username}")
	except:
		page3 = "Error 404" ; error_status = True
		print(f"Failed to reach user info at https://api.foldingathome.org/user/{username}")
	return page3

def process_tp(tp, username):
	soup = str(BeautifulSoup(tp.content, "html.parser"))

	table = soup.split("</tr>")
	ban_user_count = len(table) - 6

	users = []

	for user_row in table[5: -2]:
		i = user_data(user_row)
		i.extract_data()
		users.append(i.resume)

	user_position = 0

	for user in users:
		if user[2] == username:
			break
		else:
			user_position += 1

	return users, ban_user_count, user_position

def process_mp(mp):
	soup = str(BeautifulSoup(mp.content, "html.parser"))
	
	last_payment_info = soup.split("}")[0].split(":")
	last_score, last_wus = int(last_payment_info[7].split(",")[0]), int(last_payment_info[8])

	return last_score, last_wus

def process_up(up):
	soup = str(BeautifulSoup(up.content, "html.parser"))

	user_info = soup.split(",")
	user_id = int(user_info[1].split(":")[1])
	user_credits = int(user_info[2].split(":")[1])
	user_wus = int(user_info[3].split(":")[1])
	user_rank = int(user_info[4].split(":")[1])
	user_count = int(user_info[8].split(":")[1])

	return user_id, user_credits, user_wus, user_rank, user_count

def process_pp(pp):
	soup = BeautifulSoup(pp.content, "html.parser")

	price_info = str(soup.select("div.priceValue___11gHJ")).split(">")

	ban_price = float(price_info[1].split("<")[0][1:])

	return ban_price