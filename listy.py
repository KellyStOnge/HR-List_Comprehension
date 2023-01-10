#!/usr/bin/env python3

#hackerrank 1/10/2023
#Kelly St.Onge

#https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

"""Let's learn about list comprehensions! You are given three integers ijk and n representing the dimensions of a cuboid along with an integer n . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to n . """

#build a list of list

import itertools
if __name__ == '__main__':
    #this is some test stuff
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    i = x
    j = y
    k = z

    iCount = 0
    jCount = 0
    kCount = 0

    listMatrix = []
    ilist = []
    jlist = []
    klist = []
    sumList = []

    for iCount in range(0,i+1):
        ilist.append(iCount)
        iCount += 1

    iCount =0

    for jCount in range(0,j+1):
        jlist.append(jCount)
        jCount += 1

    jCount =0

    for kCount in range(0,k+1):
        
        klist.append(kCount)
        kCount += 1

    for i in itertools.product(ilist,jlist,klist):
        listMatrix.append(i)


    for index in listMatrix:

        if ((index[0] + index[1] + index[2]) != n):

            
            tempList = [index[0],index[1],index[2]]
            sumList.append(tempList)

    print(sumList)



