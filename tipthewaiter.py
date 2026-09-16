def bill(cost, tippercent):
    total= (cost*(tippercent/100))+cost
    print(f"Total Amount to be Paid: Rs.{total}")
bill(200,5)