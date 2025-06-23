# Copyright 2023 Tecnativa - Víctor Martínez
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models


class SignOcaRequest(models.Model):
    _inherit = "sign.oca.request"

    # This field is required for the inverse of maintenance.equipment.
    purchase_order_id = fields.Many2one(
        comodel_name="purchase.order",
        compute="_compute_purchase_order_id",
        string="Purchase Order",
        readonly=True,
        store=True,
    )

    @api.depends("record_ref")
    def _compute_maintenance_equipment_id(self):
        for item in self.filtered(
            lambda x: x.record_ref and x.record_ref._name == "purchase.order"
        ):
            item.purchase_order_id = item.record_ref.id
