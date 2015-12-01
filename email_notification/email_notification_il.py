from openerp.osv import orm
import sendmail
class stock_move(orm.Model):
	_name = 'stock.move'
	_inherit = 'stock.move'
	def create(self,cr,uid,ids,context=None):
		id2 = super(stock_move,self).create(cr,uid,ids,context=context)
		sp_obj = self.pool.get('stock.move')
		sp_info = sp_obj.read(cr, uid, id2, ['name','location_id','location_dest_id'])
		id2_name = sp_info['name']
		user_obj = self.pool.get('res.users')
		username = user_obj.read(cr,uid,uid,['name'])
		username2 = username['name']
		
		#open('/tmp/il.txt','w').write(str(sp_info['location_id']))

		if sp_info['location_id'][0] in [5,1901,1898,1899] or sp_info['location_dest_id'][0] in [5,1901,1898,1899]:
			pesan = "%s%s\r\n%s%s\r\n\r\n%s"%('Inventory Loss Movement : ',username2,'Stock Move No : ',"id2_name.decode('utf-8')",'Email ini merupakan pemberitahuan. Jangan me-reply ke email ini. Silahkan cek langsung di ERP untuk no Dokumen yang dimaksud.')
			#sendmail.sendmail('erp@pralon.com','erp.il@pralon.com','ERP Alert : Inventory Loss Movement',pesan)
		return id2
		
