from kokoro import KPipeline
from abc import ABC, abstractmethod
import io
import soundfile as sf

class TextToSpeachService(ABC):
    @abstractmethod
    def generate(self, text: str, voice: str, speed: int):
        pass


class KokoroTextToSpeachService(TextToSpeachService):
    def __init__(self):
        self.pipeline = KPipeline(lang_code='a')

    def generate(self, text: str, voice: str = 'af_heart', speed: int = 1):
        self.generator = self.pipeline(
            text, voice=voice, 
            speed=speed, split_pattern=r'\.+'
        )
        for i, (gs, ps, audio) in enumerate(self.generator):
            sf.write(f'audio_{i}.wav', audio, 24000, format='wav')

