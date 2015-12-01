from osv import osv
from osv import fields

class account_invoice_line(osv.osv):
    _inherit = 'account.invoice.line'

    _columns = {
	        'discount': fields.float('Discount (%)', digits=(16, 4)),
		}
	
account_invoice_line()
