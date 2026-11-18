# audiograb

`audiograb` is a lightweight, clean Python package for recording audio from your microphone until you press **Enter**. Built on top of `sounddevice` and `numpy`, it uses Pydantic for robust configuration validation.

---

## Features

* **Simple Workflow:** Start recording immediately and stop with a single keystroke.
* **Pydantic Validation:** Easily configure and validate recording parameters (sample rate, channels, data type) with type safety.
* **Device Control:** Seamlessly target specific audio input devices using `sounddevice` integration.

---

## Installation

You can install `audiograb` from PyPI:

```bash
pip install audiograb

```

---

## Quick Start

Here is how you can use `audiograb` to record audio into a NumPy array:

```python
import numpy as np
from audiograb.audio_recorder import AudioRecorder

# Configure your options (e.g., specifying a custom sounddevice input device)
config = {
    "sd_default_device": 7,
    "samplerate": 16000,
    "channels": 1,
    "dtype": "float32"
}

# Initialize the recorder
audio_recorder = AudioRecorder(config)

# Record until you press Enter in the terminal
np_audio = audio_recorder.record_until_enter_key_pressed()

print("Recorded audio shape:", np_audio.shape)
print(np_audio)

```

---

## Configuration

`audiograb` uses Pydantic to validate parameters passed into the configuration dictionary. The default parameters available in the schema are:

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `samplerate` | `int` | `16000` | Sampling rate in Hz. |
| `channels` | `int` | `1` | Number of audio channels (e.g., `1` for mono, `2` for stereo). |
| `dtype` | `str` | `"float32"` | NumPy data type for the audio samples. |
| `sd_default_device` | `int` / `str` | *system default* | Optional device ID or name for `sounddevice`. |

---

## License

Distributed under the MIT License. See `LICENSE` for more information.