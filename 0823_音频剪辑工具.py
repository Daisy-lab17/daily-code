from pydub import AudioSegment
import os

class AudioTool:
    def __init__(self):
        self.SECOND = 1000

    # 音频裁剪
    def cut_audio(self, input_path, output_path, start_sec, end_sec):
        try:
            audio = AudioSegment.from_file(input_path)
            start = start_sec * self.SECOND
            end = end_sec * self.SECOND
            cut_audio = audio[start:end]
            cut_audio.export(output_path, format="mp3")
            print(f"裁剪完成，输出：{output_path}")
        except Exception as e:
            print(f"裁剪失败：{e}")

    # 多音频拼接
    def merge_audio(self, audio_path_list, output_path):
        if not audio_path_list:
            print("音频文件不能为空")
            return
        combined = AudioSegment.from_file(audio_path_list[0])
        for path in audio_path_list[1:]:
            seg = AudioSegment.from_file(path)
            combined += seg
        combined.export(output_path, format="mp3")
        print(f"拼接完成，输出：{output_path}")

    # 调整音量
    def change_volume(self, input_path, output_path, db):
        audio = AudioSegment.from_file(input_path)
        new_audio = audio + db
        new_audio.export(output_path, format="mp3")
        print(f"音量调整完成，{db}分贝")

if __name__ == "__main__":
    tool = AudioTool()
    # 示例：裁剪0-10秒音频
    tool.cut_audio("input.mp3", "cut.mp3", 0, 10)
    # 示例：拼接两段音频
    # tool.merge_audio(["a.mp3", "b.mp3"], "merge.mp3")
    # 示例：音量+5db
    # tool.change_volume("input.mp3", "vol.mp3", 5)