import typing
from collections import UserDict


class CourseData(UserDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.external_id = None

    def attach_external_id(self, external_id):
        self.external_id = external_id

    @property
    def modules(self) -> typing.Generator:
        for module in self.data.get("unavailableModules", []):
            yield module

        for module in self.data.get("modules", []):
            yield module

        for module in self.data.get("extraModules", []):
            yield {**module, "is_extra": True}

    @property
    def modules_list(self) -> list:
        return list(self.modules)

    @property
    def common_data(self):
        """Not user-specific, safe to store
        """
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


class UserData(UserDict):
    UPDATE_FIELDS = (("course_path", "path"), ("avatar", "photo"))

    def update_user(self, user, commit: bool = True):
        for user_field, response_field in self.UPDATE_FIELDS:
            setattr(user, user_field, self.data.get(response_field))

        if commit:
            user.save()

        return user
