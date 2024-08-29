
class Pokemon:
  def __init__(self,entry,name,types,description,is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught
  def speak(self):
    print("---------")
    print(self.name)
    print(self.name)
    print("---------")
  def display_details(self):
    print('The entry number : ' + self.entry)
    print('Name : ' + self.name)
    print('Type : ' + self.types)
    print('Description : ' + self.description)
    if self.is_caught:
      print(self.name + ' has already been caught.')
    else:
      print(self.name + ' has not been caught yet.')
pokemon1 = Pokemon("#0460","Abomasnow","Grass and Ice","It lives a quiet life on mountains that are perpetually covered in snow. It hides itself by whipping up blizzards.",True)
pokemon2 = Pokemon("#0464","Rhyperior","Ground and Rock","This Pokémon’s sturdy carapace protects it from volcanic eruptions. It shoots round rocks from the holes in its hands.",True)
pokemon3 = Pokemon("#0466","Electivire","Electric","When it gets excited, it thumps its chest. With every thud, thunder roars and electric sparks shower all around.",False)

pokemon1.speak()
pokemon1.display_details()
pokemon2.speak()
pokemon2.display_details()
pokemon3.speak()
pokemon3.display_details()