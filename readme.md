# Organizador de Notas Kindle

 A partir do arquivo My Clippings.txt na pasta documents do Kindle, consegue-se gerar um diretório com as notas separadas por título, contendo as anotações de cada livro em específico.
 O programa está disponível para os sistemas operacionais de linux e windows. Ainda é uma versão em desenvolvimento, por isso pode apresentar alguns bugs.
 
 
 ![github-small](https://user-images.githubusercontent.com/25461720/51930274-53ad7080-23e1-11e9-9bc3-35e8ca2ce8a0.png)
 
### Pré requisitos
* Python 3.6
* PyQt4

### Instalação do PyQt

* Se você está usando linux, há a documentação no link abaixo para a instalação:
https://www.saltycrane.com/blog/2008/01/how-to-install-pyqt4-on-ubuntu-linux/

* Se você usa Windows,
é necessário baixar o arquivo PyQt4‑4.11.4‑cp36‑cp36m‑win_amd64.whl
 referente a instalação do PyQt versão 4 para a versão 3.6 do python que está disponível em :
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4

Após download no diretório de Downloads execute o comando via cmd:

```
pip install PyQt4‑4.11.4‑cp36‑cp36m‑win_amd64.whl
```

Talvez seja necessário atualizar sua versão do instaldor pip para tal, caso ocorra algum erro, para tanto utilize:

```
python -m pip install --upgrade pip
```

## Funcionamento e acesso

* Execute o comando abaixo para clonar o repositório:

```
git clone https://github.com/noreng-jg/organizador-de-notas.git
```

* Entre via terminal na pasta organizador-de-notas gerada e posteriormente na pasta GUI

* Execute o comando: 

```
python main_app.py
```

Deverá aparecer uma interface para a utilização do programa se o PyQt for instalado corretamente. 

## Observações
Devido a alguns problemas iniciais de acentuação com o utf-8 no python decidi comentar tudo no código em inglês.


