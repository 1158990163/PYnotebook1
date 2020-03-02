import csv
import re

with open("C:\\Users\\1\\Desktop\\first.csv",'w',encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=['楼主', '内容', '时间'])
    writer.writeheader()
    with open("C:\\Users\\1\\Desktop\\网页源码.txt",'r',encoding='utf-8')as file:
        message=file.read()
        file_name=re.findall(r'img username="(.*?)" class=',message)
        file_string = re.findall(r'd_post_content j_d_post_content  clearfix" style="display:;">(.*?)</div>', message)
        file_data = re.findall(r'&quot;,&quot;date&quot;:&quot;(.*?)&quot;,&quot;vote_crypt',message)
    for i in range(len(file_name)):
        writer.writerow({"楼主": file_name[i], "内容": file_string[i], "时间": file_data[i]})



