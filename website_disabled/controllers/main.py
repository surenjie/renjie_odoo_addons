# -*- coding: utf-8 -*-
import logging

from openerp import http
from openerp.http import request
from openerp.addons.website.controllers.main import Website

logger = logging.getLogger(__name__)

class WebsiteDisabled(Website):
    @http.route(auth="none", website=False)
    def index(self, **kw):
        return http.local_redirect('/web', query=request.params, keep_hash=True)
