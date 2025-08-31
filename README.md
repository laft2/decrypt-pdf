# decrypt-pdf
## Overview
暗号化されたPDFと既知のパスワードを引数に取り、復号されたPDFをファイル出力します。

## Installation
uvを用いてインストールしてください。
```sh
$ uv tool install git+https://github.com/laft2/decrypt-pdf
```

## Usage
```
usage: decrypt-pdf [-h] [-o DIST_PATH] source_path password

decrypt a pdf file you know its password

positional arguments:
  source_path           source path
  password              password of pdf

options:
  -h, --help            show this help message and exit
  -o, --dist-path DIST_PATH
                        distination path, this is source_path + _decrypted.pdf as default
```

## Acknowledgements
このツールは [pypdf](https://github.com/py-pdf/pypdf) (BSD License) を利用しています。

