# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        running = []  # this is running queue use heap for this one
        job = deque() # this is the job that is coming to be processed
        tasks = [(st, idx, et) for idx, (st, et) in enumerate(tasks)]
        tasks.sort()
        st = tasks[0][0]
        idx = 0
        while idx < len(tasks) and st == tasks[idx][0]:
            s, i, e = tasks[idx]
            heappush(running, (e, i, s))
            idx += 1
        ans = []
        time = 0
        task = None
        while running or idx < len(tasks):
            if running and not task:
                task = heappop(running)
                ans.append(task[1])
                time = task[2]
                continue

            if not running or (idx < len(tasks) and time + task[0] >= tasks[idx][0]):
                s, i, e = tasks[idx]
                heappush(running, (e, i, s))
                idx += 1
                continue
            
            if idx < len(tasks) and running[0][2] == tasks[idx][0]:
                s, i, e = tasks[idx]
                heappush(running, (e, i, s))
                idx += 1
                continue
        
            time = time + task[0]
            task = heappop(running)
            time = max(time, task[2])
            ans.append(task[1])

        return ans