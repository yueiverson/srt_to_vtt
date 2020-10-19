import re
import os
#將想刪除字幕ID與加上line:77%的srt檔
#存放至convert.py的檔案夾中
#隨後開啟demo.py，只需輸入srt檔的名稱即可
def convert_TimeNuber(filename): #filename為srt的檔案名稱
    with open(filename,'r+',encoding="utf-8") as f:
        texts = f.readline()
        rename_time=[]
        # for text in texts:
        while texts:
            time=re.compile(r'(\d\d):(\d\d):(\d\d),(\d{3}) --> (\d\d):(\d\d):(\d\d),(\d{3})$')
            times=re.sub(time,r'\1:\2:\3.\4 --> \5:\6:\7.\8 line:77%',str(texts))
            texts = f.readline()
            rename_time.append(times)
    with open('output.srt','w',encoding="utf-8") as n:
        n.writelines(rename_time)
    with open('output.srt','r',encoding="utf-8") as f:
        texts = f.readline()
        delete_number=[]
        while texts:
        # for text in texts:
            number=re.compile(r'^\d+\s$')
            numbers=re.sub(number,"",texts)
            texts = f.readline()
            delete_number.append(numbers)
            filename=filename.replace('.srt','.vtt')
    with open('convert'+filename,'w',encoding="utf-8") as n:
        n.writelines('WEBVTT\nKind:captions\nLanguage:zh-TW\n')
        n.writelines(delete_number)
    os.remove('output.srt')
    if os.path.exists(filename) is not True:
        print('轉檔完成，轉檔名稱為:convert{}，於本檔案夾中。'.format(filename))
    else:
        print("轉檔失敗") 
    
