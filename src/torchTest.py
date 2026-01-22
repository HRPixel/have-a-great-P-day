import torch

print ("CUDA Available: ", torch.cuda.is_available())


print (f"GPU可用性：{torch.cuda.is_available()}")
if torch.cuda.is_available():
    print (f"Pytorch版本：{torch.__version__}")
    print (f"CUDA版本：{torch.version.cuda}")
    print (f"CUDNN版本：{torch.backends.cudnn.version()}")
    print (f"GPU名称：{torch.cuda.get_device_name(0)}")
    print (f"GPU数量：{torch.cuda.device_count()}\n")

print(f"GPU Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"PyTorch version: {torch.__version__}")
    
    print(f"CUDA version: {torch.version.cuda}")
    print(f"CUDNN version: {torch.backends.cudnn.version()}")
    print(f"GPU name: {torch.cuda.get_device_name(0)}")
    print(f"Number of GPUs: {torch.cuda.device_count()}\n")