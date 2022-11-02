# DesignPatterns
Repositório contendo a aplicação referente aos conceitos de design pattern discutidos na disciplina de Engenharia de Software (2º semestre - 2022).

---
## Clonando projeto
O primeiro passo para executar o projeto é cloná-lo na sua máquina. Para isso, abra o terminal de comando, navegue até o diretório onde deseja alocar o projeto e entre com o seguinte comando:  
```git clone https://github.com/TiagoMPereira/DesignPatterns.git```  
Em seguida entre no diretório clonado  
```cd DesignPatterns```  

---
## Gerência de dependências
No python a gerência de dependências é feita criando um ambiente virtual e especificando quais pacotes (e quais suas versões) serão utilizados no projeto. Para criar um ambiente virtual basta digitar o seguinte comando no terminal:  
```python -m venv env_projeto```  
Uma vez criado, é preciso ativar o ambiente virtual:  
```env_projeto\Scripts\activate.bat``` (Windows cmd)  
```env_projeto\Scripts\Activate.ps1``` (Windows powershell)  
```env_projeto/bin/activate``` (Linux/MacOS)  
Com o ambiente ativado basta importar as dependências:  
```pip install -r requirements.txt```  
Da mesma forma, é possível gerar o arquivo de dependências com todos os pacotes e versões utilizadas digitando:  
```pip freeze > requirements.txt```  

---
## Testes
Caso o pytest não esteja nos requisitos instalados pelo requirements.txt é possível instalá-lo a parte.  
```pip install pytest```  
Para executar os testes, basta rodar no terminal  
```pytest```

---
## CI
Foi adicionada ao repositório uma ação automática para executar toda a suíte de testes sempre que um push for dado em qualquer uma das branches.
