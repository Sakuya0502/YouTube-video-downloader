from yt_dlp import YoutubeDL

class Download:
    def __init__(self):
        pass
    def get_title(self, yturl):
        info = YoutubeDL().extract_info(yturl, download=False)
        video_title = info.get('title', None)
        return str(video_title)
    def is_error(self, yturl: None, filename: None, outputfile: None):
        if yturl == None or outputfile == '':
            return False
        if filename == None and yturl != None and outputfile != '':
            return True
        if filename != None and yturl != None and outputfile != '':
            return True
    def nofileName(self, yturl, outputfile):
        title = Download().get_title(yturl)
        Down = Download().download_vids(yturl, title, outputfile)
        if Down:
            return True
        else:
            False
    def download_vids(self, url, file_name, output_path):
        download_data = {'format': 'best','outtmpl': f'{output_path}\{file_name}.mp4'}
        try:
            YoutubeDL(download_data).download([url])
            return True
        except:
            return False