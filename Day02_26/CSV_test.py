import csv

data = [{'name': 'first', 'age': '12', 'color': 'black'},
        {'name': 'second', 'age': '13', 'color': 'whilt'},
        {'name': 'third', 'age': '18', 'color': 'red'}
        ]
with open('E:\\new.csv', 'w', encoding='utf-8')as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "color"])
    writer.writeheader()
    writer.writerows(data)
    writer.writerow({'name': 'third', 'age': '18', 'color': 'red'})
