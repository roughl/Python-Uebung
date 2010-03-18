#!/usr/bin/python
#1310 Teilnehmer eines Kongresses koennen auf 38 cars verteilt werden, mit den Sitzplaetzanzahlen: 41, 29, 13.
#Es darf kein Sitzplatz leerbleiben.
#Wievile cars von jeder Art werden benoetigt?
 
import os
import random
 
#changeable:
avalue=41
bvalue=29
cvalue=13
total=1310
cars=38
 
#systemvars:
result=0
count=0
block=0
message=""
random.seed(os.urandom)
 
class Solution:
  def __init__(self,a, b, c):
    # Sets all the properties
    self.a = a
    self.b = b
    self.c = c
 
solutions = []
 
def check(a,b,c):
  for sol in solutions:
    if a==sol.a and b==sol.b and c==sol.c:
     return 0
  return 1
 
while 1:
  block = 0
  a=random.randint(0,cars)
  b=random.randint(0,cars-a)
  c=cars-a-b
  result=a*avalue+b*bvalue+c*cvalue
  count=count+1
  if result == total and check(a,b,c):
    print "a=",a,", b=",b,", c=",c
    solutions.append(Solution(a,b,c))
 
#Loesung mit dem Skript ermittelt:
#a= 28 , b= 2 , c= 8
#a= 24 , b= 9 , c= 5
#a= 20 , b= 16 , c= 2
