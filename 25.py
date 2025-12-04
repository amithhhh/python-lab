import csv

def create_students(stu_list):
    with open("mca.csv", "w", newline='') as csvfile:
        wob = csv.writer(csvfile)
        wob.writerow(["Name", "Gmail"])
        for name, email in stu_list:
            wob.writerow([name.title(), email])

students = [
    ("SUDEV C", "sudevc13@gmail.com"),
    ("AMAL M M", "amalmani2017@gmail.com"),
    ("HARKISHAN HEGDE", "harkishanhegde130@gmail.com"),
    ("SHAN A", "shanr1164@gmail.com"),
    ("ANJANA V P", "anjanavp231@gmail.com"),
    ("SAYOOJYA K", "sayoojyadhanes@gmail.com"),
    ("AMITH E K", "amithajith7025@gmail.com"),
    ("SHARUN T N", "sharuntn5@gmail.com"),
    ("Sumal", "eksumal@gmail.com"),
    ("Nandana Sathyan K", "nandanasathyan987@gmail.com"),
    ("ANJALI DINESAN", "anjalidinesan13@gmail.com"),
    ("Shafnas P P", "ftshaff@gmail.com"),
    ("NAFIA PV", "nafiasamad18@gmail.com"),
    ("Aiswarya Hareesh", "aiswaryaaiswarya633@gmail.com"),
    ("Fathimathul Hiba M", "fathimathulhibam1@gmail.com"),
    ("Souparnika Puthalath", "souparnikapreman108@gmail.com"),
    ("Sredha Lakshmi K", "sredhalakshmi99@gmail.com"),
    ("Hiba Abdul Jabbar", "hiba.abdul37@gmail.com"),
    ("Rana Muhammed", "rana.mxd@gmail.com"),
    ("Varsha Vinod", "varshavinod0331@gmail.com"),
    ("Hadiya Maryam Nasser", "hadiyamaryam980@gmail.com"),
    ("Huda Rasheed", "hudarasheednk0@gmail.com"),
    ("Keerthana M", "keerthanakichus22@gmail.com"),
    ("Rena Fathima", "fathimarena222@gmail.com"),
    ("Shubha", "shubhapaika03@gmail.com"),
    ("Santhwana P", "santhwanap279@gmail.com"),
    ("Anjana P K", "puthukkudianjana@gmail.com"),
    ("Sripaya V P", "sripaya2003@gmail.com"),
    ("Adithyan K", "adithya03n@gmail.com"),
    ("Aakamsh P M", "aakamshpm@gmail.com"),
    ("A Abhina", "abhinavenugopal054@gmail.com"),
    ("Sayana V K", "sayanachandran2005@gmail.com"),
    ("Fathimath Safwana C H", "fsafana982@gmail.com"),
    ("Muhamed Rishad T", "rishad4952@gmail.com")
]

create_students(students)
print("mca.csv written")
