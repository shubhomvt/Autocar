# Autocar

Autonomous car using behavioral cloning 

1. Create a virtual environment:
  Open the command prompt and paste the following-
  conda create --name Autocar python=3.9
  conda activate Autocar
2. Install Pytorch- 
 conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch (or the latest version)
3. Verify PyTorch installation-
  Open VS Code -> change the interpreter to venv (Ctrl+shift+P)-> Type the following code  
  import torch

  device =  "cuda" if torch.cuda.is_available() else "cpu"
  print(device)
