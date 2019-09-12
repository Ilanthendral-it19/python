#pass it as tuple

name="Ilanthendral"
score=100
print("Total score for %s is %d" %(name,score))

#pass it as parameters
print("Totol score for",name,"is",score)

#pass it as concadination
a=5
b=10
c=a+b
print("sum of a and b is c")
print("sum of "a"and"b "is"c)

#pass itas dictionary
print("Total score for %(n)s  is %(s)s" %{'n':Ilanthendral,'s':100})

# style string formating
print("total score for {} is {}".format(Ilanthendral,hundred))

#use new style formatting with explict name
print("Total score for {n} is {s} ".format(name,s=score))

