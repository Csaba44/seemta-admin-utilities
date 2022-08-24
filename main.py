
import time
import openpyxl
from datetime import datetime
import time, os


print("Version 3.0")

dutyperc = 0
asegit = 0
setarmor = 0
fix = 0
oilchange = 0
startTime = 0
endTime = 0


try:
    workbook = openpyxl.load_workbook(filename="./admin.xlsx")
    sheet = workbook.active
    sheet["A1"] = "MKLS ADMIN SHEET"
    sheet["A4"] = "Dutypercek:"
    sheet["A6"] = "Asegit használat:"
    sheet["A8"] = "Setarmor használat:"
    sheet["D4"] = "Fixveh használat:"
    sheet["D6"] = "Oilchange használat:"

    dutyperc = sheet.cell(row = 4, column = 2).value
    asegit = sheet.cell(row = 6, column = 2).value
    setarmor = sheet.cell(row = 8, column = 2).value
    fix = sheet.cell(row = 4, column = 5).value
    oilchange = sheet.cell(row = 6, column = 5).value

    if dutyperc == None:
        dutyperc = 0
    elif asegit == None:
        asegit = 0
    elif setarmor == None:
        setarmor = 0
    elif fix == None:
        fix = 0
    elif oilchange == None:
        oilchange = 0

    print("Percek: " + str(dutyperc))
    print("Asegit: " + str(asegit))
    print("Setarmor: " + str(setarmor))
    print("fix: " + str(fix))
    print("oilchange: " + str(oilchange))
    workbook.save(filename="./admin.xlsx")
except:
    print("FAULT: admin.xlsx not found. Create admin.xlsx at the MTA Log folder. ex.: D:\mta-root-directory\MTA\logs")

#Set the filename and open the file
filename = 'console.log'
file = open(filename,'r', encoding='utf-8')

#Find the size of the file and move to the end
st_results = os.stat(filename)
st_size = st_results[6]
file.seek(st_size)

while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        print(line) # already has newline
        if "[" in line and "]" in line and "[Output]" in line:
            timeLine = line.split("[")
            timeLine = timeLine[1].split("]")
            timeLine = timeLine[0]
            print(timeLine)
        
        if "Mkls megjavította a járművedet" in line:
            fix += 1
            print("fixek: " + str(fix))
        elif "Mkls kicserélte a járműved olaját" in line:
            oilchange += 1
            print("oilchangek: " + str(oilchange))
        elif "Sikeresen felsegítetted a kiválasztott játékost" in line:
            asegit += 1
            print("asegitek: " + str(asegit))
        elif "Mkls" in line and "páncélját" in line:
            setarmor += 1
            print("setarmorok: " + str(setarmor))
        elif "[AdminDuty]: Mkls adminszolgálatba lépett." in line or "[Infobox]: Mkls adminszolgálatba lépett." in line:
            startTime = timeLine
            print("started duty: " + timeLine)
        elif "[AdminDuty]: Mkls kilépett az adminszolgálatból." in line:
            endTime = timeLine

            print("end: " + endTime)
            t1 = datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
            t2 = datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
            delta = t2 - t1
            dutyperc += delta.total_seconds()/60
            print("dutypercek: " + str(dutyperc))


        workbook = openpyxl.load_workbook(filename="./admin.xlsx")
        sheet = workbook.active
        sheet["B4"] = dutyperc
        sheet["B6"] = asegit
        sheet["B8"] = setarmor

        sheet["E4"] = fix
        sheet["E6"] = oilchange

        workbook.save(filename="./admin.xlsx")
