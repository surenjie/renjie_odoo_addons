odoo.define('web_window_title', function (require) {
"use strict";

var AbstractWebClient = require('web.AbstractWebClient');
AbstractWebClient.include({
    init: function() {
        this._super.apply(this, arguments);
        this.set('title_part', {"zopenerp": document.title});
    }
});

});