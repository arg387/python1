  import random 
    items_list = [' 🍒 ',' 🍇 ',' 🍉 ',' 7️⃣ ']
    print('--------------------')
    name = input("What's your name? Dear Player ....")
    play = input(F'Do you want to play? Dear {name} (yes/no):')
    print('--------------------')
    print('Loading...')
    print('Loading...')
    print('Loading...')
    if play.lower() == 'yes':
      for i in range(3):
        new_list = []
        for item in range(len(items_list) - 1):
          new_list.append(random.choice(items_list))
        print('--------------------')
        print(F' {new_list[0]} | {new_list[1]} | {new_list[2]} ')
        print('--------------------')
        if new_list.count('7') == 3:
          print("Jackpot! 💰")
        else:
          print("Thanks for playing!")
    else:
      print("Thanks for visiting!")
    print('--------------------')
    print('The End.')
