import random

def get_mc_statements():
    print("+------------------------------------------------------+")
    print("| Test I. Multiple Choice                              |")
    print("+------------------------------------------------------+")
    print("| Choose from the choices given, use lowercase letters |")
    print("+------------------------------------------------------+")
    print()
    statements = []
    statements.append(["What is the capital of Chile?\na. Santiago\nb. Ben Nevis\nc. Vatican City", "a"])
    statements.append(["Alberta is a province of which country?\na. Canada\nb. United States\nc. Australia", "b"])
    statements.append(["What is the largest country in the world?\na. United Kingdom\nb. Japan\nc. Russia", "c"])
    statements.append(["What is the longest river in the world?\na. Danube River\nb. Mississippi River\nc. Nile River", "c"])
    statements.append([" What are the five colours of the Olympic rings?\na. Blue, yellow, black, green and indigo"
                       "\nb. Blue, yellow, black, green and red\nc. Blue, pink, black, green and red", "b"])
    statements.append([" Which horse is the only three-time winner of the Grand National?\na. Red Horse\nb. Red "
                       "Stallion\nc. Red Rum", "c"])
    statements.append(["Who won the FIFA Women's World Cup in 2019?\na. United States of America\nb. Philippines"
                       "\nc. Italy", "a"])
    statements.append(["In golf, where does the Masters take place?\na. Augusta National\nb. Brent University"
                       "\nc. Japan National", "a"])
    statements.append(["Which nuts are used in marzipan?\na. Hazelnut\nb. Cashew\nc. Almonds", "c"])
    statements.append(["What is Japanese sake made from?\na. Bamboo\nb. Rice\nc. Coconut", "b"])
    statements.append(["What does IPA stand for?\na. Iran Pole Ale\nb. Indian Pale Ale\nc. Indonesian Pale Ale", "b"])
    statements.append(["Which fish is the main ingredient of Scotch Woodcock?\na. Anchovy\nb. Sardines\nc. Salmon", "a"])
    statements.append(["With over 222 million units sold, what is Apple’s highest-selling iPhone model?\na. iPhone XS"
                       "\nb. iPhone 7\nc. iPhone 6/6 Plus", "c"])
    statements.append(["Which operating system does a Google Pixel phone use?\na. Apple\nb. Android\nc. Lux", "b"])
    statements.append(["OS' computer abbreviation usually means?\na. Open System\nb. Optical Sensor\nc. Operating "
                       "System", "c"])
    statements.append(["Computers calculate numbers in what mode?\na. Binary\nb. Octal\nc. Decimal", "c"])
    statements.append(["Which of these is a valid e-mail address?\na. www.learnthenet.com\nb. "
                       "professor@learnthenet.com\nc. professor.at.learnthenet", "b"])
    statements.append(["What does CPU stand for?\na. Computer Processor Unit\nb. Computar Parts Unified"
                       "\nc. Central Processing Unit", "c"])
    statements.append(["Which of these is a search engine?\na. FTP\nb. Google\nc. Archie", "b"])
    statements.append(["http://www.indiabix.com - is an example of what?\na. Server\nb. Directory\nc. URL", "c"])
    statements.append(["What's a web browser?\na. A type of Tarantula  \nb. A computer that stores WWW files"
                       "\nc. A person who likes to look at websites", "a"])
    statements.append(["Grammostola Pulchripes Tarantula is an example of ?\na. Modern Spider\nb. Old World Spider"
                       "\nc. New World Spider", "c"])

    return statements


def play_mc_quiz_average():
    mc_statements = get_mc_statements()
    random.shuffle(mc_statements)
    mc_score = 0
    question_count = 0
    for s in mc_statements:
        while  question_count < 6:
            print(s[0])
            guess = input("Answer: ")
            if guess == s[1]:
                print("Correct! :)")
                print()
                question_count += 1
                mc_score += 1
                break
            else:
                print("Wrong :(")
                question_count += 1
                print()
                break

    print("Your total score :", str(mc_score), "/ 6")

def play_mc_quiz_expert():
    mc_statements = get_mc_statements()
    random.shuffle(mc_statements)
    mc_score = 0
    question_count = 0
    for s in mc_statements:
        while question_count < 11:
            print(s[0])
            guess = input("Answer: ")
            if guess == s[1]:
                print("Correct! :)")
                print()
                question_count += 1
                mc_score += 1
                break
            else:
                print("Wrong :(")
                question_count += 1
                print()
                break

    print("Your total score :", str(mc_score), "/ 11")


def get_fitb_statements():
    print("+-------------------------------------------------------+")
    print("| Test II. Fill in the Blank                            |")
    print("+-------------------------------------------------------+")
    print("| Please type the correct answer, use lowercase letters |")
    print("+-------------------------------------------------------+")
    print()

    statements = []
    statements.append(["The Bermuda Triangle is located at ________ ocean. (at**n*ic)", "atlantic"])
    statements.append(["_______ is a state in U.S where in it is known for Peaches. (ge*rg**)", "georgia"])
    statements.append(["The ______ is a vegetable known for its ability to enhance eye sight. (c*rr**)", "carrot"])
    statements.append(["In the United States, ______ is the largest state among them. (ca**d*)", "canada"])
    statements.append(["Quebec is a province in Canada and they speak ______ there. (fr**c*)", "french"])
    statements.append(["The world's largest volcano is located at ______. (h*w**i)", "hawaii"])
    statements.append(["_____ is a plant that has the ability to help heal a sunburn. (*loe)", "aloe"])
    statements.append(["In 2003,a social media platform called _______ was released (my*p*ce)", "myspace"])
    statements.append(["Michael Phelps is an Olympic athlete known in the sport ________. (sw***in*)", "swimming"])
    statements.append(["Greece hosted the _____ Olympic Games in 1896. (f**st)", "first"])
    statements.append(["Mcdonalds is known for its burger called ______. (b** m**)", "big mac"])
    statements.append(["Tiger Woods is known in the sport _____. (g**f)", "golf"])
    statements.append(["Santa Claus has _____ reindeers. (e*g**)", "eight"])
    statements.append(["The _______ ocean is known to be the largest ocean in the Earth. (p**if**)", "pacific"])
    statements.append(["In the cartoon Bambi, Bambi is a _____. (d***)", "deer"])
    statements.append(["The attack on Pearl Harbor took place in ________ ______. (h*n*l*l* h*wa**)", "honolulu hawaii"])

    return statements


def play_fitb_quiz_average():
    fitb_statements = get_fitb_statements()
    random.shuffle(fitb_statements)
    fitb_score = 0
    question_count = 0
    for s in fitb_statements:
        while question_count < 6:
            print(s[0])
            guess = input("Answer: ")
            if guess == s[1]:
                print("Correct! :)")
                print()
                question_count += 1
                fitb_score += 1
                break
            else:
                print("Wrong :(")
                question_count += 1
                print()
                break

    print("Your total score :", str(fitb_score), "/ 6")

def play_fitb_quiz_expert():
    fitb_statements = get_fitb_statements()
    random.shuffle(fitb_statements)
    fitb_score = 0
    question_count = 0
    for s in fitb_statements:
        while question_count < 11:
            print(s[0])
            guess = input("Answer: ")
            if guess == s[1]:
                print("Correct! :)")
                print()
                question_count += 1
                fitb_score += 1
                break
            else:
                print("Wrong :(")
                question_count += 1
                print()
                break

    print("Your total score :", str(fitb_score), "/ 11")


def get_i_statements():
    print("+-------------------------------------------------------+")
    print("| Test III. Identification                              |")
    print("+-------------------------------------------------------+")
    print("| Please type the correct answer, use lowercase letters |")
    print("+-------------------------------------------------------+")
    print()

    statements = []
    statements.append(["Which is the only vowel not used as the first letter in a US State? (hint: 5th alphabet)", "e"])
    statements.append(["What is the hottest continent on Earth? (hint: where nile river is located)", "africa"])
    statements.append(["What is the smallest country in the world? (hint: Home of the Pope (city))", "vatican"])
    statements.append(["How many players are there in a rugby league team? (hint: more than 12)", "13"])
    statements.append(["In tennis, what piece of fruit is found at the top of the men's Wimbledon trophy "
                       "(hint: yellow fruit)", "pineapple"])
    statements.append(["How many world titles has Phil Taylor won in darts? (hint: more than 15)", "16"])
    statements.append([" Which country is the origin of the cocktail Mojito. (hint: c**a)", "cuba"])
    statements.append(["What is the chemical formula for Table Salt? (hint: sodium chloride)", "nacl"])
    statements.append(["What hot breakfast cereal is made from crushed or rolled oats? (hint: quaker oats)", "oatmeal"])
    statements.append(["Elon Musk is the CEO of which global car brand? (hint: chargeable car)", "tesla"])
    statements.append(["Which operating system does a Google Pixel phone use? (hint: kitkat version)", "android"])
    statements.append(["In which year was the Nintendo 64 released in Europe? (hint: 1995-2000)", "1997"])
    statements.append(["What does CPU stand for?", "central processing unit"])
    statements.append(["Solar power generates electricity from what source?", "sun"])
    statements.append(["What is the largest non-continental island in the world? (hint: gr**nl*n*)", "greenland"])
    statements.append(["Kuala Lumpur is the capital of which country? (hint: truly asia)", "malaysia"])

    return statements


def play_i_quiz_average():
    i_statements = get_i_statements()
    random.shuffle(i_statements)
    i_score = 0
    question_count = 0
    for s in i_statements:
        while question_count < 6:
            print(s[0])
            guess = input("Answer: ")
            if guess == s[1]:
                print("Correct! :)")
                print()
                question_count += 1
                i_score += 1
                break
            else:
                print("Wrong :(")
                question_count += 1
                print()
                break

    print("Your total score :", str(i_score), "/ 6")

def play_i_quiz_expert():
    i_statements = get_i_statements()
    random.shuffle(i_statements)
    i_score = 0
    question_count = 0
    for s in i_statements:
        while question_count < 11:
            print(s[0])
            guess = input("Answer: ")
            if guess == s[1]:
                print("Correct! :)")
                print()
                question_count += 1
                i_score += 1
                break
            else:
                print("Wrong :(")
                question_count += 1
                print()
                break

    print("Your total score :", str(i_score), "/ 11")


def get_tof_statements():
    print("+----------------------------+")
    print("| Test IV. True or False     |")
    print("+----------------------------+")
    print("| Type T or F                |")
    print("+----------------------------+")
    print()

    statements = []
    statements.append(["Mt. Everest is the highest mountain in Britain.", "T"])
    statements.append(["Alberta is a province of Canada.", "T"])
    statements.append(["The letter \"E\" is the only vowel that is not used as the first letter in a US State.", "T"])
    statements.append(["The River Thames is located in France.", "F"])
    statements.append(["The team \"Real Madrid\" has won the Champions League (formerly the European Cup) the most.", "T"])
    statements.append(["The Black Rum horse is the only three-time winner of the Grand National.", "F"])
    statements.append(["In tennis, grape fruit is found at the top of the men's Wimbledon trophy.", "F"])
    statements.append(["In bowling, \"Turkey\" is the term given for three consecutive strikes.", "T"])
    statements.append(["Corona is the most famous Mexican beer.", "T"])
    statements.append(["Japanese sake made from rice.", "T"])
    statements.append(["\"NaCl\" is the chemical formula for Table Salt", "T"])
    statements.append(["Meat is used in Glamorgan sausages", "F"])
    statements.append(["Apple’s highest-selling iPhone model is 6/6s", "T"])
    statements.append(["Goldfish only have a memory of three seconds", "T"])
    statements.append(["The capital of Libya is Benghazi", "F"])
    statements.append(["An octopus has five hearts", "F"])

    return statements


def play_tof_quiz_average():
    tof_statements = get_tof_statements()
    random.shuffle(tof_statements)
    tof_score = 0
    question_count = 0
    for s in tof_statements:
        while question_count < 6:
            print(s[0])
            guess = input("Answer: ")
            if guess == s[1]:
                print("Correct! :)")
                print()
                question_count += 1
                tof_score += 1
                break
            else:
                print("Wrong :(")
                question_count += 1
                print()
                break

    print("Your total score :", str(tof_score), "/ 6")

def play_tof_quiz_expert():
    tof_statements = get_tof_statements()
    random.shuffle(tof_statements)
    tof_score = 0
    question_count = 0
    for s in tof_statements:
        while question_count < 11:
            print(s[0])
            guess = input("Answer: ")
            if guess == s[1]:
                print("Correct! :)")
                print()
                question_count += 1
                tof_score += 1
                break
            else:
                print("Wrong :(")
                question_count += 1
                print()
                break

    print("Your total score :", str(tof_score), "/ 11")


def get_ptoo_statements():
    print("+------------------------------------------------------+")
    print("| Test V. Pick the Odd One                             |")
    print("+------------------------------------------------------+")
    print("| Choose from the given choices, use lowercase letters |")
    print("+------------------------------------------------------+")
    print()

    statements = []
    statements.append(["Which does not belong to the sequence? \n(2, 4, 5, 8, ,10)", "5"])
    statements.append(["Which does not belong in the colors of Olympic ring? \n(blue, yellow, orange, green, red)",
                       "orange"])
    statements.append(["Which is not part of the seven continents in the world?"
                       "\n(greenland, antarctica, asia, australia, europe, north america, south America)", "greenland"])
    statements.append(["Which one of these countries is not like the other?"
                       "\n(china, egypt, indonesia, japan)", "egypt"])
    statements.append(["Which is not an Ancient Structure?"
                       "\n(stonehenge, pyramid of giza, colossus of rhodes, lighthouse of alexandria)", "stonehenge"])
    statements.append(["Which one of the following is not an old-fashioned name for a type of golf club?\n(spoon, "
                       "niblick, brassie, dibber)", "dibber"])
    statements.append(["Pick the odd one\n(blackberry, ios, windows, android)", "windows"])
    statements.append(["pick the odd one\n(intel pentium, intel 4004, intel 8088, intel i3)", "intel 8088"])

    return statements

def play_ptoo_quiz_average():
    ptoo_statements = get_ptoo_statements()
    random.shuffle(ptoo_statements)
    ptoo_score = 0
    question_count = 0
    for s in ptoo_statements:
        while question_count < 6:
            print(s[0])
            guess = input("Answer: ")
            if guess == s[1]:
                print("Correct! :)")
                print()
                question_count += 1
                ptoo_score += 1
                break
            else:
                print("Wrong :(")
                question_count += 1
                print()
                break

    print("Your total score :", str(ptoo_score), "/ 6")

def play_ptoo_quiz_expert():
    ptoo_statements = get_ptoo_statements()
    random.shuffle(ptoo_statements)
    score = 0
    question_count = 0
    for s in ptoo_statements:
        while question_count < 8:
            print(s[0])
            guess = input("Answer: ")
            if guess == s[1]:
                print("Correct! :)")
                print()
                question_count += 1
                score += 1
                break
            else:
                print("Wrong :(")
                question_count += 1
                print()
                break

    print("Your total score :", str(score), "/ 8")



def mult_ans():
    print("Answers for multiple choice : "
              "\n1.) What is the capital of Chile? a.Santiago"
              "\n2.) Alberta is a province of which country? b.United States"
              "\n3.) What is the largest country in the world? c. Russia"
              "\n4.) What is the longest river in the world? c. Nile River"
              "\n5.) What are the five colours of the Olympic rings? b. Blue, yellow, black, green and red"
              "\n6.) Which horse is the only three-time winner of the Grand National? c. Red Rum"
              "\n7.) Who won the FIFA Women's World Cup in 2019? a. United States of America"
              "\n8.) In golf, where does the Masters take place? a. Augusta National"
              "\n9.) Which nuts are used in marzipan? c. Almonds"
              "\n10.) What is Japanese sake made from? b. Rice"
              "\n11.) What does IPA stand for? b. Indian Pale Ale"
              "\n12.) Which fish is the main ingredient of Scotch Woodcock? a. Anchovy"
              "\n13.) With over 222 million units sold, what is Apple’s highest-selling iPhone model? c. iPhone 6/6 Plus"
              "\n14.) Which operating system does a Google Pixel phone use? b. Android"
              "\n15.) OS' computer abbreviation usually means ? c. Operating System"
              "\n16.) Computers calculate numbers in what mode? c. Decimal"
              "\n18.) Which of these is a valid e-mail address? b. professor@learnthenet.com"
              "\n19.) What does CPU stand for? c. Central Processing Unit"
              "\n20.) Which of these is a search engine? b. Google"
              "\n21.) http://www.indiabix.com - is an example of what? c. URL"
              "\n22.) What's a web browser? a. A type of Tarantula"
              "\n23.) Grammostola Pulchripes Tarantula is an example of ? c. New World Spider")

def fitb_ans():
    print("Answers for Fill in the blank : "
          "\n1.) The Bermuda Triangle is located at ________ ocean. (atlantic)"
          "\n2.) _______ is a state in U.S where in it is known for Peaches. (georgia)"
          "\n3.) The ______ is a vegetable known for its ability to enhance eye sight. (carrot)"
          "\n4.) In the United States, ______ is the largest state among them. (canada)"
          "\n5.) Quebec is a province in Canada and they speak ______ there. (french)"
          "\n6.) The world's largest volcano is located at ______. (hawaii)"
          "\n7.) ____ is a plant that has the ability to help heal a sunburn. (aloe)"
          "\n8.) In 2003,a social media platform called _______ was released (myspace)"
          "\n9.) Michael Phelps is an Olympic athlete known in the sport ________. (swimming)"
          "\n10.) Greece hosted the _____ Olympic Games in 1896. (first)"
          "\n11.) Mcdonalds is known for its burger called ______. (big mac)"
          "\n12.) Tiger Woods is known in the sport _____. (golf)"
          "\n13.) Santa Claus has _____ reindeers. (eight)"
          "\n14.) The _______ ocean is known to be the largest ocean in the Earth. (pacific)"
          "\n15.) In the cartoon Bambi, Bambi is a _____. (deer)"
          "\n16.) The attack on Pearl Harbor took place in ________ ______. (honolulu hawaii)")

def identf_ans():
    print("Answers for Identification : "
          "\n1.) Which is the only vowel not used as the first letter in a US State?. (e)"
          "\n2.) What is the hottest continent on Earth?.(africa)"
          "\n3.) What is the smallest country in the world?. (vatican city)"
          "\n4.) How many players are there in a rugby league team?.(13)"
          "\n5.) In tennis, what piece of fruit is found at the top of the men's Wimbledon trophy?. (pineapple)"
          "\n6.) How many world titles has Phil Talyor won in darts?. (16)"
          "\n7.) Which country is the origin of the cocktail Mojito?. (cuba)"
          "\n8.) What is the chemical formula for Table Salt?. (nacl)"
          "\n9.) What hot breakfast cereal is made from crushed or rolled oats?. (oatmeal)"
          "\n11.) Which operating system does a Google Pixel phone use?. (android)"
          "\n12.) In which year was the Nintendo 64 released in Europe?. (1997)"
          "\n13.) What does CPU stand for?. (central processing unit)"
          "\n14.) Solar power generates electricity from what source?. (sun)"
          "\n15.) What is the largest non-continental island in the world?. (greenland)"
          "\n16.) Kuala Lumpur is the capital of which country?. (malaysia)")

def tof_ans():
    print("Answers for True or False : "
          "\n1.) Mt. Everest is the highest mountain in Britain. (F)"
          "\n2.) Alberta is a province of Canada. (T)"
          "\n3.) The letter \"E\" is the only vowel that is not used as the first letter in a US State. (T)"
          "\n4.) The River Thames is located in France. (F)"
          "\n5.) The team \"Real Madrid\" has won the Champions League (formerly the European Cup) the most. (T)"
          "\n6.) The Black Rum horse is the only three-time winner of the Grand National. (F)"
          "\n7.) In tennis, grape fruit is found at the top of the men's Wimbledon trophy. (F)"
          "\n8.) In bowling, \"Turkey\" is the term given for three consecutive strikes. (T)"
          "\n9.) Corona is the most famous Mexican beer.(T)"
          "\n10.) Japanese sake made from rice. (T)"
          "\n11.) \"NaCl\" is the chemical formula for Table Salt. (T)"
          "\n12.) Meat is used in Glamorgan sausages. (F)"
          "\n13.) Apple’s highest-selling iPhone model is 6/6s. (T)"
          "\n14.) Goldfish only have a memory of three seconds. (F)"
          "\n15.) The capital of Libya is Benghazi. (F)"
          "\n16.) An octopus has five hearts. (F)")

def ptoo_ans():
    print("Answers for 'Pick The Odd One' : "
          "\n1.) Which does not belong to the sequence? (5)"
          "\n2.) Which does not belong in the colors of Olympic ring? (orange)"
          "\n3.) Which is not part of the seven continents in the world? (greenland)"
          "\n4.) Which one of these countries is not like the other? (egypt)"
          "\n5.) Which is not an Ancient Structure? (stonehenge)"
          "\n6.) Which one of the following is not an old-fashioned name for a type of golf club? (dibber)"
          "\n7.) Pick the odd one (windows)"
          "\n8.) pick the odd one (intel 8088)")

def menu():
    print("+-------------------------------------------------------------+")
    print("| Type \"1\" to reveal answers or type \"0\" to exit the program  |")
    print("+-------------------------------------------------------------+")
    print()
    input_user = input("Enter here : ")
    while True:
        if input_user == "1":
            print()
            print("Please Select Test : "
                  "\n1 - Multiple Choice"
                  "\n2 - Fill in the blank"
                  "\n3 - identification"
                  "\n4 - True or False"
                  "\n5 - Pick the odd one"
                  "\n6 - Exit Program")
            print()
            selection = input("Enter here : ")
            if selection == "1":
                mult_ans()
                back_to_menu = input("Press 0 to go back to menu : ")
                if back_to_menu == "0":
                    menu()
            elif selection == "2":
                fitb_ans()
                back_to_menu = input("Press 0 to go back to menu : ")
                if back_to_menu == "0":
                    menu()
            elif selection == "3":
                identf_ans()
                back_to_menu = input("Press 0 to go back to menu : ")
                if back_to_menu == "0":
                    menu()
            elif selection == "4":
                tof_ans()
                back_to_menu = input("Press 0 to go back to menu : ")
                if back_to_menu == "0":
                    menu()
            elif selection == "5":
                ptoo_ans()
                back_to_menu = input("Press 0 to go back to menu : ")
                if back_to_menu == "0":
                    menu()
            elif selection == "6":
                print("Thank You!")
                print("Project by Team Pink: (BES241) 12-10-2020 \n Carl Peñaranda \n Trixxie De Asis "
                      "\n Rian Magsino \n 1CPE ")
                exit()
            elif selection == " ":
                print("Error, Please Try Again")

        elif input_user == "0":
            print("Thank You!")
            print("Project by Team Pink: (BES241) 12-10-2020 \n Carl Peñaranda \n Trixxie De Asis "
                  "\n Rian Magsino \n 1CPE ")
            exit()
            break
        else:
            print("Invalid Input! Try Again")
            menu()


print("+------------------------------------------+")
print("|    Welcome to Team Pink's Quiz Game!     |")
print("+------------------------------------------+")
print("|  Please Select Difficulty:               |")
print("|      1 - Average                         |")
print("|      2 - Expert                          |")
print("+------------------------------------------+")

def start():
    answer = input("Enter here : ")
    while True:
        if answer == "1":
            print()
            play_mc_quiz_average()
            play_fitb_quiz_average()
            play_i_quiz_average()
            play_tof_quiz_average()
            play_ptoo_quiz_average()
            print()
            menu()
            break

        elif answer == "2":
            print()
            play_mc_quiz_expert()
            play_fitb_quiz_expert()
            play_i_quiz_expert()
            play_tof_quiz_expert()
            play_ptoo_quiz_expert()
            print()
            menu()
            break
        else:
            print("Error Invalid input")
            start()


start()
