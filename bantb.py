from bancalculator import *
from webscraper import *
from arts_and_texts import *
import sys

def core(run):

	print_vertical_logo()

	team_page, miner_page, user_page, price_page, error_status = web_requests(username)

	user_id, user_credits, user_wus, user_rank, user_count = process_up(user_page)

	certificate_address = f"https://apps.foldingathome.org/awards?user={user_id}&type=wus"

	last_score, last_wus = process_mp(miner_page)

	if run == "cert-main":
		webbrowser.open(certificate_address, new=2)

	print(f"\nUsername: {'.'*(26-len(username))} {username}")
	print(f"ID: {'.'*(32-len(str(user_id)))} {user_id}")
	print(f"Completed WUs: {'.'*(21-len(str(user_wus)))} {user_wus}")
	print(f"Credits: {'.'*(27-len(str(user_credits)))} {user_credits}")

	user_pending_credits = user_credits - last_score

	ban_price = process_pp(price_page)

	mce, nce, fce = payment_predictions(user_pending_credits, ban_price)

	print(f"\nPending WUs: {'.'*(23-len(str(user_wus - last_wus)))} {user_wus - last_wus}")
	print(f"Pending Credits: {'.'*(19-len(str(user_pending_credits)))} {user_pending_credits}")
	print(f"MCE: {'.'*(25-(2+len(str('{0:.{1}f}'.format(mce, 2)))+len(str('{0:.{1}f}'.format(mce*ban_price, 2)))))} {'{0:.{1}f}'.format(mce, 2)} BAN (${'{0:.{1}f}'.format(mce*ban_price, 2)})")
	print(f"NCE: {'.'*(25-(2+len(str('{0:.{1}f}'.format(nce, 2)))+len(str('{0:.{1}f}'.format(nce*ban_price, 2)))))} {'{0:.{1}f}'.format(nce, 2)} BAN (${'{0:.{1}f}'.format(nce*ban_price, 2)})")
	print(f"FCE: {'.'*(25-(2+len(str('{0:.{1}f}'.format(fce, 2)))+len(str('{0:.{1}f}'.format(fce*ban_price, 2)))))} {'{0:.{1}f}'.format(fce, 2)} BAN (${'{0:.{1}f}'.format(fce*ban_price, 2)})")

	users, ban_user_count, user_position = process_tp(team_page, username)

	print(f"\nBANANO Rank: {'.'*(18-len(str(users[user_position][1])+str(ban_user_count)+str('{0:.{1}f}'.format((users[user_position][1]/ban_user_count)*100, 2))))} {users[user_position][1]}/{ban_user_count} ({'{0:.{1}f}'.format((users[user_position][1]/ban_user_count)*100, 2)}%)")
	if user_position>=10000:
		print(f"Credits to top 10000: {'.'*(14-len(str(users[9999][3] - users[user_position][3])))} {users[9999][3] - users[user_position][3]}")
	elif user_position>=1000:
		print(f"Credits to top 1000: {'.'*(15-len(str(users[999][3] - users[user_position][3])))} {users[999][3] - users[user_position][3]}")
	elif user_position>=100:
		print(f"Credits to top 100: {'.'*(16-len(str(users[99][3] - users[user_position][3])))} {users[99][3] - users[user_position][3]}")
	elif user_position>=10:
		print(f"Credits to top 10: {'.'*(17-len(str(users[9][3] - users[user_position][3])))} {users[9][3] - users[user_position][3]} ")
	elif user_position>=1:
		print(f"Credits to top {user_position}: {'.'*(18-len(str(users[user_position-1][3] - users[user_position][3])))} {users[user_position-1][3] - users[user_position][3]}")
	else:
		print(f"Holy bananas!    You're BANANO top 1!")
	print(f"""F@H Rank: {'.'*(21-len(str(user_rank)+str(user_count)+str('{0:.{1}f}'.format((user_rank/user_count)*100, 2))))} {user_rank}/{user_count} ({'{0:.{1}f}'.format((user_rank/user_count)*100, 2)}%)""")

	print_vertical_end()


if sys.argv[1] != "-h" and sys.argv[1] != "-l" and sys.argv[1] != "-p" and sys.argv[1] != "-c":

	username = sys.argv[1]

	core("main")

elif sys.argv[1] == "-h":

	pass

elif sys.argv[1] == "-l":

	print_horizontal_logo()

	username = sys.argv[2]

	user_page = basic_data(username)

	user_id, user_credits, user_wus, user_rank, user_count = process_up(user_page)

	print(f"\nUser page: https://statsclassic.foldingathome.org/donor/{user_id}")
	print(f"Team page: https://apps.foldingathome.org/teamstats/team234980.html")
	print(f"Certificate: https://apps.foldingathome.org/awards?user={user_id}&type=wus")
	print(f"Transactions: https://bananominer.com/user_name/{username}")
	print(f"Banano price: https://coinmarketcap.com/currencies/banano/")
	print(f"Banano miner: https://bananominer.com/")

elif sys.argv[1] == "-c":

	import webbrowser

	username = sys.argv[2]

	core("cert-main")