import initializer as scc
import iteratorService as its

initializr = scc.Initializer()
initializr.createSaveDirectory()
initializr.getConstants()
iterator = its.IteratorService().interateOverCategories()