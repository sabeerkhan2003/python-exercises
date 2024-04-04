
def compound_interest(p,r,t):
  amount=p*(pow((1+r/100),t))
  CI=amount-p
  print("compound interest is:",CI)
compound_interest(1000,4,5)
