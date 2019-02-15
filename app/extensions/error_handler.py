from flask import flash

from constant.blueprint_name import BlueprintName
from model.service.logging_service import logging_service


class ErrorHandler:
    @classmethod
    def handle_500(cls, e):
        logging_service.logger.exception(e)
        flash(str(e), 'error')
        return BlueprintName.SHARED.redirect('home_get')
