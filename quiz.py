challenge = input("Good day! Would you like to take on the challenge of Team Pink's Quiz?\n"
                  "Type 'YES' to challenge the quiz or 'NO' to exit the quiz\n : ")
if challenge == "YES":
    print(
        "Good Day Contestants! Welcome to Team Pink's Quiz Game!\n\nThe coverage of this quiz includes the general "
        "knowledge on technology,\n geography, foods and drinks, sports, and animals. The subjects are divided into "
        "five test types,\n namely, \n I.Multiple choice \n II.Fill in the blank \n III.Identification \n "
        "IV.True or false \n V.Pick the odd one \n Finally, before starting the quiz please read the "
        "instructions carefully. Good luck and hope you have a great time")
    print()
    print("Test I : Multiple choice \n TAKE NOTE: Input your answers in lowercase\n")
    mc_score = 0
    mc_questions = {"1.) What is the capital of Chile?\na. Santiago\nb. Ben Nevis\nc. Vatican City": "a",
                    "2.) Alberta is a province of which country?\na. Canada\nb. United States\nc. Australia": "b",
                    "3.) What is the largest country in the world?\na. United Kingdom\nb. Japan\nc. Russia": "c",
                    "4.) What is the longest river in the world?\na. Danube River\nb. Mississippi River\nc. Nile River":
                    "c",
                    "5.) What are the five colours of the Olympic rings?\na. Blue, yellow, black, green and indigo"
                    "\nb. Blue, yellow, black, green and red\nc. Blue, pink, black, green and red": "b",
                    "6.) Which horse is the only three-time winner of the Grand National?\na. Red Horse\nb. Red "
                    "Stallion "
                    "\nc. Red Rum": "c",
                    "7.) Who won the FIFA Women's World Cup in 2019?\na. United States of America\nb. Philippines"
                    "\nc. Italy": "a",
                    "8.) In golf, where does the Masters take place?\na. Augusta National\nb. Brent University"
                    "\nc. Japan National": "a",
                    "9.) Which nuts are used in marzipan?\na. Hazelnut\nb. Cashew\nc. Almonds": "c",
                    "10.) What is Japanese sake made from?\na. Bamboo\nb. Rice\nc. Coconut": "b",
                    "11.) What does IPA stand for?\na. Iran Pole Ale\nb. Indian Pale Ale\nc. Indonesian Pale Ale": "b",
                    "12.) Which fish is the main ingredient of Scotch Woodcock?\na. Anchovy\nb. Sardines\nc. Salmon":
                    "a",
                    "13.) With over 222 million units sold, what is Apple’s highest-selling iPhone model?\na. iPhone XS"
                    "\nb. iPhone 7\nc. iPhone 6/6 Plus": "c",
                    "14.) Which operating system does a Google Pixel phone use?\na. Apple\nb. Android\nc. Lux": "b",
                    "15.) OS' computer abbreviation usually means ?\na. Open System\nb. Optical Sensor\nc. Operating "
                    "System": "c",
                    "16.) Computers calculate numbers in what mode?\na. Binary\nb. Octal\nc. Decimal": "c",
                    "18.) Which of these is a valid e-mail address?\na. www.learnthenet.com\nb. "
                    "professor@learnthenet.com "
                    "\nc. professor.at.learnthenet": "b",
                    "19.) What does CPU stand for?\na. Computer Processor Unit\nb. Computar Parts Unified"
                    "\nc. Central Processing Unit": "c",
                    "20.) Which of these is a search engine?\na. FTP\nb. Google\nc. Archie": "b",
                    "21.) http://www.indiabix.com - is an example of what?\na. Server\nb. Directory\nc. URL": "c",
                    "22.) What's a web browser?\na. A type of Tarantula  \nb. A computer that stores WWW files"
                    "\nc. A person who likes to look at websites": "a",
                    "23.) Grammostola Pulchripes Tarantula is an example of ?\na. Modern Spider\nb. Old World Spider"
                    "\nc. New World Spider": "c",
                    "24.) Ceratogyrus Darlingi Tarantula is an example of ?\na. Modern Spider\nb. Old World Spider"
                    "\nc. New World Spider": "b",
                    "25.) What group of animals is known as a “flamboyance”?\na. Flamingo\nb. Femure\nc. Tarantula":
                    "a",
                    "26.) Who founded Microsoft?\na. Stephen Hawkins\nb. Bill Gates\nc. Indiana Jones": "b",
                    "27.) What is the #1 cookie in the United States?\na. Cream-O\nb. Presto\nc. Oreo": "c",
                    "28.) How many hearts does an octopus have?\na. 1\nb. 2\nc. 3": "c",
                    }
    for i in mc_questions:
        print(i)
        mc_answer = input("Answer: ")
        if mc_answer.lower() == mc_questions[i]:
            mc_score += 1
            print()
        else:
            print()
    print("Your score for the Multiple Choice category is", mc_score, "out of 28")

    print()
    print("Test II : Fill in the blank \n Type your answer in LOWER CASE, failure to do so would\n"
          "automatically count as a wrong answer. Double checking the spelling of your answer is highly \n"
          "recommended!!\n")
    fitb_score = 0
    fitb_questions = {"1.) The Bermuda Triangle is located at ________ ocean. (at**n*ic)": "atlantic",
                      "2.) _______ is a state in U.S where in it is known for Peaches. (ge*rg**)": "georgia",
                      "3.) The ______ is a vegetable known for its ability to enhance eye sight. (c*rr**)": "carrot",
                      "4.) In the United States, ______ is the largest state among them. (ca**d*)": "canada",
                      "5.) Quebec is a province in Canada and they speak ______ there. (fr**c*)": "french",
                      "6.) The world's largest volcano is located at ______. (h*w**i)": "hawaii",
                      "7.) ____ is a plant that has the ability to help heal a sunburn. (*loe)": "aloe",
                      "8.) In 2003,a social media platform called _______ was released (my*p*ce)": "myspace",
                      "9.) Michael Phelps is an Olympic athlete known in the sport ________. (sw***in*)": "swimming",
                      "10.) Greece hosted the _____ Olympic Games in 1896. (f**st)": "first",
                      "11.) Mcdonalds is known for its burger called ______. (b** m**)": "big mac",
                      "12.) Tiger Woods is known in the sport _____. (g**f)": "golf",
                      "13.) Santa Claus has _____ reindeers. (e*g**)": "eight",
                      "14.) The _______ ocean is known to be the largest ocean in the Earth. (p**if**)": "pacific",
                      "15.) In the cartoon Bambi, Bambi is a _____. (d***)": "deer",
                      "16.) The attack on Pearl Harbor took place in ________ ______. (h*n*l*l* h*wa**)":
                      "honolulu hawaii",
                      "17.) The commonly called firehouse dog's breed is _________. (da*ma**an)": "dalmatian",
                      "18.) The name of the company that published the Mario Kart video game is ________. (n**t*ndo)":
                      "nintendo",
                      "19.) The ______ gate bridge is a famous bridge located at San Francisco, CA. (*old*n)": "golden",
                      "20.) Mariana's Trench is known to be the _______ trench worldwide. (d**pe**)": "deepest",
                      "21.) Kung Fu was originated in _____. (ch**a)": "china",
                      "22.) The animal _______ is known for showing its colorful and beautiful tail. (pe*c**k)":
                      "peacock",
                      "23.) The world's fastest runner is _____ ____. (*s*in *olt)": "usain bolt",
                      "24.) The _______ Tunnel is the longest rail tunnel in the world. (ch*n**l)": "channel",
                      "25.) The highest mountain in England is ___ Nevis (b*n)": "ben",
                      "26.) The Statue of Liberty was a gift from ______. (f*a*c*)": "france",
                      "27.) The first tea bags were made of _____. (**lk)": "silk",
                      "28.) ______ is the capital of Bulgaria. (w*rsa*)": "warsaw",
                      }
    for i in fitb_questions:
        print(i)
        fitb_answer = input("Answer: ")
        if fitb_answer == fitb_questions[i]:
            fitb_score += 1
            print()
        else:
            print()

    print("Your score for the Fill in the Blank category is", fitb_score, "out of 28")

    print()
    print("Test III : Identification \n Type your answer in LOWER CASE, failure to do would\n"
          "automatically count as a wrong answer. Double checking the spelling of your answer is highly\n"
          "recommended\n")
    i_score = 0
    i_sentences = {"1.) Which is the only vowel not used as the first letter in a US State? (hint: 5th alphabet)": "e",
                   "2.) What is the hottest continent on Earth? (hint: where nile river is located)": "africa",
                   "3.) What is the smallest country in the world? (hint: Home of the Pope (city))": "vatican",
                   "4.) How many players are there in a rugby league team? (hint: more than 12)": "13",
                   "5.) In tennis, what piece of fruit is found at the top of the men's Wimbledon trophy "
                   "(hint: yellow fruit)": "pineapple",
                   "6.) How many world titles has Phil Taylor won in darts? (hint: more than 15)": "16",
                   "7.) Which country is the origin of the cocktail Mojito. (hint: c**a)": "cuba",
                   "8.) What is the chemical formula for Table Salt? (hint: sodium chloride)": "nacl",
                   "9.) What hot breakfast cereal is made from crushed or rolled oats? (hint: quaker oats)": "oatmeal",
                   "10.) Elon Musk is the CEO of which global car brand? (hint: chargeable car)": "tesla",
                   "11.) Which operating system does a Google Pixel phone use? (hint: kitkat version)": "android",
                   "12.) In which year was the Nintendo 64 released in Europe? (hint: 1995-2000)": "1997",
                   "13.) What does CPU stand for?": "central processing unit",
                   "14.) Solar power generates electricity from what source?": "sun",
                   "15.) What is the largest non-continental island in the world? (hint: gr**nl*n*)": "greenland",
                   "16.) Kuala Lumpur is the capital of which country? (hint: truly asia)": "malaysia",
                   "17.) What is the Capital of the United States? (hint: w** d.c)": "washington d.c",
                   "18.) What is the capital of the American state of Arizona? (hint: ph**n*x)": "phoenix",
                   "19.) What cooking technique involves submerging egg in a liquid at a relatively low temperature?":
                   "poaching",
                   "20.) What food is the leading source of salmonella poisoning? (hint: kfc)": "chicken",
                   "21.) What ingredient in fresh milk is eventually devoured by bacteria, causing the sour taste? "
                   "(hint: l*ct***)": "lactose",
                   "22.) Which bird is a symbol for peace? (hint: soap brand)": "dove",
                   "23.) What are baby kangaroo called? (hint: jo*y)": "joey",
                   "24.) What animal is said to have 9 lives? (hint: favorite food fish)": "cat",
                   "25.) Where is the Great Barrier Reef located? (hint: aust***)": "australia",
                   "26.) What sport does Cristiano Ronaldo play? (hint: in european term)": "football",
                   "27.) What is the name of the longest river in South America? (hint: ama**n)": "amazon",
                   "28.) In which ocean is the Bermuda Triangle located? (hint: atlant**)": "atlantic"
                   }

    for i in i_sentences:
        print(i)
        mc_answer = input("Answer: ")
        if mc_answer == i_sentences[i]:
            i_score += 1
            print()
        elif mc_answer != i_sentences[i]:
            print()
    else:
        print()
    print("Your score for the Identification category is", i_score, "out of 28")

    print()
    print("Test IV : True or False \n Type 'T' if the statement is TRUE and 'F' if the\n"
          "statement is FALSE. Type CAPITAL letters only. \n")
    tof_score = 0
    tof_statements = {"1.) Mt. Everest is the highest mountain in Britain.": "F",
                      "2.) Alberta is a province of Canada.": "T",
                      "3.) The letter \"E\" is the only vowel that is not used as the first letter in a US State.": "T",
                      "4.) The River Thames is located in France.": "F",
                      "5.) The team \"Real Madrid\" has won the Champions League (formerly the European Cup) the most.":
                      "T",
                      "6.) The Black Rum horse is the only three-time winner of the Grand National.": "F",
                      "7.) In tennis, grape fruit is found at the top of the men's Wimbledon trophy.": "F",
                      "8.) In bowling, \"Turkey\" is the term given for three consecutive strikes.": "T",
                      "9.) Corona is the most famous Mexican beer.": "T",
                      "10.) Japanese sake made from rice.": "T",
                      "11.) \"NaCl\" is the chemical formula for Table Salt": "T",
                      "12.) Meat is used in Glamorgan sausages": "F",
                      "13.) Apple’s highest-selling iPhone model is 6/6s": "T",
                      "14.) Goldfish only have a memory of three seconds": "F",
                      "15.) The capital of Libya is Benghazi": "F",
                      "16.) An octopus has five hearts": "F",
                      "17.) Brazil is the only country in the Americas to have the official language of Portuguese":
                      "T",
                      "18.) The Channel Tunnel is the longest rail tunnel in the world": "F",
                      "19.) The highest mountain in England is Ben Nevis": "F",
                      "20.) The Statue of Liberty was a gift from France": "T",
                      "21.) The Great Wall of China is visible from space": "F",
                      "22.) The first tea bags were made of silk": "T",
                      "23.) Warsaw is the capital of Bulgaria": "F",
                      "24.) Flying in an aeroplane is statistically safer than driving in a car": "T",
                      "25.) Valletta is the capital of Cyprus": "F",
                      "26.) Ben Nevis is the tallest mountain in the UK": "T",
                      "27.) Strawberry is the only fruit with seeds on the outside": "T",
                      "28.) In the state Georgia, US is known for peaches": "T"
                      }

    for i in tof_statements:
        print(i)
        mc_answer = input("Answer: ")
        if mc_answer == tof_statements[i]:
            tof_score += 1
            print()
        else:
            print()

    print("Your score for the True of False Category is", tof_score, "out of 28")

    print()
    print("Test V. : Pick the odd one \n Type your answer in LOWER CASE, failure to so would\n"
          "automatically count as a wrong answer. Double checking the spelling of your answer is\n"
          "highly recommended.")

    w_score = 0
    w_ans1 = "5"
    print("1.) Which does not belong to the sequence? \n(2, 4, 5, 8, ,10)")
    w_ans = input("Answer : ")
    if w_ans == w_ans1:
        w_score += 1
    print()

    w_ans2 = "orange"
    print("2.) Which does not belong in the colors of Olympic ring? \n(blue, yellow, orange, green, red)")
    w_ans = input("Answer : ")
    if w_ans == w_ans2:
        w_score += 1
    print()

    w_ans3 = "greenland"
    print("3.) Which is not part of the seven continents in the world?"
          "\n(greenland, antarctica, asia, australia, europe, north america, south America)")
    w_ans = input("Answer : ")
    if w_ans == w_ans3:
        w_score += 1
    print()

    w_ans4 = "egypt"
    print("4.) Which one of these countries is not like the other?"
          "\n(china, egypt, indonesia, japan)")
    w_ans = input("Answer : ")
    if w_ans == w_ans4:
        w_score += 1
    print()

    w_ans5 = "stonehenge"
    print("5.) Which is not an Ancient Structure?"
          "\n(stonehenge, pyramid of giza, colossus of rhodes, lighthouse of alexandria)")
    w_ans = input("Answer : ")
    if w_ans == w_ans5:
        w_score += 1
    print()

    w_ans6 = "dibber"
    print("6.) Which one of the following is not an old-fashioned name for a type of golf club?"
          "\n(spoon, niblick, brassie, dibber)")
    w_ans = input("Answer : ")
    if w_ans == w_ans6:
        w_score += 1
    print()

    w_ans7 = "windows"
    print("7.) Pick the odd one"
          "\n(blackberry, ios, windows, android)")
    w_ans = input("Answer : ")
    if w_ans == w_ans7:
        w_score += 1
    print()

    w_ans8 = "intel 8088"
    print("8.) pick the odd one"
          "\n(intel pentium, intel 4004, intel 8088, intel i3)")
    w_ans = input("Answer : ")
    if w_ans == w_ans8:
        w_score += 1
    print()

    print("Your score for the Pick the odd one category is", w_score, "out of 8")
    print()

    total_score = mc_score + fitb_score + i_score + tof_score + w_score
    print("You have finished the quiz! Your total score for the Quiz of Team Pink's Quiz is : \n ", total_score,
          "/ 120")
    print()

    def mult_ans():
        print("Answers for multiple choice : "
              "\n1. What is the capital of Chile? a.Santiago"
              "\n2. Alberta is a province of which country? b.United States"
              "\n3. What is the largest country in the world? c. Russia"
              "\n4. What is the longest river in the world? c. Nile River"
              "\n5. What are the five colours of the Olympic rings? b. Blue, yellow, black, green and red"
              "\n6. Which horse is the only three-time winner of the Grand National? c. Red Rum"
              "\n7. Who won the FIFA Women's World Cup in 2019? a. United States of America"
              "\n8. In golf, where does the Masters take place? a. Augusta National"
              "\n9. Which nuts are used in marzipan? c. Almonds"
              "\n10. What is Japanese sake made from? b. Rice"
              "\n11. What does IPA stand for? b. Indian Pale Ale"
              "\n12. Which fish is the main ingredient of Scotch Woodcock? a. Anchovy"
              "\n13. With over 222 million units sold, what is Apple’s highest-selling iPhone model? c. iPhone 6/6 Plus"
              "\n14. Which operating system does a Google Pixel phone use? b. Android"
              "\n15. OS' computer abbreviation usually means ? c. Operating System"
              "\n16. Computers calculate numbers in what mode? c. Decimal"
              "\n18. Which of these is a valid e-mail address? b. professor@learnthenet.com"
              "\n19. What does CPU stand for? c. Central Processing Unit"
              "\n20. Which of these is a search engine? b. Google"
              "\n21. http://www.indiabix.com - is an example of what? c. URL"
              "\n22. What's a web browser? a. A type of Tarantula"
              "\n23. Grammostola Pulchripes Tarantula is an example of ? c. New World Spider"
              "\n24. Ceratogyrus Darlingi Taranrula is an example of ? b. Old World Spider"
              "\n25. What group of animals is known as a “flamboyance”? a. Flamingo"
              "\n26. Who founded Microsoft? b. Bill Gates"
              "\n27. What is the #1 cookie in the United States? c. Oreo"
              "\n28. How many hearts does an octopus have?c. 3")


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
              "\n16.) The attack on Pearl Harbor took place in ________ ______. (honolulu hawaii)"
              "\n17.) The commonly called firehouse dog's breed is _________. (dalmatian)"
              "\n18.) The name of the company that published the Mario Kart video game is ________. (nintendo)"
              "\n19.) The ______ gate bridge is a famous bridge located at San Francisco, CA. (golden)"
              "\n20.) Mariana's Trench is known to be the _______ trench worldwide. (deepest)"
              "\n21.) Kung Fu was originated in _____. (china)"
              "\n22.) The animal _______ is known for showing its colorful and beautiful tail. (peacock)"
              "\n23.) The world's fastest runner is _____ ____. (usain bolt)"
              "\n24.) The _______ Tunnel is the longest rail tunnel in the world. (channel)"
              "\n25.) The highest mountain in England is ___ Nevis (ben)"
              "\n26.) The Statue of Liberty was a gift from ______. (france)"
              "\n27.) The first tea bags were made of _____. (silk)"
              "\n28.) ______ is the capital of Bulgaria. (warsaw)")


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
              "\n16.) Kuala Lumpur is the capital of which country?. (malaysia)"
              "\n17.) What is the Capital of the United States?. (washington d.c)"
              "\n18.) What is the capital of the American state of Arizona?. (phoenix)"
              "\n19.) What cooking technique involves submerging egg in a liquid at a relatively low temperature?"
              ".(poaching)"
              "\n20.) What food is the leading source of salmonella poisoning?. (chicken)"
              "\n21.) What ingredient in fresh milk is eventually devoured by bacteria, causing the sour taste?. "
              "(lactose)"
              "\n22.) Which bird is a symbol for peace?. (dove)"
              "\n23.) What are baby kangaroo called?.(joey)"
              "\n24.) What animal is said to have 9 lives?. (cat)"
              "\n25.) Where is the Great Barrier Reef located?. (australia)"
              "\n26.) What sport does Cristiano Ronaldo play?. (football)"
              "\n27.) What is the name of the longest river in South America?. (amazon river)"
              "\n28.) In which ocean is the Bermuda Triangle located?. (atlantic ocean)")


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
              "\n16.) An octopus has five hearts. (F)"
              "\n17.) Brazil is the only country in the Americas to have the official language of Portuguese. (T)"
              "\n18.) The Channel Tunnel is the longest rail tunnel in the world. (F)"
              "\n19.) The highest mountain in England is Ben Nevis. (F)"
              "\n20.) The Statue of Liberty was a gift from France. (T)"
              "\n21.) The Great Wall of China is visible from space. (F)"
              "\n22.) The first tea bags were made of silk. (T)"
              "\n23.) Warsaw is the capital of Bulgaria. (F)"
              "\n24.) Flying in an aeroplane is statistically safer than driving in a car. (T)"
              "\n25.) Valletta is the capital of Cyprus. (F)"
              "\n26.) Ben Nevis is the tallest mountain in the UK. (T)"
              "\n27.) Strawberry is the only fruit with seeds on the outside. (T)"
              "\n28.) In the state Georgia, US is known for peaches. (T)")


    def ptoo_ans():
        print("Answers for 'Pick The Odd One' : "
              "\n1.) Which does not belong to the sequence? (5)"
              "\n2.) Which does not belong in the colors of Olympic ring? (orange)"
              "\n3.) Which is not part of the seven continents in the world? (greenland)"
              "\n4.) Which one of these countries is not like the other? (egypt)"
              "\n5.) Which is not an Ancient Structure? (stonehenge)"
              "\n6.) Which one of the following is not an old-fashioned name for a type of golf club? (dibber)"
              "\n7.) Pick the odd one (windows)"
              "\n8.) pick the odd one (intel 8088)"
              )

    def menu():
        print("Type \"1\" to reveal answers or type \"0\" to exit the program.")
        input_user = input("Enter here : ")
        while True:
            if input_user == "1":
                print("Please Select Test : "
                      "\n1 - Multiple Choice"
                      "\n2 - Fill in the blank"
                      "\n3 - identification"
                      "\n4 - True or False"
                      "\n5 - Pick the odd one"
                      "\n6 - Exit Program")
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

            elif input_user == "0":
                print("Thank You!")
                print("Project by Team Pink: (BES241) 12-10-2020 \n Carl Peñaranda \n Trixxie De Asis "
                      "\n Rian Magsino \n 1CPE ")
                exit()
                break
            elif input_user == " ":
                print("Invalid Input!")


    menu()
else:
    print("Project by Team Pink: (BES241) 12-10-2020 \n Carl Peñaranda \n Trixxie De Asis \n Rian Magsino \n 1CPE")
    print("Have a nice day!")
    exit()
