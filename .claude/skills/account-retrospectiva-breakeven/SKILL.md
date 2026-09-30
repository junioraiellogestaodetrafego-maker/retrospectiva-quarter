---
name: account-retrospectiva-breakeven
description: Localiza, audita ou cria o break-even do cliente e transforma suas metas econômicas em referência para CPL, CPMQL, CPSQL, CPVenda, ROAS e rankings da retrospectiva. Use sempre que a retrospectiva precisar julgar eficiência econômica ou quando o cliente ainda não tiver break-even válido.
area: account
author: Fabio José Aiello Junior
version: 1.1.0
---

# Break-even da retrospectiva

Este módulo encapsula motores existentes; não replique a matemática.

## Ordem de descoberta

1. Procure break-even e projeção no repositório, GrowthPack e Drive.
2. Considere válido somente se refletir o último quarter fechado e fee, verba, MC1, ticket, modelo e funil atuais.
3. Se ausente ou desatualizado, ofereça ao Account criar.
4. Para criar, use `projecao-breakeven` do repositório `jeanreisv4/growth-enginner` quando disponível; use `breakeven-projetos` como motor local complementar.
5. Confirme fee, verba e MC1 com humano mesmo quando detectados.

## Extração obrigatória do forecast

Não leia apenas o resumo econômico da planilha. Inspecione o bloco completo do funil projetado, mês a mês, e preserve todas as premissas existentes:

- verba de mídia;
- CPM e impressões;
- CTR ou taxa impressões → cliques;
- cliques e CPC;
- taxa clique → lead;
- leads e CPL;
- taxa lead → MQL, MQLs e CPMQL;
- taxa MQL → SQL, SQLs e CPSQL;
- taxa SQL → venda, vendas e CPVenda;
- hit rate, faturamento, ticket e ROAS.

Registre o nome da aba, o mês/coluna e as células ou linhas de origem. Métrica projetada existente nunca pode virar sem meta por leitura incompleta do bloco.

Quando o realizado equivalente estiver ausente, mantenha o projetado preenchido e marque apenas o realizado como sem dado. Não apague a meta só porque não há contraparte observada.

Use `scripts/detect_engines.py` para registrar quais motores e dependências estão disponíveis antes de iniciar o cálculo.

## Saída

- `07-breakeven.md`

O Markdown registra fontes, aba/mês/células de origem, premissas, MC1, CAC permitido, break-even de transação, contrato e empresa, receita/vendas necessárias, funil inverso completo, metas de volumes, taxas e custos, cenários, mês no azul e mês em que o acumulado zera.

Use break-even de contrato como padrão do ROPRE. Transação e empresa são leituras complementares. Se o Account recusar a criação, registre gap crítico e não classifique custo como economicamente bom ou ruim sem outra meta validada.

Planilha é derivado opcional do motor; a interface canônica com a retrospectiva é Markdown.
