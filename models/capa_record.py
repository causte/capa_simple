from odoo import api, fields, models
from datetime import date


class CapaRecord(models.Model):
    _name = "capa.record"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "CAPA Record"
    _table = "capa_record"

    name = fields.Char(string="Title", required=True)
    date_open = fields.Date(string="Opened", required=True, default=fields.Date.context_today)
    due_date = fields.Date(string="Due Date", required=True)
    responsible_id = fields.Many2one("res.users", string="Responsible")
    description = fields.Text(string="Description")
    investigation = fields.Text(string="Investigation")
    resolution = fields.Text(string="Resolution")
    state = fields.Selection(
        [("open", "Open"), ("closed", "Closed")],
        string="State",
        default="open",
        required=True,
    )
    is_past_due = fields.Boolean(string="Past Due", compute="_compute_past_due", store=False)
    due_dot = fields.Char(string="Due", compute="_compute_past_due", store=False)

    def action_mark_closed(self):
        for rec in self:
            rec.state = "closed"
            rec.message_post(body="Marked as closed")

    @api.depends("state", "due_date")
    def _compute_past_due(self):
        for rec in self:
            rec.is_past_due = False
            rec.due_dot = "🟢"
            if rec.state == "open" and rec.due_date:
                if rec.due_date < date.today():
                    rec.is_past_due = True
                    rec.due_dot = "🔴"
