import os

from django.conf import settings
from django.views.generic import TemplateView


class SkelView(TemplateView):
    template_name = "skelslist.html"
    skels_path = os.path.join(settings.BASE_DIR, "templates", "skels")
    skels_url = "skels/"

    def is_dir(self):
        return os.path.isdir(
            os.path.join(self.skels_path, self.kwargs.get("template_name", ""))
        )

    def get_skels_path(self):
        if self.is_dir():
            return os.path.join(self.skels_path, self.kwargs.get("template_name", ""))
        return None

    def get_template_names(self):
        if self.is_dir():
            return self.template_name
        return ["{}/{}".format(self.skels_url, self.kwargs.get("template_name", ""))]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.get_skels_path():
            files = []
            dirs = []
            context["links"] = []
            p = self.get_skels_path()
            context["title"] = "{}{}".format(
                self.skels_url, self.kwargs.get("template_name", "")
            )
            if self.is_dir() and self.kwargs.get("template_name", ""):
                context["links"].extend(
                    [
                        (
                            os.path.join(self.kwargs.get("template_name", ""), ".."),
                            True,
                            "..",
                        )
                    ]
                )
            for x in os.listdir(p):
                f = os.path.join(self.kwargs.get("template_name", ""), x)
                if os.path.isdir(os.path.join(self.skels_path, f)):
                    dirs.append(
                        (
                            f,
                            True,
                            x,
                        )
                    )
                else:
                    files.append(
                        (
                            f,
                            False,
                            x,
                        )
                    )
            context["links"] += dirs + files
        return context
