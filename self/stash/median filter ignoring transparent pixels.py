"""
---
requirements: pip install numpy>=2.0.0 opencv-python>=4.11.0
timestamp: 2025-04-14T10:24:02.074+08:00
---

Median filter ignoring transparent pixels. Maybe run this twice for better effect...?
"""

import cv2
import numpy as np

image = cv2.imread("input.png", cv2.IMREAD_UNCHANGED)
shape = image.shape
image_flat = image.reshape(-1).view(np.uint32).reshape(shape[:-1])
colors, counts = np.unique(image_flat, return_counts=True)
color_palette = colors[(counts >= 2000) | (counts == 314)]
color_palette_round = colors[~((counts >= 2000) | (counts == 314))]

"""
mapping = np.argmin(
    np.sum(
        (
            color_palette.view(np.uint8).reshape((-1, 4))
            - color_palette_round.view(np.uint8).reshape((-1, 1, 4))
        )
        ** 2,
        axis=-1,
    ),
    axis=-1,
)
for idx, a in enumerate(color_palette_round):
    image_flat[image_flat == a] = 0
"""

k_size = 3
new_image = np.empty(shape[:-1] + (k_size**2,))
image_pad = (
    cv2.copyMakeBorder(
        image_flat.view(np.uint8).reshape(shape),
        k_size // 2,
        k_size // 2,
        k_size // 2,
        k_size // 2,
        borderType=cv2.BORDER_REPLICATE,
    )
    .view(np.uint32)
    .reshape(np.array(shape[:-1]) + np.array([k_size // 2 * 2, k_size // 2 * 2]))
)
new_image_min = np.zeros(shape[:-1])
for idx in range(k_size**2):
    x = idx % k_size
    y = idx // k_size
    section = image_pad[y:, x:][: shape[0], : shape[1]]
    new_image[..., idx] = section
    new_image_min[
        ((new_image_min == 0) | (new_image_min > section)) & (section != 0)
    ] = section[((new_image_min == 0) | (new_image_min > section)) & (section != 0)]
new_image_mask = new_image < new_image_min[..., np.newaxis]
new_image = (1 - new_image_mask) * new_image + new_image_mask * new_image_min[
    ..., np.newaxis
]
new_image = np.median(new_image, axis=-1).astype(np.uint32)

# image_flat = cv2.medianBlur(image_flat, 3)
image_flat[image_flat == 0] = new_image[image_flat == 0]
image = image_flat.view(np.uint8).reshape(shape)
"""
image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel=np.array([
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1],
]))
"""
cv2.imwrite("output.png", image)
