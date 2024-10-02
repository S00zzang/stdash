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
```

+ file upload
```
cd code/mnist
uvicorn src.mnist.main:app --reload
```
![image](https://github.com/user-attachments/assets/107bbc08-a65e-45bb-8947-b0a57cade5cb)
**file name must be in (code/mnist/note/train_img)**

## STEP 4
```
# Apply hotdog
```

+ Apply hotdog
  
  If not hotdog..
  
  ![image](https://github.com/user-attachments/assets/cb8fc901-5b9a-4d38-9b62-776af41fd153)
  ![image](https://github.com/user-attachments/assets/76b609c8-8ba5-42ac-8f94-a1f08430e1f3)

  If hotdog..

  ![image](https://github.com/user-attachments/assets/81a6eb27-3c01-45c7-929a-d17060ddd666)
  ![image](https://github.com/user-attachments/assets/06bbff48-c392-4e58-8425-dd07adbb3290)



