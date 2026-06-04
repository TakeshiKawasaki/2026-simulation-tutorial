import numpy as np
import matplotlib
%config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
from matplotlib.collections import PatchCollection


# ---- 描画設定 ----
plt.rcParams['animation.writer'] = 'ffmpeg'
plt.rcParams['font.family'] = 'Arial'
plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 30

# ---- シミュレーション設定 ----
Np = 1024
L = 40.0
temp = 1.000
resolution = 500

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.set_aspect('equal')

# ---- 軸設定 ----
ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.tick_params(which='major', width=1, length=10)
plt.tick_params(which='minor', width=1, length=5)
plt.xticks(color='k', size=30)
plt.yticks(color='k', size=30)
plt.xlabel(r"$x/a$", color='k', size=45)
plt.ylabel(r"$y/a$", color='k', size=45)
plt.xlim(0, L)
plt.ylim(0, L)
ax.text(0, L + 1, r"$T^*={:.3f}$".format(temp), size=40, color="k")

# ---- アニメーション初期化 ----
ims = []

# ---- 各時刻ステップの描画 ----
for j in range(0, 10):
    x, y, a = np.loadtxt(f"./Lecture6/coord_T{temp:.3f}_{j}.dat", comments='#', unpack=True)
    patches = []

    for i in range(Np):
        circle = mpatches.Ellipse((x[i], y[i]), a[i], a[i])
        patches.append(circle)

    p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=1.0, ec='k')
    p.set_array(a)
    p.set_clim(0.8, 1.2)

    ax.add_collection(p)
    title = ax.text(0.7 * L, L + 1, f"$t={j}$", size=40, color="k")
    ims.append([p, title])

# ---- アニメーション生成と保存 ----
ani = animation.ArtistAnimation(fig, ims, interval=100)
ani.save(f"LJ_temp{temp:.3f}.gif", writer="imagemagick")
ani.save(f"LJ_temp{temp:.3f}.mp4", writer="ffmpeg")

plt.show()
