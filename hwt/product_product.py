from osv import osv
from osv import fields

class product_product(osv.osv):
    _inherit = 'product.product'

    _columns = {
	        'dus': fields.integer('Dus'),
		}
	
product_product()
