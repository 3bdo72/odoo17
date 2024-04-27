odoo.define('your_module.toggle_widget', function (require) {
    "use strict";

    var basic_fields = require('web.basic_fields');
    var core = require('web.core');
    var _t = core._t;

    var ToggleWidget = basic_fields.FieldChar.extend({
        template: 'your_module.toggle_widget_template',
        events: _.extend({}, basic_fields.FieldChar.prototype.events, {
            'click .o_toggle_button': '_onToggleClick',
        }),

        _render: function () {
            this._super.apply(this, arguments);
            // Set initial visibility based on the field's value
            this.$el.find('input').attr('type', this.value ? 'text' : 'password');
        },

        _onToggleClick: function () {
            var $input = this.$el.find('input');
            $input.attr('type', $input.attr('type') === 'password' ? 'text' : 'password');
        },
    });

    core.field_registry.add('toggle_widget', ToggleWidget);

    return ToggleWidget;
});