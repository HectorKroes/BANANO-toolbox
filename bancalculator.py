import math

def payment_predictions(user_pending_credits, ban_price):
	if user_pending_credits > 740000:
		mce = ((1/(-0.05655 + (0.9598 * (1/math.log(user_pending_credits))))) - 3.3009 - math.log(ban_price))
	elif user_pending_credits >= 300000:
		mce = math.exp(-5.0657 - math.log(ban_price) + (0.4414 * math.log(user_pending_credits)))
	elif user_pending_credits >= 150000:
		mce = math.exp(-6.0370 - math.log(ban_price) + (0.5223 * math.log(user_pending_credits)))
	elif user_pending_credits >= 30000:
		mce = math.exp(-7.3263 - math.log(ban_price) + (0.6380 * math.log(user_pending_credits)))
	else:
		mce = math.exp(-9.5797 - math.log(ban_price) + (0.8545 * math.log(user_pending_credits)))

	if mce < 9.85:
		mce = 9.85
		
	nce = math.exp(-15.8968 - math.log(ban_price) + (17.6 * math.log(math.log(math.log(user_pending_credits)))))

	if nce < 9.85:
		nce = 9.85;
	elif nce > mce:
		nce = mce
		
	fce = math.exp(-10.24 + math.log(ban_price) + (17.6 * math.log(math.log(math.log(user_pending_credits)))))

	return mce, nce, fce