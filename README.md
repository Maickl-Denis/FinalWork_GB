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


7. В подключенном MySQL репозитории создать базу данных “Друзья
человека”

```shell
den@Ubuntu:~/GB/finalWork$ mysql -h localhost -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.34 MySQL Community Server - GPL

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE DATABASE Human_friends;
Query OK, 1 row affected (0,03 sec)
```

8. Создать таблицы с иерархией из диаграммы в БД
```sql
CREATE TABLE home_animals(id INT AUTO_INCREMENT PRIMARY KEY, type_name VARCHAR (20), animal_id INT, FOREIGN KEY (animal_id) REFERENCES animal (id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE pack_animals(id INT AUTO_INCREMENT PRIMARY KEY, type_name VARCHAR (20), animal_id INT, FOREIGN KEY (animal_id) REFERENCES animal (id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE dogs(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), birthday DATE, commands VARCHAR(50), type_id int, Foreign KEY (type_id) REFERENCES home_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE cats(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), birthday DATE, commands VARCHAR(50), type_id int, Foreign KEY (type_id) REFERENCES home_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE hamsters(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), birthday DATE, commands VARCHAR(50), type_id int, Foreign KEY (type_id) REFERENCES home_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE horses (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), birthday DATE, commands VARCHAR(50), type_id int, Foreign KEY (type_id) REFERENCES pack_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE Camel (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), birthday DATE, commands VARCHAR(50), type_id int, Foreign KEY (type_id) REFERENCES pack_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE Donkey (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), birthday DATE, commands VARCHAR(50), type_id int, Foreign KEY (type_id) REFERENCES pack_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);
```

9. Заполнить низкоуровневые таблицы именами(животных), командами
которые они выполняют и датами рождения

```sql
INSERT INTO animal (class_name) VALUES ('Домашние'), ('Вьючные');

INSERT INTO pack_animals (type_name, animal_id) VALUES ('Собаки', 2), ('Кошки', 2), ('Хомячки', 2); 

INSERT INTO home_animals (type_name, animal_id) VALUES ('Лошади', 2), ('Верблюды', 2), ('Ослы', 2); 

INSERT INTO dogs (name, birthday, commands, type_id) VALUES ('Лана', '2022-06-01', 'к ноге, лежать, сидеть, голос', 1), ('Шарик', '2022-06-02', "сидеть, лежать, лапу, принеси", 1), ('Полкан', '2022-06-03', "сидеть, лежать, лапу, фас", 1), ('Рэй', '2022-06-04', "сидеть, лежать, голос, место", 1);

INSERT INTO cats (name, birthday, commands, type_id) VALUES ('Киса', '2022-06-05', 'есть', 1), ('Муркзик', '2022-06-06', 'умри', 1);

INSERT INTO hamsters (name, birthday, commands, type_id) VALUES ('Лео', '2022-06-06', NULL, 1), ('Донатело', '2022-06-07', NULL, 1), ('Микеланджело', '2022-06-08', "", 1);

INSERT INTO horses (name, birthday, commands, type_id) VALUES ('Звездачка', '2022-06-09', 'Голоп', 2), ('Искорка', '2022-06-10', 'Рысь', 2), ('Задира', '2022-06-11', "Сбросить наездника", 2);

INSERT INTO Camel (name, birthday, commands, type_id) VALUES ('Верблюд 1', '2022-06-12', 'сбросить горб', 2), ('Верблюд 2', '2022-06-13', 'убить всех людей', 2), ('Верблюд 3', '2022-06-14', "Найти воду", 2);

INSERT INTO Donkey (name, birthday, commands, type_id) VALUES ('Осел 1', '2022-06-15', 'Тащить груз', 2), ('Осел 2', '2022-06-16', 'Тащить груз больше чем соседний осел', 2), ('Осел 3', '2022-06-15', "Везти человека", 2);
```

10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой
питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу.

```sql
DELETE FROM Camel;
INSERT INTO horses (name, birthday, commands) SELECT name, birthday, commands FROM Donkey;
DROP TABLE Donkey;
RENAME TABLE horses TO horses_donkeys;
```

11.Создать новую таблицу “молодые животные” в которую попадут все
животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
до месяца подсчитать возраст животных в новой таблице

```sql
CREATE TEMPORARY TABLE animals AS 
SELECT * FROM horses_donkeys
UNION SELECT * FROM dogs
UNION SELECT * FROM cats
UNION SELECT * FROM hamsters;

CREATE TABLE young_animals  AS
SELECT name, birthday, commands, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) AS Age_in_month
FROM animals WHERE birthday BETWEEN ADDDATE(curdate(), INTERVAL -3 YEAR) AND ADDDATE(CURDATE(), INTERVAL -1 YEAR);
```
