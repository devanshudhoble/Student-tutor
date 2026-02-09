from agents.tutor_agent import tutor_agent

problem = '''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''

try:
    resp = tutor_agent.handle(problem)
    print('--- RESPONSE START ---')
    if isinstance(resp, str):
        print(resp[:4000])
    else:
        print(str(resp))
    print('\n--- RESPONSE END ---')
except Exception as e:
    print('ERROR:', e)
