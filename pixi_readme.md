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
Train either reaching policy with the parameterized Pixi task:

```bash
pixi run train-franka
pixi run train-kinova
```

Both shortcuts delegate to the generic task, which accepts a full Isaac Gym
task name:

```bash
pixi run train Sim2RealFrankaTreeTactileVoxelReach franka_pcap qcr_neural_fields
```

Training uses 8,192 environments and enables W&B. The W&B project defaults to
`franka_pcap` or `kinova_pcap`, based on the selected robot, and the entity
defaults to `qcr_neural_fields`. Override either value without editing the
manifest:

```bash
pixi run train-franka my_project my_team
```

For `train-franka` and `train-kinova`, the optional arguments are ordered as
`wandb_project` and `wandb_entity`. To change only the entity, repeat the
default project, for example `pixi run train-kinova kinova_pcap my_team`.
The generic `train` task takes `task_name` first and defaults its project to
`pcap`. Additional Hydra overrides can be passed after `--`, for example:

```bash
pixi run train Sim2RealFrankaTreeTactileVoxelReach -- max_iterations=10
```

Test the latest checkpoint for a robot with:

```bash
pixi run test-franka
pixi run test-kinova
```

The runner automatically selects the latest matching checkpoint. To select a
checkpoint explicitly, or pass any other Hydra override, append it to the
task:

```bash
pixi run test-kinova checkpoint=runs/<run>/nn/Sim2RealKinovaTreeTactileVoxelReach.pth
pixi run test-kinova +real=True
```

The train task is equivalent to:

```
pixi run bash source/reinforcement/ige/ige_task_runner.sh \
  task=Sim2RealFrankaTreeTactileVoxelReach \
  num_envs=8192 \
  headless=True \
  capture_video=False \
  capture_video_freq=1500 \
  capture_video_len=100 \
  force_render=True \
  wandb_project=franka_pcap \
  wandb_entity=qcr_neural_fields \
  wandb_activate=True
```

