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
    data={
    "projectInfo": {
        "1": {
            "firstLine": "Shopify - Full stack",
            "description": "Designed a system that maintains the database of a Shopping website along with its\r\nFully Functional website.",
            "github": "https://github.com/anuragyadav19150/Shopify_DBMS",
            "image": "NA"
        },
        "2": {
            "firstLine": "Traffic Rule Violation Detection",
            "description": "We detect traffic violations like over-speeding and crossing the Red light Signal using\r\ncomputer vision and Image processing.",
            "github": "https://github.com/anuragyadav19150/Traffic-Rule-Violation-detection",
            "image": "NA"
        },
        "3": {
            "firstLine": "Color Switch",
            "description": "Made a clone of the famous game Color Switch with JavaFX in JAVA",
            "github": "https://github.com/anuragyadav19150/apFinal",
            "image": "NA"
        },
        "4": {
            "firstLine": "Dream Team Creator",
            "description": "We made a model that will make a team which will win the tournament by using the\r\ndata present online",
            "github": "https://github.com/anuragyadav19150/Machine_Learning_Final_Project",
            "image": "NA"
        },
        "5": {
            "firstLine": "GRAM VISION",
            "description": "Developing a user-friendly, Easy to use Mobile App, using Flutter, Dart, and\r\nGoogle Firebase(for backend), for the people of a village.",
            "github": "https://github.com/anuragyadav19150/GramVision",
            "image": "NA"
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
    "description": "Expert at Codeforces | Ex-SDE Intern'22 @Expedia Group | Software Developer @ Cloud Labs | ECE @ IIIT Delhi."
}
    

    context = {
    'projectInfo':data["projectInfo"],
        'skills':data["skills"],
        'firstLine':data["firstLine"],
        'description':data["description"],
}

    return render(request,'index.html',context=context)

      

   
