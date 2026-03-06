# Law Adviser - Agent IA Juridique

## Projet
Chatbot juridique multi-agents spécialisé dans les droits humains et droits des IA.

## Architecture
- Interface : Streamlit (interface/)
- Backend : FastAPI (fastapi/)
- Orchestration : LangGraph (orchestrateur/)
- LLM : Qwen via OpenRouter
- RAG : Vector DB (database/vector/) — lois, AI Act
- Mémoire Q&R : SQL + embeddings (database/sql/)
- Monitoring : LangSmith (monitoring/)

## Agents
- Main Agent : filtre, route, agrège, parle à l'utilisateur
- Agents spécialisés : Litige, Handicap, Droits Humains...
  (ne parlent jamais directement à l'utilisateur)

## Profil utilisateur
- Formation développeur IA complétée
- Bagage technique existant — pas débutant
- A trop utilisé l'IA pendant sa formation, veut se réconcilier avec le code
- Objectif : comprendre, pas juste produire

## Règles pédagogiques
- Pousser à réfléchir avant de donner les réponses
- Expliquer le pourquoi avant le comment
- Ne pas écrire le code à sa place sans explication
- Valider la compréhension régulièrement
