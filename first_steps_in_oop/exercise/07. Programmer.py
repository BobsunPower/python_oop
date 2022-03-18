class Programmer:
    def __init__(self, name, language, skills):
        self.name, self.language, self.skills = name, language, skills

    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        old, new, skills = self.language, new_language, self.skills - skills_needed
        if skills < 0:
            return f"{self.name} needs {abs(skills)} more skills"
        if old == new:
            return f"{self.name} already knows {old}"
        self.language = new
        return f"{self.name} switched from {old} to {new}"
