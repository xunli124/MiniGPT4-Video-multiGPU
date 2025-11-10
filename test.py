import torch
ckpt_path = "video_llama_checkpoint_last.pth"
ckpt = torch.load(ckpt_path, map_location="cpu")
print(ckpt.keys())
