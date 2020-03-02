import csv
import re


data = [{'name': 'first', 'age': '12', 'color': 'black'},
        {'name': 'second', 'age': '13', 'color': 'whilt'},
        {'name': 'third', 'age': '18', 'color': 'red'}
        ]
with open('C:\\Users\\1\\Desktop\\product.csv', 'w', encoding='utf-8')as f:
    writer = csv.DictWriter(f, fieldnames=["名字", "age", "color"])
    writer.writeheader()
    writer.writerow({'名字': 'third', 'age': '18', 'color': 'red'})
