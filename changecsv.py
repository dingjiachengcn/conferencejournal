import csv
from googletrans import Translator

# 初始化翻译器
translator = Translator()

# 读取CSV文件
with open('conferencejournal.csv', 'r', encoding='utf-8-sig') as file:
    rows = list(csv.reader(file))

# 修改表头
header = rows[0]
header[header.index('Category')] = 'Category_cn'
header.append('Category_us')

new_rows = [header]

for row in rows[1:]:
    # 翻译Category_cn列
    translated = translator.translate(row[header.index('Category_cn')], src='zh-cn', dest='en').text
    row.append(translated)

    # 替换会议和期刊
    row[header.index('Type')] = row[header.index('Type')].replace('会议', 'conference').replace('期刊', 'journal')

    new_rows.append(row)

# 写入修改后的数据到CSV
with open('modified_conferencejournal.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_rows)

print("CSV已修改完毕，保存为modified_conferencejournal.csv")
