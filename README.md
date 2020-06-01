
# kodanka

![](https://github.com/kodanka/kodanka.fi/workflows/Deploy%20site/badge.svg)
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

<img src="images/duck.png" width="100">

## Licens

Materialet delas under [Creative Commons Attribution-ShareAlike 4.0
International License][cc-by-sa].

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

## Utveckla

### Installera paket

```
conda install -c conda-forge jupyterlab
conda install -c conda-forge nbsphinx
conda install -c conda-forge jupyterlab
conda install sphinx_rtd_theme
```

### Producera material

```
jupyter lab
```

### Testa sidan

```
make build
```

### Nbsphinx dokumentation

https://nbsphinx.readthedocs.io
