---
name: account-retrospectiva-contexto-fontes
description: Descobre contexto, período, modelo de negócio, definições de funil, equipe e fontes antes de uma retrospectiva trimestral. Use no início de toda retrospectiva de performance, especialmente quando o cliente não tem repositório completo ou o Account ainda precisa ser sabatinado.
area: account
author: Fabio José Aiello Junior
version: 1.3.0
---

# Contexto e fontes

Leia `../account-retrospectiva-performance-maestro/references/contrato-markdown.md`, `fontes-e-reconciliacao.md` e `janelas-temporais.md`.

## Saídas

- `00-manifesto-fontes.md`
- `01-contexto-cliente.md`

## Workflow

1. Varra o repositório profissional do cliente antes de perguntar.
2. Consulte Flow, Cockpit, NEKT, GrowthPack e Drive autorizados.
3. Descubra conexões n8n para CRM, GA4, e-commerce e conversas.
4. Descubra quarter, pré-operacional, ativação técnica, primeiro evento real, relançamentos e `analysis_start`.
5. Identifique smoke tests, leads internos e reprocessamentos; preserve uma regra auditável de exclusão.
6. Registre fonte, status, cobertura temporal, última atualização, proprietário e uso pretendido.
7. Detecte conflitos e fontes congeladas.
8. Faça sabatina adaptativa apenas para completar ou validar lacunas.
9. Para cada canal, descubra antecipadamente se a fonte entrega campanha, conjunto/ad group, anúncio, criativo, público/keyword, região, gênero, idade, dispositivo, posicionamento, destino, IDs, previews, assets e métricas de vídeo.
10. Registre no manifesto quem fornecerá cada dimensão ausente: conector, API, export ou input manual.

## Contexto mínimo

- cliente, projeto, período e comparação desejada;
- quarter calendário, go-live técnico, primeiro evento real, `analysis_start`, fuso e IDs de teste;
- `inside_sales` ou `ecommerce`;
- oferta, público, região e objetivo comercial;
- canais e destinos ativos;
- CRM ou plataforma de e-commerce;
- ferramenta conversacional;
- quantidade e papéis dos vendedores;
- definições de MQL, SQL, oportunidade, orçamento e venda;
- playbook comercial, perguntas obrigatórias, objeções, promessas proibidas, próximo passo e rubrica aprovada;
- horário comercial, fuso, finais de semana e feriados aplicáveis;
- fee, verba, margem, ticket, metas e break-even existentes;
- projeção anterior e calendário do próximo ciclo disponíveis.

Para o próximo ciclo, procure por padrões como `calendario-mestre-sazonalidades`, `matriz-sazonal-clientes`, `onboarding` e `roadmap`. Apenas registre as fontes e datas candidatas; a seleção e o backlog pertencem ao ROPRE.

## Gate

Peça validação humana do manifesto. Fonte nova encontrada depois volta a este módulo. Dimensão de mídia ausente aciona solicitação de fonte/input e impede status `complete`; conflito material exige decisão.
