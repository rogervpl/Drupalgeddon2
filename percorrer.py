import percorrerlib as pl
import bs4

drupal_sites = open("drupal_sites.html", "r")
soup = bs4.BeautifulSoup(drupal_sites, features="html.parser")

sites = []

for a in soup.find_all("a", href=True):
    sites.append(a['href'])

vulnerables = []
non_vulnerables = []

for i in range(len(sites)):
    if pl.test_drupalgeddon2(sites[i]) == 1:
        vulnerables.append(sites[i])
        print(sites[i])
        print("Vulneravel")
    else:
        non_vulnerables.append(sites[i])
        print(sites[i])
        print("Nao vulneravel")
print("****Vulnerables****")
print(vulnerables)
print("****Non-vulnerables****")
print(non_vulnerables)
