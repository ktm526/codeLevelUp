#https://leetcode.com/problems/reorder-data-in-log-files/

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letterLogs = []
        digitalLogs = []

        for log in logs:
            if log.split()[1] .isdigit():
                digitalLogs.append(log)
            else:
                letterLogs.append(log)
        letterLogs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letterLogs + digitalLogs
        