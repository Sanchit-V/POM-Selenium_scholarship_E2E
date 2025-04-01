class Reference_Process:
    def __init__(self, reference_page):
        self.reference_page = reference_page

    def run_processes(self, additional_references,ref1_FirstName, ref1_LastName, ref1_Pos_Occupation,
                      ref1_email, ref1_phone_number, ref1_landline_number,ref1_phone_CC,ref1_landline_CC,
                      ref2_FirstName, ref2_LastName, ref2_Pos_Occupation, ref2_email, ref2_phone_number, ref2_landline_number,
                      ref2_phone_CC, ref2_landline_CC, ref3_FirstName, ref3_LastName, ref3_Pos_Occupation, ref3_email, ref3_phone_number,
                      ref3_landline_number, ref3_phone_CC, ref3_landline_CC, ref4_FirstName, ref4_LastName, ref4_Pos_Occupation, ref4_email, ref4_phone_number,
                               ref4_landline_number, ref4_phone_CC, ref4_landline_CC,ref5_FirstName, ref5_LastName, ref5_Pos_Occupation, ref5_email, ref5_phone_number,
                               ref5_landline_number, ref5_phone_CC, ref5_landline_CC ):

        self.reference_page.delete_references()

        self.reference_page.add_references(additional_references)

        self.reference_page.add_reference1_details(ref1_FirstName, ref1_LastName, ref1_Pos_Occupation, ref1_email, ref1_phone_number, ref1_landline_number,
                                                   ref1_phone_CC, ref1_landline_CC)

        self.reference_page.add_reference2_details(ref2_FirstName, ref2_LastName, ref2_Pos_Occupation, ref2_email, ref2_phone_number, ref2_landline_number,
                                                   ref2_phone_CC, ref2_landline_CC)

        self.reference_page.add_reference3_details(ref3_FirstName, ref3_LastName, ref3_Pos_Occupation, ref3_email, ref3_phone_number, ref3_landline_number,
                                                   ref3_phone_CC, ref3_landline_CC)

        self.reference_page.add_reference4_details(ref4_FirstName, ref4_LastName, ref4_Pos_Occupation, ref4_email, ref4_phone_number,
                               ref4_landline_number, ref4_phone_CC, ref4_landline_CC)

        self.reference_page.add_reference5_details(ref5_FirstName, ref5_LastName, ref5_Pos_Occupation, ref5_email, ref5_phone_number,
                               ref5_landline_number, ref5_phone_CC, ref5_landline_CC)

        self.reference_page.continue_references()


