import initializer as scc
import iteratorService as its
import loginService as ls

initializr = scc.Initializer()
initializr.createSaveDirectory()
initializr.getConstants()
ls.LoginService.login()
iterator = its.IteratorService().interateOverCategories()