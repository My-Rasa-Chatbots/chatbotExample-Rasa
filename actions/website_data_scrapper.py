import re
import requests
from bs4 import BeautifulSoup
req = requests.get("https://www.marlabs.com/")
soup = BeautifulSoup(req.content, "html.parser")

# menu items
def getMenuItems():
    menu_element = soup.find('ul', class_= 'menu')
    menu_list = []
    link= menu_element.find_all('a')
    for line in link:
        
        title = line.text
        link = line.get('href')
        item = {"title":title, "url":link}
        menu_list.append(item)
    return menu_list



# office locations
def getAddresses():
    locations_element= soup.find('ul', class_='sp-tab__nav sp-tab__nav-tabs')
    address_element = soup.find('div', class_='sp-tab__tab-content')

    locations= locations_element.find_all('li')
    addresses = address_element.find_all('div', class_='sp-tab__tab-pane')

    address_list = []

    for (loc_ele,add_ele) in zip(locations, addresses):
        location = loc_ele.text.strip()

        if(location == "India"):
            india_address_list = add_ele.find_all('p')
            india_address_list[:] = map(lambda x: x.text, india_address_list)

            bangalore_L = list(filter(lambda element: ('Bangalore' in element) or ('Bengaluru' in element), india_address_list))
            mysore_L = list(filter(lambda element: ('Mysore' in element), india_address_list))
            kochi_L = list(filter(lambda element: ('Kochi' in element), india_address_list))

            bangalore = {"location":"Bangalore","address":bangalore_L}
            mysore = {"location":"Mysore", "address": mysore_L}
            kochi = {"location":"Kochi", "address": kochi_L}
            
            address_list.append({"location":location, "address":[bangalore,mysore,kochi]})
        else:
            address = add_ele.find('p').text
            # print(location+':'+address)
            address_list.append({"location":location, "address":address})
    # print (address_list[3])
    return address_list
# getAddresses()

# contact details
def getContacts():
    locations_element= soup.find('ul', class_='sp-tab__nav sp-tab__nav-tabs')
    address_element = soup.find('div', class_='sp-tab__tab-content')

    locations= locations_element.find_all('li')
    addresses = address_element.find_all('div', class_='sp-tab__tab-pane')

    contacts_list = []

    for (loc_ele,add_ele) in zip(locations, addresses):
        location = loc_ele.text.strip()

        if(location == "India"):
            india_contacts_list = add_ele.find_all('p')
            india_contacts_list[:] = map(lambda x: x.text, india_contacts_list)

            bangalore_L = list(filter(lambda element: ('Bangalore' in element) or ('Bengaluru' in element), india_contacts_list))
            mysore_L = list(filter(lambda element: ('Mysore' in element), india_contacts_list))
            kochi_L = list(filter(lambda element: ('Kochi' in element), india_contacts_list))

            bangalore_C = []
            for address_text in bangalore_L:
                
                tel = re.search(r'Tel: \+[\(\)\ \d]+', address_text)
                if(tel!=None):
                    tel = tel[0]
                print(tel)
                email = re.search(r'[\w]+\@[\w]+\.[\w]+', address_text)
                if(email!=None):
                    email = "Email: "+email[0]
                print(email)
                bangalore_C = bangalore_C + [tel+"\n"+email]
            bangalore = {"location":"Bangalore","address":bangalore_L}
            mysore = {"location":"Mysore", "address": mysore_L}
            kochi = {"location":"Kochi", "address": kochi_L}
            
            contacts_list.append({"location":location, "address":[bangalore,mysore,kochi]})
        else:
            address = add_ele.find('p').text
            # print(location+':'+address)
            contacts_list.append({"location":location, "address":address})
    # print (contacts_list[3])
    return contacts_list
# getContacts()