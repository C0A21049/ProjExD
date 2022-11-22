from random import randint as ran
from datetime import datetime

def kaitou(kai_ran_num):
    st = datetime.now()
    ans = input("答え:")
    result = 1
    for correct in ans_list[kai_ran_num]:
        if ans == correct:
            result = 0
            break
    if result == 0:
        print("正解\n")
    else:
        print("不正解\n")
    ed = datetime.now()

    print("回答時間:")
    print((ed-st).seconds)

def shutudai(shutu_ran_num):
    print("問題:\n"+quiz_list[shutu_ran_num])
    kaitou(shutu_ran_num)

if __name__ == "__main__":
    quiz_list = ["サザエの旦那の名前は?", "カツオの妹の名前は?", "タラオはカツオから見てどんな関係?"]
    ans_list = [["ますお", "マスオ"],["ワカメ", "わかめ"], ["甥", "おい", "甥っ子", "おいっこ"]]
    ran_num = ran(0,2)
    shutudai(ran_num)