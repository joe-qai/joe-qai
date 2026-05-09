from PIL import Image
import numpy as np

# 读取GIF
img = Image.open('Dragon.gif')

# 获取所有帧
frames = []
for i in range(img.n_frames):
    img.seek(i)
    frame = img.convert('RGBA')
    
    # 将黑色背景变为透明
    data = np.array(frame)
    # 找到接近黑色的像素（RGB都小于阈值）
    black_mask = (data[:,:,0] < 30) & (data[:,:,1] < 30) & (data[:,:,2] < 30)
    data[black_mask] = [0, 0, 0, 0]  # 设为透明
    
    transparent_frame = Image.fromarray(data)
    frames.append(transparent_frame)

# 保存为透明背景的GIF
frames[0].save('Dragon_transparent.gif',
               save_all=True,
               append_images=frames[1:],
               duration=img.info.get('duration', 100),
               loop=0,
               disposal=2,
               transparency=0)

print(f"处理了 {len(frames)} 帧")
print("已保存透明背景GIF")