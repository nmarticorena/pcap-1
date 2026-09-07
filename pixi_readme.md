# PCAP Wrapper
Meta repository to install all the dependencies of pcap

## Clone this repo

```
git clone --recursive git@github.com:nmarticorena/pcap_experiments.git
```

## Install IsaacGym


To install IsaacGym please download and extract `isaacgym` available [here](https://developer.nvidia.com/isaac-gym/download) in this folder.

## Install dependencies
To ensure all dependencies are installed in a reproducible manner, we use the package management tool [pixi](https://pixi.prefix.dev/latest/).
### Install Pixi
If you haven't installed [pixi](https://pixi.prefix.dev/latest/) yet, please run the following command in your terminal:
```
curl -fsSL https://pixi.sh/install.sh | bash
```
*After installation, restart your terminal or source your shell for the changes to take effect*. For more details, refer to the [**pixi documentation**](https://pixi.sh/latest/).
### Install deps
Then to install all the dependencies please run:
```
pixi install
```

## Generate Trees
To generate trees and visualize them you can see the original notebook of `pcap` available by calling:
```
pixi run notebooks
```

## Train the robot
To train the `franka` reaching version in sim run the following:
```
pixi run bash pcap/source/reinforcement/ige/ige_task_runner.sh \                                    
  task=Sim2RealFrankaTreeTactileVoxelReach \                                                        
  num_envs=8192 \                                                                                   
  headless=True \                                                                                   
  capture_video=True \                                                                             
  capture_video_freq=1500 \                                                                         
  capture_video_len=100 \                                                                           
  force_render=False \                                                     
  wandb_project=franka_pcap \
  wandb_entity=qcr_neural_fields              
```






