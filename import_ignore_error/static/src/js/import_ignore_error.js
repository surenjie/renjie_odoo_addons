/** @odoo-module alias=import.ignore.error **/

import { BaseImportModel } from "@base_import/import_model";
import { patch } from "@web/core/utils/patch";

patch(BaseImportModel.prototype, {
    init() {
        Object.assign(this.importOptionsValues, {
            ignore_error: {
                value: false
            }
        });
        super.init();
    },
    _callImport(dryrun, args) {
        Object.assign(this.context, {
            import_ignore_error: this.importOptions.ignore_error
        })
        return super._callImport(dryrun, args);
    }
});
