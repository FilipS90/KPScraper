My cancelled project of web scrapping phone numbers from KupujemProdajem. It had some minor bugs, but was functional for the most part, scraping one category after another. Main obstacle was the KP server which stopped serving requests after several hundred scrapes. I have tried to get passed this with using Proton VPN cli, and switching from one vpn endpoint to another every 200-300 requests to mask myself. Also it was challenging to get KP to work from those endpoints because KP does not accept requests from outside Serbia (for the most part). But Israel, Japan and I believe Island were the ones able to send requests to KP, so I used them at the time. I was yet to try tor browser, thought it was notoriously slow. This issue remained unresolved. Anyway, due to this being in a gray legal area I decided to stop further work. It was a fun little project for a while.

# KPScraper

TODO:

- create cache with usernames
- make KPScraper completely autonomous
  1) copy proton-script to /bin in Dockerfile
  2) install protonvpn-cli in Dockerfile
- save point of current progress
- logger service
- dockerize the app

Prerequisits:
#1 - install protonvpn cli tool
#2 - move proton-script to /bin
