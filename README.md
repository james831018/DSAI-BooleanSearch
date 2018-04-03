# DSAI-BooleanSearch
做一個簡易搜尋引擎，可以做Boolean搜尋(and,or,not)


## 斷詞：
#### 下載繁體斷詞的dictionary(2-gram and 3-gram)
#### 把query裡面要搜尋的字加到dict裡面
#### 把source.csv裡的文章經過jieba斷詞系統根據剛下載的dict斷詞
* 判斷中文or英文
* 判斷是兩字或三字的
### 再把剛剛所有的斷詞分開，在做一次jieba斷詞
  以防兩個有意義的詞放在一起被斷錯或漏斷
  ex：北美國防部=>北美 & 國防部(少了美國)
### 用jieba斷詞根據三字的dict找三字的斷詞
  以防三字的被斷成兩個兩字的
### 再用jieba斷詞根據兩字的dict從三次當中找兩字的斷詞
  以防兩字的被斷再三字的
  ex：美國式 => 美國式 & 美國
  
  
## 搜尋：
### 匯入query.txt
### 判斷是否為中文 & 兩字or三字
### 找出相對應的set
### 判斷Booleab
* and：set1 & set2
* or： set1 | set2
* not set1 - set2
### 把結果匯出在output.txt
