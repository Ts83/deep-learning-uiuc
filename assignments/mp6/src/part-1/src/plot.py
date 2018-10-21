"""
HW6: Understanding CNNs and Generative Adversarial Networks.

@author: Zhenye Na
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def plot(samples):
    """Make plots."""
    fig = plt.figure(figsize=(10, 10))
    gs = gridspec.GridSpec(10, 10)
    gs.update(wspace=0.02, hspace=0.02)

    for i, sample in enumerate(samples):
        ax = plt.subplot(gs[i])
        plt.axis('off')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_aspect('equal')
        plt.imshow(sample)
    return fig