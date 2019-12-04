# ���� matplotlib ���������ݣ�nympy ������ np ���������ʹ�ã�
from pylab import *

# ����һ�� 8 * 6 �㣨point����ͼ�������÷ֱ���Ϊ 80
figure(figsize=(8, 6), dpi=80)

# ����һ���µ� 1 * 1 ����ͼ����������ͼ�����������еĵ� 1 �飨Ҳ��Ψһ��һ�飩
subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# �����������ߣ�ʹ����ɫ�ġ������ġ����Ϊ 1 �����أ�������
plot(X, C, color="red", linewidth=1.0, linestyle="-", label="cosine")

# �����������ߣ�ʹ����ɫ�ġ������ġ����Ϊ 1 �����أ�������
plot(X, S, color="green", linewidth=1.0, linestyle="-", label="sine")

# ����ͼƬ�߽�
plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.ylim(C.min() * 1.1, C.max() * 1.1)

# ����x,y��Ǻű�ǩ
xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

# �ƶ�������
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# ���ͼ��
legend(loc='upper left')

#Ϊͼ����������
zhfont1 = matplotlib.font_manager.FontProperties(fname="SimHei.ttf")
plt.title("sin��cos �Ա�ͼ", fontproperties=zhfont1)

# �Էֱ��� 72 ������ͼƬ
#savefig("exercice_2.png",dpi=72)

# ����Ļ����ʾ
show()
