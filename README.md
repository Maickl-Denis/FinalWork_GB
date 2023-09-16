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

5. Выложить историю команд в терминале ubuntu

```shell
 1289  cat > home_animals
 1290  cat > Pack_animals
 1291  cat home_animals Pack_animals > aniamls
 1292  cat aniamls
 1293  mv aniamls Mans_friend
 1294  ls
 1295  mkdir direktory
 1296  mv Mans_friend ./direktory/Mans_friend
 1297  ll ./direktory/
 1298  sudo wget https://dev.mysql.com/get/mysql-apt-config_0.8.26-1_all.deb
 1299  sudo dpkg -i mysql-apt-config_0.8.26-1_all.deb
 1300  sudo apt-get update
 1301  sudo wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-j_8.0.32-1ubuntu22.04_all.deb
 1302  sudo dpkg - i mysql-connector-j_8.0.32-1ubuntu22.04_all.deb
 1303  sudo dpkg -r mysql-connector-j
 1304  sudo apt-get autoremove
```

6. Нарисовать диаграмму, в которой есть класс родительский класс, домашние
животные и вьючные животные, в составы которых в случае домашних
животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные
войдут: Лошади, верблюды и ослы)

![image](https://github.com/Maickl-Denis/FinalWork_GB/assets/81251154/26c23dba-da4e-4c1b-86bb-46c163d78be0)



