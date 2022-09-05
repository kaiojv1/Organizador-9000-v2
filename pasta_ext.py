
import os
import PySimpleGUI as sg
from pastas_diretorio import diretorio_arquivos



pasta_para_criar = ["Arquivos_PDF", "Arquivos_EXE", "arquivos_JPEG","arquivos_MP3",
                    "Arquivos_DLL","Arquivos_ZIP","Arquivos_DOCX", "Arquivos_XLSX",
                    "Arquivos_PNG", "Arquivos_JPG","Arquivos_TXT","Arquivos_OUTROS"]



def verificar_extensao(nome_arquivo):
    index = nome_arquivo.rfind(".")
    return nome_arquivo[index:]
            
def criar_pastas(diretorio):
    
    for pastas_criar in pasta_para_criar:
        pasta_diretorio = os.path.join(diretorio, pastas_criar)

        if not os.path.isdir(pasta_diretorio):
            os.mkdir(pasta_diretorio)
            print(f'A pasta {pastas_criar} foi criada')
        else:
            print(f'A pasta {pastas_criar} ja existe')

    nomes_diretorio = os.listdir(diretorio)

    for arquivos in nomes_diretorio:
        extensao = verificar_extensao(arquivos)
        
        while os.path.isfile(os.path.join(diretorio,arquivos)):
            extensao = verificar_extensao(arquivos)
            diretorio_arquivos(diretorio,arquivos,extensao)
            
            
       

            

