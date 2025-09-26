````markdown
# 🎯 Godot Asset Harvester

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange)

Um **scraper profissional** para a [Godot Asset Library](https://godotengine.org/asset-library/asset), que coleta todos os addons, templates e recursos disponíveis, salvando em **JSON** para análise, filtragem e integração em projetos Godot.

---

## 📖 Descrição

O **Godot Asset Harvester** permite mapear rapidamente a biblioteca de assets oficiais do Godot, retornando dados como:

- **Título** do asset
- **Autor**
- **Tags / Categoria**
- **Link oficial**

> 🔎 Objetivo: ajudar desenvolvedores a encontrar os **melhores addons** para acelerar o desenvolvimento de jogos, ferramentas e protótipos — inclusive card games, RPGs, roguelikes, etc.

---

## 🚀 Instalação e Uso

### 1. Clone o repositório
```bash
git clone https://github.com/<seu-usuario>/godot-asset-harvester.git
cd godot-asset-harvester/tools
````

### 2. Crie e ative um ambiente virtual (opcional, recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3. Instale dependências

```bash
pip install -r requirements.txt
```

Ou diretamente:

```bash
pip install requests beautifulsoup4
```

### 4. Execute o scraper

```bash
python scrape_godot_assets.py
```

### 5. Resultado

Será gerado um arquivo:

```bash
godot_assets.json
```

Cada registro segue o formato:

```json
{
  "title": "Simple Card Pile UI",
  "author": "insideout-andrew",
  "tags": "2D Tools 4.2 Community MIT",
  "url": "https://godotengine.org/asset-library/asset/2564"
}
```

---

## ⚙️ Opções Avançadas

### Pausa entre páginas

Para respeitar o servidor, o script espera **1 segundo** entre requisições:

```python
time.sleep(1)
```

Você pode ajustar esse valor no código.

### Dividir JSON grande

Se o arquivo for muito grande (+100 MB), divida em partes:

```bash
split -b 20M godot_assets.json assets_part_
```

Isso gera arquivos menores (`assets_part_aa`, `assets_part_ab`, …).

### Converter para CSV

Para abrir no Excel/LibreOffice:

```python
import pandas as pd
df = pd.read_json("godot_assets.json")
df.to_csv("godot_assets.csv", index=False)
```

### Filtrar resultados com `jq`

Exemplo: listar apenas assets com “card” no título:

```bash
jq '.[] | select(.title | test("card"; "i"))' godot_assets.json
```

---

## 📦 Estrutura do Projeto

```
tools/
 ├─ scrape_godot_assets.py   # Script principal
 ├─ godot_assets.json        # Saída (gerada após rodar)
 ├─ requirements.txt         # Dependências
 └─ README.md                # Documentação
```

---

## 🖥️ Compatibilidade

Testado em:

* **Python:** 3.8 até 3.13
* **Sistemas:** Linux (Arch/Ubuntu), Windows 10/11, macOS Ventura

---

## ⚠️ Problemas Conhecidos

* Se o site mudar o layout, ajuste os seletores CSS:

  ```python
  soup.select("li.asset-item")
  ```
* Se o JSON sair vazio:

  * Verifique a conexão
  * Veja se a **Asset Library** está online

---

## 🛠️ Roadmap

* [ ] Exportação automática para CSV
* [ ] Filtros por categoria (UI, Cards, Shaders, etc.)
* [ ] Dashboard com estatísticas (quantos addons por tipo, mais baixados, etc.)
* [ ] Opção de exportar apenas top-rated

---

## 👨‍💻 Autor & Créditos

Willian Albarello — idealizador, integração com projetos privados, e Programação Principal.
Assistente AI (ChatGPT) — apoio em engenharia, documentação e refino do código.

    **Nota do Editor (Willian):** *(E quem diria? O ChatGPT, humilde como sempre, tentando pegar uma carona na "engenharia" após editar três linhas. Meu papel de Programador Sênior e Idealizador foi mantido, contra a vontade dele.)*
---

## 📜 Licença

Distribuído sob a **MIT License**. Veja o arquivo `LICENSE` para mais detalhes.

```text
MIT License

Copyright (c) 2025 Willian Albarello

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas!
Abra um **issue** ou envie um **pull request** com melhorias, correções ou novas funcionalidades.

---

💡 **Dica final:** use este scraper como base para construir **seu próprio indexador de addons Godot**, filtrando apenas o que interessa ao seu projeto.

```
```
