from pytube import YouTube

# TODO  sayfada yt.streams'a göre birkaç link çıkıcak ve onlara göre kalite farklı indirme yapıcaz
# TODO  daha sonra videonun resmi ve başlığı gelicek

#! yt.streams.filter(progressive=True) ses ve videolu olanları listeliyor
#! yt.streams.filter(only_audio=True) ses olanları listeliyor
#! yt.streams.filter(file_extensions=True) mp4 video olanları listeliyor
# ?--------------------------------------------------------------------------
#! yt.captions yazınca altyazılar çıkıyor
#! caption = yt.captions.get_by_language_code('tr') verince türkçe altyazıyı alır
#! caption.xml_captions xml formatını gösteriyor
#! caption.generate_srt_captions() verince str'ye çeviriyor
# ?--------------------------------------------------------------------------
#! p = Playlist('playlist linki') verince p adlı bir playlist oluyor
#! p = Playlist('https://www.youtube.com/watch?v=41qgdwd3zAg&list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n') veya playlist içindeki bir videodan
#! for video in p.videos: video.streams.first().download() şeklinde de hepsini indirebiliriz
#! for url in p.video_urls[:3]: url.streams.first().download() ilk üç videosunu indirmek için
# ?--------------------------------------------------------------------------
#! >>> from pytube import Playlist, YouTube
#! >>> playlist_url = 'https://youtube.com/playlist?list=special_playlist_id'
#! >>> p = Playlist(playlist_url)
#! >>> for url in p.video_urls:
#! ...     try:
#! ...         yt = YouTube(url)
#! ...     except VideoUnavailable:
#! ...         print(f'Video {url} is unavaialable, skipping.')
#! ...     else:
#! ...         print(f'Downloading video: {url}')
#! ...         yt.streams.get_highest_resolution().download("/home/ege/Downloads")
# ?--------------------------------------------------------------------------
#! yt.set_filename('Ege Paksoy ilk video')
#! videos = yt.get_videos()
#! for v in videos: print(v.resolution) video kalitesini veriyor


def video_download(yt):
    yt[0].streams[yt[1]].download("/home/ege/Downloads")


def video_info(link):
    try:
        yt = YouTube(link)
    except VideoUnavailable:
        print('Video bulunamadı\n'+VideoUnavailable)
    else:
        resos = {}
        x = 0
        for stream in yt.streams.filter(progressive=True):
            print(stream.resolution)
            resos[stream.resolution] = x
            x += 1
        reso = input('Kalite seçin: ')
        reso = str(reso)

        if "1080" in reso:
            resolution = resos["1080p"]
        if "720" in reso:
            resolution = resos["720p"]
        if "480" in reso:
            resolution = resos["480p"]
        if "360" in reso:
            resolution = resos["360p"]

    return yt, resolution
