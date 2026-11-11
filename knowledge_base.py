from typing import List, Dict, Tuple, Any
GAMES: List[str] = [
    "The Witcher 3: Wild Hunt",
    "Cyberpunk 2077",
    "Elden Ring",
    "Baldur's Gate 3",
    "Counter-Strike 2",
    "Dota 2",
    "Hades",
    "Hollow Knight"
]
GAME_METADATA: Dict[str, Dict[str, str]] = {
    "The Witcher 3: Wild Hunt": {
        "genre": "Action RPG / Відкритий світ",
        "developer": "CD Projekt RED",
        "description": "Культова сюжетна рольова гра з величезним живим світом, глибокими моральними виборами та захоплюючими квестами.",
        "tag": "Сюжетний шедевр"
    },
    "Cyberpunk 2077": {
        "genre": "Sci-Fi Action RPG / FPS",
        "developer": "CD Projekt RED",
        "description": "Масштабний кіберпанк-екшн від першої особи у футуристичному мегаполісі Найт-Сіті з передовими візуальними технологіями.",
        "tag": "Неймовірна графіка"
    },
    "Elden Ring": {
        "genre": "Soulslike / Action RPG",
        "developer": "FromSoftware",
        "description": "Епічна гра в темному фентезійному світі з безкомпромісною бойовою системою, свободою дослідження та високим викликом.",
        "tag": "Хардкорний виклик"
    },
    "Baldur's Gate 3": {
        "genre": "CRPG / Покрокова тактика",
        "developer": "Larian Studios",
        "description": "Феноменальна класична рольова гра за правилами D&D з безмежною варіативністю рішень, кооперативом та харизматичними супутниками.",
        "tag": "Глибина та вибори"
    },
    "Counter-Strike 2": {
        "genre": "Тактичний шутер / FPS",
        "developer": "Valve",
        "description": "Легендарний командний змагальний шутер, орієнтований на точність стрільби, миттєву реакцію та злагоджену тактику.",
        "tag": "Кіберспорт та PvP"
    },
    "Dota 2": {
        "genre": "MOBA / Командна стратегія",
        "developer": "Valve",
        "description": "Глибока стратегічна командна битва арени з понад сотнею унікальних героїв та практично невичерпною глибиною тактики.",
        "tag": "Глибока тактика"
    },
    "Hades": {
        "genre": "Rogue-lite / Динамічний екшн",
        "developer": "Supergiant Games",
        "description": "Швидкий та видовищний ізометричний роуглайк у давньогрецькому підземному царстві з чудовою історією та саундтреком.",
        "tag": "Швидкі драйвові забіги"
    },
    "Hollow Knight": {
        "genre": "Metroidvania / Платформер",
        "developer": "Team Cherry",
        "description": "Атмосферна та складна метроїдванія у загадковому підземному королівстві комах із мальованою анімацією та секретами.",
        "tag": "Атмосфера та дослідження"
    }
}
QUESTIONS: List[Dict[str, Any]] = [
    {
        "category": "Жанр та основна механіка",
        "question": "Якому ігровому жанру та геймплею ви віддаєте перевагу?",
        "answers": [
            ("Рольові ігри (RPG) та відкритий світ", "genre_rpg"),
            ("Шутери та екшн від першої особи (FPS)", "genre_shooter"),
            ("Тактика, стратегія та покрокові бої", "genre_strategy"),
            ("Платформери та атмосферні метроїдванії", "genre_platformer"),
            ("Динамічні роуглайки (швидкі забіги та скіл)", "genre_roguelike")
        ]
    },
    {
        "category": "Ігровий режим",
        "question": "З ким та в якому форматі ви хочете грати?",
        "answers": [
            ("Одиночна гра (занурення в окремий світ)", "mode_single"),
            ("Змагальний онлайн (PvP, боротьба з реальними гравцями)", "mode_multiplayer"),
            ("Кооператив (спільне проходження з друзями)", "mode_coop")
        ]
    },
    {
        "category": "Рівень складності та темп",
        "question": "Який рівень складності та напруження вам потрібен?",
        "answers": [
            ("Хардкорний виклик (висока концентрація, ціна помилки)", "diff_hardcore"),
            ("Збалансований рівень (цікавий геймплей без фрустрації)", "diff_medium"),
            ("Розслаблений темп (акцент на сюжеті й атмосфері)", "diff_relaxed")
        ]
    },
    {
        "category": "Тривалість сесії та масштаб",
        "question": "Скільки часу ви готові приділяти грі?",
        "answers": [
            ("Швидкі сесії (20–40 хвилин на матч або забіг)", "session_short"),
            ("Масштабна епопея (величезний світ на 50–100+ годин)", "session_epic"),
            ("Гнучкий формат (можна як на пів години, так і на весь вечір)", "session_flexible")
        ]
    },
    {
        "category": "Головний пріоритет",
        "question": "Що для вас найважливіше у відеогрі?",
        "answers": [
            ("Глибокий сюжет, лор, діалоги та вибори", "priority_story"),
            ("Азарт перемоги, командна робота й кіберспорт", "priority_pvp"),
            ("Дослідження таємничого світу та естетика", "priority_exploration"),
            ("Відточування бойової механіки та білдів", "priority_combat")
        ]
    },
    {
        "category": "Вимоги до ПК",
        "question": "Яка продуктивність вашого комп'ютера?",
        "answers": [
            ("Потужний ігровий ПК (висока графіка, ray tracing)", "hardware_high"),
            ("Середній ПК або ноутбук (стабільна середня графіка)", "hardware_mid"),
            ("Невимоглива гра (має працювати на будь-якому залізі)", "hardware_low")
        ]
    },
    {
        "category": "Сеттинг та атмосфера",
        "question": "Яка атмосфера та візуальний стиль вас приваблюють?",
        "answers": [
            ("Фентезі та міфічні світи (магія, дракони, лицарі)", "setting_fantasy"),
            ("Кіберпанк та наукова фантастика (майбутнє, технології)", "setting_scifi"),
            ("Сучасний або змагальний реалістичний стиль", "setting_realistic"),
            ("Авторський художній арт (мальований 2D-стиль, темна казка)", "setting_art")
        ]
    }
]
KNOWLEDGE_BASE: Dict[str, Dict[str, int]] = {
    "genre_rpg": {
        "The Witcher 3: Wild Hunt": 5,
        "Cyberpunk 2077": 5,
        "Elden Ring": 5,
        "Baldur's Gate 3": 5,
        "Counter-Strike 2": 0,
        "Dota 2": 1,
        "Hades": 4,
        "Hollow Knight": 3
    },
    "genre_shooter": {
        "The Witcher 3: Wild Hunt": 0,
        "Cyberpunk 2077": 5,
        "Elden Ring": 0,
        "Baldur's Gate 3": 0,
        "Counter-Strike 2": 5,
        "Dota 2": 0,
        "Hades": 1,
        "Hollow Knight": 0
    },
    "genre_strategy": {
        "The Witcher 3: Wild Hunt": 1,
        "Cyberpunk 2077": 1,
        "Elden Ring": 2,
        "Baldur's Gate 3": 5,
        "Counter-Strike 2": 2,
        "Dota 2": 5,
        "Hades": 2,
        "Hollow Knight": 2
    },
    "genre_platformer": {
        "The Witcher 3: Wild Hunt": 0,
        "Cyberpunk 2077": 0,
        "Elden Ring": 1,
        "Baldur's Gate 3": 0,
        "Counter-Strike 2": 0,
        "Dota 2": 0,
        "Hades": 3,
        "Hollow Knight": 5
    },
    "genre_roguelike": {
        "The Witcher 3: Wild Hunt": 0,
        "Cyberpunk 2077": 0,
        "Elden Ring": 2,
        "Baldur's Gate 3": 1,
        "Counter-Strike 2": 1,
        "Dota 2": 1,
        "Hades": 5,
        "Hollow Knight": 2
    },
    "mode_single": {
        "The Witcher 3: Wild Hunt": 5,
        "Cyberpunk 2077": 5,
        "Elden Ring": 4,
        "Baldur's Gate 3": 5,
        "Counter-Strike 2": 0,
        "Dota 2": 0,
        "Hades": 5,
        "Hollow Knight": 5
    },
    "mode_multiplayer": {
        "The Witcher 3: Wild Hunt": 0,
        "Cyberpunk 2077": 0,
        "Elden Ring": 3,
        "Baldur's Gate 3": 3,
        "Counter-Strike 2": 5,
        "Dota 2": 5,
        "Hades": 0,
        "Hollow Knight": 0
    },
    "mode_coop": {
        "The Witcher 3: Wild Hunt": 0,
        "Cyberpunk 2077": 0,
        "Elden Ring": 3,
        "Baldur's Gate 3": 5,
        "Counter-Strike 2": 3,
        "Dota 2": 4,
        "Hades": 0,
        "Hollow Knight": 0
    },
    "diff_hardcore": {
        "The Witcher 3: Wild Hunt": 2,
        "Cyberpunk 2077": 2,
        "Elden Ring": 5,
        "Baldur's Gate 3": 3,
        "Counter-Strike 2": 5,
        "Dota 2": 5,
        "Hades": 4,
        "Hollow Knight": 5
    },
    "diff_medium": {
        "The Witcher 3: Wild Hunt": 5,
        "Cyberpunk 2077": 5,
        "Elden Ring": 3,
        "Baldur's Gate 3": 4,
        "Counter-Strike 2": 3,
        "Dota 2": 3,
        "Hades": 4,
        "Hollow Knight": 3
    },
    "diff_relaxed": {
        "The Witcher 3: Wild Hunt": 4,
        "Cyberpunk 2077": 4,
        "Elden Ring": 1,
        "Baldur's Gate 3": 4,
        "Counter-Strike 2": 0,
        "Dota 2": 0,
        "Hades": 3,
        "Hollow Knight": 2
    },
    "session_short": {
        "The Witcher 3: Wild Hunt": 1,
        "Cyberpunk 2077": 2,
        "Elden Ring": 2,
        "Baldur's Gate 3": 1,
        "Counter-Strike 2": 5,
        "Dota 2": 4,
        "Hades": 5,
        "Hollow Knight": 3
    },
    "session_epic": {
        "The Witcher 3: Wild Hunt": 5,
        "Cyberpunk 2077": 5,
        "Elden Ring": 5,
        "Baldur's Gate 3": 5,
        "Counter-Strike 2": 1,
        "Dota 2": 2,
        "Hades": 3,
        "Hollow Knight": 4
    },
    "session_flexible": {
        "The Witcher 3: Wild Hunt": 3,
        "Cyberpunk 2077": 3,
        "Elden Ring": 3,
        "Baldur's Gate 3": 3,
        "Counter-Strike 2": 4,
        "Dota 2": 3,
        "Hades": 5,
        "Hollow Knight": 4
    },
    "priority_story": {
        "The Witcher 3: Wild Hunt": 5,
        "Cyberpunk 2077": 5,
        "Elden Ring": 3,
        "Baldur's Gate 3": 5,
        "Counter-Strike 2": 0,
        "Dota 2": 0,
        "Hades": 4,
        "Hollow Knight": 4
    },
    "priority_pvp": {
        "The Witcher 3: Wild Hunt": 0,
        "Cyberpunk 2077": 0,
        "Elden Ring": 2,
        "Baldur's Gate 3": 1,
        "Counter-Strike 2": 5,
        "Dota 2": 5,
        "Hades": 0,
        "Hollow Knight": 0
    },
    "priority_exploration": {
        "The Witcher 3: Wild Hunt": 5,
        "Cyberpunk 2077": 4,
        "Elden Ring": 5,
        "Baldur's Gate 3": 4,
        "Counter-Strike 2": 1,
        "Dota 2": 1,
        "Hades": 3,
        "Hollow Knight": 5
    },
    "priority_combat": {
        "The Witcher 3: Wild Hunt": 3,
        "Cyberpunk 2077": 4,
        "Elden Ring": 5,
        "Baldur's Gate 3": 4,
        "Counter-Strike 2": 4,
        "Dota 2": 4,
        "Hades": 5,
        "Hollow Knight": 4
    },
    "hardware_high": {
        "The Witcher 3: Wild Hunt": 4,
        "Cyberpunk 2077": 5,
        "Elden Ring": 4,
        "Baldur's Gate 3": 4,
        "Counter-Strike 2": 3,
        "Dota 2": 2,
        "Hades": 1,
        "Hollow Knight": 1
    },
    "hardware_mid": {
        "The Witcher 3: Wild Hunt": 4,
        "Cyberpunk 2077": 3,
        "Elden Ring": 4,
        "Baldur's Gate 3": 4,
        "Counter-Strike 2": 4,
        "Dota 2": 4,
        "Hades": 4,
        "Hollow Knight": 4
    },
    "hardware_low": {
        "The Witcher 3: Wild Hunt": 2,
        "Cyberpunk 2077": 1,
        "Elden Ring": 1,
        "Baldur's Gate 3": 1,
        "Counter-Strike 2": 3,
        "Dota 2": 4,
        "Hades": 5,
        "Hollow Knight": 5
    },
    "setting_fantasy": {
        "The Witcher 3: Wild Hunt": 5,
        "Cyberpunk 2077": 0,
        "Elden Ring": 5,
        "Baldur's Gate 3": 5,
        "Counter-Strike 2": 0,
        "Dota 2": 4,
        "Hades": 5,
        "Hollow Knight": 4
    },
    "setting_scifi": {
        "The Witcher 3: Wild Hunt": 0,
        "Cyberpunk 2077": 5,
        "Elden Ring": 0,
        "Baldur's Gate 3": 1,
        "Counter-Strike 2": 1,
        "Dota 2": 2,
        "Hades": 1,
        "Hollow Knight": 0
    },
    "setting_realistic": {
        "The Witcher 3: Wild Hunt": 1,
        "Cyberpunk 2077": 3,
        "Elden Ring": 0,
        "Baldur's Gate 3": 0,
        "Counter-Strike 2": 5,
        "Dota 2": 1,
        "Hades": 0,
        "Hollow Knight": 0
    },
    "setting_art": {
        "The Witcher 3: Wild Hunt": 2,
        "Cyberpunk 2077": 2,
        "Elden Ring": 4,
        "Baldur's Gate 3": 3,
        "Counter-Strike 2": 0,
        "Dota 2": 2,
        "Hades": 5,
        "Hollow Knight": 5
    }
}
