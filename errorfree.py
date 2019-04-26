#Upload the error free program on LMS.
class Cup:
    def __init__(self):
      self.color = None
      self.content = None
    def fill(self, beverage):
      self.content = beverage
      return self.content
    def empty(self):
      self.content = None
      return self.content
