# mlclusters

The mlclusters is a tool to visualize ddRAD (Double Digest Restriction Associated DNA) assemblies using machine learning clustering methods available in [scikit-learn](http://scikit-learn.org/stable/index.html). 
The mlclusters takes ipyrad output files (e.g. geno format), stores SNPS data using `numpy` and `pandas`, fit the various models currently available in scikit-learn, evaluate clustering performance and create visual plots using `Matplotlib`, and `Toyplot`.

This library is still under development. Currently, only [KMeans clustering method](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) is available, however I am adding other clustering methods soon. Input assembly files need to be in geno format, which can be obtained using [ipyrad](http://ipyrad.readthedocs.io/features.html).

Please refer the notebook (mlclusters_nb_simulated_data.ipynb) to see a demonstration of the library used with a generated data. 

#### _In Development_

One of the problems with clustering methods is how to handle missing data. In the case in PCA clustering methods, missing data is often treated as 0 (homozygous) which may skew results. However, using K-means clustering methods we can cluster data without having to assign 0. Currently, I am trying to impute missing values with column means using an iteration of PCA and K-means clustering methods. You can visit my notebook (Missing_data.ipynb) to see my progress. I am also working on this notebook (mlclusters_nb_v1.ipynb) to test the method with an example geno file that is available in the Data folder.


### Installation

```
## clone the repo 
git clone [...]  

## cd into repo dir 
cd mlclusters  

## local development install with pip 
pip install -e . 
```

### Usage

See notebooks/ directory.
