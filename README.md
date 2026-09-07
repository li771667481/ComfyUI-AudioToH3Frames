# ComfyUI-AudioToH3Frames

Audio → MiniMax H3 frame count (17k+5 grid). Reads the AUDIO tensors from LoadAudio and computes the grid-aligned frame count for the MiniMaxH3ReferenceToVideo length input, mirroring ComfyUI_MiniMaxH3_Director minimax_align_frame_count.

- No file I/O, no replacement of existing nodes, purely additive.
- Remove the folder to revert to fixed-length behavior.

## 快速使用（带工作流）

- `h3_r2v_slim_api.json`：MiniMax H3 R2V 瘦版工作流（API 格式，可直接导入 ComfyUI 或字字动画），
  节点 24 已接好本节点；`length` 跟随参考音频时长（17k+5 网格上取整），音频缺失时固定 243 帧（约 10 秒）。
- 参考图/参考音频/提示词/seed 均为平铺字段；图片音频文件按各自环境替换。

### 安装

1. 把整个 `ComfyUI-AudioToH3Frames` 文件夹放进 `ComfyUI/custom_nodes/`
2. 重启 ComfyUI
3. 导入 `h3_r2v_slim_api.json`（或手动添加节点「音频→H3帧数」：
   `LoadAudio.audio` → 节点 `audio` 口，节点 `h3_frames` → `MiniMaxH3ReferenceToVideo.length`）
