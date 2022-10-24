import initializer as i
import iteratorService as itr
import loginService as ls

initializr = i.Initializer().setup()
ls.LoginService().login()
itr.IteratorService().interateOverCategories()