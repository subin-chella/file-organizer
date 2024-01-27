from os.path import isfile, join, splitext
import os;
import shutil;

class FileOrg:
  def move_files(self):  
    txt_file_formats=['.txt']
    pdf_file_formats=['.pdf','.PDF']
    doc_file_formats=['.doc','.docx']
    excel_file_formats=['.xls','.xlsx','.csv']
    video_file_formats=['.mp4','.mov','.avi','.flv','.webm','.mkv','.mpeg','.svi']
    audio_file_formats=['.mp3','.wave','.wav']
    exe_file_formats=['.exe','.msi']
    archive_file_formats = [ ".zip", ".tar", ".gz", ".bz2", ".7z", ".rar", ".iso", ".wim", ".dmg", ".hdi", ".ape", ".cue", ".nrg", ".img", ".iso",'.jar' ]
    image_file_formats = ['.jpg','.JPG', '.jpeg', '.jpe', '.jif', '.jfif', '.png', '.gif', '.webp', '.tiff', '.tif', '.psd', '.bmp', '.dib','.svg']
    cert_formats = ['.ppk','.crt','.cer','.pem','.json']
    other_formats = ['.xml','.srt','.bat','.key','.json','.dll','.htm','.html','.md','.java','.ica','.sh','.properties']
    
    Dict = {'TEXT': txt_file_formats, 'PDFS':pdf_file_formats,
            'DOCS':doc_file_formats,
            'EXCEL':excel_file_formats,
            'VIDEOS':video_file_formats,
            'AUDIOS':audio_file_formats,
            'ARCHIVES':archive_file_formats,
            'IMAGES':image_file_formats,
            'EXE':exe_file_formats,
            'CERT_KEYS':cert_formats,
            'OTHERS': other_formats
            }
    print(Dict)
    download_folder_path = 'C:\\Users\LENOVO\Downloads'
    os.chdir(download_folder_path)
    onlyfiles = [f for f in os.listdir(download_folder_path) if isfile(join(download_folder_path, f))]
    for key, value in Dict.items():
        print(key)
        print(value)
        files = [f for f in onlyfiles if splitext(f)[1] in value ]
        for file in files:
            print('Moving file '+ file)
            shutil.move(join(download_folder_path, file), join(download_folder_path+'//'+key, file)) 
            
