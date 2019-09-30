if __name__ == '__main__':
    import sys
    import os
    import jieba
    import pymongo
    import csv
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.linear_model import SGDClassifier
    from sklearn.pipeline import Pipeline
    from sklearn import metrics
    from sklearn.externals import joblib
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import GradientBoostingClassifier


    # 汉字过滤与切词
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


    # 去除停用词
    def drop_stopwords(contents, stopwords):
        contents_clean = []
        for line in contents:
            line_clean = []
            for word in line:
                if word in stopwords:
                    continue
                line_clean.append(word)
            contents_clean.append(line_clean)
        return contents_clean


    # 去除长度仅为1的切词
    def drop_characters(contents):
        contents_clean = []
        for line in contents:
            line_clean = []
            for i in line:
                if len(i) > 1:
                    line_clean.append(i)
            contents_clean.append(line_clean)
        return contents_clean


    # 缩减每条数据特征值的数量
    def drop_words(content):
        content_clean = []
        list_clean = []
        index = 0
        for i in content:
            if len(i) < 12:
                list_clean = i[:6]
                content_clean.append(list_clean)
            elif len(i) < 20:
                index = len(i)//2
                list_clean = i[:index]
                content_clean.append(list_clean)
            else:
                index = len(i)//3
                list_clean = i[:index]
                content_clean.append(list_clean)
        return content_clean


    # 将过滤的切词重新组成有空格间隔的string
    def merge(list1):
        list2 = []
        for i in list1:
            list2.append(' '.join('%s' %id for id in i))
        #count_vect = CountVectorizer()
        #X_train_counts = count_vect.fit_transform(list2)
        #tfidf_transformer = TfidfTransformer()
        #X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        return list2

    # 去除jyfw中所有有的括号中及其之后的内容
    def parenthesis_eliminator(line1):
        line2 = 0
        location = str(line1).find('(')
        if location > -1:
            line2 = str(line1)[0:location]
        else:
            line2 = line1
        return line2


    # 打开文件，导入数据
    data = pd.read_csv(open('D:/桌面/XuanLife/NLP/crawl_Company_basicInfo.csv', errors='ignore'))
    known_id = list(data['_id'])
    known_jyfw = list(data['jyfw'])
    known_sshy = list(data['sshy'])
    known_code = list(data['tyshxydm'])


    # 去除括号内容
    known_jyfw_clean = []
    for i in known_jyfw:
        known_jyfw_clean.append(parenthesis_eliminator(i))
    X, Y = known_jyfw_clean, known_sshy


    # 进行训练集和测试集的划分
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.3, random_state = 42)


    # 去除所有非中文字符并进行切词
    X_train_seg = segment(X_train)
    X_test_seg = segment(X_test)


    # 去除所有的停用词
    stopwords = ['与', '的', '及', '和', '受', '从事', '其他', '其它', '各类', '各种', '各式', '活动', '兼']
    X_train_drop = drop_stopwords(X_train_seg, stopwords)
    X_test_drop = drop_stopwords(X_test_seg, stopwords)


    # 去除所有长度仅为1的切词
    X_train_clean = drop_characters(X_train_drop)
    X_test_clean = drop_characters(X_test_drop)


    # 缩减每行数据特征值的数量
    X_train_dropped = drop_words(X_train_clean)
    X_test_dropped = drop_words(X_test_clean)
    print(X_train_dropped[0])

    # 将词条重新组合为string
    X_train_merge = merge(X_train_drop)
    X_test_merge = merge(X_test_drop)
    print(X_train_merge[0])

    # 将词条转化为tf-idf格式并使用随机森林模型训练分类器模型，保存模型，计算准确率
    text_clf = Pipeline([("vectorizer", TfidfVectorizer()),
                         ("clf", RandomForestClassifier(n_estimators=50))
                         ])
    text_clf = text_clf.fit(X_train_tfidf, Y_train)
    joblib.dump(text_clf,'D:/桌面/XuanLife/NLP/text_clf4.pkl')
    predicted = text_clf.predict(X_test_tfidf)
    print("准确率：")
    print(np.mean(predicted == Y_test))
    print(metrics.classification_report(Y_test, predicted))
    print(metrics.confusion_matrix(Y_test, predicted))