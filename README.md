# 🚀 JobScraper - Automação Inteligente de Busca de Empregos com Python & Selenium

Automatizar a busca de empregos pode ser um **game changer** para quem está em busca de oportunidades! O **JobScraper** é um **web scraper inteligente** que coleta **automaticamente** vagas de sites como **InfoJobs** e **Gupy**, armazena os dados e envia **alertas automáticos via WhatsApp (simulado)**.  

Com suporte a **paginação automática**, **coleta de múltiplos sites** e **execução na nuvem com Google Colab**, esse projeto **simplifica** e **otimiza** o processo de busca por empregos.  

---

## 📌 **O que o JobScraper faz?**

✅ **Coleta automática de vagas** com título, data de publicação e link direto para candidatura.  
✅ **Paginação automática** - percorre várias páginas sem necessidade de intervenção manual.  
✅ **Suporte para múltiplos sites** - atualmente **InfoJobs** e **Gupy**, mas é fácil adicionar outros.  
✅ **Envio de alertas via WhatsApp (simulado)** - garantindo que você não perca oportunidades.  
✅ **Armazena os dados em CSV** - facilitando análise e acompanhamento.  
✅ **Compatível com Google Colab** - roda na nuvem sem precisar instalar nada no seu PC.  
✅ **Fácil expansão** - adicione novos sites apenas ajustando os seletores CSS.  

---

## 🛠 **Tecnologias utilizadas**

🔹 **Python** - principal linguagem do projeto  
🔹 **Selenium** - automação de navegação web  
🔹 **Pandas** - manipulação e armazenamento de dados  
🔹 **BrowserStack** - para rodar o Selenium no Google Colab  
🔹 **Web Scraping com Seletores CSS**  

---

## 📈 **Expansão e melhorias implementadas**

⚙️ **Paginação automática** - O scraper percorre várias páginas de resultados sem intervenção manual.  
⚙️ **Suporte a múltiplos sites** - Atualmente coleta vagas no **InfoJobs** e **Gupy**, mas novos sites podem ser adicionados.  
⚙️ **Segurança aprimorada** - Uso de **variáveis de ambiente** para armazenar credenciais do BrowserStack.  
⚙️ **Execução no Google Colab** - Compatível com execução remota, sem precisar instalar nada no PC.  

---

## 📌 **Como funciona?**

### **1️⃣ Instalação das dependências**
Execute o comando abaixo para instalar os pacotes necessários:
```bash
pip install selenium pandas

2️⃣ Configuração das credenciais
Para garantir a segurança, configure as credenciais do BrowserStack como variáveis de ambiente:

python
Copiar
Editar
import os
os.environ['BROWSERSTACK_USERNAME'] = 'SEU_USUARIO'
os.environ['BROWSERSTACK_ACCESS_KEY'] = 'SUA_CHAVE_DE_ACESSO'


3️⃣ Executando o JobScraper
Basta rodar o script jobscraper.py no seu ambiente Python:

python
Copiar
Editar
python jobscraper.py
O scraper vai buscar as vagas automaticamente, salvá-las em CSV e simular alertas via WhatsApp.



