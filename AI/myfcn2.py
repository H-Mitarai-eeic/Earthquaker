import os.path as osp

import fcn
import numpy as np
import torch
import torch.nn as nn
len_data = 64

# https://github.com/shelhamer/fcn.berkeleyvision.org/blob/master/surgery.py
def get_upsampling_weight(in_channels, out_channels, kernel_size):
    """Make a 2D bilinear kernel suitable for upsampling"""
    factor = (kernel_size + 1) // 2
    if kernel_size % 2 == 1:
        center = factor - 1
    else:
        center = factor - 0.5
    og = np.ogrid[:kernel_size, :kernel_size]
    filt = (1 - abs(og[0] - center) / factor) * \
           (1 - abs(og[1] - center) / factor)
    weight = np.zeros((in_channels, out_channels, kernel_size, kernel_size),
                      dtype=np.float64)
    weight[range(in_channels), range(out_channels), :, :] = filt
    return torch.from_numpy(weight).float()


class MYFCN2(nn.Module):

    pretrained_model = \
        osp.expanduser('~/data/models/pytorch/fcn32s_from_caffe.pth')

    @classmethod
    def download(cls):
        return fcn.data.cached_download(
            url='https://drive.google.com/uc?id=11k2Q0bvRQgQbT6-jYWeh6nmAsWlSCY3f',  # NOQA
            path=cls.pretrained_model,
            md5='d3eb467a80e7da0468a20dfcbc13e6c8',
        )

    def __init__(self, n_class=21):
        super(MYFCN2, self).__init__()
        # conv1 256*256
        #Hout = floor((Hin + 2*padding - kernel)/stride + 1)
        self.pool1 = nn.MaxPool2d(2, stride=2, ceil_mode=True)
        self.conv1 = nn.Conv2d(2, 8, 33, padding=16)
        self.relu1 = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(8, 8, 33, padding=16)
        self.relu2 = nn.ReLU(inplace=True)
        # self.pool2 = nn.MaxPool2d(2, stride=2, ceil_mode=True)
        # self.conv3 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu3 = nn.ReLU(inplace=True)
        # self.conv4 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu4 = nn.ReLU(inplace=True)
        # self.conv5 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu5 = nn.ReLU(inplace=True)
        # self.conv6 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu6 = nn.ReLU(inplace=True)
        # self.conv7 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu7 = nn.ReLU(inplace=True)
        # self.conv8 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu8 = nn.ReLU(inplace=True)
        # self.conv9 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu9 = nn.ReLU(inplace=True)
        # self.conv10 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu10 = nn.ReLU(inplace=True)
        # self.conv11 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu11 = nn.ReLU(inplace=True)
        # self.conv12 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu12 = nn.ReLU(inplace=True)
        # self.conv13 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu13 = nn.ReLU(inplace=True)
        # self.conv14 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu14 = nn.ReLU(inplace=True)
        # self.conv15 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu15 = nn.ReLU(inplace=True)
        # self.conv16 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu16 = nn.ReLU(inplace=True)
        # self.conv17 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu17 = nn.ReLU(inplace=True)
        # self.conv18 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu18 = nn.ReLU(inplace=True)
        # self.conv19 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu19 = nn.ReLU(inplace=True)
        # self.conv20 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu20 = nn.ReLU(inplace=True)
        # self.conv21 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu21 = nn.ReLU(inplace=True)
        # self.conv22 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu22 = nn.ReLU(inplace=True)
        # self.conv23 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu23 = nn.ReLU(inplace=True)
        # self.conv24 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu24 = nn.ReLU(inplace=True)
        # self.conv25 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu25 = nn.ReLU(inplace=True)
        # self.conv26 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu26 = nn.ReLU(inplace=True)
        # self.conv27 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu27 = nn.ReLU(inplace=True)
        # self.conv28 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu28 = nn.ReLU(inplace=True)
        # self.conv29 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu29 = nn.ReLU(inplace=True)
        # self.conv30 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu30 = nn.ReLU(inplace=True)
        # self.conv31 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu31 = nn.ReLU(inplace=True)
        # self.conv32 = nn.Conv2d(8, 8, 5, padding=2)
        # self.relu32 = nn.ReLU(inplace=True)
        self.fc = nn.Linear(int(2*len_data*len_data/16), n_class*len_data*len_data)
        

        # fc7
        # self.fc7 = nn.Conv2d(256, 256, 2)
        # self.relu7 = nn.ReLU(inplace=True)
        # self.drop7 = nn.Dropout2d(p=0.2)

        self.score_fr = nn.Conv2d(8, n_class, 1)
        self.upscore = nn.ConvTranspose2d(n_class, n_class, 4, stride=4, bias=False) #Hout = (Hin - 1)*stride - 2*padding + kernel + outputpadding n_class to 256

        self._initialize_weights()

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                m.weight.data.zero_()
                if m.bias is not None:
                    m.bias.data.zero_()
            if isinstance(m, nn.ConvTranspose2d):
                assert m.kernel_size[0] == m.kernel_size[1]
                initial_weight = get_upsampling_weight(
                    m.in_channels, m.out_channels, m.kernel_size[0])
                m.weight.data.copy_(initial_weight)

    def forward(self, x):
        
        h = x
        batch_size = len(x)
        h = self.pool1(h)
        h = self.pool1(h)
        h = h.view(-1, int(2*len_data*len_data/16))
        h = self.fc(h)
        h = h.view(batch_size, 10, len_data, len_data)
        return h