import tkinter as tk
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

def delay(x):
    time.sleep(x)

def Find_A_House(Location,range):
    l = len(range)
    range=range[:l - 1] + "000"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.redfin.com/")
    delay(5)
    driver.find_element("id", "search-box-input").send_keys(f"{Location}")
    delay(5)
    driver.find_element('css selector', "#tabContentId0 > div > div > form > div > button").click()
    delay(5)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div").click()
    # Price
    delay(10)
    driver.find_element("css selector","#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div > div.Flyout.standard.v83.position-right.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__container > div > div > div.flex.align-center.inputRangeAfterHistogram > span:nth-child(3) > span > div > input").send_keys(f"{range}")
    delay(3)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div > div.Flyout.standard.v83.position-right.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__footer.flex.align-center > div > button.button.Button.primary").click()
    delay(3)
    # SELECT hometype
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.default.desktopExposedPropertyTypeFilter.showDesktopFilterMenuRedesign").click()
    delay(2)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedPropertyTypeFilter.showDesktopFilterMenuRedesign > div.Flyout.standard.v83.position-left.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__container > div > div > div > div > div > div > div:nth-child(1)").click()
    # SELECT HOUSE

    delay(2)
    driver.find_element('xpath',"/html/body/div[1]/div[9]/div[2]/div[2]/div[2]/div/div/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/button[2]/span").click()

    delay(2)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedBedsAndBathsContainer.showDesktopFilterMenuRedesign").click()
    # HOUSE DONE
    delay(5)
    driver.find_element('xpath',"/html/body/div[1]/div[9]/div[2]/div[2]/div[2]/div/div/div[1]/form/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[6]").click()
    delay(2)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedBedsAndBathsContainer.showDesktopFilterMenuRedesign > div.Flyout.standard.v83.position-left.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__footer.flex.align-center > div > button.button.Button.primary").click()
    delay(20)

def create_lead_salesforce():
    # Get Web Chrome driver
    driver = webdriver.Chrome()

    # Maximize Driver Window
    driver.maximize_window()

    # Open our targeted webpage on driver
    driver.get("https://www.salesforce.com/in/")
    delay(2)

    # Shadow element Travesing
    shadow_root0=driver.find_element('css selector',"hgf-c360nav[locale='in']").shadow_root
    shadow_root0.find_element('css selector', ".utility-icons-items.login").click()
    delay(1)
    shadow_root1=shadow_root0.find_element('css selector',"hgf-c360login[aria-haspopup='true']").shadow_root
    delay(2)

    # Get login Page
    shadow_root1.find_element('css selector',"hgf-popover:nth-child(2)>div:nth-child(2)>div:nth-child(2)>a:nth-child(2)>h4:nth-child(1)").click()
    delay(5)

    # Enter username in Login Page
    driver.find_element('xpath'," //input[@id='password']").send_keys('Saurabh@123')
    delay(2)

    #Enter Password in Login Page
    driver.find_element('xpath', "//input[@id='username']").send_keys('radkesaurabh1999-lem3@force.com')
    delay(2)

    # Try to Login
    driver.find_element('xpath',"//input[@id='Login']").click()
    delay(10)
    # After Succesfull Login go to Leads Section
    driver.find_element('xpath', "//span[@aria-description='Show more My Leads records']").click()
    delay(4)
    driver.find_element('xpath', "//div[@title='New']").click()
    # ADD getails to create Leads
    wait = WebDriverWait(driver,10)
    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_lead___012000000000000aaa___full___create___recordlayout2/records-record-layout-block/slot/records-record-layout-section[1]/div/div/div/slot/records-record-layout-row[2]/slot/records-record-layout-item[1]/div/span/slot/records-record-layout-input-name/lightning-input-name/fieldset/div/div/div[2]/lightning-input/div/div/input"))).send_keys("Max")
    delay(1)
    driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_lead___012000000000000aaa___full___create___recordlayout2/records-record-layout-block/slot/records-record-layout-section[1]/div/div/div/slot/records-record-layout-row[2]/slot/records-record-layout-item[1]/div/span/slot/records-record-layout-input-name/lightning-input-name/fieldset/div/div/div[4]/lightning-input/div[1]/div/input").send_keys("Nye")
    delay(1)
    driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_lead___012000000000000aaa___full___create___recordlayout2/records-record-layout-block/slot/records-record-layout-section[1]/div/div/div/slot/records-record-layout-row[3]/slot/records-record-layout-item[2]/div/span/slot/records-record-layout-base-input/lightning-input/div[1]/div/input").send_keys('Workplete')
    delay(1)
    # Click to generate Lead
    driver.find_element('xpath', "//button[@name='SaveEdit']").click()
    delay(10)

def log_a_call_salesforce():
    # Get Web Chrome driver
    driver = webdriver.Chrome()

    # Maximize Driver Window
    driver.maximize_window()

    # Open our targeted webpage on driver
    driver.get("https://www.salesforce.com/in/")
    delay(2)

    # Shadow element Travesing
    shadow_root0=driver.find_element('css selector',"hgf-c360nav[locale='in']").shadow_root
    shadow_root0.find_element('css selector', ".utility-icons-items.login").click()
    delay(1)
    shadow_root1=shadow_root0.find_element('css selector',"hgf-c360login[aria-haspopup='true']").shadow_root
    delay(2)

    # Get login Page
    shadow_root1.find_element('css selector',"hgf-popover:nth-child(2)>div:nth-child(2)>div:nth-child(2)>a:nth-child(2)>h4:nth-child(1)").click()
    delay(5)

    # Enter username in Login Page
    driver.find_element('xpath'," //input[@id='password']").send_keys('Saurabh@123')
    delay(2)

    #Enter Password in Login Page
    driver.find_element('xpath', "//input[@id='username']").send_keys('radkesaurabh1999-lem3@force.com')
    delay(2)

    # Try to Login
    driver.find_element('xpath',"//input[@id='Login']").click()
    delay(10)

    # After Succesfull Login gor to Leads Section
    driver.find_element('xpath',"//span[@aria-description='Show more My Leads records']").click()
    delay(10)

    # Select the desired lead to log a Call
    driver.find_element('xpath',"//a[@title='James Wheel']").click()
    delay(5)

    # Log a call
    driver.find_element('xpath',"//span[@value='LogACall']").click()


    # Enter text message nedd to send with Log
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div[1]/section/div[2]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div[1]/section/div/section/div/div/div/div/div/div[2]/div[1]/div/div/div/div/textarea"))).send_keys("Are you looking to by 100 widgets")
    delay(3)

    # Finally Send the LOG
    driver.find_element(By.XPATH,"//button[@class='slds-button slds-button--brand cuf-publisherShareButton uiButton']").click()
    delay(20)




root=tk.Tk() # use to create new chat nav
root.geometry('350x450+30+400')
def getresult(message):
    arr=message.split(" ")
    if arr[0]=="Find":
        textarea.insert("end", "\nBot : Processing.... ")
        Location=arr[5]
        range=arr[-1]
        Find_A_House(Location,range)
    elif arr[0]=="Add":
        textarea.insert("end", "Bot : Processing.... ")
        create_lead_salesforce()
    elif arr[0]=="Log":
        textarea.insert("end", "Bot : Processing.... ")
        log_a_call_salesforce()
    else:textarea.insert("end", "Invalid Input")


def botReply():
    question=query.get()
    textarea.insert("end","\nYou : "+question)
    query.delete(0, "end")
    getresult(question)



root.title("Chat Bot for new prompt")
root.config(bg="aquamarine")
# Headear Logo
head=tk.PhotoImage(file='head1.png')
Insert_head=tk.Label(root,image=head)
Insert_head.config(bg='aquamarine')
Insert_head.pack()

#Frame[Conatiner for message]
Centeral_frame=tk.Frame(root)
Centeral_frame.pack()
scrol=tk.Scrollbar(Centeral_frame)
scrol.pack(side='right')

#Text area
textarea=tk.Text(Centeral_frame,font=('time new roman',10,'bold'),height=10,yscrollcommand=scrol.set)
textarea.pack(side='left')
scrol.config(command=textarea.yview)

#Enter message
query=tk.Entry(root,font=('verdana',10,'bold'),width=30)
query.pack(pady=15)

#Buttom
btn = tk.Button(root, text = 'Send !', bd = '5',command = botReply)
btn.pack()
root.mainloop() # use to hold our