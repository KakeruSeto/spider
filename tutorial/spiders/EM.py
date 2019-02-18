import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# データ生成 --------------------------------
np.random.seed(1) #乱数を固定
N = 100
K = 3
T3 = np.zeros((N, 3), dtype=np.uint8)
X = np.zeros((N, 2))
X_range0 = [-3, 3]
X_range1 = [-3, 3]
X_col = ['cornflowerblue', 'black', 'white']
Mu = np.array([[-.5, -.5], [.5, 1.0], [1, -.5]])  # 分布の中心
Sig = np.array([[.7, .7], [.8, .3], [.3, .8]])  # 分布の分散
Pi = np.array([0.4, 0.8, 1])  # 累積確率
for n in range(N):
    wk = np.random.rand()
    for k in range(K):
          if wk < Pi[k]:
            T3[n, k] = 1
            break
    for k in range(2):
        X[n, k] = (np.random.randn() * Sig[T3[n, :] == 1, k]
                   + Mu[T3[n, :] == 1, k])

# データの図示 ------------------------------
def show_data(x):
    plt.plot(x[:, 0], x[:, 1], linestyle='none',
             marker='o', markersize=6,
             markeredgecolor='black', color='gray', alpha=0.8)
    plt.grid(True)

# メイン ------------------------------------
plt.figure(1, figsize=(4, 4))
show_data(X)
plt.xlim(X_range0)
plt.ylim(X_range1)
plt.show()
np.savez('data_ch9.npz', X=X, X_range0=X_range0,
         X_range1= X_range1)
#print(X)

# ----------------- リスト 9-1-(2)
# Mu と R の初期化 -----------------------------
Mu = np.array([[-2, 1], [-2, 0], [-2, -1]])                         # (A)とりあえず初期値として適当に[-2, 1], [-2, 0], [-2, -1]
R = np.c_[np.ones((N, 1), dtype=int), np.zeros((N, 2), dtype=int)]  # とりあえず初期値として全てクラス0とする

# ----------------- リスト 9-1-(3)
# データの図示関数 ---------------------------
def show_prm(x, r, mu, col):
    for k in range(K):
        # データ分布の描写
        plt.plot(x[r[:, k] == 1, 0], x[r[:, k] == 1, 1], 
                 marker='o', 
                 markerfacecolor=X_col[k], markeredgecolor='k',
                 markersize=6, alpha=0.5, linestyle='none')
        # データの平均を「星マーク」で描写
        plt.plot(mu[k, 0], mu[k, 1], marker='*',
                 markerfacecolor=X_col[k], markersize=15,
                 markeredgecolor='k', markeredgewidth=1)
    plt.xlim(X_range0)
    plt.ylim(X_range1)
    plt.grid(True)

#  ------------------------------
plt.figure(figsize=(4, 4))
R = np.c_[np.ones((N, 1)), np.zeros((N, 2))]
show_prm(X, R, Mu, X_col)
plt.title('initial Mu and R')
plt.show()

# ----------------- リスト 9-1-(4)
# r を決める (Step 1) -----------
#データ点から各クラスタ中心(重心)までの二乗距離を計算
def step1_kmeans(x0, x1, mu):
    N = len(x0)
    r = np.zeros((N, K))  #100×3の配列を作成
    #print(r)
    for n in range(N):
        wk = np.zeros(K)
        for k in range(K):
            wk[k] = (x0[n] - mu[k, 0])**2 + (x1[n] - mu[k, 1])**2
        r[n, np.argmin(wk)] = 1
    return r
  

#  ------------------------------
plt.figure(figsize=(4, 4))
R = step1_kmeans(X[:, 0], X[:, 1], Mu)
show_prm(X, R, Mu, X_col)
plt.title('Step 1')
plt.show()

# ----------------- リスト 9-1-(5)
# Mu を決める (Step 2) ----------
#各クラスタに属するデータの点を使って,クラスタの中心(重心)を求め更新
def step2_kmeans(x0, x1, r):
    mu = np.zeros((K, 2))
    for k in range(K):
        mu[k, 0] = np.sum(r[:, k] * x0) / np.sum(r[:, k])
        mu[k, 1] = np.sum(r[:, k] * x1) / np.sum(r[:, k])
    return mu

#  ------------------------------
plt.figure(figsize=(4, 4))
Mu = step2_kmeans(X[:, 0], X[:, 1], R)
show_prm(X, R, Mu, X_col)
plt.title('Step2')
plt.show()

# ----------------- リスト 9-1-(6)
plt.figure(1, figsize=(10, 6.5))
Mu = np.array([[-2, 1], [-2, 0], [-2, -1]])
max_it = 6 # 繰り返しの回数
for it in range(0, max_it):
    plt.subplot(2, 3, it + 1)
    R = step1_kmeans(X[:, 0], X[:, 1], Mu)
    show_prm(X, R, Mu, X_col)
    plt.title("{0:d}".format(it + 1))
    plt.xticks(range(X_range0[0], X_range0[1]), "")
    plt.yticks(range(X_range1[0], X_range1[1]), "")
    Mu = step2_kmeans(X[:, 0], X[:, 1], R)
plt.show()
print(Mu)

# ----------------- リスト 9-1-(7)
# 目的関数 ----------------------------------
def distortion_measure(x0, x1, r, mu):
    # 入力は 2 次元に限っている
    N = len(x0)
    J = 0
    for n in range(N):
        for k in range(K):
            J = J + r[n, k] * ((x0[n] - mu[k, 0])**2 
                                + (x1[n] - mu[k, 1])**2)
    return J

# ---- test
# ---- Mu と R の初期化 
Mu = np.array([[-2, 1], [-2, 0], [-2, -1]])
R = np.c_[np.ones((N, 1), dtype=int), np.zeros((N, 2), dtype=int)]
distortion_measure(X[:, 0], X[:, 1], R, Mu)

# ----------------- リスト 9-1-(8)
# Mu と R の初期化
N=X.shape[0]
K=3
Mu = np.array([[-2, 1], [-2, 0], [-2, -1]])
R = np.c_[np.ones((N, 1), dtype=int), np.zeros((N, 2), dtype=int)]
max_it = 10
it = 0
DM = np.zeros(max_it) # 歪み尺度の計算結果を入れる
for it in range(0, max_it): # K-means 法
    R = step1_kmeans(X[:, 0], X[:, 1], Mu)
    DM[it] = distortion_measure(X[:, 0], X[:, 1], R, Mu) # 歪み尺度
    Mu = step2_kmeans(X[:, 0], X[:, 1], R)
print(np.round(DM, 2)) 
plt.figure(2, figsize=(4, 4))
plt.plot(DM, color='black', linestyle='-', marker='o')
plt.ylim(40, 80)
plt.grid(True)
plt.show()
