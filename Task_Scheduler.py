def leastInterval(N, k, tasks):
      l = len(tasks)
      if l == len(set(tasks)):
          return l
      
      else:
          
          task_frequency = {}
          
          for task in tasks:task_frequency[task] = task_frequency.get(task, 0) + 1
          
          max_count = max(task_frequency.values())
          max_count_freq = sum(1 for count in task_frequency.values() if count == max_count)
          
          intervals = (max_count - 1) * (k + 1) + max_count_freq
          return max(intervals, len(tasks))
