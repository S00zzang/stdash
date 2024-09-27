# stdash

## GOAL
+ want to know the request/processing results of the image processing system.
+ want to know which request/handler is in trouble within the cluster. - Just requesting and not processing

## Basic Tools
+ No serious errors should be seen even in situations where API is not functioning (BE Down)
+ Configuring Basic Features to Work

# Usage
```
$ source .venv/bin/activate
$ streamlit run src/stdash/home.py
```

## STEP 1
```
# Start with chart using a python, pandas
```
![image](https://github.com/user-attachments/assets/11e8cfa7-4be1-45ee-9abc-a858d7d837b3)



## STEP 2
```
# Statistics / imbalances between requester and handler (identify who has a problem with processing) -> Add VIEW

# deploy
# docker
# multi pages
# streamlit chart
```
+ deploy
  
https://s00zzang-stdash.streamlit.app/

+ docker
```
sudo docker pull s00zzang/stdash:0.2.0 
sudo docker run -d -p 8501:8501 s00zzang/stdash:0.2.0
```

![image](https://github.com/user-attachments/assets/b1b023a6-aab8-4f3b-89f5-b3ccf4c558e3)

+ multi pages

![image](https://github.com/user-attachments/assets/9595539f-ca6e-4653-af31-bbd39c0c56cd)

+ streamlit chart

![image](https://github.com/user-attachments/assets/f7500772-8727-43ab-a7c8-454a3dbd3f0b)

  
## STEP 3
```
# file upload
# Apply hotdog 
```
