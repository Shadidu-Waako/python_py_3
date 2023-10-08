class Payment:
  tuition = 100000
  balance = 0
  spls = 0
  library_fee = 500
 
  def __init__(self, fees):
    self.set_fees()
    self.set_balance(fees)
    self.set_spls(fees)
    self.fees = fees


  def set_fees(self):
    self.fees = self.tuition + self.library_fee


  def set_balance(self, fees):
    if fees < self.fees:
      self.balance = self.fees - fees


  def set_spls(self, fees):
    if fees > self.fees:
      self.spls = fees - self.fees

  
  def __str__(self):
    return f'You payed $:{self.fees} for tuition, your balance is $:{self.balance} and you demand the university $:{self.spls}'

