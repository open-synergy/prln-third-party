from openerp.osv import orm
import sendmail
class stock_picking(orm.Model):
	_name = 'stock.picking'
	_inherit = 'stock.picking'
	def create(self,cr,uid,ids,context=None):
		id2 = super(stock_picking,self).create(cr,uid,ids,context=context)
		sp_obj = self.pool.get('stock.picking')
		sp_info = sp_obj.read(cr, uid, id2, ['name'])
		id2_name = sp_info['name']
		user_obj = self.pool.get('res.users')
		username = user_obj.read(cr,uid,uid,['name'])
		username2 = username['name']
		
		signature_obj = self.pool.get('document.signature')
		do_id = signature_obj.search(cr,uid,[('doc_type','=','do')])
		user_id = signature_obj.read(cr,uid,do_id,['user_id'])
		user_id2 = user_id[0].get('user_id')[0]
		email_id = user_obj.read(cr,uid,user_id2,['user_email'])
		email_id2 = email_id.get('user_email')
		#open('/tmp/testing.txt','w').write(str(email_id2))
		

		pesan = "%s%s\r\n%s%s\r\n\r\n%s"%('Manually Created DO : ',username2,'DO No : ',id2_name,'Email ini merupakan email pemberitahuan. Jangan me-reply email ini. Silahkan cek langsung di ERP untuk no DO yang dimaksud.')
		#sendmail.sendmail('erp@pralon.com','erp.do@pralon.com','ERP Alert : Manual DO Created',pesan)
		return id2
