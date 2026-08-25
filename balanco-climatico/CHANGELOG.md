# Changelog — Balanço Climático

Todas as mudanças notáveis deste app ficam registradas aqui. O número de versão aparece
no canto do título, dentro do próprio app (`v2.0.0` etc.) — clique nele pra abrir este arquivo.

## v2.6.1 — 2026-08-25

### Alterado
- O painel "Déficit / Excedente Acumulado" (novo na v2.6.0) virou **gráfico de barras
  divergentes** (excedente acumulado pra cima, déficit acumulado pra baixo a partir do
  zero) em vez de área+linha — mesma linguagem visual do ribbon mensal logo acima, só
  que com os valores acumulados jan→dez. Diferente do ribbon mensal (que é se/senão,
  só um dos dois por mês), aqui as duas barras podem aparecer juntas no mesmo mês,
  porque o acumulado de cada uma segue independente.

## v2.6.0 — 2026-08-25

### Adicionado
- **Déficit e excedente acumulados** no gráfico de Balanço Hídrico: novo painel
  (4º, entre o ribbon mensal e o armazenamento no solo) com a soma corrida de
  jan→dez do déficit (vermelho) e do excedente (azul), como curva de área — mostra
  o quanto o "buraco" de água se aprofunda (ou a sobra se acumula) ao longo do ano,
  não só o valor isolado de cada mês. Refletido também no tooltip, na legenda, no
  resumo (déficit acumulado máximo e o mês em que ocorre) e em 2 colunas novas na
  tabela.
- **Exportar CSV** do balanço hídrico (botão no cabeçalho do gráfico), com todas as
  colunas da tabela incluindo os acumulados.
- Indicador de carregamento (spinner) na mensagem de status durante busca de dados
  climáticos e leitura de KML.

### Modernizado
- Barra de ferramentas fixa (sticky) com efeito de vidro (blur) ao rolar a página.
- Cartões (quadros), tiles e cards de mês/estatística ganharam sombra sutil,
  transições suaves e realce ao passar o mouse.
- Estado de foco visível (acessibilidade de teclado) em todos os campos e botões.

## v2.5.2 — 2026-08-24

### Corrigido
- Login do Google dava "Erro 400: invalid_request — doesn't comply with Google's
  OAuth 2.0 policy for keeping apps secure" (client ID novo, criado há poucos dias,
  caindo num fluxo antigo/descontinuado baseado em gapi.auth2). Adicionado o script
  do Google Identity Services (accounts.google.com/gsi/client), que a própria
  biblioteca do Earth Engine já usa internamente (confirmado inspecionando o código-
  fonte) quando disponível — sem ele, cai num caminho incompatível com as políticas
  atuais do Google. Testado `authenticateViaPopup` como alternativa (não usa Client
  ID próprio) mas dá erro "Missing required parameter client_id" nessa versão da
  biblioteca — mantido `authenticateViaOauth` com o Client ID de sempre.

## v2.5.1 — 2026-08-24

### Corrigido
- CFSv2 travava com `subset.select(...).pow is not a function` — `.select()` numa
  ImageCollection devolve outra ImageCollection, não uma Image (só Image tem `.pow()`).
  Corrige calculando a magnitude do vento por leitura de 6h individual (`.map()`
  imagem a imagem) antes de tirar a média do dia.

## v2.5.0 — 2026-08-24

### Adicionado
- **CFSv2 como 4ª fonte de dados** (Climate Forecast System v2, NOAA, catálogo
  oficial do Google Earth Engine — `NOAA/CFSV2/FOR6H_HARMONIZED`). Reanálise global
  de 6 em 6 horas, cobertura 1979–hoje (a mais atual de todas as fontes). Achada
  inspecionando o app público "ENSO Monitor" (Luis Fernando Chimelo Ruiz,
  ee-ruizch.projects.earthengine.app/view/enso-monitor), sugerida pelo usuário.
  Como dataset oficial do catálogo, não tem o risco de permissão que o BR-DWGD tem
  (que está num projeto pessoal do autor).
  - Vento: dataset só tem a 10m — ajustado pra 2m com a fórmula padrão FAO-56 (eq. 47).
  - Umidade: dataset só tem "umidade específica" — convertida pra pressão de vapor
    real e depois pra um "% de umidade relativa equivalente" (mesma fórmula das
    outras fontes), usando a pressão atmosférica também disponível no dataset.
  - Radiação: convertida de W/m² (potência) pra MJ/m²/dia (energia diária).
  - Testado: wiring da UI, login, sem regressão nas fontes existentes.

## v2.4.0 — 2026-08-22

### Adicionado/Corrigido
- Trocada a fonte do BR-DWGD do espelho comunitário (`sat-io/open-datasets`, que
  parava em jul/2020) para a coleção direto do projeto do autor original
  (`projects/ee-alexandrexavier/assets/BR-DWGD`), cobrindo **1961–2025**. Achada
  inspecionando o código-fonte compilado do app público DataClimaBR
  (ee-deborapdsouza.projects.earthengine.app/view/dataclimabr — colaboradora que
  cita o mesmo Xavier et al. 2022), sugerida pelo usuário.
- Corrigidos os fatores de escala/offset de RH, RS e vento (U2) — o resumo que eu
  tinha usado antes (v2.3.2) trazia offset=0 pra essas três, mas o correto (confirmado
  no mesmo código-fonte) tem um pequeno offset negativo (-0,393701 / -0,057087 /
  -0,059055 respectivamente). PR e TMAX/TMIN já estavam certos.
- Removido o limite automático de ano (antes travava em 2020) já que a nova fonte
  cobre até o presente, igual as outras.

## v2.3.2 — 2026-08-22

### Corrigido
- Bug real e sério: os valores do BR-DWGD vinham em unidades absurdas (Tmáx ~15.000,
  chuva negativa em milhares de mm). Causa: as bandas do dataset são inteiras
  (int16/byte) escaladas pra economizar espaço, e eu não estava aplicando a
  conversão. Achado o fator real de escala/offset no script de ingestão do
  publicador (github.com/samapriya/awesome-gee-community-datasets) — aplicado
  agora em cada imagem diária antes de somar/tirar média (não dava pra converter
  só o resultado agregado, o offset quebraria a soma). Depurado com dados reais
  em colaboração com o usuário (login e consultas reais no Earth Engine, algo que
  eu não consigo testar sozinho).

## v2.3.1 — 2026-08-21

### Corrigido
- BR-DWGD travava com `Image.divide: If one image has no bands...` quando o ano
  selecionado ficava fora da cobertura do dataset (Tmáx/Tmín/RH/vento/radiação só
  até 2020; chuva até 2022). Agora consultas fora da cobertura devolvem "sem dado"
  por mês, sem travar; e o "Ano final" ajusta sozinho pra 2020 ao escolher essa fonte.

## v2.3.0 — 2026-08-21

### Adicionado
- **BR-DWGD como 3ª fonte de dados** (Brazilian Daily Weather Gridded Data, Xavier et
  al./UFES — grade de 0,1° calibrada com 1.250+ estações do INMET e 11.000+ pluviômetros),
  acessada via Google Earth Engine. É a fonte "nacional" mais robusta disponível sem
  precisar de importação manual — mas só cobre dados históricos (até ~2020-2022, sem
  anos recentes) e exige login com conta Google (o Earth Engine não tem API pública
  anônima).
- O app **mudou de hospedagem**: agora vive publicado no GitHub Pages
  (`https://jpbolsairriga-lgtm.github.io/adutora/balanco-climatico/balanco-climatico.html`)
  em vez de só um arquivo local — necessário porque o login do Google não aceita a
  origem `file://`. Continua funcionando 100% no navegador, sem servidor próprio.
- "Comparar com outra fonte" virou um seletor com as 3 fontes (antes era um checkbox
  de liga/desliga só pra Open-Meteo).
- Pasta do projeto renomeada de "Balanço Climatico" pra "balanco-climatico" (sem
  acento/espaço, URL mais limpa).

## v2.2.0 — 2026-08-21

### Adicionado
- **Seletor de fonte de dados** na barra superior (NASA POWER ou Open-Meteo/ERA5-Land) —
  todos os cálculos (balanço hídrico, irrigação) passam a usar só a fonte escolhida.
  Quando a fonte é Open-Meteo, a ETo já vem pronta do provedor (não recalcula FAO-56).
- **Período de até 10 anos consecutivos**: além do ano único de sempre, agora dá pra
  escolher "N anos (média)" — cada mês do relatório vira a **média histórica** desse
  mês calendário ao longo do período (ex.: "Janeiro" = média de todos os janeiros do
  intervalo), como uma normal climatológica. Um único request a cada API (o endpoint
  mensal da NASA POWER e o diário do Open-Meteo aceitam intervalos de anos direto).
- A **Conferência entre Fontes** virou opcional: checkbox "Comparar com outra fonte"
  na barra (desligado por padrão) — só busca e mostra a segunda fonte quando ligado,
  em vez de sempre rodar as duas. Os rótulos do quadro agora refletem dinamicamente
  qual fonte é a principal e qual é a de comparação.

## v2.1.0 — 2026-08-21

### Adicionado
- **Conferência entre Fontes Climáticas**: novo quadro que busca uma segunda fonte
  independente, **Open-Meteo (reanálise ERA5-Land)**, em paralelo com a NASA POWER.
  Mostra 3 mini-gráficos comparando Tmáx, Precipitação e ETo mês a mês entre as duas
  fontes (a ETo do Open-Meteo já vem calculada por FAO-56 Penman-Monteith pelo próprio
  provedor — serve de conferência tanto dos dados quanto da fórmula usada aqui), mais
  tabela de diferenças e resumo da divergência média. NASA POWER continua sendo a
  única fonte usada nos cálculos de balanço hídrico e irrigação; a segunda fonte é
  só pra auditoria/confiança. Se o Open-Meteo falhar, o resto do app funciona normal
  só com NASA POWER.

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
