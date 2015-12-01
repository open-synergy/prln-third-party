from osv import osv
from osv import fields

class sale_order_line(osv.osv):
	_inherit = 'sale.order.line'

	_columns = {
	            'discount': fields.float('Discount (%)', digits=(16, 4), readonly=True, states={'draft': [('readonly', False)]}),
		   }

sale_order_line()
