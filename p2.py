# -*- coding: utf-8 -*-
"""p2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ze-Wmm2t8n_F2s9am4LCYfY4SNMunRrY
"""

# nama file p2.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

#netacad email cth: 'abcd@gmail.com'
email='raspianiyani@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

#modul
import matplotlib.pyplot as plt
import random
import math

#No.1
#Graded

def isPointInCircle(x,y,r,center=(0,0)):
  # MULAI KODEMU DI SINI
  pass
  L = ((x - center[0])**2) + ((y - center[1])**2) - (r**2)

  if (L <= 0):
    return True
  else:
    return False

#No.2
#Graded
import random


def generateRandomSquarePoints(n,length,center=(0,0)):
  # MULAI KODEMU DI SINI
  minx = center[0]-length/2
  miny = center[1]-length/2
  
  # Gunakan list comprehension dengan variable minx, miny, length, dan n
  points = [[random.uniform(minx, minx + length), random.uniform(miny, miny + length)] for i in range(n)]

  return points

#No.3
#Graded

def MCCircleArea(r,n=100,center=(0,0)):
  # MULAI KODEMU DI SINI
  pass
  titik = generateRandomSquarePoints(n,2*r,center=(0,0))
  jumlah_titik_dalam_lingkaran = 0
  for idx,val in enumerate(titik):
    if isPointInCircle(val[0], val[1], r, center=(0,0)) == True:
      jumlah_titik_dalam_lingkaran += 1
  return (jumlah_titik_dalam_lingkaran / n * (2*r)**2)

#No.4
#Graded

def LLNPiMC(nsim,nsample):
  # MULAI KODEMU DI SINI
  pass
  sigma = 0 
  for i in range(nsim):
    pi = MCCircleArea(1,nsample)
    sigma += pi
  return sigma/nsim

#No.5
# Graded
def relativeError(act,est):
  # MULAI KODEMU DI SINI
  pass
  error = abs((est-act)/act)*100
  return error