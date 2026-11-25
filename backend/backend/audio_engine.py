import numpy as np
def analyse_audio(audio_bytes):
    """
    Analyse incoming 16-bit PCM audio.
    Returns signal measurements for the dashboard.
    """
    if not audio_bytes:
        return None
    # Convert incoming bytes into 16-bit audio samples
    audio = np.frombuffer(audio_bytes, dtype=np.int16)
    if len(audio) == 0:
        return None
    # Normalize audio to the range -1 to +1
    samples = audio.astype(np.float32) / 32768.0
    # 1. RMS loudness
    rms = float(np.sqrt(np.mean(samples ** 2)))
    # 2. Peak amplitude
    peak = float(np.max(np.abs(samples)))
    # 3. Zero-crossing rate
    signs = np.sign(samples)
    zero_crossings = np.sum(signs[1:] != signs[:-1])
    zcr = float(zero_crossings / max(len(samples) - 1, 1))
    # 4. Spectral centroid
    spectrum = np.abs(np.fft.rfft(samples))
    frequencies = np.fft.rfftfreq(
        len(samples),
        d=1 / 16000
    )
    total_energy = np.sum(spectrum)
    if total_energy > 0:
        centroid = float(
            np.sum(frequencies * spectrum) / total_energy
        )
    else:
        centroid = 0.0
    return {
        "rms": round(rms, 4),
        "peak": round(peak, 4),
        "zero_crossing_rate": round(zcr, 4),
        "spectral_centroid": round(centroid, 2),
        "samples": int(len(samples))
    }
