import initializer as i
import iteratorService as itr
import siteLoginService as ls
import globals as gl

initializr = i.Initializer().setup()
ls.SiteLoginService().login()
try:
    itr.IteratorService().interateOverCategories()
except Exception as e:
    print(e)
    print(gl.DRIVER.current_url)