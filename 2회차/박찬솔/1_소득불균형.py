import sys

sys.stdin = open("_소득불균형.txt")
# n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력
# 첫 번째 줄에 테스트 케이스의 수 T
# 이후 T개의 테스트 케이스에 대해 각각 두 줄
# 첫 번째 줄에는 정수의 개수 N
# 두 번째 줄에는 각 사람의 소득을 뜻하는 N개의 양의 정수
# 각각 1 이상 100,000 이하
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호 의미, 1부터 시작)를 출력
# 각 테스트 케이스마다 한 줄씩 평균 이하의 소득을 가진 사람들의 수를 출력
T = map(int, input().split())
for i in range(3):
    print(f'#{i+1}')    