class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name, self.hp, self.mp, self.skills, self.guild = name, hp, mp, {}, "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        nl = "\n"
        return f"""Name: {self.name}
Guild: {self.guild}
HP: {self.hp}
MP: {self.mp}
{nl.join(f'==={k} - {v}' for k, v in self.skills.items())}"""
