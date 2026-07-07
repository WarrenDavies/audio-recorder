from audiorecorder.audio_recorder import AudioRecorder

config = {
    "sd_default_device": 7
}

audio_recorder = AudioRecorder(config)
np_audio = audio_recorder.record_until_enter_key_pressed()
print(np_audio)
