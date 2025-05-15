import streamlit as st
import json
from pathlib import Path

# Путь к prompt-шаблону
PROMPT_PATH = Path("prompts/event_template.txt")
SCENARIOS_PATH = Path("scenarios")

# Заглушка: загрузка локального сценария (на замену LLM)
def mock_ai_response(event_text: str) -> str:
    for scenario_file in SCENARIOS_PATH.glob("*.json"):
        with open(scenario_file, "r", encoding="utf-8") as f:
            scenario = json.load(f)
            if scenario["event"] in event_text:
                return f"""📌 Прогноз: всплеск спроса по сценарию '{scenario['type']}' в регионе {scenario['region']}

✅ Действия:
- Проверьте кампанию: {scenario['campaign']}
- Подготовьте логистику
- Увеличьте доступность в витрине
- Отправьте уведомление

👥 Роли:
- Маркетинг
- Логистика
- Операции

🧠 Почему:
Событие повышает вероятность заказа на 25–40%. Быстрая реакция — это снижение потерь и рост удовлетворенности.
"""
    return "Нет подходящего сценария — AI пока не обучен на этом кейсе."

# Streamlit UI
st.set_page_config(page_title="AI-коммуникатор спроса", layout="centered")
st.title("🤖 AI-коммуникатор спроса")

event_text = st.text_area("Введите событие", placeholder="Пример: 14 февраля в Москве снег + акция на цветы")

if st.button("Проанализировать"):
    if not event_text.strip():
        st.warning("Пожалуйста, введите описание события.")
    else:
        st.markdown("⏳ Анализируем...")
        result = mock_ai_response(event_text)
        st.markdown(result)
