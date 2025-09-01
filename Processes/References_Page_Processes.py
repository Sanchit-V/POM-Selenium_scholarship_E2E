class ReferencePageProcess:
    def __init__(self, reference_page):
        self.reference_page = reference_page

    def run_processes(self, additional_references,ref_First_Name, ref_Last_Name, ref_Pos_Occupation, ref_Emails,
                               ref_phone_numbers, ref_landline_numbers, ref_phone_CC, ref_landline_CC):

        self.reference_page.delete_references(additional_references)

        self.reference_page.add_references(additional_references)

        self.reference_page.add_references_details(ref_First_Name, ref_Last_Name, ref_Pos_Occupation, ref_Emails, ref_phone_numbers, ref_landline_numbers,
                                                   ref_phone_CC, ref_landline_CC)

        self.reference_page.continue_references()






