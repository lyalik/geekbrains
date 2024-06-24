### 1. Создание файлов и объединение их

Создаем два файла с помощью команды `cat`:
```bash
cat > domestic_animals.txt <<EOL
Dog
Cat
Hamster
EOL

cat > pack_animals.txt <<EOL
Horse
Camel
Donkey
EOL
```

Объединяем файлы и просматриваем содержимое:
```bash
cat domestic_animals.txt pack_animals.txt > animals.txt
cat animals.txt
```

Переименовываем файл:
```bash
mv animals.txt human_friends.txt
```

### 2. Создание директории и перемещение файла

Создаем директорию и перемещаем файл:
```bash
mkdir animal_directory
mv human_friends.txt animal_directory/
```

### 3. Подключение дополнительного репозитория MySQL и установка пакета

Добавляем репозиторий MySQL:
```bash
wget https://dev.mysql.com/get/mysql-apt-config_0.8.17-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.17-1_all.deb
sudo apt update
```

Устанавливаем пакет из репозитория:
```bash
sudo apt install mysql-server
```

### 4. Установка и удаление deb-пакета с помощью dpkg

Устанавливаем deb-пакет:
```bash
sudo dpkg -i mysql-apt-config_0.8.17-1_all.deb
```

Удаляем deb-пакет:
```bash
sudo dpkg -r mysql-apt-config
```

### 5. История команд в терминале

Для вывода истории команд используйте:
```bash
history
```

### 6. Диаграмма классов

Диаграмма классов может быть нарисована с помощью любого инструмента для создания UML-диаграмм, например, draw.io или Lucidchart. Вот пример иерархии:

```
Animal
├── DomesticAnimal
│ ├── Dog
│ ├── Cat
│ └── Hamster
└── PackAnimal
    ├── Horse
    ├── Camel
    └── Donkey
```

### 7. Создание базы данных в MySQL

```sql
CREATE DATABASE human_friends;
```

### 8. Создание таблиц с иерархией

```sql
USE human_friends;

CREATE TABLE Animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    birth_date DATE
);

CREATE TABLE DomesticAnimal (
    id INT,
    FOREIGN KEY (id) REFERENCES Animal(id)
);

CREATE TABLE Dog (
    id INT,
    FOREIGN KEY (id) REFERENCES DomesticAnimal(id)
);

CREATE TABLE Cat (
    id INT,
    FOREIGN KEY (id) REFERENCES DomesticAnimal(id)
);

CREATE TABLE Hamster (
    id INT,
    FOREIGN KEY (id) REFERENCES DomesticAnimal(id)
);

CREATE TABLE PackAnimal (
    id INT,
    FOREIGN KEY (id) REFERENCES Animal(id)
);

CREATE TABLE Horse (
    id INT,
    FOREIGN KEY (id) REFERENCES PackAnimal(id)
);

CREATE TABLE Camel (
    id INT,
    FOREIGN KEY (id) REFERENCES PackAnimal(id)
);

CREATE TABLE Donkey (
    id INT,
    FOREIGN KEY (id) REFERENCES PackAnimal(id)
);
```

### 9. Заполнение таблиц

```sql
INSERT INTO Animal (name, birth_date) VALUES ('Buddy', '2019-01-01');
INSERT INTO Dog (id) VALUES (1);

INSERT INTO Animal (name, birth_date) VALUES ('Whiskers', '2020-05-05');
INSERT INTO Cat (id) VALUES (2);

INSERT INTO Animal (name, birth_date) VALUES ('Nibbles', '2021-07-07');
INSERT INTO Hamster (id) VALUES (3);

INSERT INTO Animal (name, birth_date) VALUES ('Spirit', '2018-03-03');
INSERT INTO Horse (id) VALUES (4);

INSERT INTO Animal (name, birth_date) VALUES ('Humphrey', '2017-02-02');
INSERT INTO Camel (id) VALUES (5);

INSERT INTO Animal (name, birth_date) VALUES ('Eeyore', '2019-04-04');
INSERT INTO Donkey (id) VALUES (6);
```

### 10. Удаление верблюдов и объединение таблиц

```sql
DELETE FROM Camel WHERE id IN (SELECT id FROM Animal WHERE name = 'Humphrey');

CREATE TABLE HorseAndDonkey AS
SELECT * FROM Horse
UNION
SELECT * FROM Donkey;
```

### 11. Создание таблицы "молодые животные"

```sql
CREATE TABLE YoungAnimals AS
SELECT id, name, birth_date, TIMESTAMPDIFF(MONTH, birth_date, CURDATE()) AS age_in_months
FROM Animal
WHERE TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) BETWEEN 1 AND 3;
```

### 12. Объединение всех таблиц

```sql
CREATE TABLE AllAnimals AS
SELECT 'Dog' AS type, * FROM Dog
UNION
SELECT 'Cat' AS type, * FROM Cat
UNION
SELECT 'Hamster' AS type, * FROM Hamster
UNION
SELECT 'Horse' AS type, * FROM Horse
UNION
SELECT 'Donkey' AS type, * FROM Donkey;