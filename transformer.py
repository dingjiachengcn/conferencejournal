from bs4 import BeautifulSoup
import csv

# 读取HTML文件
with open('conferencejournal.txt', 'r', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

# 查找所有<tr class="item">标签
rows = soup.find_all('tr', class_='item')

# 准备数据
data = []

for row in rows:
    th = row.find('th').text.strip()
    tds = row.find_all('td')
    # 根据你给的示例，我们取出每一列的数据
    tcss_code = tds[0].text.strip()
    title = tds[1].text.strip()
    grade = tds[2].text.strip()
    type_ = tds[3].text.strip()
    category = tds[4].text.strip()

    data.append([th, tcss_code, title, grade, type_, category])

# 写入CSV文件
with open('conferencejournal.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    # 写入表头
    writer.writerow(['Index', 'Code', 'Title', 'Grade', 'Type', 'Category'])
    # 写入数据
    writer.writerows(data)

print('转换完成，数据已保存为conferencejournal.csv')
