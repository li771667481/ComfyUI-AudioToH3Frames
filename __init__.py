"""AUDIO -> MiniMax H3 frame count (17k+5 grid, video >= audio).

Only reads the AUDIO tensors already produced by LoadAudio, so it is a pure
addition (no LoadAudio replacement, no file I/O): feed it the same audio that
feeds <Audio 1>. Empty/invalid audio falls back to fallback_frames; audio 未接
(无音频输入)时同样回退 fallback_frames(默认 243 = 约10.1秒)。

Grid rule mirrors ComfyUI_MiniMaxH3_Director's minimax_align_frame_count().
"""

from __future__ import annotations

import torch


class AudioToH3Frames:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "min_frames": ("INT", {"default": 124, "min": 5, "max": 362, "step": 17}),
                "max_frames": ("INT", {"default": 362, "min": 5, "max": 362, "step": 17}),
                "fallback_frames": ("INT", {"default": 243, "min": 5, "max": 362, "step": 17,
                                            "tooltip": "音频无效/空/未接时使用（243 = 约10.1秒 = 固定10秒档）"}),
            },
            "optional": {
                "audio": ("AUDIO",),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("h3_frames", "audio_seconds")
    FUNCTION = "convert"
    CATEGORY = "audio/minimax"

    def convert(self, audio=None, min_frames=124, max_frames=362, fallback_frames=243):
        if not isinstance(audio, dict):
            # 无音频输入(未接线/节点删除):固定回退,默认 243 帧(=~10.1秒)
            return (int(fallback_frames), 0.0)
        wave = audio.get("waveform")
        sr = int(audio.get("sample_rate") or 24000)
        samples = int(wave.shape[-1]) if torch.is_tensor(wave) and wave.numel() > 0 else 0
        if samples <= 0 or sr <= 0:
            return (int(fallback_frames), 0.0)
        seconds = samples / float(sr)
        n = max(5, int(seconds * 24 + 0.999999))
        while n % 17 != 5:
            n += 1
        n = max(min_frames, min(max_frames, n))
        return (n, round(seconds, 3))


NODE_CLASS_MAPPINGS = {"AudioToH3Frames": AudioToH3Frames}
NODE_DISPLAY_NAME_MAPPINGS = {"AudioToH3Frames": "音频→H3帧数 (17k+5)"}
