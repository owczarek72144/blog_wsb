# 1.Blog App 
Zadanie na zaliczenie przedmiotu 

# 2.Wykorzystane tehcnologie 
-python \
-flask \
-sqllite3 

# 3.Deployment

## 3.1 Zmienne środowiskowe 

```
$ $LOCATION='<twoja_lokacja>'
$ $RESOURCE_GROUP_NAME='<twoja_nazwa_grupy_zasobów>'
$APP_SERVICE_PLAN_NAME='<twoja_nazwa_planu>'
$APP_SERVICE_NAME='<twoja_nazwa_app_service>'
```
## 3.2 Deployment
3.2.1 Utworzenie grupy zasobów azure
```
az group create --location $LOCATION --name $RESOURCE_GROUP_NAME
```
3.2.2 Utworzenie planu app service
```
az appservice plan create --name $APP_SERVICE_PLAN_NAME --resource-group $RESOURCE_GROUP_NAME --sku B1 --is-linux    
```
3.2.3 Utworzenie App Service na podstawie planu
```
az webapp create --name $APP_SERVICE_NAME --runtime 'PYTHON:3.9' \
--plan $APP_SERVICE_PLAN_NAME --resource-group $RESOURCE_GROUP_NAME \
--query 'defaultHostName' --output table
```
3.2.4 Wdrażanie przy pomocy pliku zip.
Utworz archiwum zip zawierajacy pliki aplikacji.
3.2.5 Włączenie automatyzacji kompilacji na platformie azure 
```
az webapp config appsettings set --resource-group $RESOURCE_GROUP_NAME --name $APP_SERVICE_NAME --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true
```
3.2.6 Wdrożenie aplikacji
```
az webapp deploy --name $APP_SERVICE_NAME --resource-group $RESOURCE_GROUP_NAME --src-path news.zip
```
3.2.6 Aplikacja powinna być widoczna pod adresem twojanazwa.azurewebsites.net gdzie twojanazwa to wartość ze zmiennej $APP_SERVICE_NAME




