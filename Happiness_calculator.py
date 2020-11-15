print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("This program is going to calculate your happiness!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("You should go though 7 questions.\nPlease select 1, 2 or 3 for answer and press enter\nfor the next question.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

q_1 = int(input("\n1. Do you want to be happy?\n\n 1: Yes, I am on my way\n 2: Too late\n 3: I do not think about happiness \n\n Your answer is: "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

q_2 = int(input("\n2. Do you have  goals in your life?\n\n 1: I have clear goals\n 2: I am working on it\n 3: I think it is not my cup of tea \n\n Your answer is: ")) 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    

q_3 = int(input("\n3. Could you make more effort for better life?\n\n 1: This is what I am doing\n 2: I am looking for my way\n 3: I do not care about happiness, I do not have time for this at all \n\n Your answer is: "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

q_4 = int(input("\n4. Do you have hobby?\n\n 1: My hobby is my job\n 2: My hobby helps me  relax\n 3: I do not have a hobby \n\n Your answer is: "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

q_5 = int(input("\n5. Do you believe in something?\n\n 1: I believe in myself\n 2: I believe in destiny\n 3: I do not believe nothing \n\n Your answer: "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    

q_6 = int(input("\n6. Do you make decision on your own?\n\n 1: Easier to deal with things which I choose for myself\n 2: I do not have a choice\n 3: Let come what may \n\n Your answer is: "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

q_7 = int(input("\n7. Have you learnt something new recently?\n\n 1: I believe in a lifelong learning policy \n 2: I would like to, but I have not started yet\n 3: I do not like new things \n\n Your answer is: "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")      

happiness_meter = (q_1 + q_2 + q_3 + q_4 + q_5 + q_6 + q_7)
     
if(happiness_meter <= 10):
     print("\nHello Sunshine, your happiness meter is", happiness_meter, ":" "'The more you give the more you receive.'") 

elif(happiness_meter >= 11 and happiness_meter <= 17):
    print("\nHello Dr. Skeptical, your happiness meter is", happiness_meter, ":" "'Fear less, love more.'")

elif(happiness_meter >= 18 and happiness_meter <= 21):
    print("\nHello my dearest Grinch, your happiness meter is", happiness_meter, ":" "\n\n'Do not think about what might go wrong, think about what could be right.'")
     
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


