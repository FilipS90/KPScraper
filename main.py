import dlUtil

url = 'https://www.kupujemprodajem.com/odmor-u-srbiji/zlatibor/zlatibor-centar/oglas/136119879?filter_id=1456699685'
downloader = dlUtil.DownloaderUtil(url)
downloader.downloadImage()
