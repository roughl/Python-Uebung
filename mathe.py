#!/usr/bin/python
#1310 Teilnehmer eines Kongresses können auf 38 cars verteilt werden, mit den Sitzplaetzanzahlen: 41, 29, 13.
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

while (( result != total) | block):
  block = 0
  a=random.randint(0,cars)
  b=random.randint(0,cars-a)
  c=cars-a-b
  result=a*avalue+b*bvalue+c*cvalue
  count=count+1
  if ((a==28) & (b==2) & (c==8)):
    message = "28-2-8 already used"
    block = 1
  if ((a==24) & (b==9) & (c==5)):
    message = "24-9-5 already used"
    block = 1
  if ((a==20) & (b==16) & (c==2)):
    message = "28-2-8 already used"
    block = 1
  if (block == 1) :
    print message,", count=",count

print "a=",a,", b=",b,", c=",c

#Loesung mit dem Skript ermittelt:
#a= 28 , b= 2 , c= 8
#a= 24 , b= 9 , c= 5
#a= 20 , b= 16 , c= 2

