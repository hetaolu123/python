import csv

# 将Excel文件另存为CSV格式，假设文件名为'attack.csv'
csv_filename = 'C:/Users/Administrator/Desktop/attack.csv'

# 初始化字典来记录IP的出现次数
ip_counts = {}

# 打开CSV文件并读取内容
with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        ip = row[0]  # 假设IP地址在第一列
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

# 创建两个列表来存储未重复和重复的IP地址及其计数
unique_ips = [ip for ip, count in ip_counts.items() if count == 1]
duplicate_ips = {ip: count for ip, count in ip_counts.items() if count > 1}

# 输出未重复的IP地址
print("未重复的IP地址：")
for ip in unique_ips:
    print(ip)

# 输出重复的IP地址及其出现的次数
print("\n重复的IP地址及其次数：")
for ip, count in duplicate_ips.items():
    print(f"{ip}： {count} 次")

# 记录并输出重复和未重复IP的个数
print("\n重复的IP地址个数：", len(duplicate_ips))
print("未重复的IP地址个数：", len(unique_ips))