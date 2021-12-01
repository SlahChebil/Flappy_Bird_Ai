import vcsn
ctx = vcsn.context('lal, b')
e = ctx.expression('a+b')
e.star()
e.thompson()