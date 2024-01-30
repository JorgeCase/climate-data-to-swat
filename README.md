<body>
  <h1 align="center">Climate Data To SWAT</h1>
  <h2 align="center">Descrição</h2>
  <p align="center">Esta é uma <b>ferramenta de processamento de dados para o modleo SWAT</b>. O aplicativo foi desenvolvido em <b>Python</b> para auxiliar no processamento de arquivos de dados climáticos fornecidos pelo <b>Instituto Nacional de Meteorologia (INMET)</b>, convertendo-os para um formato adequado para ser utilizado no <b>Soil and Water Assessment Tool (SWAT)</b>.</p>
  <h2 align="center">Recursos</h2>
  <ul>
    <li><b>Interface Gráfica de Usuário (GUI)</b>: O aplicativo oferece uma interface gráfica intuitiva que permite aos usuários navegar e selecionar facilmente a pasta de entrada contendo os arquivos de dados climáticos.</li>
    <li><b>Processamento de Dados</b>: A ferramenta lê arquivos CSV, extrai dados relevantes do cabeçalho, remove informações desnecessárias e preenche datas ausentes nos dados usando as bibliotecas <b>pandas</b> e <b>tkinter</b>.</li>
    <li><b>Formatação de Saída</b>: Os dados processados são salvos em arquivos de texto, cada um nomeado de acordo com o nome e código do conjunto de dados.</li>
  </ul>
  <h2 align="center">Habilidades desenvolvidas</h2>
  <ul>
    <li><b>Programação em Python</b>: O projeto é implementado usando a linguagem de programação Python, utilizando as bibliotecas <b>pandas</b>, <b>tkinter</b> e <b>os</b> para a manipulação de dados, desenvolvimento da interface gráfica e operações de arquivos.</li>
    <li><b>Desing de Interface Gráfica de Usuário</b>: A biblioteca <b>tkinter</b> é empregada para criar uma interface gráfica interativa e amigável para o aplicativo.</li>
    <li><b>Manipulação de Dados</b>: A extração, limpeza e transformação de dados foram realizadas usando <b>pandas</b></li>
    <li><b>Manipulação de Arquivos</b>: O projeto envolve leitura e escrita de arquivos, criação de diretórios e manipulação de caminhos de arquivo usando a biblioteca <b>os</b> do Python.</li>
  </ul>
  <h2 align="center">📁 Acesso ao Projeto</h2>
  <ol>
    <li><strong>Clonar o Repositório</strong>: Clone este repositório do GitHub para sua máquina local usando o seguinte comando:<br><code>git clone git@github.com:JorgeCase/climate-data-to-swat.git</code></li>
    <li><strong>Navegar até a Pasta do Projeto</strong>: Altere o diretório atual para a pasta do repositório clonado:<br><code>cd climate-data-to-swat</code></li>
    <li><strong>Instalar Dependências</strong>: Certifique-se de ter o Python instalado em seu sistema. Instale as dependências necessárias executando o seguinte comando em seu terminal:<br><code>pip install -r requirements.txt</code></li>
    <li><strong>Executar o Aplicativo</strong>: Execute o script principal para iniciar o aplicativo:<br><code>python3 climate-data-to-swat.py</code></li>
    <li><strong>Usar a GUI</strong>: Uma interface gráfica será exibida. Siga as instruções na tela para selecionar a pasta de entrada contendo seus arquivos de dados climáticos e iniciar o processamento. A ferramenta criará uma pasta de saída chamada <code>output_climate2swat</code> dentro da pasta de entrada e salvará os arquivos de dados processados lá.</li>
    <li><strong>Conclusão e Saída</strong>: Após o processamento ser concluído, a ferramenta exibirá uma mensagem de conclusão. Os arquivos de dados processados estarão disponíveis na pasta <code>output_climate2swat</code> dentro da pasta de entrada selecionada.</li>
  </ol>
  <h2 align="center">Observações</h2>
  <ul>
    <li> O aplicativo é desenvolvido usando o Python 3.</li>
    <li>Se encontrar algum problema ou tiver dúvidas e sugestões, entre em contato pelo e-mail:<br><code>jorgekzbra@gmail.com</code></li>
  </ul>
  <p>Aproveite o Climate-data-to-swat para simplificar a preparação de dados para suas simulações no SWAT!</p>
</body>
