# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:18:15 2022

@author: carme
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distList = []
        for x, y in points:
            dist = (x**2)+(y**2)
            distList.append([dist,x,y])
        heapq.heapify(distList)
        sol = []
        while k > 0:
            dist, x, y = heapq.heappop(distList)
            sol.append([x,y])
            k -= 1
        return sol