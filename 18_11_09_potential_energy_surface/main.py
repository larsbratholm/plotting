import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from scipy.stats import kde

def open_pickle(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

# exp/primary: -26
# cf-upbe/tzvp/primary: -24.41321864
# cf-upbe0/tzvp/primary: 

if __name__ == "__main__":
    data = open_pickle("data.pkl")

    idx = 7

    x,y,z = data[idx][:,0], data[idx][:,1], data[idx][:,5]
    z *= 627.509
    z -= np.min(z)

    uniq = np.unique(np.concatenate([x,y]))[:-3]
    value_to_index = {}
    for i, v in enumerate(uniq):
        value_to_index[v] = i

    X,Y = np.meshgrid(uniq,uniq)

    Z = [[None for i in range(uniq.size)] for j in range(uniq.size)]

    for a,b,c in zip(x,y,z):
        if a not in value_to_index or b not in value_to_index:
            continue
        i = value_to_index[a]
        j = value_to_index[b]
        Z[i][j] = c


    # This bit is just to make it easier to spot discontinuities
    # int the energy
    #plt.scatter(x,y)
    #plt.xlim([0.8,3.1])
    #plt.ylim([0.8,3.1])
    #plt.show()

    #for i in range(uniq.size):
    #    print(uniq[i])
    #    plt.plot(X[0],Z[i], 'o')
    #    plt.show()
    #for i in range(uniq.size):
    #    print(uniq[i])
    #    plt.plot(X[0],[Z[j][i] for j in range(uniq.size)], 'o')
    #    plt.show()
    #quit()


    # pink
    # RdGy
    # RdBu
    plt.contourf(Y,X,Z,50, cmap="RdGy")
    #plt.contour(Y,X,Z,20, cmap="RdGy")
    #plt.imshow(Z, extent=[uniq[0],uniq[-1],uniq[0],uniq[-1]], origin='lower', cmap='RdGy')
    plt.colorbar()
    plt.show()
