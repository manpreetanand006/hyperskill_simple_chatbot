def greet(bot_name, birth_year):
      print(f"Hello! My name is {bot_name}.")
      print(f"I was created in {birth_year}.")

def introducing_self():
      print("Please, remind me your name.")
      name = input() 
      print(f'What a great name you have, {name}!')

def guess_age():
      print("Let me guess your age")
      print("Enter remainders of dividing your age by 3, 5 and 7")
      remainder3 = int(input())
      remainder5 = int(input())
      remainder7 = int(input())
      age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
      print(f"Your age is {age} ; that's a good time to start programming!")

def count_numbers():
      print("Now I will prove to you that I can count to any number you want.")
      number = int(input())
      for i in range(0, number+1):
            print(i,"!")
            i =+ 1
      print("Completed, have a nice day!")

questions = [{"question": "Why do we use methods", "options":["1. To repeat a statement multiple times.", "2. To decompose a program into several small subroutines.", "3. To determine the execution time of a program.", "4. To interrupt the execution of a program."], "answer":2},
             {"question": "Which symbol is used for comments in Python?", "options":["1. //", "2. #", "3. /", "4. <!-- -->"], "answer":2},
             {"question": "Which of the following data types is mutable?", "options":["1. int", "2. float", "3. tuple","4. list"], "answer":4},
             {"question": "What does the len() function do in Python?", "options":["1. Returns the total number of elements in a list", "2. Returns the square root of a numbe", "3. Returns the length of a string","4. Returns the largest element in a list"], "answer":1},
             {"question": "Which loop in Python is used to iterate over a sequence of items?", "options":["1. while loop", "2. do-while loop", "3. for loop","4. foreach loop"], "answer":3},
            ]

def quiz():
      print("Let's test your python programming knowledge.")
      
      for ques in questions:
            print("Question: ",ques['question'])
            for option in ques['options']:
                  print(option)
            while True:
                  try:
                        user_answer = int(input())
                        if user_answer == ques['answer']:
                              print("Correct!")
                              break
                        else:
                              print("Try Again!")
                  except ValueError:
                        print("Please enter valid option between 1 to 4!")
                        continue 


def end():
      print("Congratulations! Have a nice day!")

greet('Adi', 2023)
introducing_self()
guess_age()
count_numbers()
quiz()
end()
