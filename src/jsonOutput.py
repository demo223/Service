import json

# 读取数据      , encoding="utf-8"
with open('./data/Test2.json', 'r') as f:
    data1 = json.load(f)  # data1为dictionary格式
# print(data1)
json_str = json.dumps(data1, ensure_ascii=False)  # json对象
# 存储数据
output_path = "data/jsonTxt2.txt"
head_word = []  # 存放中心词
with open(output_path, 'w', encoding='utf-8') as o:
    for index in range(0, 276):
        qas = data1[index]["qas"][0]
        for key in qas:
            if len(key["answers"]) == 1:
                print(key["question"] + " : " + key["answers"][0]["text"])
                o.write(key["question"] + " : " + key["answers"][0]["text"] + "\n")
                if key["question"] == "中心词":
                    head_word.append(key["answers"][0]["text"])
            else:
                for num in range(len(key["answers"])):
                    print(key["question"] + " : " + key["answers"][num]["text"])
                    o.write(key["question"] + " : " + key["answers"][num]["text"] + "\n")
                    if key["question"] == "中心词":
                        head_word.append(key["answers"][num]["text"])
        print("---------------------------------")
        o.write("---------------------------------" + "\n")
print(set(head_word))   # 输出所有不重复的中心词
