# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{

    "name": "Textile Shop ",
    "version": "14.0.0.1",
    "currency": 'EUR',
    "summary": "Apps basic Hospital Management system Healthcare Management Clinic Management apps manage clinic manage Patient hospital manage Healthcare system Patient Management Hospital Management Healthcare Management Clinic Management hospital Lab Test Request",
    "category": "Industries",
    "description": """
    BrowseInfo developed a new odoo/OpenERP module apps
    This module is used to manage Hospital and Healthcare Management and Clinic Management apps. 
    manage clinic manage Patient hospital in odoo manage Healthcare system Patient Management, 
    Odoo Hospital Management odoo Healthcare Management Odoo Clinic Management
    Odoo hospital Patients
    Odoo Healthcare Patients Card Report
    Odoo Healthcare Patients Medication History Report
    Odoo Healthcare Appointments
    Odoo hospital Appointments Invoice
    Odoo Healthcare Families Prescriptions Healthcare Prescriptions
    Odoo Healthcare Create Invoice from Prescriptions odoo hospital Prescription Report
    Odoo Healthcare Patient Hospitalization
    odoo Hospital Management System
    Odoo Healthcare Management System
    Odoo Clinic Management System
    Odoo Appointment Management System
    health care management system
    Generate Report for patient details, appointment, prescriptions, lab-test

    Odoo Lab Test Request and Result
    Odoo Patient Hospitalization details
    Generate Patient's Prescriptions

    
""",

    "depends": ["base", "sale_management", "stock", "account","mail"],
    "data": [
         'security/ir.model.access.csv',
        #'views/menu.xml' 
         'views/customer.xml'    



    ],
    "author": "BrowseInfo",
    "sequence": -100,
    "website": "https://www.browseinfo.in",
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": ["static/description/Banner.png"],
    "live_test_url": 'https://youtu.be/fk9dY53I9ow',
}