# Copyright 2023-2024 Tecnativa - Víctor Martínez
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # This field is stored as a help to filter by.
    sign_request_ids = fields.One2many(
        comodel_name="sign.oca.request",
        inverse_name="purchase_order_id",
        string="Sign Requests",
    )
    sign_request_count = fields.Integer(
        string="Sign request count",
        compute="_compute_sign_request_count",
        compute_sudo=True,
        store=True,
    )

    @api.depends("sign_request_ids")
    def _compute_sign_request_count(self):
        request_data = self.env["sign.oca.request"].read_group(
            [("purchase_order_id", "in", self.ids)],
            ["purchase_order_id"],
            ["purchase_order_id"],
        )
        mapped_data = {
            x["purchase_order_id"][0]: x["purchase_order_id_count"]
            for x in request_data
        }
        for item in self:
            item.sign_request_count = mapped_data.get(item.id, 0)

    def action_view_sign_requests(self):
        self.ensure_one()
        result = self.env["ir.actions.act_window"]._for_xml_id(
            "sign_oca.sign_oca_request_act_window"
        )
        result["domain"] = [("id", "in", self.sign_request_ids.ids)]
        ctx = dict(self.env.context)
        ctx.update(
            {
                "default_purchase_order_id": self.id,
                "search_default_purchase_order_id": self.id,
            }
        )
        result["context"] = ctx
        return result
