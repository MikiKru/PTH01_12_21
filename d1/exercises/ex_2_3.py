actual_status = 10000
percent = 2
years = 3

account_status = actual_status * ((1 + percent/100) ** years)

print(f"Po upływie {years} lat Twój stan konta wynosi {account_status:.2f} zł")