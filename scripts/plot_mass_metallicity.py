#!/usr/bin/env python3
"""
Plot mass-metallicity relation for galaxies.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    # Load data
    data_path = os.path.join(os.path.dirname(__file__), '../data/galaxy_snapshot.csv')
    data = np.genfromtxt(data_path, delimiter=',', skip_header=1, names=True)
    
    stellar_mass = data['stellar_mass']
    gas_metallicity = data['gas_metallicity']
    
    # Create figure
    plt.figure(figsize=(8, 6))
    plt.scatter(stellar_mass, gas_metallicity, alpha=0.7, edgecolors='k', linewidth=0.5)
    
    # Set logarithmic scale for mass axis (galaxy masses span many orders of magnitude)
    plt.xscale('log')
    
    # Labels and title
    plt.xlabel('Stellar Mass [M$_\odot$]', fontsize=14)
    plt.ylabel('Gas Metallicity [Z$_\odot$]', fontsize=14)
    plt.title('Galaxy Mass-Metallicity Relation', fontsize=16)
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    
    # Ensure output directory exists
    output_dir = os.path.join(os.path.dirname(__file__), '../output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save figure
    output_path = os.path.join(output_dir, 'mass_metallicity_relation.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f'Plot saved to {output_path}')
    
    plt.show()

if __name__ == '__main__':
    main()