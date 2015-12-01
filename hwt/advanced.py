import time
from report import report_sxw
import utilities


class rwk_stock_picking(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(rwk_stock_picking, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'cr': cr,
            'uid': uid,
            'date_order_fmt': self.date_order_fmt,
            'wrap_line': self.wrap_line,
        })

    def date_order_fmt(self, value):
        return utilities.date_order_fmt(value=value)

    def wrap_line(self, column_list_source, column_width_list, total_column):
        return utilities.wrap_line(column_list_source, column_width_list, total_column)


report_sxw.report_sxw('report.webkit_stock_picking',
                       'stock.picking',
                       'thirdparty/hwt/delivery_order_adv.mako',
                       parser=rwk_stock_picking, header=False)

