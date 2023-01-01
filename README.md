# Self driving car in simulated env
Author - Shubhom VT, Rudresh Lonkar

Date - 5 October 2022 

---

## Description

Autonomous car using behavioral cloning with CNN 
- Generate data using Udacity simulator
---
## Installation


Create a virtual environment:
  Open the command prompt and paste the following-
  ```
  conda create --name Autocar python=3.9
  conda activate Autocar
  ```
Install Pytorch- 
 ```
 conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch (or the latest version)
 ```
Verify PyTorch installation-
  
  Open VS Code -> change the interpreter to venv (Ctrl+shift+P)-> Type the following code
  ```  
  import torch

  device =  "cuda" if torch.cuda.is_available() else "cpu"
  print(device)
  ```
---
## Running the Simulation

## Dependencies
