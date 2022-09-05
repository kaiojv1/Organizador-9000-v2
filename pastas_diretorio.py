import os
import PySimpleGUI as sg

arquivos_PDF = ['.pdf','.PDF','.Pdf']
arquivos_TXT = ['.txt','.TXT']
arquvios_EXE  = ['.exe','.app']
arquvios_DLL  = ['.dll']
arquvios_ZIP = ['.zip','.rar']
arquvios_MP3  = ['.mp3','.MP3']
arquvios_JPEG  = ['.jpeg','.Jpeg','.jpg','.png']
arquvios_XLSX  = ['.xlsx','.xls']
arquvios_DOCX  = ['.docx','.doc']

def diretorio_arquivos(diretorio, arquivos, extensao):
    pasta_pdf = os.path.join(diretorio, "Arquivos_PDF")
    pasta_exe = os.path.join(diretorio, "Arquivos_EXE")
    pasta_jpeg = os.path.join(diretorio, "arquivos_JPEG")
    pasta_mp3 = os.path.join(diretorio, "arquivos_MP3")
    pasta_dll = os.path.join(diretorio, "Arquivos_DLL")
    pasta_ZIP = os.path.join(diretorio, "Arquivos_ZIP")
    pasta_DOCX = os.path.join(diretorio, "Arquivos_DOCX")
    pasta_XLSX = os.path.join(diretorio, "Arquivos_XLSX")
    pasta_JPG = os.path.join(diretorio, "Arquivos_JPG")
    pasta_PNG = os.path.join(diretorio, "Arquivos_PNG")
    pasta_TXT = os.path.join(diretorio, "Arquivos_TXT")
    pasta_outros = os.path.join(diretorio, "Arquivos_OUTROS")

    if extensao in arquivos_PDF:
        nova_pasta = pasta_pdf

    elif extensao in arquvios_EXE:
        nova_pasta = pasta_exe

    elif extensao in arquvios_JPEG:
        nova_pasta = pasta_jpeg

    elif extensao in arquvios_MP3:
        nova_pasta = pasta_mp3

    elif extensao in  arquivos_TXT:
        nova_pasta = pasta_TXT

    elif extensao in  arquvios_ZIP:
        nova_pasta = pasta_ZIP

    elif extensao in  pasta_PNG:
        nova_pasta = pasta_PNG

    elif extensao in arquvios_XLSX:
        nova_pasta = pasta_XLSX

    elif extensao in  arquvios_DOCX :
        nova_pasta = pasta_DOCX

    elif extensao in arquvios_DLL:
        nova_pasta = pasta_dll
    else:
        nova_pasta = pasta_outros

    velho = os.path.join(diretorio, arquivos)
    novo = os.path.join(nova_pasta, arquivos)
    os.rename(velho,novo)
    