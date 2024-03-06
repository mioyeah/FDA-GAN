# FDA-GAN

Our image warping-based method implements a highly robust motion transmission model, Filter Deform Attention Generative Adversarial Network (FDA GAN), which can transmit complex human motion videos using only a small number of human body images. We use a 3D pose shape estimator to replace traditional 2D pose estimation. We design a new attention mechanism and fuse it with the GAN network to propose a new network that can extract image features well and generate human motion videos. The entire process of FDA GAN is divided into three parts. Firstly, we obtain the pose and shape of the human through the 3D pose shape estimator. Secondly, we analyze the pose shape to obtain the foreground and background images of the human, as well as motion transformation streams. Finally, in the generative adversarial network, the foreground, background, and texture features are fused into new-person images. We show in the experimental section that our method outperforms recent methods overall and on various evaluation metrics.

## Approach

![FDA-GAN](3.png)

## IPER datasets
https://svip-lab.github.io/dataset/iPER_dataset.html

## Updates

Coming Soon



