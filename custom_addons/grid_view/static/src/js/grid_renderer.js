/** @odoo-module **/
import { Component } from "@odoo/owl";
import { View } from "@web/views/view";
import { Field } from "@web/views/fields/field";
import { Record } from "@web/model/record";
import { ViewScaleSelector } from "@web/views/view_components/view_scale_selector";
export class GridRenderer extends Component {
    async setup() {
    }
}
GridRenderer.template = "grid_view.GridRenderer";
GridRenderer.components = {
    View,
    Field,
    Record,
    ViewScaleSelector,
};