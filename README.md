# brs-libs

[![Anaconda-Server Badge](https://anaconda.org/brsynth/brs_libs/badges/latest_release_date.svg)](https://anaconda.org/brsynth/brs_libs) [![Anaconda-Server Badge](https://anaconda.org/brsynth/brs_libs/badges/version.svg)](https://anaconda.org/brsynth/brs_libs)

Libraries for rpTools:
* rpCache
* rpSBML

## rpSBML
Defines SBML structure with additional fields relative to [RetroPath2](https://github.com/brsynth/RetroPath2-wrapper) objects.

### Prerequisites
* Python 3 with the following modules:
    * python-libsbml
* [RDKit](https://www.RDKit.org)


## rpCache

### Memory management

#### File mode
This is the default mode. All cache data are stored into files on disk and loaded in memory each time the tool is used. In this mode, fingerprint in memory is equal to the size of cache files loaded in memory multiplied by the number of processes which are running at the same time. Option can be specified by `--store-mode file`.

#### DB mode
In order to save memory space, cache data can be loaded once in a database (redis) so that the memory space taken is equal to one instance of the cache, whatever the number of processes whic are running. Option can be specified by `--store-mode <db_host>`, where `db_host` is the hostname on which redis server is running.


### Install
rpCompletion requires [RDKit](https://www.RDKit.org) which is not available through pip. It can be installed through Conda:
```sh
[sudo] conda install -c rdkit rdkit
```
#### From pip
```sh
[sudo] python -m pip install brs_libs
```
#### From Conda
```sh
[sudo] conda install -c brsynth brs_libs
```

### Run

#### (Re-)generate the cache
**From Python code**
```python
from brs_libs import rpCache

rpCache.generate_cache(outdir)
```

**From CLI**

After having installed brs_libs Python module:
```sh
python -m brs_libs --gen_cache <folder>
```


### Test
Tests can be runned. To do so, please follow insructions below:
```
cd tests
./test-in-docker.sh
```


## Authors

* **Melchior du Lac**
* **Joan Hérisson**

## Acknowledgments

* Thomas Duigou


## Licence
brs_libs is released under the MIT licence. See the LICENCE file for details.
