print(int("000999"))
def 将Ocr识别返回的字符串格式化为列表(输入字符串):
    # 用|分割字符串
    split_list = 输入字符串.split("|")

    # 对每个分割后的子字符串再用,分割，并形成最终列表
    final_list = [item.split(",") for item in split_list]

    return final_list
import re
要升级的建筑物名称="星空实验室"
print(1241)
识别到的字符串 = "369,91,城墙|505,91,400000|369,119,星空实验室|495,117,4000000|369,145,战争机器|499,144,1900000|368,172,战斗直升机|493,171,42600000|368,199,治疗小屋|494,197,42000000|368,225,储金罐x2|497,224,2500000|369,251,建筑大师训练营|494,250,42000000|369,279,宝石矿井|495,278,3500000|369,305,特斯拉电磁塔|514,304,150000|369,331,特斯拉电磁塔|509,330,0100000|370,360,防空火炮x2|525,359,80000"
if 要升级的建筑物名称 in 识别到的字符串:
    #将英文字母o和O都替换为数字0,因为识别可能将数字0错误地识别为英文字母o或O
    识别到的字符串=识别到的字符串.replace('o', '0').replace('O', '0')
    建筑和价格列表 = 将Ocr识别返回的字符串格式化为列表(识别到的字符串)
    #类似于这样子[['369', '91', '城墙'], ['505', '91', '400000'], ['369', '119', '星空实验室'], ['495', '117', '4000000'], ['369', '145', '战争机器'], ['499', '144', '1900000'], ['368', '172', '战斗直升机'], ['493', '171', '42600000'], ['368', '199', '治疗小屋'], ['494', '197', '42000000'], ['368', '225', '储金罐x2'], ['497', '224', '2500000'], ['369', '251', '建筑大师训练营'], ['494', '250', '42000000'], ['369', '279', '宝石矿井'], ['495', '278', '3500000'], ['369', '305', '特斯拉电磁塔'], ['514', '304', '150000'], ['369', '331', '特斯拉电磁塔'], ['509', '330', '0100000'], ['370', '360', '防空火炮x2'], ['525', '359', '80000']]
    for 第几个建筑物 in range(0,len(建筑和价格列表)+1,2):
        print(第几个建筑物)
        print(建筑和价格列表[第几个建筑物])
        print(建筑和价格列表[第几个建筑物+1])
        if 要升级的建筑物名称 in 建筑和价格列表[第几个建筑物][2]:
            print("要升级的建筑物在",第几个建筑物)
            剔除多余字符后的字符串列表=re.findall(r'\d+', 建筑和价格列表[第几个建筑物+1][2])
            剔除多余字符后的价格=int(剔除多余字符后的字符串列表[0])
            print("价格为",剔除多余字符后的价格)
            break
else:
    print("未找到要升级的建筑物")
