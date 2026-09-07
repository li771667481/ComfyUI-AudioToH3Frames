# ComfyUI-AudioToH3Frames

Audio → MiniMax H3 frame count (17k+5 grid). Reads the AUDIO tensors from LoadAudio and computes the grid-aligned frame count for the MiniMaxH3ReferenceToVideo length input, mirroring ComfyUI_MiniMaxH3_Director minimax_align_frame_count.

- No file I/O, no replacement of existing nodes, purely additive.
- Remove the folder to revert to fixed-length behavior.
