import torch
import torchvision

print(torch.__version__)
print(torchvision.__version__)

boxes = torch.tensor([[0, 0, 1, 1], [0, 0, 1, 1]], dtype=torch.float)
scores = torch.tensor([0.9, 0.8], dtype=torch.float)
nms_indices = torchvision.ops.nms(boxes, scores, 0.5)
print(nms_indices)
