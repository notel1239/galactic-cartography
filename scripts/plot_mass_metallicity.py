#!/usr/bin/env python3
"""
Plot mass-metallicity relation for galaxies with star formation rate color mapping.
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
    star_formation_rate = data['star_formation_rate']
    
    # Create figure
    plt.figure(figsize=(9, 6))
    
    # Scatter plot with color representing star formation rate
    sc = plt.scatter(stellar_mass, gas_metallicity, 
                     c=star_formation_rate, 
                     cmap='viridis', 
                     alpha=0.8, 
                     edgecolors='k', 
                     linewidth=0.5)
    
    # Set logarithmic scale for mass axis (galaxy masses span many orders of magnitude)
    plt.xscale('log')
    
    # Labels and title
    plt.xlabel('Stellar Mass [M$_\odot$]', fontsize=14)
    plt.ylabel('Gas Metallicity [Z$_\odot$]', fontsize=14)
    plt.title('Galaxy Mass-Metallicity Relation (colored by SFR)', fontsize=16)
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    
    # Add colorbar
    cbar = plt.colorbar(sc)
    cbar.set_label('Star Formation Rate [M$_\odot$ yr$^{-1}$]', fontsize=12)
    
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