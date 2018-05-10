class Payment:
    def __init__(self, **kwargs):
        self.attributes = dict(
            payment_type = None,
            pay_date = None,
            effective_pay_date = None,
            favored_name = None,
            favored_bank = None,
            agency = None,
            our_number = None,
            currency_type = 'BRA',
            your_number = None,
            ispb_code = None,
            goal_detail = None,
            payment_document_number = None,
            doc_goal = None,
            ted_goal = None,
            nf_document = None,
            identify_type = None,
            barcode = None,
            dv = None,
            due_rule = None,
            amount = None,
            free_field = None,
            due_date = None,
            title_amount = None,
            discounts = None,
            additions = None,
            payment_amount = None,
            favored_message = None,
            occurrences = None,
        )

        kwargs_keys = kwargs.keys()
        for attr_name in self.attributes.keys():
            if attr_name in kwargs_keys:
                self.attributes[attr_name] = kwargs[attr_name]
    
    def get_attribute(self, attr_name):
        if attr_name in self.attributes.keys():
            return self.attributes[attr_name]
        raise Exception('Payment does not have attribute called "' + attr_name + '"')