/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import {Dropdown} from '@web/core/dropdown/dropdown';
import {DropdownItem} from '@web/core/dropdown/dropdown_item';
class SystrayIcon extends Component {
   setup() {
       super.setup(...arguments);
       this.action = useService("action");
   }
   _openGeneral() {
       this.action.doAction({
           type: "ir.actions.act_window",
           name: "General Settings",
           res_model: "res.config.settings",
           view_mode: "form",
           views: [[false, "form"]],
           target: "new",
           });
           }
   _openServerActions(){
       this.action.doAction({
           type: "ir.actions.act_window",
           name: "Server Actions",
           res_model: "ir.actions.server",
           view_mode: "tree",
           views: [[false, "tree"]],
           target: "new",
           });
    }_openViews(){
       this.action.doAction({
           type: "ir.actions.act_window",
           name: "Views",
           res_model: "ir.ui.view",
           view_mode: "tree",
           views: [[false, "tree"]],
           target: "new",
        });
    } _openModels() {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Models",
            res_model: "ir.model",
            view_mode: "tree",
            views: [[false, "tree"]],
            target: "new",
        });
    }_openAutomationRules() {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Automation Rules",
            res_model: "base.automation",
            view_mode: "kanban",
            views: [[false, "kanban"]],
            target: "new",
        });
    }_openUsers() {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Users",
            res_model: "res.users",
            view_mode: "kanban",
            views: [[false, "kanban"]],
            target: "new",
        });
    }
}
   SystrayIcon.template = "systray_icon";
   SystrayIcon.components = {Dropdown, DropdownItem };
   export const systrayItem = { Component: SystrayIcon,};
   registry.category("systray").add("SystrayIcon", systrayItem, { sequence: 1 });
