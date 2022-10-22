# -*- coding: utf-8 -*-
from odoo import api, fields, models

class TextileRegistration(models.Model):
    _name = "textile.registration"
    _description = "Textile Registration"
    _rec_name = "no_of_quantity"
    dress_name = fields.Char(string='Model')
    price = fields.Integer(string='Price')
    
    size = fields.Integer(string='Size')
    note = fields.Text(string='Note')
    image = fields.Binary(string="Image")

    no_of_quantity= fields.Char(string="No of Quantity")
    details = fields.Text(string = 'Details')
    address = fields.Char(string = 'Address')
    quantity = fields.Integer(string='Quantity')
    medical_doctor=fields.Many2one('textile.registration',string="Patient Name",ondelete='cascade')
    
    # sequence_ref = fields.One2many('textile.billing', 'document_note', string='ID')
    currents_ailments = fields.One2many('textile.billing','medical_doctor',string="Amount")
    no_of_pieces = fields.Char(string="No of Pieces")
    # no_of_pieces = fields.One2many('textile.billing','doctor_aliments',string="No of Pieces")
    # total =fields.One2many('textile.billing','doctor_aliments',string="Total")
    total = fields.Integer(string = "Total")
    tax = fields.One2many('textile.billing','billing_note', string='Tax')
    state_tax = fields.Integer(string='State Tax')
    central_tax = fields.Integer(string='Central Tax')
    
    def edit_button(self):
        return {
        'name': "Edit Symptoms",
        'view_mode': 'tree',
        'res_model': 'textile.registration',
        'view_type': 'form',
        'type': 'ir.actions.act_window',
        'view_id': self.env.ref('Textile.view_doctor_form').id,
        'target': 'new'
        }


    @api.depends('medical_doctor.currents_ailments', 'medical_doctor.currents_ailments')
    def _sequence_ref(self):
        for line in self:
            no = 0
            line.sequence_ref = no
            for l in line.medical_doctor.currents_ailments:
                no += 1
                l.sequence_ref = no
    

class TextileBilling(models.Model):
    _name = "textile.billing"
    _description = "Textile Billing"
    _rec_name = 'document_note'
    _inherit='textile.registration'

    no_of_quantity= fields.Many2one('textile.registration',string="No of Quantity")
    doctor_aliments = fields.Many2one('textile.registration', string='Patient Name',ondelete='cascade')
    document_note = fields.Many2one('textile.registration',string="Details")
    billing_note = fields.Many2one(string="Billing")
    s_no = fields.One2many('textile.billing', 'billing_note', string='SI.NO')
    offers = fields.Many2one('textile.registration', string='Offers')
    sequence_ref = fields.Integer('ID', compute="_sequence_ref")
   