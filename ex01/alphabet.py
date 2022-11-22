from random import randint as rd

#重複ないか探す
def search(a, c, l):#a=今の数c=検索対象l=検索するリスト
    for i in range(0,a):
        if c == l[i]:
            return 1

# ２回目の質問をする
def next_quiz(sub_tup, res_tup):
    amount = sub_tup[1]
    lost_str_list = res_tup[1]
    lost_amount = res_tup[2]
    ans_next_quiz =[]
    for i in range (lost_amount):
        ans = input(str(i+1)+"つ目の文字を入力してください：")
        ans_next_quiz.append(ans)
        result_ans_next_quiz = search(amount, ord(ans), lost_str_list)
        if result_ans_next_quiz != 1:
            break
        result_str_ans_next_quiz = search(amount, ord(ans), ans_next_quiz)
        if result_str_ans_next_quiz == 1:
            break
        if i == lost_amount:
            print("正解です。")
            return 0
    print("不正解です。またチャレンジしてください")

# 質問する
def quiz(res_tup):
    lost_amount = res_tup[2]
    ans_num = input("欠損文字はいくつあるでしょうか？")
    if ans_num == lost_amount:
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
        next = 0
    else:
        print("不正解です。またチャレンジしてください")
        next = 1
    return next

# 表示される文字の表示
def display(str_list):
    print("表示文字：")
    for dp_str in str_list:
        print(str_list[dp_str])

#欠損文字を決める
def defect(stuple):
    print("欠損文字：")
    str_list = stuple[0]
    amount = stuple[1]
    lost_str_list = []
    for lost_amount in range(rd(1,amount-1)):
        lost_str = rd(str_list)
        next = search(amount, lost_str, lost_str_list)
        if next == 1:
            continue
        lost_str_list.append(str_list.pop[lost_str])
        print(chr(lost_str_list[lost_str]))
    return str_list, lost_str_list, lost_amount

# 問題の解答作成
def result_maker(sub_tup):
    def_tup = defect(sub_tup)
    display(def_tup[0])
    return def_tup

#対象文字を決める
def subject():
    print("対象文字：")
    str_list = []
    for amount in range(rd(2,26)):
        str_code = range(rd(65,90))
        next = search(amount, str_code, str_list)
        if next == 1:
            continue
        str_list.append(str_code)
        print(chr(str_list[amount]))
    return str_list, amount

#消えたアルファベットを探すゲーム
if __name__ == "__main__":
    next_quiz = 1
    sub_tup = subject()
    res_tup = result_maker(sub_tup)
    next_quiz = quiz(res_tup)
    if next_quiz == 0:
        next_quiz(sub_tup, res_tup)
    
