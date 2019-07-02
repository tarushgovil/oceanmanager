#imports all necessary modules and libraries
import urllib.request as urllib2
import json
import csv 
import pandas as pd
import numpy as np
#opens the url containing the dataset
url = urllib2.urlopen('https://portal.emsa.europa.eu/portlet-public/rest/inspection/getPublicInspections.json?_dc=shipImoNumber=9241061&shipName=&flags=&shipTypes=&grossTonnageMin=&grossTonnageMax=&ageMin=&ageMax=&ismCompanyImoNumber=&ismCompanyName=&classificationSocieties=&recognizedOrganizations=&periodMin=28%2F06%2F2016&periodMax=28%2F06%2F2019&pscInspectionRegime=1&inspectionTypes=&portStates=&ports=&inspectionResults=&deficienciesNumberMin=&deficienciesNumberMax=&deficiencyAreas=&detentionDurationMin=&detentionDurationMax=&page=1&start=0&limit=20') 
#loads the data in json format
json_data = json.load(url)
results = json_data['results']
#opens the csv file on which we wish to write
with open('/Users/tarushgovil/Desktop/Task2OceanManagerExcelsheet.csv','w') as f: 
    fieldnames = ['id','imoNumber','shipName','id','code','description','abbreviation','performanceType','imoAudited','pmou','subsidiary','countryDescription','shipFlagRatifiesAllConventions','certifiers','shipTypeDescription','age','inspectionDate','type','description','effectDate','expiryDate','active','id','memeberStateDescription','portName','nDeficiencies','portAndMS','resultsDesc','ndeficiencies']
    #establishes object parameter as thewriter
    thewriter = csv.writer(f)
    #writes the top row of the table 
    thewriter.writerow(fieldnames) 
    #iterates over the keys in the results dictionary
    for key in results: 
#we wish to write row by row for each dictionary in results as each key contains id,imoNumer,etc. upto ndeficiencies and we want to write it only once for each key in results
        for i in range(1):
            #since we write only one row each time we use the function writerow
            thewriter.writerow([key['id'],key['imoNumber'],key['shipName'],key['flag']['id'],key['flag']['code'],key['flag']['description'],key['flag']['abbreviation'],key['flag']['performanceType'],key['flag']['imoAudited'],key['flag']['pmou'],key['flag']['subsidiary'],key['flag']['countryDescription'],key['flag']['shipFlagRatifiesAllConventions'],key['flag']['certifiers'],key['shipTypeDescription'],key['age'],key['inspectionDate'],key['inspectionType']['type'],key['inspectionType']['description'],key['inspectionType']['effectDate'],key['inspectionType']['expiryDate'],key['inspectionType']['active'],key['inspectionType']['id'],key['memberStateDescription'],key['portName'],key['nDeficiencies'],key['portAndMS'],key['ndeficiencies']]) 
    

