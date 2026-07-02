class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired_list = list(zip(position, speed))
        paired_list.sort(reverse=True)
        stack = []

        for i,j in paired_list:
            position = i
            speed = j
            time = (target - position) / speed
            if not stack:
                stack.append(time)
            if stack and time > stack[-1]:
                stack.append(time)

        print(paired_list)
        

        return len(stack)