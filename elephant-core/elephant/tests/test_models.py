# Copyright (c) 2021, Ko Sugawara
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1.  Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
# 2.  Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# ==============================================================================
"""Test models."""

import torch

from elephant.models import FlowResNet
from elephant.models import UNet


def weight_init(m):
    if isinstance(m, (torch.nn.Conv2d, torch.nn.Conv3d)):
        torch.manual_seed(42)
        torch.nn.init.kaiming_normal_(m.weight.data, mode='fan_in')
        if m.bias is not None:
            m.bias.data.zero_()


def test_three_class_segmentation():
    model = UNet.three_class_segmentation(is_eval=True)
    model.apply(weight_init)
    keep_axials = (True,) * 4
    x = torch.tensor([[[[[0.0213, 0.1214, 0.5833, 0.4821, 0.9276],
                         [0.1276, 0.1708, 0.8123, 0.7659, 0.6194],
                         [0.6735, 0.5342, 0.3016, 0.1573, 0.4630],
                         [0.7540, 0.5064, 0.1403, 0.6465, 0.6818],
                         [0.1920, 0.0685, 0.8489, 0.1659, 0.0420]],

                        [[0.8294, 0.1707, 0.2999, 0.7442, 0.3222],
                         [0.3553, 0.5667, 0.7530, 0.1452, 0.9759],
                         [0.9214, 0.8777, 0.7721, 0.6300, 0.4785],
                         [0.0869, 0.6856, 0.2463, 0.7662, 0.2288],
                         [0.8264, 0.8035, 0.2603, 0.4886, 0.8670]],

                        [[0.8854, 0.7353, 0.4443, 0.3498, 0.4592],
                         [0.9509, 0.0367, 0.9297, 0.0967, 0.1051],
                         [0.7824, 0.8415, 0.1543, 0.3896, 0.4633],
                         [0.9893, 0.5569, 0.9794, 0.9304, 0.6912],
                         [0.5967, 0.5523, 0.0221, 0.8204, 0.3253]],

                        [[0.1614, 0.7406, 0.3958, 0.6050, 0.7746],
                         [0.4516, 0.6159, 0.6993, 0.0285, 0.9561],
                         [0.2412, 0.8015, 0.9938, 0.3466, 0.2625],
                         [0.4958, 0.7861, 0.9308, 0.5967, 0.7743],
                         [0.3409, 0.4553, 0.8547, 0.6212, 0.9174]],

                        [[0.0640, 0.4244, 0.1806, 0.6024, 0.3920],
                         [0.6016, 0.6889, 0.3446, 0.3780, 0.2883],
                         [0.2582, 0.6657, 0.6541, 0.6908, 0.8935],
                         [0.5897, 0.7156, 0.6651, 0.7115, 0.3478],
                         [0.5155, 0.8412, 0.1721, 0.4139, 0.8159]]]]])
    with torch.no_grad():
        y = model(x, keep_axials)
    expected = torch.tensor([[
        [
            [[-0.89785796,  -0.45465508, -0.71851385, -0.19897324, -0.7427523],
             [-0.6003499,   -0.76410306, -2.1086311,  -0.65808946, -0.6325148],
             [-1.9341741,   -1.995651,   -2.3343947,  -0.5504082,  -0.5338505],
             [-0.94323933,  -1.4058473,  -0.0901193,  -0.5428375,  -0.5306641],
             [-0.6894991,   -1.1253357,  -0.47578138, -1.4340975,  -1.437032]],

            [[-2.372988,    -1.1819886,  -3.272229,   -4.3676634,  -0.634865],
             [-1.3511579,   -1.3914855,  -2.2630773,  -1.7014171,  -2.7186768],
             [-2.5874946,   -3.4608614,  -2.3322241,  -0.7468437,  -1.3343489],
             [-6.3837156,   -5.602231,   -0.64931655, -0.7317372,  -0.7911072],
             [-1.7777826,   -4.1542387,  -3.4457126,  -1.5937366,  -0.6089516]],

            [[-0.543884,    -0.4155617,  -1.9117365,  -2.2428098,  -3.8330903],
             [-2.6778173,   -0.21767116, -1.7694219,  -2.378309,   -2.5110173],
             [-1.5643374,   -0.05319992, -2.6654203,  -4.0756826,  -1.1332623],
             [-2.6309881,   -0.8510356,  -0.1897386,  -2.075014,   -0.14453809],
             [-0.8906499,   -1.8203454,  -1.2656603,  -0.42081356, -3.495089]],

            [[-1.5527005,   -2.3285608,  -1.1900437,  -2.6469069,  -3.0467777],
             [-1.3468263,   -2.194508,   -1.28304,    -0.8987359,  -1.2822591],
             [-0.75391555,  -0.44117376, -0.7448928,  -1.3386325,  -0.88684106],
             [-0.9369168,   -0.56638,    -4.3556175,  -0.8795471,  -0.9557092],
             [-0.47928953,  -1.5564768,  -3.1644988,  -0.5147881,  -1.7620918]],

            [[-1.1888745,   -1.4153641,  -0.727897,   -0.63343304, -0.99381477],
             [-0.6424313,   -0.67965484, -1.7840016,  -0.6908759,  -1.5062102],
             [-1.4386238,   -3.0332704,  -2.9095888,  -1.7108437,  -3.446537],
             [-4.152298,    -1.0465248,  -1.0168853,  -2.1842237,  -1.2969161],
             [-0.600914,    -0.4418257,  -2.6891143,  -1.1377318,  -1.0225295]]
        ],


        [
            [[-3.296192,   -1.8130541,  -1.9776605,  -2.1908557,  -2.7087889],
             [-2.06594,    -2.614739,   -1.6237593,  -2.384003,   -2.090174],
             [-2.2383041,  -1.4703726,  -2.2930293,  -1.5541376,  -3.2776942],
             [-2.975119,   -2.324096,   -3.725559,   -1.5609896,  -3.1711755],
             [-1.8626432,  -2.589551,   -2.6042001,  -3.1994927,  -1.7261316]],

            [[-1.3612422,  -2.7743244,  -2.7914934,  -1.2379353,  -1.5677915],
             [-3.5538845,  -0.9439302,  -0.9379673,  -1.8203406,  -0.49049154],
             [-1.0064836,  -3.6345327,  -1.5635982,  -2.0397856,  -1.0035522],
             [-2.3672225,  -2.5932598,  -3.0807943,  -3.298914,   -1.0849692],
             [-2.4140744,  -0.335187,   -0.07654761, -0.7002523,  -1.6112518]],

            [[-1.5769863,  -1.9104897,  -1.3337158,  -0.2645627,  -0.08979644],
             [-1.5564194,  -3.4305086,  -0.6458024,  -0.99527484, -0.3986171],
             [-0.67380744, -3.2753696,  -0.1528171,  -2.856497,   -1.604029],
             [-0.37017098, -3.0180972,  -2.127459,   -1.051781,   -4.46945],
             [-2.317488,   -0.3484861,  -1.1142445,  -2.0416732,  -0.12187587]],

            [[-2.3109012,  -1.6372089,  -2.5276217,  -0.9947612,  -0.08063686],
             [-2.030987,   -2.243927,   -1.5246712,  -1.7863072,  -0.63341844],
             [-3.5496302,  -3.610197,   -1.8778696,  -1.7733855,  -0.87908],
             [-1.9205639,  -2.7522326,  -0.19886783, -1.4579859,  -2.7197526],
             [-3.908918,   -0.5401063,  -0.06332783, -1.2146639,  -0.21079388]],

            [[-1.8601775,  -1.8048489,  -2.6956775,  -3.9523916,  -1.7026827],
             [-2.1676579,  -1.7242043,  -2.7639468,  -2.5457435,  -2.320756],
             [-1.7012358,  -1.6653948,  -1.9388254,  -0.89232075, -0.78306115],
             [-0.6737232,  -2.5646758,  -0.85858166, -1.2605556,  -0.6359675],
             [-2.9794955,  -3.3468337,  -0.32364792, -0.42415673, -1.5285733]]
        ],


        [
            [[-0.58782434, -1.633432,   -0.9972351,  -3.184642,   -0.7818035],
             [-1.178038,   -0.9520997,  -0.4615475,  -2.7055984,  -1.1599627],
             [-0.29461843, -0.99022377, -0.75408065, -2.8402886,  -1.4192758],
             [-0.5841787,  -0.5310508,  -3.427271,   -2.3018947,  -1.3592477],
             [-1.0702846,  -0.5906837,  -1.3129708,  -0.7332138,  -0.5371757]],

            [[-0.43008158, -0.6189095,  -0.11041372, -0.36275524, -1.3413677],
             [-0.35904387, -1.9256718,  -1.1359055,  -0.9065745,  -1.6193105],
             [-0.6686352,  -0.19705988, -1.0722613,  -2.2107804,  -1.2439554],
             [-0.10798735, -0.9256339,  -1.5231009,  -4.242077,   -1.649843],
             [-0.29902968, -1.3461429,  -4.3885202,  -1.4394164,  -1.3608541]],

            [[-1.5468671,  -1.6754824,  -0.6774817,  -2.0870397,  -2.7451274],
             [-0.34069097, -2.3935633,  -2.3375442,  -2.382381,   -1.5840478],
             [-2.1935325,  -4.908925,   -7.4619145,  -0.13267492, -0.75519574],
             [-1.6607456,  -1.6448206,  -5.7349553,  -1.0826788,  -2.34913],
             [-0.7111272,  -2.7398868,  -1.5372912,  -2.8168263,  -2.4722385]],

            [[-0.37229258, -0.4211079,  -0.4868297,  -0.64746207, -3.5079062],
             [-0.5611461,  -0.3086287,  -1.9222423,  -1.1286343,  -1.7891487],
             [-0.74476194, -3.0375519,  -1.5335201,  -0.8717614,  -1.8194759],
             [-0.9237992,  -1.6657202,  -5.2014112,  -1.8273655,  -0.6131041],
             [-1.0196682,  -1.7267451,  -5.6272573,  -3.4225645,  -3.9968374]],

            [[-0.61657304, -0.53715646, -0.9313696,  -0.80600435, -0.803757],
             [-1.0689514,  -1.7615526,  -0.51552296, -1.8903534,  -0.7130591],
             [-0.5777452,  -0.63980645, -0.6721512,  -2.9511452,  -0.73203886],
             [-0.83362025, -1.6382282,  -2.5767176,  -0.9678207,  -1.7188845],
             [-0.91411495, -1.222617,   -2.769664,   -4.5017776,  -0.85926974]]
        ]]])
    assert torch.allclose(y, expected)


def test_three_dimensional_flow():
    model = FlowResNet.three_dimensional_flow(is_eval=True)
    model.apply(weight_init)
    keep_axials = (True,) * 4
    x = torch.tensor([[[[[0.1186, 0.2931, 0.8046, 0.3549, 0.3548],
                         [0.3617, 0.1403, 0.6212, 0.4167, 0.4423],
                         [0.0822, 0.0843, 0.7522, 0.3163, 0.7114],
                         [0.9633, 0.5980, 0.4706, 0.6413, 0.2824],
                         [0.0951, 0.0769, 0.7034, 0.2974, 0.0721]],

                        [[0.9956, 0.5365, 0.1665, 0.7520, 0.6726],
                         [0.7450, 0.5169, 0.3923, 0.7558, 0.0773],
                         [0.5676, 0.4889, 0.3975, 0.8417, 0.8471],
                         [0.3507, 0.0794, 0.6013, 0.4954, 0.9965],
                         [0.9416, 0.3163, 0.8404, 0.3057, 0.4073]],

                        [[0.2781, 0.6499, 0.2623, 0.8073, 0.3875],
                         [0.7490, 0.1614, 0.7163, 0.1129, 0.8551],
                         [0.2783, 0.4236, 0.6739, 0.5475, 0.0841],
                         [0.8323, 0.0106, 0.4955, 0.5920, 0.3649],
                         [0.1006, 0.9107, 0.0971, 0.4464, 0.4640]],

                        [[0.5141, 0.2878, 0.6094, 0.3405, 0.5137],
                         [0.9176, 0.4937, 0.1001, 0.6948, 0.2177],
                         [0.4926, 0.0801, 0.7241, 0.9975, 0.0668],
                         [0.4955, 0.1946, 0.3624, 0.0114, 0.7565],
                         [0.3316, 0.6063, 0.2125, 0.0629, 0.8766]],

                        [[0.1611, 0.8570, 0.6128, 0.2304, 0.5572],
                         [0.4511, 0.8625, 0.3962, 0.9372, 0.7202],
                         [0.4225, 0.8103, 0.5146, 0.4342, 0.4050],
                         [0.6026, 0.6169, 0.0952, 0.3021, 0.2472],
                         [0.5243, 0.4573, 0.5214, 0.5072, 0.5656]]],


                       [[[0.4872, 0.9581, 0.3305, 0.5007, 0.2765],
                         [0.9324, 0.1461, 0.6846, 0.5098, 0.0013],
                         [0.6768, 0.9638, 0.7432, 0.9380, 0.6803],
                         [0.9240, 0.8899, 0.9291, 0.0700, 0.7288],
                         [0.6669, 0.7255, 0.8110, 0.9446, 0.3734]],

                        [[0.3805, 0.3756, 0.6386, 0.6716, 0.8142],
                         [0.5567, 0.4304, 0.8964, 0.6553, 0.6355],
                         [0.1460, 0.3177, 0.9564, 0.8001, 0.5037],
                         [0.7873, 0.8890, 0.9200, 0.9767, 0.7219],
                         [0.0247, 0.6693, 0.1103, 0.7691, 0.4491]],

                        [[0.3493, 0.7522, 0.4513, 0.9973, 0.8848],
                         [0.4545, 0.0806, 0.6812, 0.2347, 0.3586],
                         [0.5125, 0.7913, 0.0310, 0.0454, 0.6903],
                         [0.4579, 0.9778, 0.8814, 0.4267, 0.6170],
                         [0.4164, 0.3889, 0.4754, 0.8077, 0.5869]],

                        [[0.6152, 0.7325, 0.5898, 0.6584, 0.7899],
                         [0.7984, 0.8705, 0.5421, 0.7181, 0.9823],
                         [0.6820, 0.1283, 0.9679, 0.3454, 0.1938],
                         [0.0465, 0.5746, 0.9780, 0.5171, 0.6491],
                         [0.3339, 0.2343, 0.4421, 0.1869, 0.8682]],

                        [[0.5130, 0.3768, 0.0619, 0.8489, 0.2844],
                         [0.5386, 0.9742, 0.2941, 0.7574, 0.1055],
                         [0.4202, 0.9958, 0.0273, 0.9545, 0.5714],
                         [0.5397, 0.5361, 0.3217, 0.2765, 0.6029],
                         [0.7706, 0.0840, 0.9713, 0.4732, 0.0272]]]]])
    with torch.no_grad():
        y = model(x, keep_axials)
    expected = torch.tensor([[
        [
            [[-0.67856324, -0.6524984,  -0.7127741,  -0.6192062,   0.11910772],
             [-0.8518106,  -0.79060984, -0.89294815, -0.8154753,  -0.06821556],
             [-0.83144593, -0.86310315, -0.8493521,  -0.8301666,  -0.01109819],
             [-0.8906575,  -0.8589544,  -0.8488567,  -0.798619,   -0.01629373],
             [-0.43293375, -0.4964185,  -0.35946965, -0.35822394, -0.04150017]],

            [[-0.6862707,  -0.50794685, -0.6323254,  -0.77604246, -0.18321949],
             [-0.8927449,  -0.8454243,  -0.95744795, -0.9164563,  -0.40675962],
             [-0.90135324, -0.952127,   -0.9718721,  -0.9340451,  -0.34826633],
             [-0.90717065, -0.93359566, -0.949733,   -0.8954966,  -0.48255688],
             [-0.4804304,  -0.82115555, -0.76807785, -0.8289759,  -0.3291714]],

            [[-0.6182486,  -0.43585217, -0.46820253, -0.6845529,  -0.08807469],
             [-0.9219494,  -0.9348146,  -0.9644646,  -0.96606255, -0.5148618],
             [-0.8993014,  -0.946424,   -0.9858645,  -0.97116387, -0.20059961],
             [-0.8785307,  -0.9435316,  -0.9669531,  -0.969311,   -0.38640007],
             [-0.43445414, -0.7024977,  -0.81505144, -0.771825,   -0.3229839]],

            [[-0.5950193,  -0.5890775,  -0.44820374, -0.51570886, -0.18592174],
             [-0.83566636, -0.9325236,  -0.8782885,  -0.93115085, -0.14781086],
             [-0.81875825, -0.9412899,  -0.85771364, -0.8944199,  -0.29254103],
             [-0.8108608,  -0.9348321,  -0.9326869,  -0.8706081,  -0.3035171],
             [-0.52732694, -0.7044143,  -0.7501101,  -0.7540904,  -0.18759274]],

            [[-0.07379024, -0.03173352,  0.01433889, -0.12642772,  0.08335657],
             [-0.4732507,  -0.5272969,  -0.54723483, -0.5675055,  -0.25899082],
             [-0.24124894, -0.48479152, -0.61355555, -0.6519972,   0.14277229],
             [-0.3180673,  -0.5427555,  -0.5856876,  -0.523786,   -0.11781295],
             [-0.18139675, -0.38827848, -0.37769306, -0.19474846, -0.23045184]]
        ],


        [
            [[0.48885685,   0.7661205,   0.8023897,   0.8473568,   0.6081667],
             [0.60197705,   0.79536766,  0.91741693,  0.9172642,   0.6094425],
             [0.62481093,   0.8699287,   0.90033495,  0.9132537,   0.6302303],
             [0.7222947,    0.90821546,  0.9362171,   0.9122511,   0.6431991],
             [0.33378375,   0.6722115,   0.5841116,   0.6787486,   0.46946242]],

            [[0.5970022,    0.7588563,   0.845755,    0.9115762,   0.5653155],
             [0.76450324,   0.91700494,  0.96519643,  0.94930834,  0.70518607],
             [0.8267078,    0.96368194,  0.97847986,  0.9738547,   0.61395],
             [0.84188664,   0.9556205,   0.98211217,  0.9729848,   0.700631],
             [0.42282966,   0.8136635,   0.78779685,  0.8567707,   0.6031074]],

            [[0.63709474,   0.81476194,  0.8061509,   0.9215972,   0.56383455],
             [0.8224442,    0.9356345,   0.9680455,   0.96914315,  0.7658695],
             [0.80682516,   0.9768574,   0.9847771,   0.9793253,   0.7317985],
             [0.8008921,    0.9769673,   0.98439014,  0.9713045,   0.74444497],
             [0.35488975,   0.77008986,  0.7558211,   0.84268814,  0.62116146]],

            [[0.6459798,    0.7939647,   0.7922472,   0.8263682,   0.51047903],
             [0.7934972,    0.9723252,   0.9569799,   0.9706063,   0.68687177],
             [0.801692,     0.9690751,   0.980429,    0.9721291,   0.7204307],
             [0.75010645,   0.96280354,  0.96632016,  0.94528174,  0.64409566],
             [0.45734087,   0.6589871,   0.7389551,   0.7166514,   0.49274534]],

            [[0.3116956,    0.35333055,  0.36209986,  0.46174845,  0.25068685],
             [0.6643647,    0.90493685,  0.83302814,  0.86281955,  0.6566325],
             [0.49646848,   0.9208368,   0.86615676,  0.87871313,  0.61219656],
             [0.6083197,    0.87222695,  0.8088976,   0.7703279,   0.58375156],
             [0.43378982,   0.65042377,  0.7461842,   0.63045436,  0.2570601]]],


        [
            [[0.16832109,   0.0688961,  -0.01448629, -0.15992872, -0.13405068],
             [0.4525485,   -0.02152996, -0.08481486, -0.31844974, -0.08378484],
             [0.3776964,   -0.01166885, -0.17485236, -0.25902313, -0.05047183],
             [0.4674101,   -0.07292683, -0.2568433,  -0.26368347, -0.14224654],
             [0.03019566,  -0.19317387, -0.33466363, -0.26315826, -0.16654478]],

            [[0.04012941,  -0.34036222, -0.14487472, -0.47965133, -0.32349068],
             [-0.08654612, -0.53118634, -0.6338563,  -0.66260123, -0.19665132],
             [-0.12146575, -0.79477787, -0.76898366, -0.7945482,  -0.39211226],
             [-0.210501,   -0.6676867,  -0.8491397,  -0.7769341,  -0.24831723],
             [-0.15718688, -0.68641025, -0.7606044,  -0.8074904,  -0.23274033]],

            [[-0.10304928, -0.41120818, -0.34191936, -0.40256467, -0.3013989],
             [0.03134106,  -0.6105689,  -0.83283097, -0.7047243,  -0.5361049],
             [-0.06173312, -0.8137784,  -0.83780104, -0.89272714, -0.49914104],
             [-0.3241258,  -0.858798,   -0.86998236, -0.7890742,  -0.44513288],
             [-0.11465643, -0.68083286, -0.5770303,  -0.74217826, -0.31880465]],

            [[-0.30750138, -0.3954554,  -0.5485485,  -0.3984359,  -0.39488158],
             [-0.46001118, -0.75625736, -0.7930408,  -0.7615351,  -0.24615479],
             [-0.511795,   -0.84802055, -0.9176481,  -0.7884873,  -0.6246375],
             [-0.3523456,  -0.8306421,  -0.8986174,  -0.80587244, -0.56114966],
             [-0.02614028, -0.5331757,  -0.51859874, -0.5947131,  -0.27652696]],

            [[-0.34503305, -0.65188336, -0.5939615,  -0.61834955, -0.47775197],
             [-0.42937148, -0.8993313,  -0.8168583,  -0.86321783, -0.68601304],
             [-0.31295222, -0.8997968,  -0.8123516,  -0.8360734,  -0.5874901],
             [-0.44132188, -0.87742317, -0.79334104, -0.7186437,  -0.64516896],
             [-0.42390147, -0.54549336, -0.7307426,  -0.66375196, -0.2771961]]
        ]]])
    assert torch.allclose(y, expected)
