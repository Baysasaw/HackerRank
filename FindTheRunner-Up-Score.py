# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = max(arr)
    # he string '-inf' is a special value recognized by Python to represent negative infinity.
    runner_up = float('-inf')
    for i in arr:
        if i < max_num and i > runner_up:
            runner_up = i
    print(runner_up)

    