import percorrerlib as pl
import bs4

drupal_sites = open("drupal_sites.html", "r")
soup = bs4.BeautifulSoup(drupal_sites, features="html.parser")

sites = []

for a in soup.find_all("a", href=True):
    sites.append(a['href'])

vulnerable = []
non_vulnerable = []

for i in range(len(sites)):
    print(sites[i])
    if pl.test_drupalgeddon2(sites[i]) == 1:
        vulnerable.append(sites[i])
        print("Vulneravel")
    else:
        non_vulnerable.append(sites[i])
        print("Nao vulneravel")

#print("****Vulnerable****")
#print(vulnerable)
#print("****Non-vulnerable****")
#print(non_vulnerable)
