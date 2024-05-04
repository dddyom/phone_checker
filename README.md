# Phone checker

Сервис для поиска оператора и региона по номеру телефона.

Алгоритм запуска

- Загрузка репозитория

```bash
git clone https://github.com/dddyom/phone_checker.git && cd phone_checker
```
- Заполнение .env

```bash
cp .env.example .env
sed -i '/^REGISTRY_URL=/d' .env && echo "REGISTRY_URL=<registry_url>" >> .env
sed -i '/^UPDATE_REGISTRY_ON_START=/d' .env && echo "UPDATE_REGISTRY_ON_START=True" >> .env
sed -i '/^SECRET_KEY=/d' .env && echo "SECRET_KEY=<secret_key>" >> .env
```
- Запуск docker-compose
```bash
docker-compose up --build
```

Для заполнения .env необходимо указать registry_url и secret_key
`UPDATE_REGISTRY_ON_START` необходим при первой загрузке, для явной выгрузки реестра в БД сервиса. Далее БД будет обновляться раз в сутки.
