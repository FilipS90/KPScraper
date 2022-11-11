# KPScraper

TODO:

- error on second page of ads
File "/home/filips/MyCode/KPScraper/main.py", line 7, in <module>
    itr.IteratorService().interateOverCategories()
  File "/home/filips/MyCode/KPScraper/iteratorService.py", line 27, in interateOverCategories
    self.iterateAdCategory(downloader)
  File "/home/filips/MyCode/KPScraper/iteratorService.py", line 31, in iterateAdCategory
    adUrls = self.getAdUrlsFromCurrentPage(self.driver.current_url)
  File "/home/filips/MyCode/KPScraper/iteratorService.py", line 42, in getAdUrlsFromCurrentPage
    adUrlsArray = soup.find('div', class_='Grid_col-lg-10__tIdze Grid_col-xs__6oZvU Grid_col-sm__hxOHE Grid_col-md__1bRJZ').find_all('a', class_='Link_link__J4Qd8 Link_inherit___qXEP AdGoldHeader_goldHeader__t_ira')
AttributeError: 'NoneType' object has no attribute 'find_all'

- make KPScraper completely autonomous
  1) copy proton-script to /bin in Dockerfile
  2) install protonvpn-cli during initialization (if not installed ...)
- save point of current progress
- hashmap for numbers;
- logger service
- dockerize the app

Prerequisits:
#1 - install protonvpn cli tool
#2 - move proton-script to /bin