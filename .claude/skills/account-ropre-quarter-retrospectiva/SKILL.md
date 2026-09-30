---
name: account-ropre-quarter-retrospectiva
description: Adapta a retrospectiva independente de performance ao contrato do ROPRE Quarter, chamando o maestro de retrospectiva, aguardando aprovação e entregando dados consolidados, análise e evidências aos blocos de planejamento. Use quando o ROPRE Quarter chegar à retrospectiva ou quando um bloco ROPRE exigir retrospectiva aprovada.
area: account
author: Fabio José Aiello Junior
version: 2.0.0
---

# Adaptador Retrospectiva → ROPRE Quarter

Esta skill não refaz coleta nem análise. Ela chama `account-retrospectiva-performance-maestro` e traduz sua saída para o contrato legado do ROPRE.

## Entrada

- cliente, ano, quarter e período;
- diagnóstico de fontes do ROPRE, quando já aprovado;
- memória longitudinal e quarter anterior;
- `invocation_mode: ropre_adapter` para impedir recursão.

Se o diagnóstico do ROPRE já existir, entregue-o ao novo maestro como fonte previamente validada. O maestro ainda pode encontrar fontes adicionais; conflito material volta ao gate humano.

## Execução

1. Rode `account-retrospectiva-performance-maestro` para `inside_sales` ou `ecommerce`.
2. Aguarde a consolidação e o comando `retrospectiva aprovada`.
3. Gere `12-handoff-ropre.md` na mesma `run_id`.
4. Mapeie os arquivos aprovados para:

```text
ropre-quarter/retrospectiva/dados-consolidados.md
ropre-quarter/retrospectiva/analise-quarter.md
ropre-quarter/retrospectiva/evidencias.md
ropre-quarter/retrospectiva/assets/criativos/
```

## Mapeamento

- `dados-consolidados.md`: índice e síntese de mídia, funil, CRM/e-commerce, vendedores, atendimento, break-even e reconciliação, com links para a execução versionada.
- `analise-quarter.md`: conteúdo de `11-retrospectiva-final.md`, preservando `evidence_id`.
- `evidencias.md`: conteúdo ou índice de `09-evidencias.md`.
- assets: referencie os originais; não duplique quando a plataforma suportar links estáveis.

## Handoff para os blocos

Inclua em `12-handoff-ropre.md`:

- vencedores e perdedores por lente;
- projetado versus realizado;
- gaps comprovados e hipóteses;
- metas e limites do break-even;
- lacunas, conflitos e cobertura;
- calendário global, onboardings e funcionalidades disponíveis para o próximo ciclo, quando encontrados;
- índice de evidências.

O ROPRE transforma esses insumos em priorização, plano, responsáveis, prazos, projeção e backlog.

## Gate

Sem `retrospectiva aprovada`, nenhum bloco do ROPRE é liberado. Como a invocação veio do ROPRE, retorne ao maestro existente depois do handoff; não ofereça iniciar outro ROPRE.
