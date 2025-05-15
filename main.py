import streamlit as st
from datetime import datetime

st.title("Тест по предметам для выбора профессии")
user_name = st.text_input("Введите ваше имя:")

if user_name:
    questions = {

        "Химия": {
            "Вопрос": "Какая формула воды?",
            "Варианты": [
                "H2O",
                "CO2",
                "NaCl",
                "O2"
            ],
            "Правильный": 0
        },
        "Физика": {
            "Вопрос": "Что измеряется в Ньютонах?",
            "Варианты": [
                "Сила",
                "Энергия",
                "Масса",
                "Температура"
            ],
            "Правильный": 0
        },
        "Математика": {
            "Вопрос": "Чему равен интеграл от 0 до 1 функции f(x) = 1?",
            "Варианты": [
                "0",
                "1",
                "2",
                "Не существует"
            ],
            "Правильный": 1
        },
        "Информатика": {
            "Вопрос": "Что такое алгоритм?",
            "Варианты": [
                "Последовательность действий для решения задачи",
                "Вирус",
                "Компьютер",
                "Тип данных"
            ],
            "Правильный": 0
        },
    }
    answers = {}

    for subject, data in questions.items():
        st.write(f"**{subject}:** {data['Вопрос']}")

        options = ["-- выберите вариант --"] + data["Варианты"]
        answer = st.selectbox("", options, key=subject)
        answers[subject] = answer

    if st.button("Посмотреть результат и рекомендации"):

        if any(ans == "-- выберите вариант --" for ans in answers.values()):
            st.warning("Пожалуйста, ответьте на все вопросы перед получением результата.")
        else:
            score = 0
            for subject, data in questions.items():
                if answers[subject] == data["Варианты"][data["Правильный"]]:
                    score += 1

            st.write(f"{user_name} правильно ответил на {score} из {len(questions)} вопросов.")

            profession_map = {
                "Биология": ["Врач", "Биолог", "Биоинформатик"],
                "Химия": ["Химик", "Фармацевт", "Эколог"],
                "Физика": ["Инженер", "Физик-исследователь", "Энергетик"],
                "Математика": ["Аналитик", "Программист", "Экономист"],
                "Информатика": ["Программист", "Системный администратор", "Разработчик ПО"],
                "История": ["Историк", "Архивист", "Политолог"]
            }

            correct_subjects = [subj for subj, data in questions.items()
                                if answers[subj] == data["Варианты"][data["Правильный"]]]

            if not correct_subjects:
                st.write("Рекомендуем углубить знания по предметам, чтобы лучше понять возможные профессии.")
            else:
                st.write("Рекомендуемые профессии на основе ваших знаний:")
                for subj in correct_subjects:
                    st.write(f"{subj}: {', '.join(profession_map[subj])}")

            with open("results.txt", "a", encoding="utf-8") as f:
                result_text = f"Имя: {user_name}\nДата: {datetime.now()}\n"
                for subj in questions.keys():
                    result_text += f"{subj}: Выбран ответ — {answers[subj]}\n"
                result_text += f"Правильных ответов: {score} из {len(questions)}\n"
                result_text += "-" * 40 + "\n"
                f.write(result_text)

            st.download_button(
                label="Скачать результат теста",
                data=result_text,
                file_name="result_test.txt",
                mime="text/plain"
            )


else:
    st.info("Пожалуйста, введите имя, чтобы начать тест.")

