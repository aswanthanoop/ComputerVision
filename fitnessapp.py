#health management system
#3 clients -harry , vaibhav , samarth

def getdate():
    import datetime
    return datetime.datetime.now()

# Excersixe Functions
def exc(a):
    Excersize_name = input("Which Excersize You Complete  ==>>")
    date = getdate()
    f = open(a, "a")
    f.write("\n")
    f.write("[")
    f.write(str(date))
    f.write("]")
    f.write("\t")
    f.write(":")
    f.write("\t")
    f.write(Excersize_name)

    f.close()
    print("well Done Keep up\n")

def exc_show(a):
    f = open(a)
    content = f.read()
    print(content)

    f.close()




#FoodFunctions


def food(b):
    print("Which Food You ate ",b[0:7])
    Excersize_name = input(" ==>>")
    date = getdate()
    f = open(b, "a")
    f.write("Following is List of Food You eat")
    f.write("\n")
    f.write("[")
    f.write(str(date))
    f.write("]")
    f.write("\t")
    f.write(":")
    f.write("\t")
    f.write(Excersize_name)
    f.close()
    print("follow the food chart giver by Gym\n")

def food_show(b):
    f = open(b)
    content = f.read()
    print(content)

    f.close()


#adding new member function new here
def New():

 name = input("What is your Name (Ex. abc .a.c) ==>>")
 age =  input("What is your Age ==>>")
 cat = int(input("PRess 1 for Excersize And Press 2 for food"))
 if(cat == 1):
     file2 = "e.txt"
 if(cat == 2):
     file2 = "f.txt"

     file1 = (name + file2)
     f = open(file1, "a")
     date = str(getdate())

     f.write("Following is the information of ")
     f.write(name)
     f.write("\t\t\t\t\t\t")
     f.write(date)
     f.write("\n")
     f.write("name:\t")

     f.write(name)
     f.write("\n")
     f.write("Age : \t")
     f.write(age)

     f.close()



work=1
while (work <= 50):
 print("What do You Want To Chnage Or Show  ")
 print("press 1 for Excersize ")
 print("press 2 for Food ")
 print("press 3 for EXIT")
 print("press 4 for New Admission")
 user_input1 = int(input("==>>>"))

#Excersize Data

 if(user_input1 == 1):
           print("WELCOME TO GYM DATABASE ")
           print("1-retrive or 11-Show For Harry ")
           print("2-retrive or 22-Show for Vaibhav")
           print("3-retrive or 33-Show for Samrth")
           print("4 for Others\n")
           a1 = "he.txt"
           a2 = "ve.txt"
           a3 = "se.txt"
           user_name = int(input("==>>>"))
           if(user_name == 1):
               exc(a1)
           if (user_name == 2):
               exc(a2)
           if (user_name == 3):
               exc(a3)
           if (user_name == 11):
               exc_show(a1)
           if (user_name == 22):
               exc_show(a2)
           if (user_name == 33):
               exc_show(a3)
           if (user_name == 4):
               print("1 For Record and 11 For Show Record \n")
               user_other = int(input("PLZ ENTER THE NUMBER==>>>"))
               if (user_other == 1):
                   user_response = input("Enter Your name Same as Registraion")
                   n = user_response + "e.txt"
                   exc(n)
               if (user_other == 11):
                   user_response = input("Enter Your name Same as Registraion")
                   n = user_response + "e.txt"
                   exc_show(n)
# food data
 if(user_input1 == 2):
         print("Whos Food You want to Save record or Show Record\n")
         print("1-retrive or 11-Show For Harry ")
         print("2-retrive or 22-Show for Vaibhav")
         print("3-retrive or 33-Show for Samrth")
         print("4 for Others\n")
         b1 = "hf.txt"
         b2 = "vf.txt"
         b3 = "sf.txt"
         user_name = int(input("PLZ ENTER THE NUMBER ===>>>"))
         if (user_name == 1):
             food(b1)
         if (user_name == 2):
             food(b2)
         if (user_name == 3):
             food(b3)
         if (user_name == 11):
             food_show(b1)
         if (user_name == 22):
             food_show(b2)
         if (user_name == 33):
             exc_show(b3)
         if (user_name == 4):
             print("1 For Record and 2 For Show Record \n")
             user_other = int(input("PLZ ENTER THE NUMBER==>>>"))
             if(user_other == 1):
                 user_response = input("Enter Your name Same as Registraion")
                 n = user_response + "f.txt"
                 food(n)
             if(user_other == 2):
                 user_response = input("Enter Your name Same as Registraion")
                 n = user_response + "f.txt"
                 food_show(n)
             if(user_other != 1 and user_other != 2):
                 print("Plz Enter Coreect Number")









 if(user_input1 != 1 and user_input1 != 2 and user_input1 != 3 and user_input1!= 4):
    print("You Enter Wrong one")

 if(user_input1 == 4):
     New()
     print("Thanks for show interset in our gym ..We will update your name soon \n")
 if(user_input1 == 3):
     exit()
