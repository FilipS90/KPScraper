import initializer as i
import iteratorService as itr
import siteLoginService as ls

initializr = i.Initializer().setup()
ls.SiteLoginService().login()
itr.IteratorService().interateOverCategories()