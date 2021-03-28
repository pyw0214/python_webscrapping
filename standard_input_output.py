# import sys
# print("Python", "Java", file=sys.stdout)  # standard output
# print("Python", "Java", file=sys.stderr)  # standard error


# scores = {"Math": 0, "Eng": 95, "Coding": 100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")  # left, right adjust

# waiting number
# 001, 002, 003, ..
# for num in range(1, 21):
#     print("waiting num : " + str(num).zfill(3))

# answer = input("Input anything: ")
# print(type(answer))
# print("you input " + answer + " accordingly.")

#score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 90")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #줄별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동.
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()
lines = score_file.readlines()   #list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()


