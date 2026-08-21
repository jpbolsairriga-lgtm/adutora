# Changelog — Balanço Climático

Todas as mudanças notáveis deste app ficam registradas aqui. O número de versão aparece
no canto do título, dentro do próprio app (`v2.0.0` etc.) — clique nele pra abrir este arquivo.

## v2.0.0 — 2026-08-21

### Adicionado
- **Módulo de Irrigação**, inspirado no "Estudo de Lâmina" (planilha Bolsa Irriga):
  - Quadro **Parâmetros de Irrigação**: espaçamento entre linhas/plantas, projeção de copa,
    coeficiente de localização (Kl, Keller & Bliesner) e grade de Kc mensal editável por
    fase fenológica do café (Florada/Chumbinho/Granação/Maturação/Colheita).
  - Quadro **Necessidade de Irrigação**: Etc bruto e localizado (mm/dia), litros/planta/dia,
    m³/ha/dia, gráfico com o mês crítico destacado, e tabela completa.
- **Balanço Hídrico Climático reescrito** para o método sequencial de **Thornthwaite & Mather
  (1955)** (mesma formulação da planilha ESALQ/USP de Rolim, Sentelhas & Barbieri, 1998):
  agora considera capacidade de água disponível no solo (CAD, editável), armazenamento (ARM),
  ETR, déficit e excedente reais — substitui o balanço ingênuo P−ETo da v1, que não
  considerava o efeito-tampão do solo. Novo gráfico de 3 painéis (chuva×ETP, déficit/excedente,
  armazenamento no solo).
- Todos os cálculos de irrigação reagem em tempo real a mudanças nos parâmetros (sem precisar
  reconsultar as APIs de clima).
- Badge de versão no cabeçalho, linkando para este changelog.

### Corrigido
- `.no-print` nunca tinha uma regra CSS de verdade — o relatório impresso duplicava o
  cabeçalho. Agora `@media print` esconde corretamente qualquer elemento com essa classe.

## v1.1.0 — 2026-08-20

### Corrigido
- Elevação usada no cálculo de ETo não vinha mais de "assumir nível do mar" quando o KML não
  tinha altitude real (caso comum em exports do Google Earth) — agora é consultada de verdade
  via Open-Meteo Elevation API (SRTM/Copernicus DEM), com a fonte sempre visível na UI.

## v1.0.0 — 2026-08-20

### Adicionado
- Primeira versão: importação de polígono KML, imagem de satélite (Esri World Imagery) com
  data/fonte reais via serviço de metadados, clima mensal (NASA POWER) com ETo calculada pelo
  método padrão FAO-56 Penman-Monteith, gráfico de balanço P×ETo, gráfico de temperatura
  máxima, relatório imprimível.
