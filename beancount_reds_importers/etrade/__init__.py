""" ETrade Brokerage ofx importer."""

import ntpath
from beancount_reds_importers.libreader import ofxreader
from beancount_reds_importers.libtransactionbuilder import investments


class Importer(investments.Importer, ofxreader.Importer):
    IMPORTER_NAME = 'ETrade'
    def custom_init(self):
        self.max_rounding_error = 0.11
        self.filename_pattern_def = '.*etrade'
        self.get_ticker_info = self.get_ticker_info_from_id

    def skip_transactions(self, ot):
        if 'JNL' in ot.memo:
            return True
        return False

    def get_target_acct_custom(self, transaction, ticker=None):
        return self.target_account_map.get(transaction.type, None)
