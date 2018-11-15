import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from scipy.stats import kde

def open_pickle(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)


if __name__ == "__main__":
    data = open_pickle("data.pkl")

    # 7 is tertiary, 10 primary and 11 secondary
    idx = 7

    # x is R-H distance. y is NC-H distance. z is CF-uPBE/TZVP energy
    x,y,z = data[idx][:,0], data[idx][:,1], data[idx][:,5]
    # Convert to kcal/mol
    z *= 627.509
    # Subtract reference
    z -= np.min(z)

    # Get the unique elements (the grid points).
    # Due to convergence issues I only consider up to 3Å,
    # even though the data has values up to 3.9.
    uniq = np.unique(np.concatenate([x,y]))[:-3]
    # Look up table to convert a distance to the index in the grid
    value_to_index = {}
    for i, v in enumerate(uniq):
        value_to_index[v] = i

    # create grids
    X,Y = np.meshgrid(uniq,uniq)

    # Make an array. Could probably use a float np.array with
    # np.nan instead of None
    Z = [[None for i in range(uniq.size)] for j in range(uniq.size)]

    # Fill the array
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
