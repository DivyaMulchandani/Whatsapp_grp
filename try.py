def Group_add(name):
    l=[]
    with open('registrationliist.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            if row[0] != "Name":
                l.append(row[0])

    option = webdriver.ChromeOptions()
    option.add_argument(r' --user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default')
    browser = webdriver.Chrome(options=option)
    browser.get("https://web.whatsapp.com/")
    time.sleep(20)
    search_box = browser.find_element(By.XPATH, '//input[@title="Search or start new chat"]')
    search_box.send_keys(name)
    time.sleep(5)
    user = browser.find_element(By.XPATH, '//span[@title="{}"]'.format(name))
    user.click()
    time.sleep(5)
    msg_box = browser.find_element(By.XPATH, '//div[@title="Type a message"]')
    for i in l:
        msg_box.send_keys(i+Keys.ENTER)
        time.sleep(1)
    browser.quit()