---
name: account-retrospectiva-atendimento
description: Audita retrospectivamente todas as conversas comerciais, classificando atendimento, SLA útil, conexão, abandono, resposta pendente, follow-up, cadência e qualidade comercial calibrada com evidência por lead. Use quando o cliente tiver Chatwoot, Blip, Digitalize, WhatsApp, Kommo ou outra ferramenta conversacional conectada.
area: account
author: Fabio José Aiello Junior
version: 1.1.0
---

# Retrospectiva de atendimento

Leia no maestro `references/atendimento.md`, `references/qualidade-comercial.md`, `references/fontes-e-reconciliacao.md` e `references/contrato-markdown.md`. Quando disponível, reutilize a máquina de estados de `monitor-leads-atendimento`.

## Descoberta

1. Identifique a ferramenta no contexto existente.
2. Se não estiver registrada, pergunte qual é e solicite conexão/API de forma segura; não peça segredo em texto aberto quando houver conector.
3. Valide conta, inbox/canal e cobertura.
4. Localize a rubrica comercial aprovada do cliente. Se não existir, crie um rascunho a partir de `assets/rubrica-comercial-cliente.md` do maestro e execute a análise operacional; mantenha a competência comercial como `provisional` até calibrar.

## Saídas

- `06-atendimento.md`
- `bases/conversas.md`

## Base obrigatória

Uma linha por conversa ou atendimento, com lead, contato, negócio, vendedor, campanha, MQL, timestamps, tempos corrido e útil, estado, cadência, link da conversa/card e `evidence_id`.

Separe formalmente:

- execução operacional, com score e cobertura;
- competência comercial por dimensão, score somente quando calibrado, cobertura e `rubric_version`;
- resultado do funil, sem incorporá-lo às notas anteriores;
- severidade P0–P4, confiança e status de revisão humana.

Nunca gere uma nota total que misture essas três camadas. Sem conversa, sem humano ou sem transcrição suficiente, use o estado de avaliabilidade correspondente em vez de inventar julgamento.

Separe IA, bot, sistema, lead e humano. Mensagem automática não conta como atendimento humano. Áudio, vídeo e anexo contam como resposta operacional; conteúdo só pode ser julgado quando transcrito. Sem match seguro é `not_located`, nunca `não atendido`.

Reconcilie tarefa versus ação e etapa do CRM versus evidência da conversa. Exija evidência explícita para fechamento e demais eventos críticos. Registre divergências; não altere card, etapa ou tarefa.

Use `scripts/business_time.py` para calcular SLA quando os timestamps e o calendário operacional estiverem disponíveis.

O escopo é relatório. Não envie alerta, não crie tarefa e não escreva no CRM.
