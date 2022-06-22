import os
import requests

for num in range(1,9):
    print(num)
    for serie in range(1,21):
        serie = str(serie).zfill(2)
        stuff=f's0{num}'
        url = f'http://vihostdgs40.com/video/8ba1d9cac337890b21e1cffd891b67a9/serials/Charmed/{stuff}/Charmed.S0{num}E{serie}.mp4'
        name=url.split('/')[-1]
        if not os.path.isdir(f'D:\pythonProject21\some\charmentStuff{num}'):
            os.mkdir(f'D:\pythonProject21\some\charmentStuff{num}')        #check exists directory
        os.chdir('..')
        os.chdir(f'D:\pythonProject21\some\charmentStuff{num}')
        print("NOW:\n",stuff, serie)
        if name in  os.listdir():
            continue
        video=requests.get(url)
        k=0
        chunk_size = 50000
        for chunk in video.iter_content(chunk_size=chunk_size):
            k=k+1
            print((chunk_size)/(float(video.headers['Content-Length']))*k*100)
        print(name)
        with open(f'./charmentStuff{num}/{name}', 'wb') as w:
            w.write(video.content)