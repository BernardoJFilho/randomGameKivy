import requests , os

def getImg(game):
    try:
        link = game['thumbnail']
        response = requests.get(link)
        diretorioDestino = 'randomGameKivy/src/images'
        
        image_data = response.content
        
        nameImg = game['title'].replace(" ", "")
        file_name = nameImg+'.jpg'
        caminho_completo = os.path.join(diretorioDestino, file_name)
        
        with open(caminho_completo, 'wb') as file:
            file.write(image_data)
        
        return diretorioDestino+'/'+file_name
    except:
        return 'images/notFound/imageNotFound.jpg'