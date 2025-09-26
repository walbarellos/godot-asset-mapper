````markdown
# Godot Asset Harvester

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
[![Made with Love](https://img.shields.io/badge/Made%20with-Love-red)](#)

---

## 📖 Descrição

**Godot Asset Harvester** é um script em Python que faz *scraping* da **[Godot Asset Library](https://godotengine.org/asset-library/asset)**, coletando todos os addons, templates e recursos disponíveis e salvando em formato **JSON**.  

Ele foi criado para auxiliar desenvolvedores na análise e seleção das melhores ferramentas para seus jogos, com especial ênfase em projetos como *deck-builders* ou jogos caricaturais.

> 🔎 Objetivo: oferecer uma visão geral das ferramentas disponíveis e acelerar o desenvolvimento com base no ecossistema da comunidade Godot.

---

## 🚀 Como usar

### 1. Pré-requisitos

- Python **3.8+**
- Bibliotecas:
  ```bash
  pip install requests beautifulsoup4
````

### 2. Executar

```bash
python scrape_godot_assets.py
```

### 3. Resultado

Será gerado o arquivo:

```bash
godot_assets.json
```

Cada entrada segue a estrutura:

```json
{
  "title": "Simple Card Pile UI",
  "author": "insideout-andrew",
  "tags": "2D Tools 4.2 Community MIT",
  "url": "https://godotengine.org/asset-library/asset/2564"
}
```

---

## ⚙️ Opções avançadas

### ⏱️ Pausa entre requisições

Para não sobrecarregar o servidor, o script faz `time.sleep(1)` a cada página.
Você pode aumentar ou diminuir esse valor conforme necessário.

### 📂 Dividir JSON grande

Se o arquivo ultrapassar **100 MB**, use o comando `split` no Linux:

```bash
split -b 20M godot_assets.json assets_part_
```

Isso gera arquivos menores (`assets_part_aa`, `assets_part_ab` …).

### 📊 Converter para CSV

Para abrir no Excel/LibreOffice:

```python
import pandas as pd

df = pd.read_json("godot_assets.json")
df.to_csv("godot_assets.csv", index=False)
```

---

## 📦 Estrutura do Projeto

```
tools/
 ├─ scrape_godot_assets.py   # Script principal
 ├─ godot_assets.json        # Saída (gerada após rodar)
 └─ README.md                # Documentação
```

---

## 🖥️ Compatibilidade

Testado em:

* Python **3.8 – 3.13**
* Linux (Arch, Ubuntu), Windows 10/11, macOS Ventura

---

## ⚠️ Problemas conhecidos

* Se o JSON vier vazio, verifique:

  * Conexão com a internet
  * Se a **Asset Library** está online
  * Se os seletores HTML mudaram (`soup.select("li.asset-item")` no script)

---

## 📌 Roadmap

* [ ] Exportação CSV nativa
* [ ] Filtros automáticos por categoria (UI, Cards, Shaders, etc.)
* [ ] Dashboard com estatísticas (mais baixados, mais bem avaliados)
* [ ] Integração com projetos Godot via EditorPlugin

---

## 👨‍💻 Autores

* **Willian Albarello** — idealizador, integração com projeto de cartas caricatural *Skill Pobre Royale*
* **Assistente AI (Ohr/ChatGPT)** — apoio técnico na engenharia, scraping e documentação

---

## 💡 Dicas práticas

* Explorar rapidamente o JSON com `jq`:

  ```bash
  jq '.[] | select(.title | test("card"; "i"))' godot_assets.json
  ```
* Usar filtros para encontrar **card games**:

  ```bash
  jq '.[] | select(.tags | test("2D|card"; "i"))' godot_assets.json
  ```
---

## 📜 Licença

Distribuído sob a licença **MIT**. Uso livre para modificar, redistribuir e publicar, mantendo os créditos.

```text

MIT License

Copyright (c) 2025 Willian Albarello

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```

---
