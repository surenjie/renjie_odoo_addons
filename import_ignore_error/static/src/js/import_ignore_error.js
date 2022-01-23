odoo.define('import_ignore_error', function (require) {
"use strict";

var core = require('web.core');
var DataImport = require('base_import.import').DataImport;
DataImport.include({
    call_import: function(kwargs) {
        var self = this;
        var ignore_error = 'ignore_error' in kwargs ? kwargs.ignore_error : this.$('#oe_import_ignore_error').prop('checked');
        delete kwargs.ignore_error;
        self.parent_context = _.extend(
            self.parent_context || {},
            {import_ignore_error: ignore_error}
        );
        return self._super.call(self, kwargs);
    }
});

});