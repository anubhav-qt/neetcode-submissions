class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(speed))]
        cars.sort(reverse = True)
        time_stack = []
        
        for position, speed in cars:
            time = float((target - position) / speed)
            if not time_stack or time > time_stack[-1]:
                time_stack.append(time)
        
        return len(time_stack)
