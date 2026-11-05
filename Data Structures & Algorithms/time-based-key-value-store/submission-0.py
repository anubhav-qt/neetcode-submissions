from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list) # key: [[value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if (len(self.time_map[key]) == 0):
            return ""
        l, r = 0, len(self.time_map[key]) - 1
        most_recent_index = -1

        while l <= r:
            m = l + (r - l) // 2
            
            if self.time_map[key][m][1] == timestamp:
                return self.time_map[key][m][0]
            elif self.time_map[key][m][1] > timestamp:
                r = m - 1
            else:
                most_recent_index = m
                l = m + 1

        return "" if most_recent_index == -1 else self.time_map[key][most_recent_index][0]
