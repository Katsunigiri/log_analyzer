# log_parser.py

import re

# Открываем лог-файл
with open("auth.log", "r") as file:
	for line in file:
		# Поиск неудачных попыток входа
		if "Failed password" in line:
			print("Неудачный вход: ", line.strip())
			
		# Поиск sudo
		if "sudo" in line and "COMMAND=" in line:
			print("SUDO команда: ", line.strip())
		
		# Ищем IP-адреса
		ip_matches = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
		if ip_matches:
			print("IP найден: ", ip_matches, "->", line.strip())	
