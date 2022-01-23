/** @odoo-module alias=web.window.title **/

import { WebClient } from "@web/webclient/webclient";
import {patch} from "@web/core/utils/patch";

patch(WebClient.prototype, "Web Window Title", {
    setup() {
        const title = document.title;
        this._super();
        this.title.setParts({ zopenerp: title });
    }
});
