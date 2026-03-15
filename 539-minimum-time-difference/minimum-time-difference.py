class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # PARSE TIME 
        timePoints = [int(i.replace(":", "")) for i in timePoints]
        timePoints.sort()

        # print(timePoints)

        timePoints.append(timePoints[0]+2400)
        # print(timePoints)

        main_diff=24*60+20

        for i in range(len(timePoints)-1):
            h = abs((timePoints[i+1]//100 - timePoints[i]//100)) *60
            m = ((timePoints[i+1] %100 - timePoints[i]%100))
            diff = h+m
            
            if diff < main_diff:
                main_diff = diff

        return main_diff
            