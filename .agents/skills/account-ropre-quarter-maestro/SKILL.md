---
name: account-ropre-quarter-maestro
description: Orquestra a geracao de ROPRE Quarter em Markdown para clientes V4, consumindo uma retrospectiva de performance aprovada para criar gargalos, plano 5W1H, projecao, objetivos, premissas, entregas, backlog, memoria e guardrails. Use sempre que o usuario pedir ROPRE Quarter, planejamento trimestral, teste do fluxo de ROPRE ou criacao de output final de quarter para cliente.
area: account
author: Fabio José Aiello Junior
version: 1.2.0
---

# Account ROPRE Quarter Maestro

Orquestre a esteira canonica de ROPRE Quarter. A V1 gera Markdown auditavel, nao HTML/PPT. A camada visual vem depois da validacao do conteudo.

Antes de executar, leia `ropre-do-quarter/arquitetura-skills-fluxos.md` se existir no workspace. Esse arquivo e a fonte de verdade da arquitetura.

## Objetivo

Gerar uma execucao completa de ROPRE Quarter dentro da pasta do cliente:

```text
Clientes V4/[TICKER] nome-cliente/checkins/quarter/{ano}/Q{n}/ropre-quarter/
```

Arquivos esperados:

```text
ropre-quarter-final.md
preview-consolidacao.md
memoria-proximo-quarter.md
ropre-quarter-visual-input.md
observacoes-confiabilidade.md
decisoes-humanas.md
guardrails.md
retrospectiva/dados-consolidados.md
retrospectiva/analise-quarter.md
retrospectiva/assets/criativos/
blocos/resultados.md
blocos/gargalos.md
blocos/plano-acao.md
blocos/projecao-proximo-quarter.md
blocos/objetivos.md
blocos/premissas-riscos.md
blocos/entregas.md
blocos/backlog-proximos-passos.md
```

## Fluxo obrigatório

1. Localize o cliente pelo Flow ou pela pasta `Clientes V4/[TICKER] nome-cliente`.
2. Identifique ano, quarter analisado e quarter anterior.
3. Identifique e valide com o humano o tipo de projeto:
   - `inside sales`
   - `e-commerce`
4. Crie a pasta do quarter se nao existir.
5. Leia `memoria-quarter-cliente.md` e a memoria do quarter anterior quando existirem.
6. Rode diagnostico de fontes e valide com humano.
7. Rode o adaptador `account-ropre-quarter-retrospectiva`, que chama `account-retrospectiva-performance-maestro` com `invocation_mode: ropre_adapter`. Consuma rankings, funis, atendimento, e-commerce, break-even, assets e evidencias da execucao versionada. Pause para o humano complementar e espere o comando explicito `retrospectiva aprovada` antes de qualquer bloco.
8. Gere os blocos nesta ordem narrativa, usando `retrospectiva/dados-consolidados.md` como fonte primaria (re-colete apenas o que faltar):
   - resultados
   - gargalos
   - plano de acao
   - projecao do proximo quarter
   - objetivos
   - premissas-riscos
   - entregas
   - backlog-proximos-passos
9. Gere `preview-consolidacao.md`.
10. Pare e espere aprovacao explicita: `aprovado, consolidar`.
11. So depois gere `ropre-quarter-final.md`, `memoria-proximo-quarter.md` e atualize a memoria longitudinal.
12. Se o usuario pedir camada visual, gere `ropre-quarter-visual-input.md` e chame `account-checkin-ropre-v2` para compilar HTML standalone.

## Skills/blocos liderados

Use estes blocos quando disponiveis:

- `account-ropre-quarter-diagnostico-fontes`
- `account-ropre-quarter-retrospectiva`
- `account-retrospectiva-performance-maestro`
- `account-ropre-quarter-resultados`
- `account-ropre-quarter-gargalos`
- `account-ropre-quarter-plano-acao`
- `account-ropre-quarter-projecao`
- `account-ropre-quarter-objetivos`
- `account-ropre-quarter-premissas-riscos`
- `account-ropre-quarter-entregas`
- `account-ropre-quarter-backlog-proximos-passos`
- `account-ropre-quarter-preview`
- `account-ropre-quarter-consolidacao`
- `account-ropre-quarter-memoria`
- `account-ropre-quarter-visual-handoff`
- `account-ropre-quarter-atualizar-memoria-pos-checkin`
- `account-ropre-quarter-encerramento`

Se algum bloco nao estiver disponivel, execute inline seguindo o mesmo contrato.

## Ordem narrativa final

```text
1. Abertura
2. Retrospectiva do quarter
3. Resultados
4. Projetado vs realizado
5. Funil por canal
6. Gaps e gargalos
7. Plano de acao em 5W1H
8. Projecao do proximo quarter
9. Objetivos do proximo quarter
10. Premissas e riscos
11. Entregas do quarter
12. Backlog e proximos passos
13. Memoria
14. Handoff visual, quando solicitado
```

## Pausas obrigatórias

Pause e pergunte ao humano quando:

- A analise previa da retrospectiva estiver pronta (pausa de co-construcao: humano complementa e aprova com `retrospectiva aprovada`).
- Tipo de projeto nao estiver definido/validado.
- Nao houver projetado vs realizado overall.
- Houver meta financeira sem fonte de venda/faturamento.
- Houver conflito entre fontes estruturadas.
- Houver canal pago ativo sem dado suficiente para funil.
- Houver objetivo SMART ou OKR sem fonte.
- Houver objetivo SMART ou OKR sem projecao validada ou autorizacao humana para seguir sem ela.
- Ekyte/timesheet nao tiver dados confiaveis para entregas.
- A restricao principal ou causa provavel estiver incerta.
- Qualquer lacuna critica alterar a conclusao.

Registre pausas em `guardrails.md`, `observacoes-confiabilidade.md` e `decisoes-humanas.md`.

## Aprovações humanas obrigatórias

- Fontes encontradas.
- Canais ativos.
- Tipo de projeto.
- Retrospectiva complementada, com comando explicito `retrospectiva aprovada`.
- Uso de Apify para assets de criativos (gasto de credito).
- Restricao principal.
- Plano 5W1H.
- Score/prioridade.
- Seguir sem dado.
- Preview final.
- Consolidacao final.

Sem `aprovado, consolidar`, nao gere o arquivo final.

Sem `ropre-quarter-final.md` aprovado, nao gere HTML visual. A camada visual sempre compila o Markdown aprovado; ela nao substitui a validacao de conteudo.

## Regra de não invenção

Dado ausente vira lacuna. Dado declarado pelo cliente fica marcado como `dado declarado pelo cliente`. Inferencia vira `hipotese`. Fonte conflitante exige decisao humana.
