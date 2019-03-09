# -*- coding: utf-8 -*-
import logging

from odoo.addons.website.controllers.main import Website

from odoo import http
from odoo.http import request

logger = logging.getLogger(__name__)

class WebsiteDisabled(Website):
    @http.route(auth="none", website=False)
    def index(self, **kw):
        return http.local_redirect('/web', query=request.params, keep_hash=True)
