#encoding=utf-8
import time
import jieba
import csv
import urllib,urllib.request
# 判断一个unicode是否是汉字
def is_chinese(uchar):         
    if '\u4e00' <= uchar<='\u9fff':
        return True
    else:
        return False
 
# 判断一个unicode是否是数字
def is_number(uchar):
    if '\u0030' <= uchar and uchar<='\u0039':
        return True
    else:
        return False
 
# 判断一个unicode是否是英文字母
def is_alphabet(uchar):         
    if ('\u0041' <= uchar<='\u005a') or ('\u0061' <= uchar<='\u007a'):
        return True
    else:
        return False
 
# 判断是否非汉字，数字和英文字符
def is_other(uchar):
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False
def insert(original,new,pos):
    return original[:pos]+new+original[pos:]




#計時

if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                       default='source.csv',
                       help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    args = parser.parse_args()
    
    # Please implement your algorithm below
    
    # TODO load source data, build search engine

    # TODO compute query result
  
    # TODO output result
tStart=time.time()

#下載檔案
print("downloading urllib")
url="https://raw.githubusercontent.com/james831018/DSAI-BooleanSearch/master/dict_new.txt.big"
urllib.request.urlretrieve(url,"demo_new.txt.big")
url="https://raw.githubusercontent.com/james831018/DSAI-BooleanSearch/master/dict_three.txt.big"
urllib.request.urlretrieve(url,"demo_three.txt.big")
url="https://raw.githubusercontent.com/james831018/DSAI-BooleanSearch/master/dict_two.txt.big"
urllib.request.urlretrieve(url,"demo_two.txt.big")

#宣告
output=""
chinese=""
english=""
two_word={}
three_word={}
english_word={}
multiple_word={}

#把新的字加到dict
f=open(args.query,'r')
f2=open('demo_new.txt.big','a')
for row in f:
    row=row.strip('\n')
    #print("row is",row)
    for i in row.split(" "):
        if(i!="and" and i!="or" and i!="not"):
            new_word=i+" "+str(30)
            f2.writelines(new_word+"\n")
f.close()
f2.close()

#index
jieba.set_dictionary('demo_new.txt.big')
f = open(args.source, 'r')
for row in csv.DictReader(f, ["項目", "內容"]):
    #print (row['項目']+"內容："+row['內容'])
    #print(row['項目'])
    #words = jieba.cut(row['內容'], cut_all=False)
    words=jieba.tokenize(row['內容'], 'utf-8')
    shift=0
    for word in words:
        #print(word)
        tmp_word1=word[1]+1+shift
        tmp_word2=word[2]+shift
        while(tmp_word1<tmp_word2):
            row['內容']=insert(row['內容']," ",tmp_word1)
            #print(row['內容'],tmp_word1,tmp_word2)
            tmp_word1+=2
            tmp_word2+=1
            shift+=1
        if(is_chinese(word[0])):
            if len(word[0])==2:
                #print(two_word)
                #print(word)
                if((word[0] in two_word)==False):
                    #print(row['項目'])
                    tmp_int=int(row['項目'])
                    tmp_set=set([tmp_int])
                    tmp={word[0]:tmp_set}
                    #print(tmp)
                    two_word.update(tmp)
                elif((word[0] in two_word)==True):
                    two_word[word[0]].add(int(row['項目']))
                    #print(word,two_word[word])
            elif (len(word[0])==3):
                if((word[0] in three_word)==False):
                    tmp_int=int(row['項目'])
                    tmp_set=set([tmp_int])
                    tmp={word[0]:tmp_set}
                    #print(tmp)
                    three_word.update(tmp)
                elif((word[0] in three_word)==True):
                    three_word[word[0]].add(int(row['項目']))
                    #print(word,three_word[word])
            elif (len(word[0])>3):
                if((word[0] in multiple_word)==False):
                    tmp_int=int(row['項目'])
                    tmp_set=set([tmp_int])
                    tmp={word[0]:tmp_set}
                    #print(tmp)
                    multiple_word.update(tmp)
                elif((word[0] in multiple_word)==True):
                    multiple_word[word[0]].add(int(row['項目']))
        elif(is_alphabet(word[0])):
                if((word[0] in english_word)==False):
                    tmp_int=int(row['項目'])
                    tmp_set=set([tmp_int])
                    tmp={word[0]:tmp_set}
                    #print(tmp)
                    english_word.update(tmp)
                elif((word[0] in english_word)==True):
                    english_word[word[0]].add(int(row['項目']))
                    #print(word,english_word[word])
    #print (row['項目']+"內容："+row['內容'])
    #=======================================================第二次分析
    words=jieba.tokenize(row['內容'], 'utf-8')
    for word in words:
        #print(word)
        if(is_chinese(word[0])):
            if len(word[0])==2:
                #print(two_word)
                #print(word)
                if((word[0] in two_word)==False):
                    tmp_int=int(row['項目'])
                    tmp_set=set([tmp_int])
                    tmp={word[0]:tmp_set}
                    #print(tmp)
                    two_word.update(tmp)
                elif((word[0] in two_word)==True):
                    two_word[word[0]].add(int(row['項目']))
                    #print(word,two_word[word])
            elif len(word[0])==3:
                if((word[0] in three_word)==False):
                    tmp_int=int(row['項目'])
                    tmp_set=set([tmp_int])
                    tmp={word[0]:tmp_set}
                    #print(tmp)
                    three_word.update(tmp)
                elif((word[0] in three_word)==True):
                    three_word[word[0]].add(int(row['項目']))
                    #print(word,three_word[word])
            elif len(word[0])>3:
                if((word[0] in multiple_word)==False):
                    tmp_int=int(row['項目'])
                    tmp_set=set([tmp_int])
                    tmp={word[0]:tmp_set}
                    #print(tmp)
                    multiple_word.update(tmp)
                elif((word[0] in multiple_word)==True):
                    multiple_word[word[0]].add(int(row['項目']))
        elif(is_alphabet(word[0])):
                if((word[0] in english_word)==False):
                    tmp_int=int(row['項目'])
                    tmp_set=set([tmp_int])
                    tmp={word[0]:tmp_set}
                    #print(tmp)
                    english_word.update(tmp)
                elif((word[0] in english_word)==True):
                    english_word[word[0]].add(int(row['項目']))
                    #print(word,english_word[word])
f.close()

#找三字的
f = open(args.source, 'r')
jieba.set_dictionary('demo_three.txt.big')
for row in csv.DictReader(f, ["項目", "內容"]):
    #print (row['項目']+"內容："+row['內容'])
    #print(row['項目'])
    #words = jieba.cut(row['內容'], cut_all=False)
    words=jieba.tokenize(row['內容'], 'utf-8')
    shift=0
    for word in words:
        #print(word)
        if(is_chinese(word[0])):
            if (len(word[0])==3):
                if((word[0] in three_word)==False):
                    tmp_int=int(row['項目'])
                    tmp_set=set([tmp_int])
                    tmp={word[0]:tmp_set}
                    #print(tmp)
                    three_word.update(tmp)
                elif((word[0] in three_word)==True):
                    three_word[word[0]].add(int(row['項目']))
                    #print(word,three_word[word])
f.close()
#從三個裡找有沒有兩個字的
jieba.set_dictionary('demo_two.txt.big')
#print(three_word.items())
#for row in csv.DictReader(f, ["項目", "內容"]):
for key,value in three_word.items():
    #print("key ",key,"value",value)
    words = jieba.cut(key, cut_all=False)
    for word in words:
        #print(word)
        if len(word)==2:
            #print(two_word)
            #print(word)
            if((word in two_word)==False):
                #tmp_int=value
                #tmp_set=set([tmp_int])
                tmp={word:value}
                #print(tmp)
                two_word.update(tmp)
            elif((word in two_word)==True):
                two_word[word]=two_word[word] | value
                #print(word,two_word[word])
#搜尋
boolean=""
third=0
output=set([])
output1=set([])

f=open(args.query,'r')
f2=open(args.output,'w')

for row in f:
    row=row.strip('\n')
   #print("row is",row)
#query="川普 and 美國"
    #print(row.split(" "))
    for i in row.split(" "):
        #print("the i is",i)
        if(i=="and" or i=="or" or i=="not"):
            boolean=i
            #print("boolean="+i)
        elif(is_chinese(i)):
            if(len(i)==2):
                if(boolean==""):#第一個
                    output1=two_word[i]
                    #print(i,":",two_word[i])
                    #print("output1=",output1)
                elif(boolean=="and" and third==0):#第二個
                    output2=two_word[i]
                    #print(i,":",two_word[i])
                    output=output1 & output2
                    #print("third=0~~",output)
                    third=1
                elif(boolean=="and" and third==1):#第三個
                    #print(i,":",two_word[i])
                    output2=two_word[i]
                    output=output & output2
                elif(boolean=="or" and third==0):#第二個
                    output2=two_word[i]
                    #print("output2=",output2)
                    #print(i,":",two_word[i])
                    output=output1 | output2
                    #print("output=",output)
                    #print("third=0~~",output)
                    third=1
                elif(boolean=="or" and third==1):#第三個
                    #print(i,":",two_word[i])
                    output2=two_word[i]
                    #print("output2=",output2)
                    #print("output_befre=",output)
                    output=output | output2
                    #print("output_after=",output)
                elif(boolean=="not" and third==0):#第二個
                    output2=two_word[i]
                    #print(i,":",two_word[i])
                    output=output1 - output2
                    #print("third=0~~",output)
                    third=1
                elif(boolean=="not" and third==1):#第三個
                    #print(i,":",two_word[i])
                    output2=two_word[i]
                    output=output - output2
            if(len(i)==3):
                if(boolean==""):
                    output1=three_word[i]
                    #print(i,":",three_word[i])
                elif(boolean=="and" and third==0):
                    output2=three_word[i]
                    #print(i,":",three_word[i])
                    output=output1 & output2
                    #print("third=0~~",output)
                    third=1
                elif(boolean=="and" and third==1):
                    #print(i,":",three_word[i])
                    output2=three_word[i]
                    output=output & output2
                elif(boolean=="or" and third==0):#第二個
                    output2=three_word[i]
                    #print(i,":",three_word[i])
                    output=output1 | output2
                    #print("third=0~~",output)
                    third=1
                elif(boolean=="or" and third==1):#第三個
                    #print(i,":",three_word[i])
                    output2=three_word[i]
                    output=output | output2
                elif(boolean=="not" and third==0):#第二個
                    output2=three_word[i]
                    #print(i,":",three_word[i])
                    output=output1 - output2
                    #print("third=0~~",output)
                    third=1
                elif(boolean=="not" and third==1):#第三個
                    #print(i,":",three_word[i])
                    output2=three_word[i]
                    output=output - output2
        elif(is_alphabet(i)):
            if(boolean==""):
                output1=english_word[i]
                #print(i,":",english_word[i])
            elif(boolean=="and" and third==0):
                output2=english_word[i]
                #print(i,":",english_word[i])
                output=output1 & output2
                #print("third=0~~",output)
                third=1
            elif(boolean=="and" and third==1):
                #print(i,":",english_word[i])
                output2=english_word[i]
                output=output & output2
            elif(boolean=="or" and third==0):#第二個
                output2=english_word[i]
                #print(i,":",english_word[i])
                output=output1 | output2
                #print("third=0~~",output)
                third=1
            elif(boolean=="or" and third==1):#第三個
                #print(i,":",english_word[i])
                output2=english_word[i]
                output=output | output2
            elif(boolean=="not" and third==0):#第二個
                output2=english_word[i]
                #print(i,":",english_word[i])
                output=output1 - output2
                #print("third=0~~",output)
                third=1
            elif(boolean=="not" and third==1):#第三個
                #print(i,":",english_word[i])
                output2=english_word[i]
                output=output - output2
            #output_tmp=english_word[i]
            #print("output_tmp=",output_tmp)
            #if(boolean=="and"):
             #   output=output_tmp & output
             #   print("output=",output)
    #print("row is",row,"output=",sorted(output))

    #去{}
    output2=str(sorted(output))
    f2.writelines(output2[1:-1]+"\n")
    output=set([])
    output1=set([])
    boolean=""
    third=0
f.close
f2.close
tEnd=time.time()
print("時間：",tEnd-tStart)
#print ("two_word：", two_word)
#print("two_word:",two_word)
#print("three_word:",three_word)
#print("english_word:",english_word)

