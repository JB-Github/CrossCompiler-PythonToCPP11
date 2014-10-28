from pyListener import pyListener

class pyClasses(pyListener):
    def exitNumber(self, ctx):
        print ctx.getChild(0)

    def exitFor_(self, ctx):
        print "for test"

    def exitString(self, ctx):
        print ctx.getChild(0)
