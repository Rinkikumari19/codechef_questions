# T = int(input("test cases "))
# for i in range(T):
#     sum = 0 
#     origin = input("indian h or non indian ")
#     CONTEST_WON,rank = input()
#     CONTEST_WON,rank = CONTEST_WON,rank.split()
#     TOP_CONTRIBUTOR = input("top contributer h ya nhi ")
#     BUG_FOUND = int(input("bug kiya h nahi "))
#     CONTEST_HOSTED = 50
#     if CONTEST_WON > 0:
#         sum = 300
#         rank = int(input("any rank "))
#         if rank < 20:
#             bonus = 20-rank
#             sum = sum + bonus
#         sum = sum
#     if TOP_CONTRIBUTOR == 'top_contributor':
#         sum = sum + 300
#     if BUG_FOUND >= 50 or BUG_FOUND <= 1000:
#         sum = sum + BUG_FOUND
#     if origin == 'INDIAN':
#         sum = sum + CONTEST_HOSTED
#         print(sum//200)
#     else:
#         sum = sum + CONTEST_HOSTED
#         print(sum//400)
    
               



# 2
# 4 INDIAN
# CONTEST_WON 1
# TOP_CONTRIBUTOR
# BUG_FOUND 100
# CONTEST_HOSTED
# 4 NON_INDIAN
# CONTEST_WON 1
# TOP_CONTRIBUTOR
# BUG_FOUND 100
# CONTEST_HOSTED


# T = int(input("test cases "))
# for i in range(T):
#     laddu = 0
#     activities,origin =input().split()
#     activities = int(activities)
#     for index in range(activities):
#         a = list(input().split())
#         if len(a)=='1':
#             if a[0]=='TOP_CONTRIBUTOR':
#                 laddu = laddu + 300
#             else:
#                 laddu = laddu + 50
#         else:
#             if a[0]=='CONTEST_WON':
#                 if int(a[1]) <= 20:
#                     laddu = laddu + 300 + (20-int(a[1]))
#                 else:
#                     laddu = laddu + 300
#             else:
#                 laddu = laddu + int(a[1])
#     if origin == "INDIAN":
#         print(laddu//200)
#     else:
#         print(laddu//400)


T = int(input("test cases "))
for i in range(T):
    laddu = 0
    activities,origin =input().split()
    activities = int(activities)
    for index in range(activities):
        a = list(input().split())
        if len(a)==1:
            if a[0]=='TOP_CONTRIBUTOR':
                laddu = laddu + 300
            else:
                laddu = laddu + 50
        else:
            if a[0]=='CONTEST_WON':
                if int(a[1]) <= 20:
                    laddu = laddu + 300 + (20-int(a[1]))
                else:
                    laddu = laddu + 300
            else:
                if int(a[1])>=50 or int(a[1])<=1000:
                    laddu = laddu + int(a[1])
                else:
                    laddu = laddu
    if origin == "INDIAN" or origin=='indian':
        print(laddu//200)
    else:
        print(laddu//400)
