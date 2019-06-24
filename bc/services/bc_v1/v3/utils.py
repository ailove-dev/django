from collections import UserDict


class CourseResponse(UserDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(args, kwargs)

    @property
    def modules(self):
        for module in self.data.get("unavailableModules", []):
            yield module

        for module in self.data.get("modules", []):
            yield module

        for module in self.data.get("extraModules", []):
            yield {**module, "is_extra": True}

    @property
    def modules_list(self):
        return list(self.modules)

    def serialize(self):
        course_duration = 0
        modules = []
        for module in self.modules:
            duration = module["duration"]
            modules.append(
                {
                    "pk": module["pk"],
                    "duration": duration,
                    "title": module["title"],
                    "info": module["info"],
                }
            )
            course_duration += duration
        return {"modules": modules, "duration": course_duration}
