from django.shortcuts import render


def index(request):
    # print("check 1")

    # projectss=Projects.objects.all()
    # projectInfo={}

    # for x in projectss:
    #     projectInfo[x.priority]={"firstLine":x.firstLine,"description":x.description,"github":x.github,"image":x.images}

    # print(projectInfo)
    # projectInfo = OrderedDict(sorted(projectInfo.items()))

    # infos=Info.objects.all()
    # skills={}

    # for x in infos:
    #     skills[x.priority]=x.skill

    # print(skills)
    # skills = OrderedDict(sorted(skills.items()))

    # abouts=About.objects.all()
    # firstLine=""
    # description=""

    # for x in abouts:
    #     if x.priority==1:
    #         firstLine=x.firstLine
    #         description=x.description
    #         break
    # print("sending")
    data = {
        "projectInfo": {
            "1": {
                "firstLine": "Microsoft Teams Engage",
                "description": "I made this Microsoft Teams Clone App in Microsoft Engage 2021.You can download and run this app.",
                "github": "https://github.com/anuragyadav19150/ms_engage_2021",
                "image": "../static/projects/ms.jpg",
                "techStack":"Futter , Dart , Android Studio , Agora video service",
                "descriptionNew": "I made this Microsoft Teams Clone App in Microsoft Engage 2021.You can download and run this app. Create an Account and Obtain an App ID To build and run the sample application, first obtain an app ID: Create a developer account at agora.io. Once you finish the sign-up process, you are redirected to the dashboard. Navigate in the dashboard tree on the left to Projects > Project List. Copy the app ID that you obtain from the dashboard into a text file. You will use this when you launch the app.",
 
            },
            "2": {
                "firstLine": "Shopify - Full stack",
                "description": "Designed a system that maintains the database of a Shopping website along with its\r\nFully Functional website.",
                "github": "https://github.com/anuragyadav19150/Shopify_DBMS",
                "image": "../static/projects/shop.png",
                "techStack":"React , Node , MySql ",
                "descriptionNew": "Designed a system that maintains the database of a Shopping website along with its\r\nFully Functional website. We ahave added many features like Login , signup and admin control where admin can control every thing fromuser info to product infomation.",
                

            },
            "3": {
                "firstLine": "Traffic Rule Violation Detection",
                "description": "We detect traffic violations like over-speeding and crossing the Red light Signal using\r\ncomputer vision and Image processing.",
                "github": "https://github.com/anuragyadav19150/Traffic-Rule-Violation-detection",
               "image": "../static/projects/ms.png",
                "techStack":"Python , computer vision",
                "descriptionNew": "a traffic violation system using Computer vision is highly needed as these systems can act as an efficient tool to reduce traffic violations and penalise violators. So in this project, we are trying to develop a computer vision model that can detect violations of basic traffic rules like not wearing a helmet, overspeeding, and jumping red lights",
                

            },
            "4": {
                "firstLine": "Color Switch",
                "description": "Made a clone of the famous game Color Switch with JavaFX in JAVA.",
                "github": "https://github.com/anuragyadav19150/apFinal",
                "image": "../static/projects/ms.png",
                "techStack":"Java , Java FX",
                "descriptionNew": "Made a clone of the famous game Color Switch with JavaFX in JAVA. We have used many oop's features to make this project, We also have made the uml diagram so that we can plan how we are going to do this project and also a use case diagram so that we have a clear picture of the final product in our mind hope you like it!",
                

            },
            "5": {
                "firstLine": "Dream Team Creator",
                "description": "We made a model that will make a team which will win the tournament by using the\r\ndata present online",
                "github": "https://github.com/anuragyadav19150/Machine_Learning_Final_Project",
                "image": "../static/projects/ms.png",
                "techStack":"Pyhton , Machine Learning ",
                "descriptionNew": "The main focus of this project is to create a winning fantasy team by looking at the huge amount of data present online and predicting which team will win by analyzing player’s performance history, statistics against the opponent team, home ground status, weather impact, and many other factors and attempt to predict the outcome",
                
            },
            "6": {
                "firstLine": "GRAM VISION",
                "description": "Developing a user-friendly, Easy to use Mobile App, using Flutter, Dart, and\r\nGoogle Firebase(for backend), for the people of a village.",
                "github": "https://github.com/anuragyadav19150/GramVision",
                "image": "../static/projects/ms.png",
                "techStack":"Futter , Dart , Android Studio , Google fire base",
                "descriptionNew": "Developing a user-friendly, Easy to use Mobile App, using Flutter, Dart, and\r\nGoogle Firebase(for backend), for the people of a village. Made an app Panchayat using Flutter, Dart and Google Firebase. It is centered around people of villages where they can get info about latest announcements & policies, file personal and general complaints, sell/buy products and contact buyer/seller using the inbuilt messaging app and many other features.",
 
            }
        },
        "skills": {
            "1": "C++",
            "2": "Python",
            "3": "Java",
            "4": "React",
            "5": "Django",
            "6": "Django REST Framework",
            "7": "JSON Web Token (JWT)",
            "8": "AWS Lambda",
            "9": "Postman API",
            "10": "Flutter",
            "11": "MySql",
            "12": "MongoDB",
            "13": "Sqlite",
            "14": "Html",
            "15": "Css",
            "16": "JavaScript",
            "17": "Flask",
            "18": "Git",
            "19": "Github",
            "20": "Node"
        },
        "firstLine": "HEY, I'M ANURAG YADAV",
        "description": "Expert at Codeforces | Ex-SDE Intern'22 @Expedia Group | Software Developer @ Cloud Labs | ECE @ IIIT Delhi.",
        "amazing": {
            "1": {
                "type": "Blog",
                "title": "Django Vercel Deployment",
                "description": "To deploy your Django Frontend on Free platform Vercel you can follow this.",
                "link":"https://docs.google.com/document/d/10T-cco1ve1iCJA-WsEt_q_de7PvIGd8ovv8Pkj-q3vw/edit?usp=sharing"
            },
            "2": {
                "type": "Time Pass",
                "title": "relieve stress",
                "description": "Here are 9 websites to help you relieve stress and avoid boredom at work:",
                "link":"https://twitter.com/MakadiaHarsh/status/1599753120133058562"
            },
            "3": {
                "type": "Time Pass",
                "title": "Practice Web Dev",
                "description": "13 Apps to build to practice your HTML, CSS, and Javascript",
                "link":"https://twitter.com/csaba_kissi/status/1599330144820383744"
            },
            "4": { 
                "type": "Time Pass",
                "title": "Design resource",
                "description": "My Top 10 FREE Resources for Design 🚀",
                "link":"https://twitter.com/_vargaalex/status/1607018293805699072"
            },
            "5": { 
                "type": "Time Pass",
                "title": "Google Chrome extensions",
                "description": "10 Google Chrome extensions that'll make you a super productive developer.",
                "link":"https://twitter.com/csaba_kissi/status/1604840475512524803"
            },
            "6": { 
                "type": "Time Pass",
                "title": "CSS generators",
                "description": "9 CSS generators that can save you from writing CSS code 🧵:",
                "link":"https://twitter.com/Prathkum/status/1605913312591548416"
            }
        }
    }

    context = {
        'projectInfo': data["projectInfo"],
        'skills': data["skills"],
        'firstLine': data["firstLine"],
        'description': data["description"],
        'amazing': data["amazing"]
    }

    return render(request, 'index.html', context=context)
