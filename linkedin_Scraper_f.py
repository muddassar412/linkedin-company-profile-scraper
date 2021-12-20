from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas




email = input("enter email address : ")
password = input("enter password : ")

file_name = input("enter file name for input '(without xlsx)': ")
file_link = (file_name+".xlsx")

file_n = input("enter file name for output, 'not same as input '(without xlsx)': ")
file_l = (file_n+".xlsx")
workbook.close()
driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.linkedin.com/")






def scrape(link):
        driver.get(link)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        
        try:
                names=soup.find("div",{"class":"artdeco-entity-lockup__title ember-view"})
                name=names.text
        except:
                name="NO"
        try:
                desination=soup.find("span",{"data-anonymize" : "industry"})
                industry=desination.text
        except:
                industry="NO"

        try:
                dscm=soup.find("a",{"class" : "ember-view link-without-visited-and-hover-state"})
                decisionMakersCount =dscm.text
        except:
                decisionMakersCount ="NO"


        try:
                employee=soup.find("dt",{"class" : "t-14 t-bold"})
                employees=employee.text
        except:
                employees="NO"

        try:
                revenu=soup.find("span",{"data-anonymize" : "revenue"})
                revenue =revenu.text
        except:
                revenue="NO"

        try:
                loc=soup.find("div",{"class" : "t-12 t-black--light"})
                location =loc.text
        except:
                location="NO"

        try:
                web=soup.find("a",{"class" : "ember-view artdeco-button view-website-link artdeco-button--2 artdeco-button--secondary artdeco-button--muted ml2"})
                website =web['href']
        except:
                website="NO"

        try:
                lo=soup.find("img",{"class" : "ember-view account-top-card__lockup-photo elevation-0dp"})
                logolink = lo['src']
        except:
                logolink="NO"


        try:
                m6=soup.find("div",{"class" :"t-14 t-bold"})
                sixmonth =m6.text
        except:
                sixmonth="NO"

        try:
                y1=soup.find_all("div",{"class" :"t-14 t-bold"})
                oneyear =y1[1].text
        except:
                oneyear="NO"

        try:
                y2=soup.find_all("div",{"class" :"t-14 t-bold"})
                twoyear =y2[2].text
        except:
                twoyear="NO"



        try:
                hed=soup.find("dd",{"class" :"company-details-panel__content company-details-panel-headquarters t-black--light"})
                headquarter =hed.text
                info = headquarter.split(",")

        except:
                headquarter="NO"
        try:
                address = info[0]
        except:
                address = "NO"
        try:
                city = info[1]
        except:
                city = "NO"


                ##############################################



        try:
                empsrurl = "https://www.linkedin.com/sales/search/people/list/employees-for-account/"
                employeeSearchUrl = empsrurl+companyid
        except:
                employeeSearchUrl = "NO"

        try:
                dcm = "?seniority=6%2C7%2C8"
                decisionMakersSearchUrl = employeeSearchUrl + dcm
        except:
                decisionMakersSearchUrl = "NO"

        try:
                curl = "https://www.linkedin.com/company/"
                linkedInCompanyUrl = curl+companyid
        except:
                decisionMakersSearchUrl = "NO"

        try:
                salesNavigatorCompanyUrl = link
        except:
                salesNavigatorCompanyUrl = "NO"
 
        print (name,industry, employees, revenue,website,description,headquarter,sixmonth, oneyear, twoyear,location,address,city,postalcode,country, salesNavigatorCompanyUrl, companyid, decisionMakersCount, logolink,employeeSearchUrl,decisionMakersSearchUrl)
#---------------------appand record -------------------------------------
 


df = pd.read_excel(file_link)

##url = df[df.columns[0]].count()
for row in df.iterrows():

                scrape(url)


df=pd.DataFrame(record,columns=['name','industry', 'employees', 'revenue','website','description','headquarter','sixmonth', 'oneyear', 'twoyear','location','address','city','postalcode','country', 'salesNavigatorCompanyUrl', 'companyid', 'decisionMakersCount', 'logolink','employeeSearchUrl','decisionMakersSearchUrl']) 

driver.close()       
