import time
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("DesafioTunts-6ba8226cb26c.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Engenharia de Software – Desafio Augusto Cesar T. Ferreira").sheet1



classes = 60  #--- Number of classes

for row in range(4,28):
    missedClasses = sheet.cell(row,3).value
    test1 = sheet.cell(row,4).value
    test2 = sheet.cell(row,5).value
    test3 = sheet.cell(row,6).value

    #--- Grades and presence in classes
    average = (float(test1) +float(test2) +float(test3)) / 3
    missedPercentage = float(missedClasses) / float(classes)
    naf = 0

    #--- Situations for students approval
    if (missedPercentage) > 0.25:               #--- Not approved by absences
        sheet.update_cell(row,7, "Reprovado por faltas")
        
    elif average < 50:                          #--- Disapproved for grades
        sheet.update_cell(row,7, "Reprovado por nota")
        
    elif average >= 50 and average < 70:          #--- Final exam
        sheet.update_cell(row,7, "Exame final")
        naf = float(100 - average)
        
    else:                                       #--- Approved student
        sheet.update_cell(row,7, "Aprovado")
        
    sheet.update_cell(row,8, naf)               #--- Grade needed for approval
    time.sleep(3)
