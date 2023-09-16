Задание
1. Используя команду cat в терминале операционной системы Linux, создать
два файла Домашние животные (заполнив файл собаками, кошками,
хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и
ослы), а затем объединить их. Просмотреть содержимое созданного файла.
Переименовать файл, дав ему новое имя (Друзья человека)

![image](https://github.com/Maickl-Denis/FinalWork_GB/assets/81251154/f8026325-cfbf-4f10-a3e5-335ed5c6d5ba)

2. Создать директорию, переместить файл туда.

![image](https://github.com/Maickl-Denis/FinalWork_GB/assets/81251154/29e1a202-2fe8-40de-b350-5e9594e0e8ce)

3. Подключить дополнительный репозиторий MySQL. Установить любой пакет
из этого репозитория.

![image](https://github.com/Maickl-Denis/FinalWork_GB/assets/81251154/0362a130-1e52-47d9-9b5d-03311918ba07)


4. Установить и удалить deb-пакет с помощью dpkg

```shell
#Скачиваем пакет для установки:
wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-j_8.0.32-1ubuntu22.04_all.deb
#Устанавливаем пакет mysql-connector-j_8.0.32-1ubuntu22.04_all.deb:
sudo dpkg - i mysql-connector-j_8.0.32-1ubuntu22.04_all.deb
#Удаляем пакет и его сопутствующие пакеты:
sudo dpkg -r mysql-connector-j
sudo apt-get autoremove
```
