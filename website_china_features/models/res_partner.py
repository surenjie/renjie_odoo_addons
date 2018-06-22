# -*- coding: utf-8 -*-

import logging
import werkzeug

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

def urlplus(url, params):
    return werkzeug.Href(url)(params or None)

class ResPartner(models.Model):
    _inherit = "res.partner"

    def baidu_map_img(self, zoom=15, width=298, height=298):
        country_name = self.country_id and self.country_id.name or ''
        state_name = self.state_id and self.state_id.name or ''
        city_name = self.city or ''
        street_name = self.street or ''
        street2_name = self.street2 or ''
        params = {
            'markers': '%s' % street2_name,
            'center': '%s%s%s%s' % (country_name, state_name, city_name, street_name),
            'height': "%s" % height,
            'width': "%s" % width,
            'zoom': zoom,
            'copyright': 1,
        }
        #http://lbsyun.baidu.com/index.php?title=static
        return urlplus('//api.map.baidu.com/staticimage' , params)

    def baidu_map_link(self):
        partner_name = self.name
        city_name = self.city or ''
        street2_name = self.street2 or ''
        params = {
            'address': '%s,%s,%s' % (city_name, street2_name, partner_name),
            'output': 'html',
            'src': 'odoo',
        }
        #http://lbsyun.baidu.com/index.php?title=uri
        return urlplus('//api.map.baidu.com/geocoder' , params)
