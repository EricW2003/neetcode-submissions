class TimeMap:
    def __init__(self):
        self.dico={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dico:
            self.dico[key].append([timestamp,value])
        else:
            self.dico[key]=[[timestamp,value]]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dico:
            return ""
        dico=self.dico[key]
        l=0
        r=len(dico)-1
        while l<=r:
            mid=(l+r)//2
            mid_time=dico[mid][0]
            if mid_time<=timestamp:
                l=mid+1
            else:
                r=mid-1

        if dico[r][0]>timestamp:
            return ""
        return dico[r][1]

