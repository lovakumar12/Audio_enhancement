from pedalboard.io import AudioFile
from pedalboard import *
import noisereduce as nr

sr=44100
with AudioFile('audios/audio4.wav').resampled_to(sr) as f:

    audio = f.read(f.frames)

reduced_noise = nr.reduce_noise(y=audio, sr=sr, stationary=True, prop_decrease=0.75)


##############good for audio1,2 3
# board = Pedalboard([
#     NoiseGate(threshold_db=-30, ratio=1.5, release_ms=250),
#     Compressor(threshold_db=-16, ratio=2.5),
#     LowShelfFilter(cutoff_frequency_hz=400, gain_db=10, q=1),
#     Gain(gain_db=10)
# ])


#############good for audio4 and 1,2,3,4
# board = Pedalboard([
#     NoiseGate(threshold_db=-25, ratio=2.0, release_ms=300),  # Adjusted NoiseGate parameters
#     Compressor(threshold_db=-16, ratio=2.5),
#     LowShelfFilter(cutoff_frequency_hz=400, gain_db=5, q=1),  # Adjusted LowShelfFilter parameters
#     Gain(gain_db=10)
# ])


board = Pedalboard([
    NoiseGate(threshold_db=-30, ratio=3.0, release_ms=400),  # Adjusted NoiseGate parameters
    Compressor(threshold_db=-20, ratio=3.0),  # Adjusted Compressor parameters
    LowShelfFilter(cutoff_frequency_hz=300, gain_db=0, q=1),  # Adjusted LowShelfFilter parameters
    Gain(gain_db=5)  # Adjusted Gain parameters
])

effected = board(reduced_noise, sr)


with AudioFile('audios/audio4_enhenced.wav', 'w', sr, effected.shape[0]) as f:
  f.write(effected)




















  """
print('original audio')
sd.play(audio[0],sr)
sd.wait()

print('enhanced audio')
sd.play(effected[0],sr)
sd.wait()

"""