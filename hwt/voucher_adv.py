import time
from report import report_sxw
import utilities


class rwk_voucher(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(rwk_voucher, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'cr': cr,
            'uid': uid,
            'date_order_fmt': self.date_order_fmt,
            'wrap_line': self.wrap_line,
        })

    def date_order_fmt(self, value=None):
        return utilities.date_order_fmt(value=value)

    def wrap_line(self, column_list_source, column_width_list, total_column):
        return utilities.wrap_line(column_list_source, column_width_list, total_column)

report_sxw.report_sxw('report.webkit_journal_voucher2',
                       'account.move',
                       'thirdparty/hwt/voucher_adv.mako',
                       parser=rwk_voucher)
