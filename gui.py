from typing import List, Optional
import customtkinter as ctk
from knowledge_base import QUESTIONS, GAMES, GAME_METADATA
from expert_engine import calculate_results, get_explanation, get_alternative
COLOR_BG = "#12111A"                                 
COLOR_CARD = "#1C182A"                           
COLOR_CARD_BORDER = "#2D2545"                 
COLOR_PURPLE = "#8B5CF6"                                    
COLOR_PURPLE_HOVER = "#7C3AED"                            
COLOR_PURPLE_LIGHT = "#DDD6FE"                                 
COLOR_PURPLE_BG = "#2B2146"                             
COLOR_BAR_BG = "#262038"                             
COLOR_BTN_SECONDARY = "#231F35"                              
COLOR_BTN_HOVER = "#2E2847"                             
COLOR_TEXT_MAIN = "#F8FAFC"                           
COLOR_TEXT_MUTED = "#94A3B8"                             
COLOR_ACCENT_ALT = "#A78BFA"                                     
class GameExpertApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("Експертна система — Підбір комп'ютерної гри")
        self.geometry("960x740")
        self.minsize(860, 680)
        self.configure(fg_color=COLOR_BG)
        self.current_question_idx: int = 0
        self.selected_answers: List[str] = []
        self.selected_labels: List[str] = []
        self.selected_categories: List[str] = []
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True, padx=25, pady=25)
        self.show_welcome_screen()
    def _clear_container(self) -> None:
        for widget in self.container.winfo_children():
            widget.destroy()
    def show_welcome_screen(self) -> None:
        self._clear_container()
        center_frame = ctk.CTkFrame(
            self.container,
            fg_color=COLOR_CARD,
            corner_radius=20,
            border_width=1,
            border_color=COLOR_CARD_BORDER
        )
        center_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.88, relheight=0.86)
        content = ctk.CTkFrame(center_frame, fg_color="transparent")
        content.place(relx=0.5, rely=0.5, anchor="center")
        badge = ctk.CTkLabel(
            content,
            text="ЕКСПЕРТНА СИСТЕМА • AI CONSULTANT",
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            text_color=COLOR_PURPLE,
            fg_color=COLOR_PURPLE_BG,
            corner_radius=8,
            height=28
        )
        badge.pack(pady=(0, 20))
        title = ctk.CTkLabel(
            content,
            text="ВИБІР КОМП'ЮТЕРНОЇ ГРИ",
            font=ctk.CTkFont(family="Arial", size=36, weight="bold"),
            text_color=COLOR_TEXT_MAIN
        )
        title.pack(pady=(0, 10))
        subtitle = ctk.CTkLabel(
            content,
            text="Інтелектуальна консультаційна система підбору ідеальної відеогри",
            font=ctk.CTkFont(family="Arial", size=17),
            text_color=COLOR_PURPLE_LIGHT
        )
        subtitle.pack(pady=(0, 25))
        desc_text = (
            "Дайте відповіді на 7 запитань щодо ваших уподобань:\n"
            "жанр, ігровий режим, рівень складності, тривалість сесій,\n"
            "пріоритети, характеристики комп'ютера та атмосферу.\n\n"
            "Система проаналізує вашу відповідь через вагову базу знань\n"
            "і сформує персональну рекомендацію з детальним поясненням висновку."
        )
        desc = ctk.CTkLabel(
            content,
            text=desc_text,
            font=ctk.CTkFont(family="Arial", size=14),
            text_color=COLOR_TEXT_MUTED
        )
        desc.pack(pady=(0, 35))
        start_btn = ctk.CTkButton(
            content,
            text="Розпочати підбір",
            font=ctk.CTkFont(family="Arial", size=17, weight="bold"),
            fg_color=COLOR_PURPLE,
            hover_color=COLOR_PURPLE_HOVER,
            text_color="#FFFFFF",
            width=260,
            height=52,
            corner_radius=14,
            command=self.start_consultation
        )
        start_btn.pack()
    def start_consultation(self) -> None:
        self.current_question_idx = 0
        self.selected_answers = []
        self.selected_labels = []
        self.selected_categories = []
        self.show_question()
    def show_question(self) -> None:
        self._clear_container()
        total_questions = len(QUESTIONS)
        q_data = QUESTIONS[self.current_question_idx]
        top_bar = ctk.CTkFrame(self.container, fg_color="transparent")
        top_bar.pack(fill="x", pady=(10, 20))
        step_label = ctk.CTkLabel(
            top_bar,
            text=f"Питання {self.current_question_idx + 1} із {total_questions}",
            font=ctk.CTkFont(family="Arial", size=15, weight="bold"),
            text_color=COLOR_PURPLE_LIGHT
        )
        step_label.pack(anchor="w")
        progress_val = (self.current_question_idx + 1) / total_questions
        progress = ctk.CTkProgressBar(
            top_bar,
            height=8,
            corner_radius=4,
            fg_color=COLOR_BAR_BG,
            progress_color=COLOR_PURPLE
        )
        progress.pack(fill="x", pady=(6, 0))
        progress.set(progress_val)
        q_card = ctk.CTkFrame(
            self.container,
            fg_color=COLOR_CARD,
            corner_radius=18,
            border_width=1,
            border_color=COLOR_CARD_BORDER
        )
        q_card.pack(fill="both", expand=True, padx=5, pady=5)
        cat_badge = ctk.CTkLabel(
            q_card,
            text=q_data["category"].upper(),
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            text_color=COLOR_PURPLE,
            fg_color=COLOR_PURPLE_BG,
            corner_radius=6,
            height=24
        )
        cat_badge.pack(pady=(28, 10))
        q_title = ctk.CTkLabel(
            q_card,
            text=q_data["question"],
            font=ctk.CTkFont(family="Arial", size=22, weight="bold"),
            text_color=COLOR_TEXT_MAIN,
            wraplength=780
        )
        q_title.pack(pady=(0, 25), padx=20)
        answers_box = ctk.CTkFrame(q_card, fg_color="transparent")
        answers_box.pack(fill="x", padx=40, pady=(0, 20))
        for answer_text, answer_id in q_data["answers"]:
            btn = ctk.CTkButton(
                answers_box,
                text=answer_text,
                font=ctk.CTkFont(family="Arial", size=15),
                fg_color=COLOR_BTN_SECONDARY,
                hover_color=COLOR_PURPLE_HOVER,
                border_width=1,
                border_color=COLOR_CARD_BORDER,
                text_color=COLOR_TEXT_MAIN,
                height=52,
                corner_radius=12,
                command=lambda val=answer_id, txt=answer_text, cat=q_data["category"]: self.handle_answer(val, txt, cat)
            )
            btn.pack(fill="x", pady=6)
        if self.current_question_idx > 0:
            back_btn = ctk.CTkButton(
                q_card,
                text="← Попереднє питання",
                font=ctk.CTkFont(family="Arial", size=13),
                fg_color="transparent",
                hover_color=COLOR_PURPLE_BG,
                text_color=COLOR_TEXT_MUTED,
                width=160,
                height=32,
                command=self.go_back
            )
            back_btn.pack(pady=(5, 15))
    def handle_answer(self, answer_id: str, answer_text: str, category: str) -> None:
        self.selected_answers.append(answer_id)
        self.selected_labels.append(answer_text)
        self.selected_categories.append(category)
        if self.current_question_idx + 1 < len(QUESTIONS):
            self.current_question_idx += 1
            self.show_question()
        else:
            self.show_results()
    def go_back(self) -> None:
        if self.current_question_idx > 0:
            self.current_question_idx -= 1
            self.selected_answers.pop()
            self.selected_labels.pop()
            self.selected_categories.pop()
            self.show_question()
    def show_results(self) -> None:
        self._clear_container()
        ranking = calculate_results(self.selected_answers)
        best = ranking[0]
        alt = get_alternative(ranking)
        explanation = get_explanation(
            self.selected_answers,
            self.selected_labels,
            self.selected_categories,
            best["game"]
        )
        scroll = ctk.CTkScrollableFrame(
            self.container,
            fg_color="transparent",
            scrollbar_button_color=COLOR_PURPLE,
            scrollbar_button_hover_color=COLOR_PURPLE_HOVER
        )
        scroll.pack(fill="both", expand=True)
        header = ctk.CTkLabel(
            scroll,
            text="РЕЗУЛЬТАТ ЕКСПЕРТНОЇ СИСТЕМИ",
            font=ctk.CTkFont(family="Arial", size=26, weight="bold"),
            text_color=COLOR_TEXT_MAIN
        )
        header.pack(pady=(10, 5))
        sub = ctk.CTkLabel(
            scroll,
            text="Оптимальний вибір на основі зіставлення ваших відповідей з базою знань",
            font=ctk.CTkFont(family="Arial", size=14),
            text_color=COLOR_PURPLE_LIGHT
        )
        sub.pack(pady=(0, 18))
        rec_card = ctk.CTkFrame(
            scroll,
            fg_color=COLOR_CARD,
            corner_radius=18,
            border_width=2,
            border_color=COLOR_PURPLE
        )
        rec_card.pack(fill="x", padx=10, pady=(0, 15))
        rec_header_frame = ctk.CTkFrame(rec_card, fg_color="transparent")
        rec_header_frame.pack(fill="x", padx=25, pady=(20, 10))
        rec_tag = ctk.CTkLabel(
            rec_header_frame,
            text=f"ТОП РЕКОМЕНДАЦІЯ • {best['tag'].upper()}",
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            text_color=COLOR_PURPLE,
            fg_color=COLOR_PURPLE_BG,
            corner_radius=6,
            height=24
        )
        rec_tag.pack(anchor="w")
        game_title = ctk.CTkLabel(
            rec_card,
            text=best["game"],
            font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
            text_color=COLOR_TEXT_MAIN
        )
        game_title.pack(anchor="w", padx=25, pady=(5, 2))
        game_meta = ctk.CTkLabel(
            rec_card,
            text=f"Жанр: {best['genre']}   |   Розробник: {best['developer']}",
            font=ctk.CTkFont(family="Arial", size=14),
            text_color=COLOR_TEXT_MUTED
        )
        game_meta.pack(anchor="w", padx=25, pady=(0, 15))
        match_frame = ctk.CTkFrame(rec_card, fg_color="transparent")
        match_frame.pack(fill="x", padx=25, pady=(0, 10))
        match_lbl = ctk.CTkLabel(
            match_frame,
            text=f"Відповідність: {best['percentage']}%",
            font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
            text_color=COLOR_PURPLE
        )
        match_lbl.pack(side="left")
        score_lbl = ctk.CTkLabel(
            match_frame,
            text=f"Експертна оцінка: {best['score']} із {best['max_score']} балів",
            font=ctk.CTkFont(family="Arial", size=14),
            text_color=COLOR_TEXT_MUTED
        )
        score_lbl.pack(side="right")
        prog = ctk.CTkProgressBar(
            rec_card,
            height=12,
            corner_radius=6,
            fg_color=COLOR_BAR_BG,
            progress_color=COLOR_PURPLE
        )
        prog.pack(fill="x", padx=25, pady=(0, 15))
        prog.set(best["percentage"] / 100.0)
        desc_lbl = ctk.CTkLabel(
            rec_card,
            text=best["description"],
            font=ctk.CTkFont(family="Arial", size=14),
            text_color=COLOR_PURPLE_LIGHT,
            wraplength=800
        )
        desc_lbl.pack(anchor="w", padx=25, pady=(0, 20))
        exp_card = ctk.CTkFrame(
            scroll,
            fg_color=COLOR_CARD,
            corner_radius=18,
            border_width=1,
            border_color=COLOR_CARD_BORDER
        )
        exp_card.pack(fill="x", padx=10, pady=(0, 15))
        exp_title = ctk.CTkLabel(
            exp_card,
            text="Чому система рекомендує цей варіант? (Підсистема пояснень)",
            font=ctk.CTkFont(family="Arial", size=17, weight="bold"),
            text_color=COLOR_TEXT_MAIN
        )
        exp_title.pack(anchor="w", padx=25, pady=(18, 12))
        for item in explanation:
            row = ctk.CTkFrame(exp_card, fg_color="transparent")
            row.pack(fill="x", padx=25, pady=4)
            cat_lbl = ctk.CTkLabel(
                row,
                text=f"{item['category']}:",
                font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
                text_color=COLOR_PURPLE_LIGHT,
                width=230,
                anchor="w"
            )
            cat_lbl.pack(side="left")
            crit_lbl = ctk.CTkLabel(
                row,
                text=item["criterion"],
                font=ctk.CTkFont(family="Arial", size=13),
                text_color=COLOR_TEXT_MAIN,
                anchor="w"
            )
            crit_lbl.pack(side="left", padx=5)
            score_badge = ctk.CTkLabel(
                row,
                text=f"{item['weight']}/{item['max_weight']}",
                font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
                text_color=COLOR_PURPLE if item['weight'] >= 4 else COLOR_TEXT_MUTED,
                fg_color=COLOR_PURPLE_BG if item['weight'] >= 4 else COLOR_BTN_SECONDARY,
                corner_radius=6,
                width=45,
                height=22
            )
            score_badge.pack(side="right")
        ctk.CTkFrame(exp_card, fg_color="transparent", height=10).pack()
        if alt:
            alt_card = ctk.CTkFrame(
                scroll,
                fg_color=COLOR_CARD,
                corner_radius=18,
                border_width=1,
                border_color=COLOR_CARD_BORDER
            )
            alt_card.pack(fill="x", padx=10, pady=(0, 15))
            alt_frame = ctk.CTkFrame(alt_card, fg_color="transparent")
            alt_frame.pack(fill="x", padx=25, pady=16)
            alt_left = ctk.CTkFrame(alt_frame, fg_color="transparent")
            alt_left.pack(side="left")
            alt_tag = ctk.CTkLabel(
                alt_left,
                text="АЛЬТЕРНАТИВНИЙ ВАРІАНТ",
                font=ctk.CTkFont(family="Arial", size=11, weight="bold"),
                text_color=COLOR_ACCENT_ALT
            )
            alt_tag.pack(anchor="w")
            alt_name = ctk.CTkLabel(
                alt_left,
                text=f"{alt['game']} — {alt['percentage']}%",
                font=ctk.CTkFont(family="Arial", size=19, weight="bold"),
                text_color=COLOR_TEXT_MAIN
            )
            alt_name.pack(anchor="w")
            alt_genre = ctk.CTkLabel(
                alt_left,
                text=f"{alt['genre']} ({alt['developer']})",
                font=ctk.CTkFont(family="Arial", size=13),
                text_color=COLOR_TEXT_MUTED
            )
            alt_genre.pack(anchor="w")
        rating_card = ctk.CTkFrame(
            scroll,
            fg_color=COLOR_CARD,
            corner_radius=18,
            border_width=1,
            border_color=COLOR_CARD_BORDER
        )
        rating_card.pack(fill="x", padx=10, pady=(0, 20))
        rating_title = ctk.CTkLabel(
            rating_card,
            text="Рейтинг усіх варіантів за базою знань",
            font=ctk.CTkFont(family="Arial", size=17, weight="bold"),
            text_color=COLOR_TEXT_MAIN
        )
        rating_title.pack(anchor="w", padx=25, pady=(18, 12))
        for idx, item in enumerate(ranking, start=1):
            row = ctk.CTkFrame(rating_card, fg_color="transparent")
            row.pack(fill="x", padx=25, pady=6)
            rank_num = ctk.CTkLabel(
                row,
                text=f"{idx}.",
                font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
                text_color=COLOR_PURPLE,
                width=25
            )
            rank_num.pack(side="left")
            name_lbl = ctk.CTkLabel(
                row,
                text=item["game"],
                font=ctk.CTkFont(family="Arial", size=14),
                text_color=COLOR_TEXT_MAIN,
                width=240,
                anchor="w"
            )
            name_lbl.pack(side="left")
            bar_wrap = ctk.CTkFrame(row, fg_color="transparent")
            bar_wrap.pack(side="left", fill="x", expand=True, padx=15)
            p_bar = ctk.CTkProgressBar(
                bar_wrap,
                height=8,
                corner_radius=4,
                fg_color=COLOR_BAR_BG,
                progress_color=COLOR_PURPLE
            )
            p_bar.pack(fill="x")
            p_bar.set(item["percentage"] / 100.0)
            pct_lbl = ctk.CTkLabel(
                row,
                text=f"{item['percentage']}%",
                font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
                text_color=COLOR_PURPLE_LIGHT,
                width=50,
                anchor="e"
            )
            pct_lbl.pack(side="right")
        ctk.CTkFrame(rating_card, fg_color="transparent", height=10).pack()
        restart_btn = ctk.CTkButton(
            scroll,
            text="Пройти ще раз",
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            fg_color=COLOR_PURPLE,
            hover_color=COLOR_PURPLE_HOVER,
            text_color="#FFFFFF",
            width=240,
            height=48,
            corner_radius=12,
            command=self.start_consultation
        )
        restart_btn.pack(pady=(5, 25))
def run_app() -> None:
    app = GameExpertApp()
    app.mainloop()
if __name__ == "__main__":
    run_app()
