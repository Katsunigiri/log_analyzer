import re
from collections import Counter
import matplotlib.pyplot as plt

ip_counter = Counter()
sudo_counter = Counter()

ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

with open("test_auth.log", "r") as file:
	for line in file:
		# Фильтрация строк с ssh попытками входа
		if "Failed password" in line or "Accepted password" in line:
			ips = re.findall(ip_pattern, line)
			for ip in ips:
				ip_counter[ip] += 1
		# Ищем sudo попытки
		if "sudo" in line:
			sudo_counter[line.strip()] += 1
				
# Вывод 10 самых частых IP

print("to 10 IP adresses: ")
for ip, count in ip_counter.most_common(10):
	print(f"{ip}: {count} attemps")

print("\nОбнаруженные sudo-события и их количество: ")
for event, count in sudo_counter.items():
	print(f"{event}: {count} раз")
	
# Построение графика
top_ips = ip_counter.most_common(10)
ips = [ip for ip, _ in top_ips]
counts = [count for _, count in top_ips]

plt.figure(figsize=(10,6))
plt.bar(ips, counts, color='skyblue')
plt.title('10 попыток входа')
plt.xlabel('IP-адрес')
plt.ylabel('Количество попыток')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("ip_attemps.png")
print("\График сохранен в файл ip_attemps.png")

# HTML-отчет
with open("report.html", "w") as report:
	report.write("<html><head><meta charset='utf-8'><title>log Report</title></head></body>")
	report.write("<h1>Отчет по логам</h1>")
	
	# IP таблица
	report.write("<h2>Top 10 ip</h2><table border='1'><tr><th>attemps</th></tr>")
	for ip, count in top_ips:
		report.write(f"<tr><td>{ip}</td><td>{count}</td></tr>")
	report.write("</table>")

	#Sudo таблица
	report.write("<h2>Обнаружениные sudo события</h2><table border='1'><tr><th>Событие</th></tr>")
	for event, count in sudo_counter.items():
		report.write(f"<tr><td>{event}</td><td>{count}</td></tr>")
	report.write("</table>")

	# График
	report.write("<h2>График попыток входа</h2><img src='ip_attemps.png' width='600'>")
	
	report.write("</body></html>")

print("HTML-отчет сохранен подл названием report.html")



