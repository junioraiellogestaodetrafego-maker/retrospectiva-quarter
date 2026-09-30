---
name: account-retrospectiva-consolidacao
description: Consolida todos os módulos em uma retrospectiva trimestral única, auditável e pronta para aprovação, preservando rankings, funis, gaps, limitações e evidências. Use no fim da retrospectiva antes do handoff opcional para ROPRE e Drive.
area: account
author: Fabio José Aiello Junior
version: 1.4.0
---

# Consolidação da retrospectiva

Leia todos os Markdown da mesma `run_id`, `references/profundidade-entrega.md` e `references/janelas-temporais.md` do maestro. Valide a estrutura durante a execução e rode `account-retrospectiva-performance-maestro/scripts/validate_retrospectiva.py <run_dir> --approval-ready` antes de declarar o pacote pronto para aprovação.

## Saída

- `11-retrospectiva-final.md`

## Ordem narrativa

1. Escopo, quarter e cobertura.
2. Janelas temporais: pré-operacional, go-live, `analysis_start`, performance e snapshots.
3. Resumo executivo.
4. Projetado versus realizado em janela compatível.
5. Visão geral e canais competindo.
6. Mídia macro até micro.
   - matriz de cobertura;
   - canais e destinos;
   - tabela-mãe de campanhas;
   - tabela-mãe de conjuntos;
   - tabela-mãe de anúncios e criativos;
   - públicos, keywords e breakdowns;
7. Criativos.
8. Funil de inside sales ou e-commerce.
9. Vendedores e atendimento, quando aplicável.
   - execução operacional;
   - competência comercial, versão e status da rubrica;
   - resultado de funil, em bloco separado;
10. Break-even e eficiência econômica.
11. Achados e gaps.
12. Limitações, conflitos, testes e não atribuídos.
13. Índice de evidências.

## Política de consolidação

Consolide por integração, não por redução. O resumo executivo abre a leitura, mas o mesmo pacote preserva:

- análise detalhada de todos os módulos;
- tabelas-mãe e rankings integrais;
- todas as entidades, inclusive intermediárias, perdedoras e de zero resultado;
- bases linha a linha;
- conflitos, hipóteses, limitações e evidências.

Não gere um “resumo dos resumos”. Não use top N como substituto. Se houver muitas linhas, divida a base em partes e crie índice. O `11-retrospectiva-final.md` deve conter `## Janelas temporais da retrospectiva`, `## Análise detalhada` e `## Índice de insumos completos`, com links para todos os módulos, bases e assets aplicáveis e contagem de entidades por base.

Se o gate `--approval-ready` falhar, apresente a versão como `PRELIMINAR — DADOS INCOMPLETOS`, liste as falhas e não peça aprovação. Incorpore complementos como `[complemento humano]`, rode novamente o gate e somente então espere o comando exato `retrospectiva aprovada`. Sem aprovação, não gere handoff externo nem inicie o ROPRE.
