import numpy as np
import matplotlib.pyplot as plt

## 跑高4Mb 延迟0
# KP = 1.
# KI = 0.00001
# KD = 3
# SEC = 1
# BETA = 1000000
# DELAY = 0

## 跑高4Mb 延迟15
KP = 0.9
KI = 0.00001
KD = 15
SEC = 1
BETA = 1000000
DELAY = 15

## 跑高4Mb 延迟30
# KP = 0.8
# KI = 0.00001
# KD = 30
# SEC = 1
# BETA = 1000000
# DELAY = 30


def gen_bwi():
    x = np.linspace(0, 3, 1000)
    y = np.zeros(x.shape[0]) + BETA * 4
    # y = np.zeros(x.shape[0] * 2) + BETA * 4
    a = 2 * np.sin(np.pi * 3 * x + 1)
    b = np.cos(np.pi * x)
    c = (a + b + 4) * BETA
    # c = np.append(c, np.zeros(x.shape) + BETA * 6)
    return c, y


def pid(ori, target, delay=0):
    pred = []
    cumulate_diff = 0.0
    last = 0
    i = 0
    for k, y in enumerate(target):
        if k < delay:
            continue

        if not pred:
            pred.append(0)
            i += 1
            continue

        diff = y - ori[k - delay]
        cumulate_diff += diff * SEC
        if last == 0:
            last = diff
        pred.append(KP * diff + KI * cumulate_diff + KD * (diff - last) / SEC)
        last = diff

    return pred


def show(data):
    plt.figure(figsize=(18, 6))
    for label, d in data.items():
        plt.plot(d, label=label)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    x, y = gen_bwi()
    pred = pid(x, y, DELAY)
    print(x[DELAY:DELAY+100])
    print(pred[0:100])
    print((pred + x[DELAY:])[0:100])
    # show({"ort": x})
    show({"ort": x[DELAY:], "line": y[DELAY:], "pred": pred + x[DELAY:]})
