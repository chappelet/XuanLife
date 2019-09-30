if __name__ == '__main__':
    import sys
    import os
    import jieba
    import csv
    import pandas as pd
    import numpy as np

    # Chinese characters filter and segment
    def is_chinese(uchar):
        if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
            return True
        else:
            return False


    def format_str(content):
        content_str = ''
        for i in content:
            if is_chinese(i):
                content_str = content_str + ｉ
        return content_str


    def fenci(datas):
        datas = [datas]
        cut_words = map(lambda s: list(jieba.cut(s)), datas)
        return list(cut_words)[0]


    def segment(content):
        seg_content = ''
        chinese_list = []
        for row in content:
            seg_content = fenci(format_str(row))
            chinese_list.append(seg_content)
        return chinese_list

    data = pd.read_csv(open('D:/XuanLife/Area_corporation/crawl_basicInfo.csv', errors='ignore'))
    gsmc = list(data['gsmc'])
    zcdz = list(data['zcdz'])

    print(gsmc[0],zcdz[0])

    #南昌市: 东湖区、西湖区、青云谱区、湾里区、青山湖区、新建区、南昌县、安义县、进贤县
    num_nc = 0
    #景德镇市: 珠山区、昌江区、浮梁县、乐平市
    num_jdz = 0
    #萍乡市: 安源区、湘东区、莲花县、上栗县、芦溪县
    num_px = 0
    #九江市: 浔阳区、濂溪区、柴桑区、永修县、德安县、都昌县、湖口县、彭泽县、武宁县、修水县、瑞昌市、共青城市、庐山市
    num_jj = 0
    #新余市: 渝水区、分宜县
    num_xy = 0
    #鹰潭市: 月湖区、余江区、贵溪市
    num_yt = 0
    #赣州市: 章贡区、南康区、赣县区、信丰县、大余县、龙南县、定南县、全南县、寻乌县、安远县、瑞金市、宁都县、于都县、会昌县、石城县、上犹县、兴国县、崇义县
    num_gz = 0
    #吉安市: 吉州区、青原区、吉安县、井冈山市、吉水县、新干县、永丰县、泰和县、遂川县、万安县、安福县、永新县、峡江县
    num_ja = 0
    #宜春市: 袁州区、高安市、丰城市、樟树市、奉新县、万载县、上高县、宜丰县、靖安县、铜鼓县
    num_yc = 0
    #抚州市: 临川区、东乡区、南城县、黎川县、南丰县、崇仁县、乐安县、宜黄县、金溪县、资溪县、广昌县
    num_fz = 0
    #上饶市: 信州区、广丰区、广信区、玉山县、铅山县、横峰县、弋阳县、余干县、鄱阳县、万年县、婺源县、德兴市
    num_sr = 0
    num_unknown = 0
    unknown = []

    for i in range(826636):
        # 南昌市: 东湖区、西湖区、青云谱区、湾里区、青山湖区、新建区、南昌县、安义县、进贤县
        if '南昌' in zcdz[i] or '东湖' in zcdz[i] or '西湖' in zcdz[i] or '青云谱' in zcdz[i] or '湾里' in zcdz[i] or '青山湖' in zcdz[i] or '新建' in zcdz[i] or '安义' in zcdz[i] or '进贤' in zcdz[i] or '南昌' in gsmc[i] or '东湖' in gsmc[i] or '西湖' in gsmc[i] or '青云谱' in gsmc[i] or '湾里' in gsmc[i] or '青山湖' in gsmc[i] or '新建' in gsmc[i] or '安义' in gsmc[i] or '进贤' in gsmc[i]:
            num_nc += 1
        # 景德镇市: 珠山区、昌江区、浮梁县、乐平市
        elif '景德镇' in zcdz[i] or '珠山' in zcdz[i] or '昌江' in zcdz[i] or '浮梁' in zcdz[i] or '乐平' in zcdz[i] or '景德镇' in gsmc[i] or '珠山' in gsmc[i] or '昌江' in gsmc[i] or '浮梁' in gsmc[i] or '乐平' in gsmc[i]:
            num_jdz += 1
        # 萍乡市: 安源区、湘东区、莲花县、上栗县、芦溪县
        elif '萍乡' in zcdz[i] or '安源' in zcdz[i] or '湘东' in zcdz[i] or '莲花' in zcdz[i] or '上栗' in zcdz[i] or '芦溪' in zcdz[i] or '萍乡' in gsmc[i] or '安源' in gsmc[i] or '湘东' in gsmc[i] or '莲花' in gsmc[i] or '上栗' in gsmc[i] or '芦溪' in gsmc[i]:
            num_px += 1
        # 九江市: 浔阳区、濂溪区、柴桑区、永修县、德安县、都昌县、湖口县、彭泽县、武宁县、修水县、瑞昌市、共青城市、庐山市
        elif '九江' in zcdz[i] or '浔阳' in zcdz[i] or '濂溪' in zcdz[i] or '柴桑' in zcdz[i] or '永修' in zcdz[i] or '德安' in zcdz[i] or '都昌' in zcdz[i] or '湖口' in zcdz[i] or '彭泽' in zcdz[i] or '武宁' in zcdz[i] or '修水' in zcdz[i] or '瑞昌' in zcdz[i] or '共青城' in zcdz[i] or '庐山' in zcdz[i] or '九江' in gsmc[i] or '浔阳' in gsmc[i] or '濂溪' in gsmc[i] or '柴桑' in gsmc[i] or '永修' in gsmc[i] or '德安' in gsmc[i] or '都昌' in gsmc[i] or '湖口' in gsmc[i] or '彭泽' in gsmc[i] or '武宁' in gsmc[i] or '修水' in gsmc[i] or '瑞昌' in gsmc[i] or '共青城' in gsmc[i] or '庐山' in gsmc[i]:
            num_jj += 1
        # 新余市: 渝水区、分宜县
        elif '新余' in zcdz[i] or '渝水' in zcdz[i] or '分宜' in zcdz[i] or '新余' in gsmc[i] or '渝水' in gsmc[i] or '分宜' in gsmc[i]:
            num_xy += 1
        # 鹰潭市: 月湖区、余江区、贵溪市
        elif '鹰潭' in zcdz[i] or '月湖' in zcdz[i] or '余江' in zcdz[i] or '贵溪' in zcdz[i] or '鹰潭' in gsmc[i] or '月湖' in gsmc[i] or '余江' in gsmc[i] or '贵溪' in gsmc[i]:
            num_yt += 1
        # 赣州市: 章贡区、南康区、赣县区、信丰县、大余县、龙南县、定南县、全南县、寻乌县、安远县、瑞金市、宁都县、于都县、会昌县、石城县、上犹县、兴国县、崇义县
        elif '赣州' in zcdz[i] or '章贡' in zcdz[i] or '南康' in zcdz[i] or '赣县' in zcdz[i] or '信丰' in zcdz[i] or '大余' in zcdz[i] or '龙南' in zcdz[i] or '定南' in zcdz[i] or '全南' in zcdz[i] or '寻乌' in zcdz[i] or '安远' in zcdz[i] or '瑞金' in zcdz[i] or '宁都' in zcdz[i] or '于都' in zcdz[i] or '会昌' in zcdz[i] or '石城' in zcdz[i] or '上犹' in zcdz[i] or '兴国' in zcdz[i] or '崇义' in zcdz[i] or '赣州' in gsmc[i] or '章贡' in gsmc[i] or '南康' in gsmc[i] or '赣县' in gsmc[i] or '信丰' in gsmc[i] or '大余' in gsmc[i] or '龙南' in gsmc[i] or '定南' in gsmc[i] or '全南' in gsmc[i] or '寻乌' in gsmc[i] or '安远' in gsmc[i] or '瑞金' in gsmc[i] or '宁都' in gsmc[i] or '于都' in gsmc[i] or '会昌' in gsmc[i] or '石城' in gsmc[i] or '上犹' in gsmc[i] or '兴国' in gsmc[i] or '崇义' in gsmc[i]:
            num_gz += 1
        # 吉安市: 吉州区、青原区、吉安县、井冈山市、吉水县、新干县、永丰县、泰和县、遂川县、万安县、安福县、永新县、峡江县
        elif '吉安' in zcdz[i] or '吉州' in zcdz[i] or '青原' in zcdz[i] or '井冈山' in zcdz[i] or '吉水' in zcdz[i] or '新干' in zcdz[i] or '永丰' in zcdz[i] or '泰和' in zcdz[i] or '遂川' in zcdz[i] or '万安' in zcdz[i] or '安福' in zcdz[i] or '永新' in zcdz[i] or '峡江' in zcdz[i] or '吉安' in gsmc[i] or '吉州' in gsmc[i] or '青原' in gsmc[i] or '井冈山' in gsmc[i] or '吉水' in gsmc[i] or '新干' in gsmc[i] or '永丰' in gsmc[i] or '泰和' in gsmc[i] or '遂川' in gsmc[i] or '万安' in gsmc[i] or '安福' in gsmc[i] or '永新' in gsmc[i] or '峡江' in gsmc[i]:
            num_ja += 1
        # 宜春市: 袁州区、高安市、丰城市、樟树市、奉新县、万载县、上高县、宜丰县、靖安县、铜鼓县
        elif '宜春' in zcdz[i] or '袁州' in zcdz[i] or '高安' in zcdz[i] or '丰城' in zcdz[i] or '樟树' in zcdz[i] or '奉新' in zcdz[i] or '万载' in zcdz[i] or '上高' in zcdz[i] or '宜丰' in zcdz[i] or '靖安' in zcdz[i] or '铜鼓' in zcdz[i] or '宜春' in gsmc[i] or '袁州' in gsmc[i] or '高安' in gsmc[i] or '丰城' in gsmc[i] or '樟树' in gsmc[i] or '奉新' in gsmc[i] or '万载' in gsmc[i] or '上高' in gsmc[i] or '宜丰' in gsmc[i] or '靖安' in gsmc[i] or '铜鼓' in gsmc[i]:
            num_yc += 1
        # 抚州市: 临川区、东乡区、南城县、黎川县、南丰县、崇仁县、乐安县、宜黄县、金溪县、资溪县、广昌县
        elif '抚州' in zcdz[i] or '临川' in zcdz[i] or '东乡' in zcdz[i] or '南城' in zcdz[i] or '黎川' in zcdz[i] or '南丰' in zcdz[i] or'崇仁' in zcdz[i] or '乐安' in zcdz[i] or '宜黄' in zcdz[i] or '金溪' in zcdz[i] or '资溪' in zcdz[i] or '广昌' in zcdz[i] or '抚州' in gsmc[i] or '临川' in gsmc[i] or '东乡' in gsmc[i] or '南城' in gsmc[i] or '黎川' in gsmc[i] or '南丰' in gsmc[i] or'崇仁' in gsmc[i] or '乐安' in gsmc[i] or '宜黄' in gsmc[i] or '金溪' in gsmc[i] or '资溪' in gsmc[i] or '广昌' in gsmc[i]:
            num_fz += 1
        # 上饶市: 信州区、广丰区、广信区、玉山县、铅山县、横峰县、弋阳县、余干县、鄱阳县、万年县、婺源县、德兴市
        elif '上饶' in zcdz[i] or '信州' in zcdz[i] or '广丰' in zcdz[i] or '广信' in zcdz[i] or '玉山' in zcdz[i] or '铅山' in zcdz[i] or '横峰' in zcdz[i] or '弋阳' in zcdz[i] or '余干' in zcdz[i] or '鄱阳' in zcdz[i] or '万年' in zcdz[i] or '婺源' in zcdz[i] or '德兴' in zcdz[i] or '上饶' in gsmc[i] or '信州' in gsmc[i] or '广丰' in gsmc[i] or '广信' in gsmc[i] or '玉山' in gsmc[i] or '铅山' in gsmc[i] or '横峰' in gsmc[i] or '弋阳' in gsmc[i] or '余干' in gsmc[i] or '鄱阳' in gsmc[i] or '万年' in gsmc[i] or '婺源' in gsmc[i] or '德兴' in gsmc[i]:
            num_sr += 1
        else:
            num_unknown += 1
            unknown.append(zcdz[i])

    #a = pd.Series(unknown)
    #data = pd.DataFrame({'zcdz': a})
    #data.to_csv('D:/XuanLife/Area_corporation/crawl_basicInfo_address_only.csv', encoding='utf-8', index=False)
    num_corporation = [num_nc, num_jdz, num_px, num_jj, num_xy, num_yt, num_gz, num_ja, num_yc, num_fz, num_sr, num_unknown]
    print(num_corporation)

