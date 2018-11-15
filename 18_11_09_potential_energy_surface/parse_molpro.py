import numpy as np
import pickle
import sys

def parse_energies(filename):
    """
    Return all the energies in a molpro out-file
    """
    with open(filename) as f:
        lines = f.readlines()

    if "Molpro calculation terminated" not in lines[-1]:
        print("Error parsing %s" % filename)
        return

    energies = lines[-3].split()[:8]
    return energies

def parse_filename(filename):
    tokens = filename.split("/")[-1].split("_")
    tokens[-1] = tokens[-1][:-4]
    tokens[0] = int(tokens[0])
    return tokens



if __name__ == "__main__":
    filenames = sys.argv[1:]
    energies = {}
    for filename in filenames:
        energy = parse_energies(filename)
        if energy is None:
            continue
        atom, d1, d2 = parse_filename(filename)
        if atom not in energies: energies[atom]=[]

        energies[atom].append(np.asarray([d1,d2] + energy, dtype=float))

    for key in energies.keys():
        energies[key] = np.asarray(energies[key], dtype=float)

    with open("data.pkl", "wb") as f:
        pickle.dump(energies, f)
