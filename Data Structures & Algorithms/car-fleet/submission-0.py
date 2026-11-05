class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # get position and speed together (O(n))
        cars = [(position[i], speed[i]) for i in range(len(speed))]

        # sort the cars based on position (O(n logn))
        cars.sort(reverse = True)
        time_stack = [float((target - cars[0][0]) / cars[0][1])]
        
        for position, speed in cars:
            time = float((target - position) / speed)
            if time > time_stack[-1]:
                time_stack.append(time)
        
        return len(time_stack)
