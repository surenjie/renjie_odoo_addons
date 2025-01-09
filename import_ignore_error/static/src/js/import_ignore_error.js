/** @odoo-module **/

import { BaseImportModel } from "@base_import/import_model";
import { patch } from "@web/core/utils/patch";

patch(BaseImportModel.prototype, {
    async init() {
        Object.assign(this.importOptionsValues, {
            ignore_error: {
                value: false
            }
        });
        return super.init();
    },
    async _callImport(dryrun, args) {
        Object.assign(this.context, {
            import_ignore_error: this.importOptions.ignore_error
        })
        return super._callImport(dryrun, args);
    }
});
