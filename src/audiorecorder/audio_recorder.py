from pydantic import BaseModel
import sounddevice as sd
import soundfile as sf
import numpy as np

class AudioRecorder():
    """
    """
    def __init__(self, config):
        self.config = config
        if "sd_default_device" in self.config:
            sd.default.device = self.config["sd_default_device"]


    def get_kwargs(self):
        ParamsSchema = self.get_params_schema()
        validated = ParamsSchema(**self.config)

        kwargs = {
            k: v
            for k, v in validated.model_dump().items()
        }

        return kwargs


    def record_until_enter_key_pressed(self):
        print("Recording... Press Enter to stop.")
        
        audio = []
        kwargs = self.get_kwargs()

        def _callback(indata, frames, time, status):
            audio.append(indata.copy())

        with sd.InputStream(
            callback=_callback,
            **kwargs
        ):
            input()

        audio_np = np.concatenate(audio, axis=0)

        return audio_np    

    
    def get_params_schema(self):
        """
        Returns Pydantic class listing params that the model can accept
        """
        class ParamsSchema(BaseModel):
            samplerate: int = 16000
            channels: int = 1
            dtype: str = "float32"

        return ParamsSchema