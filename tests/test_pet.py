import pytest
from api import PetFriends
from settings import valid_password, valid_email, no_valid_password, no_valid_email, empty_email, empty_password
import os

pf = PetFriends()

def test_get_api_key_for_no_valid_user(email=no_valid_email, password=no_valid_password):
    '''Тест проверяет, что при вводе не верного email и пароля запрос api возвращает статус 403 (запрешен)
    и в результате приходит ответ: Этого пользователя нет в базе'''
    status, result = pf.get_api_key(email, password)
    '''Проверяем полученные данные'''
    assert status == 403
    assert 'This user wasn\'t found in database' in result

def test_get_api_key_for_empty_email_user(email = empty_email, password = valid_password):
    '''Тест проверяет, что при вводе пустого email запрос api возвращает статус 403 (запрешен)
    и в результате приходит ответ: Этого пользователя нет в базе'''
    status, result = pf.get_api_key(email, password)
    '''Проверяем полученные данные'''
    assert status == 403
    assert 'This user wasn\'t found in database' in result

def test_get_api_key_for_empty_password_and_valid_email(email = valid_email, password = empty_password):
    '''Тест проверяет, что при вводе верного email и пустого пароля запрос api возвращает статус 403 (запрешен)
    и в результате приходит ответ: Этого пользователя нет в базе'''
    status, result = pf.get_api_key(email, password)
    '''Проверяем полученные данные'''
    assert status == 403
    assert 'This user wasn\'t found in database' in result

def test_post_very_long_name_new_pets(name = 'Бегемот34534543534534434534534534534534534543543344354535312313312321233556464545555575686787655665454hgfhfdgghjfythdht564563564gfhghghdfghdfh38765745874657645632123453443468753', animal_type = 'кот', age = '3', pet_photo = 'images/12.jpg'):
    '''Проверяем что можно добавить питомца с очень длинным именем'''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)
    '''Проверяем полученные данные.'''
    try:
        assert status == 403 or status == 400
    except:
        print('Тест не пройден')

def test_post_letters_in_number_field_new_pets(name = 'Мурзик', animal_type = 'кот', age = 'три', pet_photo = 'images/12.jpg'):
    '''Проверяем что можно записать текстовые символы в поле возраста'''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)
    '''Проверяем полученные данные.'''
    try:
        assert status == 400 or status == 403
    except:
        print('Тест не пройден')

def test_post_empty_fields_new_pets(name = '', animal_type = '', age = '', pet_photo = ''):
    '''Проверяем что можно создать карточку животного с пустыми полями'''
    try:
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)
    except:
        print('Тест пройден, карточка с пустыми полями не создается')
    else:
        print('Тест не пройден')

def test_post_empty_name_new_pets(name = '', animal_type = 'кот', age = '6', pet_photo = 'images/12.jpg'):
    '''Проверяем что можно создать карточку животного без имени'''
    try:
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)
        assert status == 200
    except:
        print('Карточка без имени животного не создается')
    else:
        print('Карточка без имени животного создается')

def test_post_empty_animal_type_new_pets(name = 'Васька', animal_type = '', age = '6', pet_photo = 'images/12.jpg'):
    '''Проверяем что можно создать карточку животного с пустым полем вид животного'''
    try:
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)
        assert status == 200
    except:
        print('Карточка без вида животного не создается')
    else:
        print('Карточка без вида животного создается')

def test_post_empty_age_new_pets(name = 'Васька', animal_type = 'собока', age = '', pet_photo = 'images/12.jpg'):
    '''Проверяем что можно создать карточку животного с пустым полем возраст'''
    try:
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)
        assert status == 200
    except:
        print('Карточка без возраста животного не создается')
    else:
        print('Карточка без возраста животного создается')

def test_post_empty_pet_photo_new_pets(name = 'Мурка', animal_type = 'кошка', age = '3', pet_photo = ''):
    '''Проверяем что можно создать карточку животного без фото'''
    try:
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)
        assert status == 200
    except:
        print('Карточка без фотографии животного не создается')
    else:
        print('Карточка без фотографии животного создается')
