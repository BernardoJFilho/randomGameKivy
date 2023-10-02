import requests , os

def getImg(game):
    try:
        link = game['thumbnail']
        response = requests.get(link)
        
        image_data = response.content
        
        nameImg = game['title'].replace(" ", "")
        file_name = nameImg+'.jpg'
        caminho_completo = os.path.join('src/images', file_name)
        
        with open(caminho_completo, 'wb') as file:
            file.write(image_data)
        
        return 'src/images/'+file_name
    except Exception as e:
        print("Erro:", str(e))
        return 'images/notFound/imageNotFound.jpg'
