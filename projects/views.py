from django.shortcuts import render


def index(request):
    data = {
        "projectInfo": {
            "1": {
                "firstLine": "Microsoft Teams Engage",
                "description": "Developed a Microsoft Teams Clone App as part of Microsoft Engage 2021. The app is available for download and use.",
                "github": "https://github.com/anuragyadav19150/ms_engage_2021",
                "image": "../static/projects/ms.jpg",
                "techStack": "Flutter, Dart, Android Studio, Agora Video Service",
                "descriptionNew": "Built a Microsoft Teams Clone App during Microsoft Engage 2021. Users can download, install, and run this application. To get started, create an account and obtain an App ID from Agora. Sign up on agora.io, navigate to Projects > Project List in the dashboard, and copy your App ID. This ID is required to launch the app."
            },
            "2": {
                "firstLine": "Shopify - Full Stack",
                "description": "Designed and developed a fully functional shopping website with a database management system.",
                "github": "https://github.com/anuragyadav19150/Shopify_DBMS",
                "image": "../static/projects/shop.png",
                "techStack": "React, Node.js, MySQL",
                "descriptionNew": "Built a shopping website with full-stack development, integrating a database system for user and product management. Features include login, signup, and an admin panel for managing users and product information."
            },
            "3": {
                "firstLine": "Traffic Rule Violation Detection",
                "description": "Developed a computer vision model to detect traffic violations like overspeeding and red light crossing.",
                "github": "https://github.com/anuragyadav19150/Traffic-Rule-Violation-detection",
                "image": "../static/projects/ms.png",
                "techStack": "Python, Computer Vision",
                "descriptionNew": "Designed a computer vision-based system to automatically detect traffic violations such as not wearing helmets, overspeeding, and jumping red lights. This project aims to improve road safety and ensure efficient enforcement of traffic rules."
            },
            "4": {
                "firstLine": "Color Switch",
                "description": "Developed a clone of the popular game Color Switch using JavaFX with object-oriented programming principles.",
                "github": "https://github.com/anuragyadav19150/apFinal",
                "image": "../static/projects/ms.png",
                "techStack": "Java, JavaFX",
                "descriptionNew": "Recreated the famous Color Switch game using JavaFX. This project heavily utilizes OOP principles like inheritance and encapsulation. We also designed UML and use case diagrams to plan and visualize the final product effectively."
            },
            "5": {
                "firstLine": "Dream Team Creator",
                "description": "Developed a machine learning model that predicts a winning fantasy team using online data.",
                "github": "https://github.com/anuragyadav19150/Machine_Learning_Final_Project",
                "image": "../static/projects/ms.png",
                "techStack": "Python, Machine Learning",
                "descriptionNew": "Created a predictive model to generate the best fantasy team by analyzing online data. The model considers player performance history, opponent statistics, home ground advantage, weather conditions, and other factors to optimize team selection."
            },
            "6": {
                "firstLine": "Gram Vision",
                "description": "Developed a mobile app for village communities using Flutter and Google Firebase.",
                "github": "https://github.com/anuragyadav19150/GramVision",
                "image": "../static/projects/ms.png",
                "techStack": "Flutter, Dart, Android Studio, Google Firebase",
                "descriptionNew": "Built a community-based mobile app to help villagers access announcements, policies, file complaints, and trade products. The app features a built-in messaging system, allowing buyers and sellers to communicate seamlessly."
            },
            "7": {
                "firstLine": "RISC-V Assembler & Simulator",
                "description": "Built a C++ program to simulate a subset of the RISC-V instruction set architecture (RV32).",
                "github": "https://github.com/anuragyadav19150/RISC-V-Assembler-Simulator",
                "image": "../static/projects/ms.png",
                "techStack": "C++, RISC-V",
                "descriptionNew": "Developed a tool in C++ that converts RISC-V assembly code into 32-bit binary instructions. Also created a 5-stage simulator (IF, ID, EX, MEM, WB) for RV32 ISA that executes and debugs these instructions."
            }
        },
        "skills": {
            "1": "C++",
            "2": "Python",
            "3": "Java",
            "4": "JavaScript",
            "5": "AWS",
            "6": "React",
            "7": "Node.js",
            "8": "Django",
            "9": "Django REST Framework",
            "10": "Flask",
            "11": "MongoDB",
            "12": "MySQL",
            "13": "SQLite",
            "14": "AWS Lambda",
            "15": "Git / GitHub",
            "16": "GitHub Actions",
            "17": "Postman API",
            "18": "JWT (JSON Web Tokens)",
            "19": "Ansible",
            "20": "Datadog",
            "21": "HTML/CSS",
            "22": "Bootstrap",
            "23": "Redux",
            "24": "Computer Vision"
        },
        "firstLine": "Hey, I'm Anurag Yadav",
        "description": "Software Development Engineer - II at Expedia Group | Ex-Cloud Labs, Iuraverse | IIIT Delhi (ECE) | Python | C++ | AWS | React | Django | Ansible | Datadog",
        "amazing": {
            "1": {
                "type": "Blog",
                "title": "Django Vercel Deployment",
                "description": "To deploy your Django Frontend on Free platform Vercel you can follow this.",
                "link": "https://docs.google.com/document/d/10T-cco1ve1iCJA-WsEt_q_de7PvIGd8ovv8Pkj-q3vw/edit?usp=sharing"
            },
            "2": {
                "type": "Time Pass",
                "title": "relieve stress",
                "description": "Here are 9 websites to help you relieve stress and avoid boredom at work:",
                "link": "https://twitter.com/MakadiaHarsh/status/1599753120133058562"
            },
            "3": {
                "type": "Time Pass",
                "title": "Practice Web Dev",
                "description": "13 Apps to build to practice your HTML, CSS, and Javascript checkout",
                "link": "https://twitter.com/csaba_kissi/status/1599330144820383744"
            },
            "4": {
                "type": "Time Pass",
                "title": "Design resource",
                "description": " Top 10 Resources for Design , absolutely FREE for use , checkout and implement🚀",
                "link": "https://twitter.com/_vargaalex/status/1607018293805699072"
            },
            "5": {
                "type": "Time Pass",
                "title": "Google Chrome extensions",
                "description": "10 Google Chrome extensions that'll make you a super productive developer.",
                "link": "https://twitter.com/csaba_kissi/status/1604840475512524803"
            },
            "6": {
                "type": "Time Pass",
                "title": "CSS generators",
                "description": "some of best CSS generators that can save you from writing CSS code 🧵:",
                "link": "https://twitter.com/Prathkum/status/1605913312591548416"
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
