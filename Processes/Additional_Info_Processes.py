from Data.Additional_Information_Page_Data import AdditionalInformationMother
class AdditionalInfoProcess:
    def __init__(self, additional_info):
        self.additional_info = additional_info

    def run_processes(self):
        data = AdditionalInformationMother.get()
        self.additional_info.select_Option(data.AdditionalTypeData)




