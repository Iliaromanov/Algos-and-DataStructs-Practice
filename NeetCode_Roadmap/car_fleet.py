# O(nlogn) ; n = len(pos)
class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        sorted_pos = sorted(zip(pos, speed), reverse=True)
        stack = []
        for pos_i_val, speed_i_val in sorted_pos:
            if not stack or (
             stack[-1][0] > pos_i_val and stack[-1][1] >= speed_i_val
            ):
                stack.append([pos_i_val, speed_i_val])
                continue
            
            time_to_target_fleet = (target - stack[-1][0]) / stack[-1][1]
            time_to_target_cur = (target - pos_i_val) / speed_i_val

            if time_to_target_fleet < time_to_target_cur:
                stack.append([pos_i_val, speed_i_val])

        return len(stack)

# O(m) ; m = target
class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        time_to_target = [0] * target
        for i, pos_i in enumerate(pos):
            time_to_target[pos_i] = (target - pos_i) / speed[i]
        
        num_fleets = 0
        ahead_fleet_time_to_target = 0
        for i in range(target - 1, -1, -1):
            cur_time_to_target = time_to_target[i]
            if cur_time_to_target > ahead_fleet_time_to_target:
                num_fleets += 1
                ahead_fleet_time_to_target = cur_time_to_target

        return num_fleets
