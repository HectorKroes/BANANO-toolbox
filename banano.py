import time, sys
from webscraper import *
from bancalculator import *

username = "6lu546t6upgl" #sys.argv[1]

print(f"""=====================================\n _                                   
| |__   __ _ _ __   __ _ _ __   ___  
| '_ \ / _` | '_ \ / _` | '_ \ / _ \ 
| |_) | (_| | | | | (_| | | | | (_) |
|_.__/ \__,_|_| |_|\__,_|_| |_|\___/ 
                                     
  _              _ _                  
 | |_ ___   ___ | | |__   _____  __   
 | __/ _ \ / _ \| | '_ \ / _ \ \/ /   
 | || (_) | (_) | | |_) | (_) >  <    
  \__\___/ \___/|_|_.__/ \___/_/\_\   
                                    
=====================================
Version 1.0 - {time.asctime()}
=====================================""")

team_page, miner_page, user_page, price_page, error_status = web_requests(username)

user_id, user_credits, user_wus, user_rank, user_count = process_up(user_page)

last_score, last_wus = process_mp(miner_page)

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
print(f"""F@H Rank: {'.'*(21-len(str(user_rank)+str(user_count)+str('{0:.{1}f}'.format((user_rank/user_count)*100, 2))))} {user_rank}/{user_count} ({'{0:.{1}f}'.format((user_rank/user_count)*100, 2)}%)

=====================================""")