from enum import Enum
from flask import url_for
from werkzeug.utils import redirect


class BlueprintName(Enum):

    def url_for(
            self,
            function_name,
            **kwargs
    ):
        return url_for(
            '{}.{}'.format(
                self.value,
                function_name
            ),
            **kwargs
        )

    def redirect(
            self,
            function_name,
            **kwargs
    ):
        return redirect(self.url_for(function_name, **kwargs))
