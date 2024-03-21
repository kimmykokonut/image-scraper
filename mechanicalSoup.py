import mechanicalsoup
import os
import wget

#obj enter command w/o new var
browser = mechanicalsoup.StatefulBrowser()
#url
url = 'https://images.google.com/'

browser.open(url)
#print(browser.get_url())

#get hmtl
browser.get_current_page()

# target search input tags
browser.select_form()
#browser.get_current_form().print_summary()

#search for a term
search_term = 'alpaca'
browser["q"] = search_term

#submit/click search
browser.launch_browser()
response = browser.submit_selected()

#print('new url', browser.get_url())
#print('my response:\n', response.text[:500])

#open new url
new_url = browser.get_url()
browser.open(new_url)

#get html
page = browser.get_current_page()
all_images = page.find_all('img')
#print(all_images)

# target src att
image_source = []
for image in all_images:
  image = image.get('src')
  image_source.append(image)
#print(image_source)

#fix broken/incomplete links
image_source = [image for image in image_source if image.startswith('https')]
#print(image_source)

#save img. create new dir w/os and wget
path = os.getcwd()
print(path) #current path
path = os.path.join(path, search_term + 's')

#create dir
os.mkdir(path)
print(path) #path with new dir in it

#save img to folder
counter = 0
for image in image_source:
  save_as = os.path.join(path, search_term + str(counter) + '.jpg')
  wget.download(image, save_as)
  counter += 1
