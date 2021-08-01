# LEM.Django

this app just for REST api's for my <a href="https://cafebazaar.ir/app/com.mahdirahmani8.learnenglishwithmusicapp?l=en">LEM Application</a>

### API's:
```
POST  create music  =>     HOST_NAME(127.0.0.1/8000)/create/Music/
GET   show all musics =>   HOST_NAME(127.0.0.1/8000)/list/
PUT   update music  =>     HOST_NAME(127.0.0.1/8000)/{id}/update/
POST  create user =>       HOST_NAME(127.0.0.1/8000)/create/user/
PUT   edit user =>         HOST_NAME(127.0.0.1/8000)/{id}/user/
```


### Usage:
```
git clone https://github.com/MahdiRahmani80/LEM.Django.git
cd LEM.Django/
python3 manage.py makemigrations       
python3 manage.py migrate             # for create table in sqlite3
python3 manage.py createsuperuser     
python3 manage.py runserver 8000      # Run the web application :)
```

## Screen shots :
<img src="https://raw.githubusercontent.com/MahdiRahmani80/LEM.Django/main/CreateMusic.png">
<img src="https://github.com/MahdiRahmani80/LEM.Django/blob/main/List.png">
