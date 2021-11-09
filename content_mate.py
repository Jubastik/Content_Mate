from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import VideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import numpy as np


def pause_handler(end_process, input_path, output_path, sensitivity=0.10, indent=0.2, step_vol=0.1, log=False, log_file=""):
    def remove_silence(clip, sensitivity, indent, step, log = False, log_file = ""):
        # Разбивает клип на звуковые части с учетом шага и преобразует в массив.
        cut_volume = lambda i: clip.audio.subclip(i, i + step).to_soundarray(fps=44100)

        # нормализация звуковой дорожки
        volume = lambda array: abs(array).mean()

        # Дельта между максимальной и минимальной громкостью
        volume_delta = lambda array: max(array) - min(array)

        # разбиваем клип на части
        parts_clip = np.arange(0, clip.duration, step)
        # разбиваем звук на части
        parts_volume = [volume(cut_volume(i)) for i in parts_clip]
        # максимальная громкость в клипе
        max_volume = max(parts_volume)
        # порог шума, свыше которого есть информация
        del_volume = sensitivity * volume_delta(parts_volume)

        ok_parts = []  # части с информацией будут сохранены в формате (старт, стоп)
        start = -1
        for c, vol in zip(parts_clip, parts_volume):
            if start == -1 and vol > del_volume:
                # сохраняем начало информации
                start = c - indent
            if start != -1 and vol < del_volume:
                # сохраняем пару начало\конец информации с учетом отступов
                ok_parts.append([start, c + indent])
                start = -1
        if start != -1:
            ok_parts.append([start, c + indent])
        # Исправляем выходы за пределы клипа
        if ok_parts[0][0] < 0:
            ok_parts[0][0] = 0
        if ok_parts[-1][1] > clip.duration:
            ok_parts[-1][1] = clip.duration

        if len(ok_parts) > 1:
            # убираем накладывание частей клипа
            i = 0
            while i < (len(ok_parts) - 1):
                if ok_parts[i][1] >= ok_parts[i + 1][0]:
                    ok_parts[i][1] = ok_parts[i + 1][1]
                    del ok_parts[i + 1]
                else:
                    i += 1
        if log:
            log_file.write(f"Обработка завершена, начало склеивания клипов {path}\n")

        out_clip = [clip.subclip(s, f) for s, f in ok_parts]
        return concatenate_videoclips(out_clip)


    for path in input_path:
        if log:
            log_file.write(f"Старт обработки файла {path}\n")
        try:
            with VideoFileClip(path) as clip:  # создание клипа
                clip = remove_silence(clip, sensitivity, indent, step_vol, log, log_file)
                if log:
                    log_file.write(f"Клип склеен, начало создания .mp4 {path}\n")
                clip.write_videofile(f"{output_path}/short-{path.split('/')[-1]}", preset="superfast")
                if log:
                    log_file.write(f"Видеофайл обработан {path}\n")
        except:
            if log:
                log_file.write(f"Ошибка при обработке файла {path}\n")
    end_process()
    return
