from typing import Optional
import numpy as np
import time
import timeit
import matplotlib.pyplot as plt
from matplotlib import colors
from pympler import asizeof
from tqdm import trange
import matplotlib.backend_bases
import matplotlib.text

def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=4.0):
    # t = time.time()
    X = np.linspace(xmin, xmax, xn).astype(np.float64)
    Y = np.linspace(ymin, ymax, yn).astype(np.float64)
    C = X + Y[:, None] * 1j
    N = np.zeros_like(C, dtype=int)
    Z = np.zeros_like(C)
    for n in trange(maxiter):
            I = abs(Z) < horizon
            N[I] = n
            Z[I] = Z[I]**2 + C[I]
    N[N == maxiter-1] = 0
    # print(*size_of(X, Y, C, N, Z, I, val_names='X Y C N Z I'), sep='\n')
    # t = time.time() - t
    # print(f'Время выполнения {t:.2f} секунд')
    return Z, N

# marker: Optional[matplotlib.text.Text] = None


def onMouseClick(event: matplotlib.backend_bases.MouseEvent) -> None:
    axes = event.inaxes

    # Если кликнули вне какого-либо графика, то не будем ничего делать
    if axes is None:
        return

    global xmin, xmax, ymin, ymax

    # # Если маркер с текстом уже был создан, то удалим его
    # if marker is not None:
    #     marker.remove()

    # В качестве текущих выберем оси, внутри которых кликнули мышью
    # pylab.sca(axes)

    # Координаты клика в системе координат осей
    x = event.xdata
    y = event.ydata
    x_dif = (xmax - xmin) / 4
    y_dif = (ymax - ymin) / 4
    xmin = x - x_dif
    xmax = x + x_dif
    ymin = y - y_dif
    ymax = y + y_dif

    another_mandel()

    # text = f'({x:.3f}; {y:.3f})'

    # Выведем текст в точку, куда кликнули
    # marker = axes.text(x, y, text)


    # Обновим график
    axes.figure.canvas.draw()

def another_mandel():
    Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)

    # global fig, log_horizon, xmin, xmax, ymin, ymax
    with np.errstate(invalid='ignore'):
        M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)

    # dpi = 72
    # width = 10
    # height = 10 * yn / xn
    # fig = plt.figure(figsize=(width, height), dpi=dpi)
    # ax = fig.add_axes((0, 0, 1, 1), frameon=False, aspect=1)

    # Shaded rendering
    light = colors.LightSource(azdeg=315, altdeg=10)
    M = light.shade(M, cmap=plt.cm.hot, vert_exag=1.5,
                    norm=colors.PowerNorm(0.3), blend_mode='hsv')
    ax.imshow(M, extent=(xmin, xmax, ymin, ymax), interpolation="bicubic")
    ax.set_xticks([])
    ax.set_yticks([])

# def size_of(*args, val_names: str):
#     text = []
#     val_names = val_names.split()
#     all_size = 0
#     for i, v in enumerate(args):
#         v_size = asizeof.asizeof(v)/2**20
#         text.append(f'Массив {val_names[i]}: {v_size:.2f} Mбайт, тип {v.dtype}, кол-во элементов {v.size}, '
#                     f'размер элемента {v.itemsize} байт')
#         all_size +=v_size
#     text.append(f'Общий размер = {all_size:.2f} Mбайт')
#     return text

if __name__ == '__main__':

    xmin, xmax, xn = -2.25, +0.75, 200
    ymin, ymax, yn = -1.25, +1.25, 2000
    maxiter = 100
    horizon = 10.0
    log_horizon = np.log2(np.log(horizon))
    Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)

    #print(f'Время выполнения {timeit.timeit("Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)",
    #                                        globals=globals(), number=1):.2f} секунд')
    #exit()

    # Normalized recount as explained in:
    # https://linas.org/art-gallery/escape/smooth.html
    # https://web.archive.org/web/20160331171238/https://www.ibm.com/developerworks/community/blogs/jfp/entry/My_Christmas_Gift?lang=en
    #
    # This line will generate warnings for null values but it is faster to
    # process them afterwards using the nan_to_num
    with np.errstate(invalid='ignore'):
        M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)
    # print(*size_of(M, val_names='M'), sep='\n')

    dpi = 72
    width = 10
    height = 10*yn/xn
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    ax = fig.add_axes((0, 0, 1, 1), frameon=False, aspect=1)

    # Shaded rendering
    light = colors.LightSource(azdeg=315, altdeg=10)
    M = light.shade(M, cmap=plt.cm.hot, vert_exag=1.5,
                    norm=colors.PowerNorm(0.3), blend_mode='hsv')
    ax.imshow(M, extent=(xmin, xmax, ymin, ymax), interpolation="bicubic")
    ax.set_xticks([])
    ax.set_yticks([])

    # Some advertisement for matplotlib
    # year = time.strftime("%Y")
    # text = ("The Mandelbrot fractal set\n"
    #         "Rendered with matplotlib %s, %s - https://matplotlib.org"
    #         % (matplotlib.__version__, year))
    # ax.text(xmin+.025, ymin+.025, text, color="white", fontsize=12, alpha=0.5)

    fig.canvas.mpl_connect('button_press_event', onMouseClick)
    plt.show()