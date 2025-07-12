from pytubefix import YouTube
import os
def DownloadAudio(link, caminho_salvar):
    yt = YouTube(link)
    video_title = yt.title
    video_title = "".join(
        char for char in video_title if char.isalnum() or char in [" ", "-", "_"]
    )

    caminho_completo = os.path.join(caminho_salvar, f"{video_title}.mp4")

    try:
        audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
        audio_stream.download(
            output_path=caminho_salvar, filename=f"{video_title}-cheevi.mp3"
        )
    except Exception as e:
        print(e)

    if os.path.exists(caminho_completo):
        print(f"O arquivo {caminho_completo} foi salvo.")
        os.startfile(caminho_salvar)
    else:
        print(f"O arquivo {caminho_completo} não foi encontrado.")


def DownloadVideo(link, caminho_salvar):
    yt = YouTube(link)
    video_title = yt.title

    video_title = "".join(
        char for char in video_title if char.isalnum() or char in [" ", "-", "_"]
    )

    caminho_completo = os.path.join(caminho_salvar, f"{video_title}.mp4")

    try:
        yt.streams.filter(
            progressive=True, file_extension="mp4"
        ).get_highest_resolution().download(
            output_path=caminho_salvar, filename=f"{video_title}.mp4"
        )
    except Exception as e:
        print(e)

    if os.path.exists(caminho_completo):
        print(f"O arquivo {caminho_completo} foi salvo.")
        os.startfile(caminho_salvar)
    else:
        print(f"O arquivo {caminho_completo} não foi encontrado.")
