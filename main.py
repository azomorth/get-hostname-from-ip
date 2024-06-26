import socket
import time

def get_hostname_by_ip(ip_address):
  """Получает имя хоста по IP-адресу.

  Args:
    ip_address: IP-адрес для поиска имени хоста.

  Returns:
    Имя хоста, если оно было найдено, иначе "Неизвестно".
  """
  try:
    hostname = socket.gethostbyaddr(ip_address)[0]
    return hostname
  except socket.herror:
    return "Неизвестно"

def main():
  """Основная функция скрипта.
  """
  input_file_path = "D:\\ip_addresses.txt"  # Путь к файлу с IP-адресами
  output_file_path = "D:\\ip_addresses_with_hostnames.txt"  # Путь к выходному файлу

  with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    for line in input_file:
      ip_address = line.strip()
      hostname = get_hostname_by_ip(ip_address)
      output_file.write(f"{ip_address} - {hostname}\n")
      time.sleep(0.5)  # Задержка для предотвращения перегрузки сервера DNS

if __name__ == "__main__":
  main()