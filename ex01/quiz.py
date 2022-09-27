import random

def shutudai(qa_lst):
    qa = random.choice(qa_lst)
    print("問題："+qa["q"])
    return qa["a"]


def kaito(ans_lst):
    ans = input("答えるんだ：")
    if ans in ans_lst:
        print("正解")
    else:
        print("不正解")


if __name__ == "__main__":
    qa_lst = [
        {"q": "サザエの旦那は？", "a": ["ますお", "マスオ"]},
        {"q": "カツオの妹は？", "a": ["わかめ", "ワカメ"]},
        {"q":"タラオはカツオからみて何？", "a": ["おい", "オイ", "甥", "おいっこ"]},
    ]
    ans_lst = shutudai(qa_lst)
    kaito(ans_lst)