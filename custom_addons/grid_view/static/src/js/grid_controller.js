/** @odoo-module **/
import { Component, useState } from "@odoo/owl";
import { Layout } from "@web/search/layout";
import { useModelWithSampleData } from "@web/model/model";
import { CogMenu } from "@web/search/cog_menu/cog_menu";
import { SearchBar } from "@web/search/search_bar/search_bar";
import { ViewButton } from "@web/views/view_button/view_button";
import { Dropdown } from "@web/core/dropdown/dropdown";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";
import { extractFieldsFromArchInfo } from "@web/model/relational_model/utils";
import { session } from "@web/session";
import { useBus, useService } from "@web/core/utils/hooks";
import { useSearchBarToggler } from "@web/search/search_bar/search_bar_toggler";
import { useSetupView } from "@web/views/view_hook";

export class GridController extends Component {
    static components = {
        Layout,
        Dropdown,
        DropdownItem,
        ViewButton,
        CogMenu,
        SearchBar,
    };
    async setup() {
        this.viewService = useService("view");
        this.dataSearch = []
        this.ui = useService("ui");
        useBus(this.ui.bus, "resize", this.render);
        this.archInfo = this.props.archInfo;
        const fields = this.props.fields;
        this.model = useState(useModelWithSampleData(this.props.Model, this.modelParams));
        this.searchBarToggler = useSearchBarToggler();
        useSetupView({
            rootRef: this.rootRef,
            beforeLeave: async () => {
                return this.model.root.leaveEditMode();
            },
            beforeUnload: async (ev) => {
                const editedRecord = this.model.root.editedRecord;
                if (editedRecord) {
                    const isValid = await editedRecord.urgentSave();
                    if (!isValid) {
                        ev.preventDefault();
                        ev.returnValue = "Unsaved changes";
                    }
                }
            },
            getOrderBy: () => {
                return this.model.root.orderBy;
            },
        });
    }
    get modelParams() {
        const { defaultGroupBy, rawExpand } = this.archInfo;
        const { activeFields, fields } = extractFieldsFromArchInfo(
            this.archInfo,
            this.props.fields
        );
        const groupByInfo = {};
        for (const fieldName in this.archInfo.groupBy.fields) {
            const fieldNodes = this.archInfo.groupBy.fields[fieldName].fieldNodes;
            const fields = this.archInfo.groupBy.fields[fieldName].fields;
            groupByInfo[fieldName] = extractFieldsFromArchInfo({ fieldNodes }, fields);
        }
        const modelConfig = this.props.state?.modelState?.config || {
            resModel: this.props.resModel,
            fields,
            activeFields,
            openGroupsByDefault: true,
        };
        return {
            config: modelConfig,
            state: this.props.state?.modelState,
            groupByInfo,
            limit: null,
            countLimit: this.archInfo.countLimit,
            defaultOrderBy: this.archInfo.defaultOrder,
            defaultGroupBy: this.props.searchMenuTypes.includes("groupBy") ? defaultGroupBy : false,
            groupsLimit: this.archInfo.groupsLimit,
            multiEdit: this.archInfo.multiEdit,
            activeIdsLimit: session.active_ids_limit,
        };
    }
}
GridController.template = "grid_view.GridView";