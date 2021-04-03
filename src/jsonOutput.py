import json

# 读取数据      , encoding="utf-8"
with open('./data/Test2.json', 'r') as f:
    data1 = json.load(f)  # data1为dictionary格式
# print(data1)
json_str = json.dumps(data1, ensure_ascii=False)  # json对象
# 存储数据
output_path = "data/jsonTxt2.txt"
with open(output_path, 'w', encoding='utf-8') as o:
    for index in range(0, 275):
        qas = data1[index]["qas"][0]
        for key in qas:
            if len(key["answers"]) == 1:
                print(key["question"] + " : " + key["answers"][0]["text"])
                o.write(key["question"] + " : " + key["answers"][0]["text"]+"\n")
            else:
                for num in range(len(key["answers"])):
                    print(key["question"] + " : " + key["answers"][num]["text"])
                    o.write(key["question"] + " : " + key["answers"][num]["text"]+"\n")
        print("---------------------------------")
        o.write("---------------------------------"+"\n")
