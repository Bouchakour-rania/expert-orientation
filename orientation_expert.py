import tkinter as tk
from tkinter import messagebox, ttk

# --- Système expert pour l'orientation professionnelle ---
class OrientationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Système Expert d'Orientation Professionnelle")
        self.root.geometry("700x550")
        self.root.configure(bg="#f2f6fc")

        self.questions = [
            ("Quel domaine t’intéresse le plus ?", [
                "Informatique", "Médecine", "Art", "Éducation", "Droit", "Ingénierie",
                "Business", "Marketing", "Design", "Psychologie", "Langues", "Finance",
                "Tourisme", "Agroalimentaire", "Sport", "Architecture"
            ]),
            ("Tu préfères travailler avec :", ["Des gens", "Des machines"]),
            ("Tu préfères un travail :", ["Créatif", "Analytique"]),
            ("Tu veux un métier :", ["Stable", "Flexible"]),
            ("Tu préfères :", ["Télétravail", "Présentiel"]),
            ("Tu veux :", ["Beaucoup de responsabilités", "Moins de responsabilités"]),
            ("Le plus important pour toi :", ["Un très bon salaire", "Équilibre vie pro/perso"]),
            ("Tu es plutôt :", ["Logique", "Artistique", "Pratique"])
        ]

        self.answers = []
        self.current_question = 0

        self.main_frame = tk.Frame(root, bg="#f2f6fc")
        self.main_frame.pack(fill="both", expand=True)

        self.create_intro()

    def create_intro(self):
        self.clear_frame()
        intro_label = tk.Label(
            self.main_frame,
            text="Bienvenue dans le système d'orientation professionnelle",
            font=("Helvetica", 16, "bold"),
            pady=30,
            bg="#f2f6fc"
        )
        intro_label.pack()

        start_btn = tk.Button(
            self.main_frame,
            text="Commencer",
            command=self.start_questions,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=10
        )
        start_btn.pack(pady=10)

    def start_questions(self):
        self.answers = []
        self.current_question = 0
        self.show_question()

    def show_question(self):
        self.clear_frame()
        question, options = self.questions[self.current_question]

        question_label = tk.Label(
            self.main_frame,
            text=question,
            font=("Arial", 14, "bold"),
            wraplength=600,
            pady=20,
            bg="#f2f6fc"
        )
        question_label.pack()

        option_frame = tk.Frame(self.main_frame, bg="#f2f6fc")
        option_frame.pack()

        canvas = tk.Canvas(option_frame, width=550, height=200, bg="#f2f6fc")
        scrollbar = ttk.Scrollbar(option_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f2f6fc")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for option in options:
            btn = tk.Button(
                scrollable_frame,
                text=option,
                width=40,
                bg="#3498db",
                fg="white",
                font=("Arial", 11),
                command=lambda o=option: self.record_answer(o)
            )
            btn.pack(pady=5)

        nav_frame = tk.Frame(self.main_frame, bg="#f2f6fc")
        nav_frame.pack(pady=15)

        if self.current_question > 0:
            back_btn = tk.Button(
                nav_frame,
                text="← Retour",
                command=self.previous_question,
                bg="#e67e22",
                fg="white",
                font=("Arial", 10)
            )
            back_btn.pack(side="left", padx=5)

    def record_answer(self, answer):
        if len(self.answers) > self.current_question:
            self.answers[self.current_question] = answer
        else:
            self.answers.append(answer)

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.show_question()

    def show_result(self):
        self.clear_frame()
        result = self.infer_job()

        tk.Label(
            self.main_frame,
            text="Métiers suggérés :",
            font=("Helvetica", 16, "bold"),
            pady=20,
            bg="#f2f6fc"
        ).pack()

        tk.Label(
            self.main_frame,
            text=result,
            font=("Arial", 13),
            wraplength=600,
            justify="center",
            bg="#f2f6fc"
        ).pack(pady=10)

        btn_frame = tk.Frame(self.main_frame, bg="#f2f6fc")
        btn_frame.pack(pady=20)

        tk.Button(
            btn_frame,
            text="Recommencer",
            command=self.create_intro,
            bg="#27ae60",
            fg="white",
            padx=15,
            font=("Arial", 11)
        ).pack(side="left", padx=10)

    def infer_job(self):
        domaine = self.answers[0]
        style = self.answers[2]
        logique = self.answers[7]

        if domaine == "Informatique" and style == "Analytique":
            return "Développeur Web, Analyste de données, Ingénieur IA"
        elif domaine == "Art" or logique == "Artistique":
            return "Designer graphique, Illustrateur, Web Designer"
        elif domaine == "Business" and style == "Analytique":
            return "Consultant en gestion, Chef de projet"
        elif domaine == "Marketing" and style == "Créatif":
            return "Spécialiste en marketing digital, Community Manager"
        elif domaine == "Médecine":
            return "Médecin, Infirmier, Radiologue"
        elif domaine == "Finance":
            return "Comptable, Analyste financier, Contrôleur de gestion"
        elif domaine == "Psychologie":
            return "Psychologue, Coach de vie, Conseiller scolaire"
        elif domaine == "Langues":
            return "Traducteur, Enseignant, Rédacteur Web"
        elif domaine == "Ingénierie":
            return "Ingénieur civil, Électromécanicien, Roboticien"
        elif domaine == "Tourisme":
            return "Agent de voyage, Guide touristique, Responsable hôtelier"
        elif domaine == "Architecture":
            return "Architecte, Dessinateur technique, Urbaniste"
        elif domaine == "Sport":
            return "Coach sportif, Kinésithérapeute, Entraîneur"
        elif domaine == "Agroalimentaire":
            return "Ingénieur agro, Technicien qualité, Responsable production"
        else:
            return "Enseignant, Assistant administratif, Entrepreneur"

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

# --- Lancer l'application ---
if __name__ == "__main__":
    root = tk.Tk()
    app = OrientationSystem(root)
    root.mainloop()


