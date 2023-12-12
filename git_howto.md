# Подсказка по GIT:

Создание репозитория
```sh
git init
```
Добавление файла или добавление изминений
```sh
git add
```
Внесение изменений в проект и репу
```sh
git commit -m "Message"
```
Просмотр логов
```sh
git log
```

```sh
git log --oneline
```
Проверка где были изменения
```sh
git checkout
```
Просмсотр изменения файлов.
```sh
git diff
```
Указать в какую ветку отправляем
```sh
git push -u origin main
```
Отправить в репу
```sh
git push 
```

Удаление через консоль
Удаляет локальную ветку, если уже сделан её пуш и мердж:
```sh
git branch -d branch_name
```
Принудительно (force) удаляет локальную ветку, несмотря ни на что:
```sh
git branch -D branch_name
```
Теперь удалим такую же ветку из самого репозитория:
```sh
git push origin --delete stage
```
Удаление всех локальных веток, если не существует удаленных (были удалены):
```sh
git fetch --all --prune
```
```sh
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -d
```