class TimeMap:
    def __init__(self):
        self.dico = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dico:
            self.dico[key].append([timestamp, value])
        else:
            self.dico[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dico:
            return ""
        
        arr = self.dico[key]
        l, r = 0, len(arr) - 1

        # Binary search classique pour trouver le dernier timestamp <= target
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                l = mid + 1  # chercher à droite
            else:
                r = mid - 1  # chercher à gauche

        # r pointe sur le dernier élément <= timestamp
        if r < 0:
            return ""
        return arr[r][1]