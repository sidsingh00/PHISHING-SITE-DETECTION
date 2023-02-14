import requests as re


import os

'''URL="https://www.kaggle.com"

response = re.get(URL)'''

'''print("response -->", response, "\ntype -->", type(response))

print("text -->", response.text, "\ncontent --> ", response.content, "\nstatus_code --> ", response.status_code)

if response.status_code != 200:

    print("HTTP connection is not successful! Try again.")

else:

    print("HTTP connection is successful!")'''

'''soup = BeautifulSoup (response.content, "html.parser")

print("title with tags -->", soup.title, "\ntitle without tags -->", soup.title.text)

for link in soup.find_all("link"):

    print(link.get("href"))

print(soup.get_text())
for link in soup.find_all("link"):
    print (link.get("href"))

print (soup.get_text())
'''

folder = "mini_dataset"

if not os.path.exists(folder):
    os.mkdir(folder)
def scrape_content (URL):
    response = re.get(URL)
    if response.status_code == 200:
        print("HTTP connection is successful for the URL:", URL)
        return response
    else:
        print("HTTP connection is NOT successful! for the URL:", URL)
        return None

path = os.getcwd() + "/" + folder

def save_html(to_where, text, name):

    file_name = name + ".html"
    with open(os.path.join(to_where, file_name), "w") as f:
        f.write(text)
'''
test_text= response.text
save_html(path, test_text, "example")'''
URL_list = [
    "https://www.kaggle.com",
    "https://stackoverflow.com",
    "https://www.researchgate.net",
    "https://www.python.org",
    "https://www.w3schools.com",

    "https://github.com"

]
def create_mini_dataset(to_where, URL_list):

    for i in range(0, len(URL_list)):
        content= scrape_content(URL_list[i])

        if content is not None:
            save_html(to_where, content.text, str(i))

        else:

            pass

    print("Mini dataset is created!")

create_mini_dataset(path, URL_list)
