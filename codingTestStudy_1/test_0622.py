# -*- coding: utf-8 -*-

# 완주하지 못한 선수 문제

# participant = 참여한 선수들의 이름이 담긴 배열
# completion = 완주한 선수들의 이름이 담긴 배열
# return = 완주하지 못한 선수의 이름을 반환

# collctions.Counter를 이용하여

import collections


def soultion(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

if __name__ == '__main__':
    soultion()



# Hash를 이용한 풀이


# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]
#
#     return answer
