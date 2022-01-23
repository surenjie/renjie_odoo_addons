# -*- coding: utf-8 -*-
import logging

from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website

logger = logging.getLogger(__name__)

class WebsiteDisabled(Website):
    @http.route(auth="none", website=False, sitemap=False)
    def index(self, **kw):
        return request.redirect_query('/web', query=request.params)
