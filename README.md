# Filter Deform Attention GAN: Constructing Human Motion Videos from Few Images

Our image warping-based method implements a highly robust motion transmission model, Filter Deform Attention Generative Adversarial Network (FDA GAN), which can transmit complex human motion videos using only a small number of human body images. We use a 3D pose shape estimator to replace traditional 2D pose estimation. We design a new attention mechanism and fuse it with the GAN network to propose a new network that can extract image features well and generate human motion videos. The entire process of FDA GAN is divided into three parts. Firstly, we obtain the pose and shape of the human through the 3D pose shape estimator. Secondly, we analyze the pose shape to obtain the foreground and background images of the human, as well as motion transformation streams. Finally, in the generative adversarial network, the foreground, background, and texture features are fused into new-person images. We show in the experimental section that our method outperforms recent methods overall and on various evaluation metrics.

## Approach

![FDA-GAN](https://github.com/mioyeah/FDA-GAN/blob/main/model/FDA-GAN.jpg)

## IPER datasets
https://svip-lab.github.io/dataset/iPER_dataset.html

## Installation
### Environment Setup
This repository has been tested on the following platform:
Python 3.8.15, PyTorch 1.7.0 with CUDA 11.0 and cuDNN 8.0, Ubuntu 22.04

To clone the repo, run either:
```
git clone --recursive https://github.com/mioyeah/FDA-GAN.git

Next, you have to make sure that you have all dependencies in place.
The simplest way to do so, is to use [anaconda](https://www.anaconda.com/). 

```
conda env create -f environment.yml -n my-env
conda activate my-env
```

## Pre-trained Models
Download the following models and place them in their correspoding directories:
- [FDAGAN.pth]((https://drive.google.com/file/d/19_rbhSSDknZO4DnBU018uaW9QratNxbk/view?usp=drive_link)) in
`assets/checkpoints/neural_reders`.
